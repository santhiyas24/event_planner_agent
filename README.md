# EventPal - AI Event Planner

EventPal is a simple AI-powered event planning agent that creates a complete event plan from a user's event description.

The user can provide basic details such as the event type, number of guests, location, date, and budget. EventPal then generates the required arrangements, venue suggestions, budget allocation, checklist, schedule, and backup plan.

## Project Objective

Planning an event requires managing many small and large arrangements.

EventPal helps users organize all these requirements in one place by using an AI agent with memory and planning tools.

The agent can handle events such as:

- Birthdays
- College events
- Workshops
- Conferences
- Cultural events
- Hackathons
- Small functions

The complexity of the plan automatically changes according to the size and type of the event.

For example, a small birthday party does not require unnecessary security teams, transportation teams, or complex technical arrangements.

---

## Key Features

### 1. AI Event Planning

The user can describe an event in simple language.

Example:

> I want to organize a birthday party for 10 students in Cuddalore with a budget of ₹3000 on September 9.

EventPal understands the information and creates a structured event plan.

### 2. Complete Event Requirements

EventPal identifies the important requirements for the event, including:

- Event details
- Venue
- Guests
- Seating
- People and responsibilities
- Food and drinks
- Decorations
- Equipment
- Registration
- Communication
- Safety
- Permissions
- Budget
- Schedule
- Event-day activities
- Final checklist
- Backup plan

### 3. Budget Planning

The Budget Calculator divides the available budget into useful categories.

It calculates:

- Venue
- Food and beverages
- Decoration
- Equipment
- Staff and services
- Marketing and printing
- Transportation
- Safety and security
- Emergency reserve
- Miscellaneous expenses

### 4. Venue Recommendation

EventPal recommends suitable venues based on:

- City
- Number of guests
- Event type
- Available venue budget

The project contains a sample venue dataset for demonstration.

### 5. Complete Event Checklist

EventPal generates a checklist covering the planning process from preparation to completion.

The checklist includes:

- Planning
- Venue
- People
- Program
- Equipment
- Food
- Decoration
- Communication
- Safety
- Permissions
- Event day
- After-event activities

### 6. Memory

EventPal remembers previous conversations using SQLite.

This allows the user to continue planning without repeatedly providing the same event details.

Example:

**User:**
> Plan a birthday party for 10 students in Cuddalore.

**User:**
> Change the budget to ₹5000.

EventPal remembers the birthday event and updates the budget instead of starting from the beginning.

---

## AI Agent Architecture

The project uses three main components:

```text
User
  |
  v
EventPal AI Agent
  |
  +---- LLM
  |
  +---- Memory (SQLite)
  |
  +---- Budget Calculator
  |
  +---- Venue Recommender
  |
  +---- Event Checklist Generator