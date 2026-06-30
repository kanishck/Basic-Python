salary = int(input("Enter your monthly salary: "))
emp_type = int(input("Enter your employment type (1 Government, 2 Private, 3 Self-Employed): "))
credit_score = int(input("Enter your credit score: "))
active_loans = int(input("Enter the number of active loans you have: "))

if salary < 40000:
    print("Loan Rejected Salary Requirement Not Met")
else :
    print("Salary Verified")

    if emp_type == 1 and credit_score >= 700:
        print("Employement : Government")
        print("Credit Score Approved")
            
        if (active_loans < 2):
            print("Loan Approved")
        else:
            print("Loan Rejected Too Many Active Loans")
   
   
    if emp_type == 2 and credit_score >= 750:
        print("Employement : Private")
        print("Credit Score Approved")
        if active_loans < 2:
            print("Loan Approved")
        else:
            print("Loan Rejected Too Many Active Loans")
   
   
    if emp_type == 3 and credit_score >= 780:
        print("Employement : Self-Employed")
        print("Credit Score Approved")
        if active_loans < 2:
            print("Loan Approved")
        else:
            print("Loan Rejected Too Many Active Loans")

