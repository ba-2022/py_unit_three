#Betel Alemu
#10/9/22
#This is adding two numbers and returning a value

def addTwo(firstNumber, secondNumber):
    total_value = firstNumber + secondNumber
    return total_value

def main():
    length = 3
    height = 10
    total_of_two_numbers = addTwo(length, height)
    print(total_of_two_numbers)

main()