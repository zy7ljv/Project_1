print("""You enter a dark room with two doors.
      do you go through door #1 or door #2? """)

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. kick the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face pff. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    elif bear == "3":
        print("Bear eats your toes away")
    else:
        print(f"Well, doing {bear} is probable better.")
        print("bear runs away")

elif door == "2":
    print("you stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket Clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")






