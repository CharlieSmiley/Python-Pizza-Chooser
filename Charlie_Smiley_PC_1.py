'''
Charlie Smiley
Program Challenge 1
Due: Sept. 2, 2024
IS 310-02
'''
#Variable holding name of customer
name = ""

#Loop created to recieve name of customer
while name == "":
    print("Enter your name.")
    name = input().capitalize()

#Greets customer once name is given
print("Hello {}. Welcome to the python Pizza chooser.".format(name))

#Variable holding name of pizza and count of pizzas
pizza = ""
count = 0

#Ask customers what pizza they want
print("Would you like to order a cheese pizza, pepperoni pizza, or a supreme pizza.")
pizza = input().lower()

#Loop to valiadate pizza entered
while pizza != "no":
    if pizza in ["cheese", "pepperoni", "supreme", "no"]:
        #Checks to see if entry i valid
        if pizza == "no":
            #If entry is "no" exits loop
            break
        else:
            #If entry is valid asks if more pizza is wanted and adds 1 to the count
            print("Would you like to order a cheese pizza, pepperoni pizza, or a supreme pizza.")
            pizza = input().lower()
            count += 1
    else:
        #If entry is invalid asks for valid entry
        print("You may choose to order a cheese pizza, pepperoni pizza, or a supreme pizza only. Please choose again.")
        pizza = input().lower()

#Thanks customer for entry and prints out amount of pizzas ordered
print("Thank you {}. The {} pizzas you ordered will be ready in 30 minutes.".format(name, count))
