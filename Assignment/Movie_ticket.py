age = int(input("Enter your age : "))
price_1 = 12
price_2 = 8
day = input("Today is wednesday: ")
if day == "y" :
    amt = price_1 -2
    amt_1 = price_2 - 2
else :
    amt = price_1
    amt_1 = price_2
if age < 18 :
    print("Ticket price is $",amt_1)
else :
    print("Ticket price is $",amt)
