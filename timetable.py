monday = ('\nMonday \n1 Maths\n2 English\n3 Science\n4 Science\n5 Info Tech\n6 History')
tuesday = ('\nTuesday \n1 History\n2 History\n3 Science\n4 English\n5 Maths\n6 Geography')
wednesday = ('\nWednesday \n1 Science\n2 English\n3 Info Tech\n4 Geography\n5 Geography\n6 History')
thursday = ('\nThursday \n1 English\n2 Science\n3 Geography\n4 History\n5 Info Tech\n6 Info Tech')
friday = ('\nFriday \n1 English\n2 Science\n3 Math\n4 Maths\n5 Info Tech\n6 History')

day = input("What day do you want to display the timetable for?\n- Monday\n- Tuesday\n- Wednesday\n- Thursday\n- Friday\n").lower()

if day == "monday": 
    print(monday)
elif day == "tuesday":
    print(tuesday)
elif day == "wednesday":
    print(wednesday)
elif day == "thursday":
    print(thursday)
elif day == "friday":
    print(friday)

else:
    print("you entered an invalid day, restart this proccess and make sure your input is correct")