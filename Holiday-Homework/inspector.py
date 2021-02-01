import time

print("Hello there!")
print("What's your name?")
name = input()
print("Hello there, " + name)
time.sleep(2)
print("You have arrived at a horror mansion!\nIt's a large and spooky house with strange noises coming from inside")
time.sleep(2)
print("You hop out of the car and walk closer...")
time.sleep(2)
print("You tread carefully onto the rotten woodpath porch.")
time.sleep(2)
print("You trip over a loose plank of wood and fall over")
time.sleep(2)
print("Your knee hurts. But you notice something under the porch...")
time.sleep(2)
print("It's a box...")
time.sleep(2)
print("Inside it was a blooded hand!")
time.sleep(2)
print("You wonder wether to go inside or leave...")

question = input("What is your next move?\n - Type in `inside` to go inside the house\n - Type in `leave` to leave away!\n")

if question == "inside":
    print("you pick yourself up and head inside the house and only to be greated with a mysterious character, the door slams behind you and you are trapped!")

if question == "leave":
    print("you rush back into your car and drift away, very far!")

