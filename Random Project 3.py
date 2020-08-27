is_started = False
while True:
    command = input(">").lower()
    if command == "start":
        if not is_started:
            print("Car Started")
            is_started = True
        else:
            print("Car already on.")
    elif command == "stop":
        if is_started:
            print("Car Stopped")
            is_started = False
        else:
            print("Car is already stopped.")
    elif command == "help":
        print("""
"start : start the car"
"stop : stop the car"
"quit : quit the game"
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand that...")
