#car game(exercise)
command = ''
started = False
while command !="quit":
    command = input(">>> ").lower()
    if command=="start":
        if started:
            print("car is already started")
        else:
            started=True
            print("engine start......\n ready to go")
    elif command=="go":
        if not started:
            print("car is stopped")
        else:
            started=True
            print("car is on road.........go go go")
    elif command=="stop":
        if not started:
            print("car is already stopped")
        else:
            started=False
            print("car stopped....")
    elif command=="help":
        print("start-start the car\n go-engine start\n stop-stop the car\n quit-to quit")
    elif command=="quit":
        break
    else:
        print("sorry i dont understand that")