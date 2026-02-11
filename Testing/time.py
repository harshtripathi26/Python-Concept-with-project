import time
timestamp = (time.strftime("%H:%M:%S"))

print(timestamp)
timestamp = int(time.strftime("%H%M%S"))
print(timestamp)
if timestamp > 000000 and timestamp < 120000:
    print("Good Morning")
elif timestamp > 120000 and timestamp < 180000:
    print("Good Afternoon")
else:
    print("Good Night")