lives = 1

while lives > 0:
    answer = input("What is 6 * 6? ")

    if answer == "36":
        print("🎉 Correct!")
        break
    else:
        lives -= 1
        print("❌ Wrong! Lives left:", lives)

if lives == 0:
    print("💀 Game Over!,answer is 36")
