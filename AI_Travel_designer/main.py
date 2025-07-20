

def main():
    print("🧳 Welcome to AI Travel Designer!")
    print("Tell us your mood or interest (e.g., relaxing, adventure, history):")
    mood = input("💬 Your Input: ")

    print("\n🎯 Choosing destination...")
    destination = f"🏖️  Based on '{mood}', try: Bali"  # Mocked response
    print(destination)

    print("\n📦 Booking travel...")
    flight_hotel_info = ("booking_agent", destination)
    print(flight_hotel_info)

    print("\n🍽️  Explore suggestions...")
    explore = f"🏞️  Must-visit: Ubud Monkey Forest\n🍜 Try: Babi Guling"
    print(explore)

    print("\n✅ Your trip is planned! Bon Voyage! 🌍")

if __name__ == "__main__":
    main()
