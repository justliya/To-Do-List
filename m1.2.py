#User inputs exam score

exam_score=int(input("Enter score:"))

if exam_score > 90:
    print('Excellent')
elif exam_score >= 70 and exam_score <= 90:
    print("Good")
else: 
    print("Needs improvement")