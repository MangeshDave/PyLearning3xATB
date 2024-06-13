# Write a program to display grade of students based on their score

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

Score = int(input("Enter your score"))

if Score <= 100 and Score >= 90:
    print("Grade is A")
elif Score < 90 and Score >= 80:
    print("Grade is B")
elif Score < 80 and Score >= 70:
    print("Grade is C")
elif Score < 70 and Score >= 60:
    print("Grade is D")
elif Score > 0 and Score <= 59:
    print("Grade is F")
else:
    print("Invalid score")
