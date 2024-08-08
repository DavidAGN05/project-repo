grade = int(input("What is your score?\n"))
if 90 <= grade <= 100:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
elif 0 <= grade < 60:
    print("Grade: F")
else:
    print("Invalid Grade")
