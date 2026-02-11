Fruit = "Banana"
print("1. Yellow" \
"2. Green" \
"3. Brown")

color = int(input("choose number: "))

if color == 1:
    print(Fruit, "is ripe")
elif color == 2 :
    print(Fruit, "is unripe")
else :
    print(Fruit, "is overripe")