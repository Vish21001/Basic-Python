answer = input("What is the command?")

while answer == "start":
    print("Car started...Ready to go!")
    answer = input("What is the command?")
while answer == "stop":
    print("Car stopped.")
    answer = input("What is the command?")
while answer == "quit":
    print("Quitting...")
    break
while answer == "help":
    print("""
start - to start the car
stop - to stop the car
quit - to quit
help - to show this help message
""")
    answer = input("What is the command?")
else:
    print("I don't understand that...")
    answer = input("What is the command?")
