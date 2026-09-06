# EventPal - AI Event Planner

EventPal is an AI-powered event planning agent that creates a complete event plan from a simple user description.

## Features

- AI-powered event planning
- Persistent memory using SQLite
- Budget calculation
- Venue recommendation
- Complete event checklist
- Handles small and large event requirements
- Remembers previous event details
- CLI-based application
- No frontend required

## Project Structure

event_planner_agent/
│
├── data/
│   └── venues.json
│
├── memory/
│
├── main.py
├── agent.py
├── tools.py
├── requirements.txt
├── .env
└── README.md

## Three Tools

### 1. Budget Calculator

Calculates an estimated event budget and divides it into categories such as:

- Venue
- Food
- Decoration
- Equipment
- Staff
- Marketing
- Transportation
- Safety
- Emergency reserve
- Miscellaneous

### 2. Venue Recommender

Recommends suitable venues based on:

- City
- Number of guests
- Event type
- Venue budget

The venue data is stored in `data/venues.json`.

### 3. Event Checklist Generator

Generates a complete checklist covering:

- Planning
- Venue
- Staff
- Program
- Equipment
- Food
- Decoration
- Registration
- Safety
- Permissions
- Event day
- Post-event activities

## Memory

EventPal uses SQLite session memory to remember previous conversations.

The database is automatically created inside:

memory/eventpal_memory.db

This allows users to continue discussing the same event without repeating all details.

## Installation

Create and activate a virtual environment:

```bash
python -m venv venv