CGPA = float(input("Enter the candidate's CGPA : "))
AptMarks = int(input("Enter the Aptitude marks : "))
TechRound = int(input("Enter the Technical round marks : "))
HRRound = int(input("Enter the HR interview rating : "))

if CGPA < 7:
    print("Application Rejected")
else:
    print("CGPA Verified")
    if AptMarks < 60:
        print("Application Rejected")
    elif AptMarks < 79:
        print("Technical Round")
        if TechRound > 70:
            print("Technical Round Cleared")
            if HRRound > 3:
                print("You are Selected!!")
            elif HRRound == 3:
                print("Waiting List")
            else:
                print("Rejected")
        else: 
            print("Rejected in technical round")
    else:
        print("Qualified for Direct Technical + HR")
        if TechRound > 70:
            print("Technical Round Cleared")
            if HRRound > 3:
                print("You are Selected!!")
            elif HRRound == 3:
                print("Waiting List")
            else:
                print("Rejected")
        else: 
            print("Rejected in technical round")