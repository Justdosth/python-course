grade = float(input("Enter the grade="))
if 0 <= grade < 10:
    print("fail")
elif 10 <= grade < 15:
    print("good")
elif 15 <= grade < 18:
    print("very good")
elif 18 <= grade <= 20:
    print("excellent")
else:
    print("invalid grade")
