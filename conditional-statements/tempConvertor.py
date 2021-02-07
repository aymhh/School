method = input('What would you like to convert? (Input the letter)\nA) Fahrenheit -> Celsius?\nB) Celsius -> Fahrenheit\n')

if (method.lower() == "a"):
    value = input("What's the value you want to convert to?\n")      
    updatedValue = int(value)
    x = round((updatedValue - 32) * 5/9, 2)
    print(f"{value} fahrenhiet -> {x} celsius") 

if (method.lower() == "b"):
    value = input("What's the value you want to convert to?\n")
    updatedValue = int(value)
    x = round((updatedValue* 9/5) + 32, 2)
    print("The answer is: " + str(x) + "\n") 
