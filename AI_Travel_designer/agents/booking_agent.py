
from tools.get_flights import get_flights
from tools.suggest_hotels import suggest_hotels

def booking_logic(destination):
    flight = get_flights(destination)
    hotel = suggest_hotels(destination)
    return f"{flight}\n{hotel}"

BookingAgent = Agent(
    name="booking_agent",
    instructions="Book flights and hotels based on the selected destination.",
    description="📦 Mocks booking for travel.",
    tools=[get_flights, suggest_hotels],
    handle=booking_logic
)
