import math
import sys

#### Simple Python Program with various Tasks ####
def start():
    print("\n\n1. Print numbers 1 through 5.\n"
      "2. Print sum of 3 and 5.\n"
      "3. Print sum of constant Pi and square root of 2.\n"
      "4. Print sum of cos30 + sin30 Where cos and sin are trig functions and angle specified is in degrees.\n"
      "5. Write code to print values of interger x, y, and z in a single line such that each value is left justified in 6 columns.\n"
      "6. write code to print area of a circle given the value of the radius of the circle.\n"
      "7. Write code to print the greater of two given numbers x and y\n"
      "8. Write code to print the result of negation of AND of two Boolean variables A and B.\n"
      "9. Write a for loop to sum the first 10 non-zero intergers.\n"
      "10. Write a while-loop to sum the first 10 non-zero intergers.\n")

    global task
    task = input("Please select the task that you wish to complete. ")
    print("You have selected option: " + task)
    ops()

def task1():
    for x in range(6):
        if x >= 1:
            print(x)

def task2():
    print("\nModule for simple addition!\n")
    x = input("Please enter the first number. ")
    y = input("Please enter the second number. ")
    result = float(x) + float(y)
    print(result)

def task3():
    print("\nThe sum of Pi and the square root of 2 is: ")
    value = math.pi * 2**2
    print(value)

def task4():
    print(("\nSimple math function with Cos and Sin: "))
    angle = int(input("Input Degrees: "))
    print("You have entered: " + str(angle))
    radian = math.radians(angle)
    result = math.cos(radian) + math.sin(radian)
    print(result)

def task5():
    print("\nSpacing numbers is as easy as: ")
    x, y, z = 1, 2, 3
    print("%-6d %-6d %-6d" %(x, y, z))

def task6():
    radius = float(input(("\nEnter the radius of a cicle: ")))
    area = math.pi * radius ** 2
    print(area)

def task7():
    x = input("Enter your first Number: ")
    y = input("Enter your second Number: ")
    if x>y:
        print(x)
    else:
        print(y)

#def task8()

def task9():
    sum = 0
    num = 10
    for i in range(1, num + 1):
        sum += i
    print(sum)
    
def task10():
    total = 0
    num = 1
    while num <= 10:
        total += num
        num += 1
    print(total)

def ops():
    match task:
        case "1":
            return task1()
        case "2":
            return task2()
        case "3":
            return task3()
        case "4":
            return task4()
        case "5":
            return task5()
        case "6":
            return task6()
        case "7":
            return task7()
        case "9":
            return task9()
        case "10":
            return task10()       
try:
    start()
except KeyboardInterrupt:
    print("Exiting Program!")
