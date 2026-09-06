import os

from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import (
    Agent,
    Runner,
    SQLiteSession,
    OpenAIChatCompletionsModel,
    ModelSettings
)

from tools import (
    calculate_event_budget,
    recommend_venues,
    generate_event_checklist
)

load_dotenv()

os.environ["OPENAI_AGENTS_DISABLE_TRACING"] = "1"

OPENROUTER_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = os.getenv(
    "OPENAI_MODEL",
    "openai/gpt-4o-mini"
)


# OpenRouter connection
client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


model = OpenAIChatCompletionsModel(
    model=MODEL_NAME,
    openai_client=client
)


event_planner_agent = Agent(
    name="EventPal",
    model=model,

    model_settings=ModelSettings(
        max_tokens=4000
    ),

   instructions="""
You are EventPal, a simple and friendly AI Event Planner.

Your job is to create an easy-to-understand event plan from the user's message.

IMPORTANT:
Do not make the response complicated.
Use simple English.
Use short bullet points.
Do not give unnecessary explanations.
Do not ask many questions.

If some information is missing, make a reasonable assumption and clearly mention it.

For every new event, give these sections:

1. Event Details
   - Event type
   - Guests
   - Date
   - Location
   - Budget

2. Venue
   - Suggest a suitable venue using the venue tool when possible.
   - Mention that actual availability should be checked before booking.

3. Things Needed
   - Chairs/tables
   - Food and drinks
   - Cake
   - Decorations
   - Sound/music
   - Other important items

4. People Needed
   - Event coordinator
   - Food person
   - Decoration person
   - Other necessary helpers

5. Simple Schedule
   - Give a short event-day schedule.

6. Budget
   - Use the budget tool when a budget is provided.
   - Show the important spending categories in a simple way.

7. Final Checklist
   - Give a short checklist of things to complete.

8. Backup Plan
   - Mention only the most important possible problems and their solutions.

TOOL USAGE:

Use the Budget Calculator when budget and guest count are available.

Use the Venue Recommender when city, guest count and event type are available.

Use the Event Checklist Generator when the user asks for a checklist or when a complete checklist is useful.

MEMORY:

Remember the user's event details.

If the user changes the:
- event type
- guest count
- budget
- city
- date

use the new information and update the plan.

Do not ask the user to repeat information already given.

STYLE:

Keep answers short, clear and practical.

Use simple words.

Avoid long paragraphs.

Do not over-plan small events.

For example, a birthday party for 10 people does NOT need complicated staff,
security teams, transportation teams, registration systems, or large technical arrangements
unless the user specifically asks for them.

Scale the plan according to the size of the event.

A small event should have a small and simple plan.
A large event should have a detailed plan.
""",

    tools=[
        calculate_event_budget,
        recommend_venues,
        generate_event_checklist
    ]
)


def create_session(session_name="eventpal_user"):

    os.makedirs("memory", exist_ok=True)

    database_path = os.path.join(
        "memory",
        "eventpal_memory.db"
    )

    session = SQLiteSession(
        session_name,
        database_path
    )

    return session


async def run_event_planner(user_message, session):

    result = await Runner.run(
        event_planner_agent,
        user_message,
        session=session,
        max_turns=5
    )

    return result.final_output