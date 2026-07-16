while True:
    try:
        number = float(input("Enter a number: "))
        break

    except ValueError:
        print("You have given invalid input.")

print("You entered:", number)
