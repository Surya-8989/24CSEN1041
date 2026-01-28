hungry = input("Are you hungry? (yes / no): ").lower()
mood = input("What is your mood? (happy / sad / tired): ").lower()
money = int(input("How much money do you have? ₹"))

if hungry == "yes":
    if money >= 150:
        print("\n🍕 Pizza time!")

        if mood == "happy":
            print("😄 Extra cheese because you're happy!")
        elif mood == "tired":
            print("😴 Quick delivery ordered!")
        elif mood == "sad":
            print("💖 Comfort pizza coming up!")
        else:
            print("🙂 Regular pizza ordered.")
    else:
        print("\n💸 Not enough money for pizza.")
        print("🍜 Instant noodles instead!")
else:
    print("\n🙂 You're not hungry right now.")
    print("☕ Maybe just have a drink.")
