# Simple If-else statement

marks = 80

if (marks >= 90 and marks <= 100):
    print("Grade: A")
elif (marks >= 80 and marks < 90):
    print("Grade: B")
elif (marks >= 70 and marks < 80):
    print("Grade: C")
elif(marks >= 60 and marks < 70):
    print("Grade: D")
else:
    print("Grade: F")

# Nested If-else statement

is_allowed = True
friends_available = True

if is_allowed:
    if friends_available:
        print("You can go out with your friends.")
    else:
        print("You cannot go out with your friends.")
else:
    print("You are not allowed to go out.")