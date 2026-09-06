import asyncio
import os

from dotenv import load_dotenv
from agent import create_session, run_event_planner


load_dotenv()


async def main():

    print("=" * 60)
    print("              EVENTPAL - AI EVENT PLANNER")
    print("=" * 60)
    print("Tell me about your event, and I will create a complete plan.")
    print("Type 'exit' or 'quit' to stop.")
    print("=" * 60)

    # Check API key
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("\nERROR: OPENAI_API_KEY is not configured in .env")
        return

    # Create persistent memory session
    session = create_session("eventpal_user")

    while True:

        try:
            user_message = input("\nYou: ").strip()

        except (KeyboardInterrupt, EOFError):
            print("\n\nEventPal stopped.")
            break

        # Ignore empty messages
        if not user_message:
            continue

        # Exit commands
        if user_message.lower() in ["exit", "quit"]:
            print("\nEventPal: Goodbye! 👋")
            break

        try:
            # Send message to AI agent
            response = await run_event_planner(
                user_message,
                session
            )

            print("\nEventPal:")
            print(response)

        except Exception as error:

            print("\nSomething went wrong.")
            print("Error:", error)


if __name__ == "__main__":
    asyncio.run(main())