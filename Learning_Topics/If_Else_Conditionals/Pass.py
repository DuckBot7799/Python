my_score = int(input("Enter your score: "))

if 80 >= my_score >= 89:
    print("Good.")
elif my_score >= 90:
    print("VERY Good Job!")
elif 60 <= my_score <= 79:
    print("Well it's decent.")
elif my_score >= 50:
    print("It's Ok but do better next time.")
else:
    pass
