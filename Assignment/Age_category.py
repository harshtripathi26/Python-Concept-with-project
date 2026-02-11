user = int(input("Enter your age: "))

if user < 13 :
    print("Child")
elif user >= 13 and user < 19:
    print("Teenager")
elif user >= 19 and user <= 59 :
    print("Adults")
else :
    print("Seniors")