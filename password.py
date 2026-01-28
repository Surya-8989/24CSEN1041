correct_password = "python123"
attempts = 2

while attempts > 0:
    password = input("Enter password: ")

    if password == correct_password:
        print("✅ Access Granted")
        break
    else:
        attempts -= 1
        print("❌ Wrong password! Attempts left:", attempts)

        # Give hint after the first wrong attempt
        if attempts == 1:
            print("💡 Hint: It starts with 'py' and ends with '123'")

if attempts == 0:
    print("🔒 Access Denied")
