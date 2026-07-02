Membership = int(input("Which membership do you have( 1(Gold), 2(Silver), 3(Regular)) : "))
OrderValue = int(input("what is total order value for your order : "))
Distance = float(input("Enter the delivery distance : "))
PaymentMode = input(" How are you paying?")

del_charge = 0


if(Membership == 1):
    if(OrderValue >= 300):
        print("Order Accepted")
        if(Distance >10):
            del_charge = 80
        elif(Distance>5 and Distance<=10):
            del_charge = 40
        if (PaymentMode == "UPI"):
            print("Cashback : 50")
        print(f"Delivery charge : {del_charge}")

elif(Membership == 2):
     if(OrderValue >= 500):
        print("Order Accepted")
        if(Distance >10):
            del_charge = 80
        elif(Distance>5 and Distance<=10):
            del_charge = 40
        if (PaymentMode == "UPI"):
            print("Cashback : 50")
        print(f"Delivery charge : {del_charge}")

elif(Membership == 3):
     if(OrderValue >= 700):
        print("Order Accepted")
        if(Distance >10):
            del_charge = 80
        elif(Distance>5 and Distance<=10):
            del_charge = 40
        if (PaymentMode == "UPI"):
            print("Cashback : 50")
        print(f"Delivery charge : {del_charge}")

else:
    print("Invalid Membership")
            