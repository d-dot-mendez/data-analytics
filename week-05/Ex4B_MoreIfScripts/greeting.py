time = int(input("Please go by military time. What hour of the day is it?") )

if time >= 0 and time <=  4:
    print("What are you doing up so late?")
elif time > 4 and time <= 10:
    print("Good morning!")
elif time > 10 and time < 17:
    print("Good day!")
elif time >17 and time < 23:
    print("Good evening!")
elif time == 23:
    print("What are you doing up so late?")