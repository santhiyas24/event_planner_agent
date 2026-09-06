import json
import os

from agents import function_tool


# ============================================================
# TOOL 1: EVENT BUDGET CALCULATOR
# ============================================================

@function_tool
def calculate_event_budget(
    total_budget: float,
    guests: int,
    event_type: str
) -> dict:
    """
    Calculates an estimated budget for an event.
    """

    if total_budget <= 0:
        return {
            "error": "Budget must be greater than zero."
        }

    if guests <= 0:
        return {
            "error": "Number of guests must be greater than zero."
        }

    # Percentage allocation for different event requirements
    allocation = {
        "venue": 0.20,
        "food_and_beverages": 0.25,
        "decoration_and_branding": 0.10,
        "equipment_and_technology": 0.10,
        "staff_and_services": 0.08,
        "marketing_and_printing": 0.05,
        "transportation": 0.05,
        "safety_and_security": 0.05,
        "emergency_reserve": 0.07,
        "miscellaneous": 0.05
    }

    budget_breakdown = {}

    for category, percentage in allocation.items():
        budget_breakdown[category] = round(
            total_budget * percentage,
            2
        )

    cost_per_guest = round(
        total_budget / guests,
        2
    )

    return {
        "event_type": event_type,
        "guests": guests,
        "total_budget": total_budget,
        "cost_per_guest": cost_per_guest,
        "budget_breakdown": budget_breakdown,
        "note": (
            "This is an estimated planning budget. "
            "Actual costs depend on vendors, location and "
            "event requirements."
        )
    }


# ============================================================
# TOOL 2: VENUE RECOMMENDER
# ============================================================

@function_tool
def recommend_venues(
    city: str,
    guests: int,
    event_type: str,
    max_venue_budget: float = 0
) -> dict:
    """
    Recommends suitable venues from the sample venue dataset.
    """

    if guests <= 0:
        return {
            "error": "Number of guests must be greater than zero."
        }

    # Find venues.json
    file_path = os.path.join(
        os.path.dirname(__file__),
        "data",
        "venues.json"
    )

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            venues = json.load(file)

    except FileNotFoundError:
        return {
            "error": "venues.json file was not found."
        }

    city_lower = city.strip().lower()
    event_lower = event_type.strip().lower()

    matching_venues = []

    # First: find exact city + capacity + event type + budget
    for venue in venues:

        venue_city = venue["city"].lower()

        venue_event_types = [
            event.lower()
            for event in venue["event_types"]
        ]

        city_match = venue_city == city_lower

        capacity_match = (
            venue["capacity"] >= guests
        )

        event_match = (
            event_lower in venue_event_types
        )

        budget_match = (
            max_venue_budget <= 0
            or venue["approximate_rent"] <= max_venue_budget
        )

        if (
            city_match
            and capacity_match
            and event_match
            and budget_match
        ):
            matching_venues.append(venue)

    # If no exact event match,
    # search using city + capacity + budget
    if not matching_venues:

        for venue in venues:

            city_match = (
                venue["city"].lower() == city_lower
            )

            capacity_match = (
                venue["capacity"] >= guests
            )

            budget_match = (
                max_venue_budget <= 0
                or venue["approximate_rent"] <= max_venue_budget
            )

            if (
                city_match
                and capacity_match
                and budget_match
            ):
                matching_venues.append(venue)

    # Return maximum 5 venues
    matching_venues = matching_venues[:5]

    if not matching_venues:
        return {
            "city": city,
            "guests": guests,
            "event_type": event_type,
            "venues": [],
            "message": (
                "No suitable venue was found in the sample dataset. "
                "Try another city, guest count or venue budget."
            )
        }

    return {
        "city": city,
        "guests": guests,
        "event_type": event_type,
        "venues": matching_venues,
        "note": (
            "Venue information comes from the project's "
            "sample dataset and should be verified before "
            "making real bookings."
        )
    }


# ============================================================
# TOOL 3: COMPLETE EVENT CHECKLIST GENERATOR
# ============================================================

@function_tool
def generate_event_checklist(
    event_type: str,
    guests: int,
    days_before_event: int = 30
) -> dict:
    """
    Generates a complete checklist for organizing an event.
    """

    if guests <= 0:
        return {
            "error": "Number of guests must be greater than zero."
        }

    if days_before_event <= 0:
        days_before_event = 30

    checklist = {

        # ----------------------------------------------------
        # PLANNING
        # ----------------------------------------------------

        "planning": [
            "Define event objective",
            "Finalize event date",
            "Prepare estimated budget",
            "Create organizing team",
            "Assign responsibilities",
            "Prepare event schedule"
        ],

        # ----------------------------------------------------
        # VENUE
        # ----------------------------------------------------

        "venue": [
            "Select suitable venue",
            "Check venue capacity",
            "Confirm seating arrangement",
            "Check parking facilities",
            "Check restrooms",
            "Check electricity and backup power",
            "Confirm venue booking",
            "Check venue rules and restrictions"
        ],

        # ----------------------------------------------------
        # PEOPLE AND STAFF
        # ----------------------------------------------------

        "people_and_staff": [
            "Event coordinator",
            "Registration team",
            "Volunteers",
            "Stage coordinator",
            "Technical team",
            "Food service team",
            "Security team",
            "First-aid support",
            "Cleaning team"
        ],

        # ----------------------------------------------------
        # PROGRAM
        # ----------------------------------------------------

        "program": [
            "Prepare event agenda",
            "Finalize speakers or guests",
            "Confirm performers or participants",
            "Prepare announcements",
            "Prepare stage schedule",
            "Assign time slots",
            "Prepare backup activities"
        ],

        # ----------------------------------------------------
        # EQUIPMENT AND TECHNOLOGY
        # ----------------------------------------------------

        "equipment_and_technology": [
            "Microphones",
            "Speakers",
            "Amplifier",
            "Projector",
            "Laptop",
            "Display screen",
            "Extension boards",
            "Power cables",
            "Internet connection",
            "Power backup",
            "Lighting equipment"
        ],

        # ----------------------------------------------------
        # FOOD AND GUEST FACILITIES
        # ----------------------------------------------------

        "food_and_guest_facilities": [
            "Estimate food quantity",
            "Select caterer",
            "Arrange drinking water",
            "Plan food serving area",
            "Arrange guest seating",
            "Arrange special dietary requirements",
            "Arrange waste collection"
        ],

        # ----------------------------------------------------
        # DECORATION AND BRANDING
        # ----------------------------------------------------

        "decoration_and_branding": [
            "Stage decoration",
            "Entrance decoration",
            "Banners",
            "Posters",
            "Directional signs",
            "Name boards",
            "Event branding",
            "Photo area if required"
        ],

        # ----------------------------------------------------
        # REGISTRATION AND COMMUNICATION
        # ----------------------------------------------------

        "registration_and_communication": [
            "Create registration form",
            "Prepare attendee list",
            "Prepare badges or passes",
            "Send invitations",
            "Send event reminders",
            "Prepare contact list",
            "Prepare emergency contact information"
        ],

        # ----------------------------------------------------
        # SAFETY AND SECURITY
        # ----------------------------------------------------

        "safety_and_security": [
            "Prepare emergency plan",
            "Arrange security personnel",
            "Keep first-aid kit",
            "Identify emergency exits",
            "Check fire safety equipment",
            "Maintain crowd control",
            "Keep emergency contact numbers",
            "Prepare evacuation procedure"
        ],

        # ----------------------------------------------------
        # PERMISSIONS
        # ----------------------------------------------------

        "permissions": [
            "Check venue permissions",
            "Check local authority requirements",
            "Obtain required event permissions",
            "Confirm music or performance permissions if required",
            "Confirm insurance requirements if applicable"
        ],

        # ----------------------------------------------------
        # EVENT DAY
        # ----------------------------------------------------

        "event_day": [
            "Inspect venue",
            "Test sound system",
            "Test projector and displays",
            "Check lighting",
            "Check seating",
            "Check registration desk",
            "Check food arrangements",
            "Brief volunteers",
            "Brief security team",
            "Keep emergency contacts ready",
            "Follow event schedule",
            "Monitor crowd and facilities"
        ],

        # ----------------------------------------------------
        # AFTER EVENT
        # ----------------------------------------------------

        "after_event": [
            "Collect equipment",
            "Clean venue",
            "Check for lost items",
            "Settle vendor payments",
            "Collect feedback",
            "Review event performance",
            "Prepare final expense report"
        ]
    }

    return {
        "event_type": event_type,
        "expected_guests": guests,
        "planning_window": (
            f"{days_before_event} days before event"
        ),
        "checklist": checklist,
        "note": (
            "This checklist is a general planning guide. "
            "Additional requirements may depend on the event "
            "type, venue and local regulations."
        )
    }