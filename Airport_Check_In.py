IfPassport = int(input("Do you have a valid passport? (0/1):"))
visa = int(input("Do you have a valid visa? (0/1):"))
BaggageWeight = int(input("Enter your baggage weight in kg: "))
ArrivalTime = int(input("How many hours before the flight are you arriving at the airport?"))

if IfPassport==1 :
    print("Passport is valid.")
    if visa==1 :
        print("Visa is valid.")
        if BaggageWeight <= 20 :
            print("Baggage weight is within limit.")
            if ArrivalTime >= 2 :
                print("Boarding Pass Generated")
            else :
                print("Late Arrival. Boarding Cancelled")
        elif (BaggageWeight > 20 and BaggageWeight <= 30) :
            print("Extra charge of 1500 for baggage.")
            if ArrivalTime >= 2 :
                print("Boarding Pass Generated")
            else :
                print("Late Arrival. Boarding Cancelled")
        else :
            print("Baggage not allowed.")
    else :
        print("Visa is not valid. Boarding Cancelled")
else :
    print("Passport is not valid. Boarding Cancelled")
        