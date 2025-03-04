def main():
  print("Hello learners!")

# Function to add multiple numbers
def addmultiplenumbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Function to multiply multiple numbers
def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Function to check if a number is even
def isiteven(num):
    return num % 2 == 0

# Function to check if a number is an integer
def isitaninteger(num):
    return float(num).is_integer()

# Main function
def main():
    while True:
        print("\nChoose an operation:")
        print("1. Add multiple numbers")
        print("2. Multiply multiple numbers")
        print("3. Check if a number is even")
        print("4. Check if a number is an integer")
        print("5. Exit")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == '5':
            break
        
        if choice == '1':
            numbers = list(map(float, input("Enter numbers separated by space: ").split()))
            result = addmultiplenumbers(numbers)
        
        elif choice == '2':
            numbers = list(map(float, input("Enter numbers separated by space: ").split()))
            result = multiplymultiplenumbers(numbers)
        
        elif choice == '3':
            num = float(input("Enter a number: "))
            result = isiteven(num)
        
        elif choice == '4':
            num = float(input("Enter a number: "))
            result = isitaninteger(num)
        
        
        
        print(f"Result: {result}")

if __name__ == "__main__":
  main()

#QUESTION
''' *addmultiplenumbers([num, num, ..]) - this function must exist in your program, it should take a list of numbers as input, and it should output the sum of those numbers.
* multiplymultiplenumbers([num, num, ..]) - this function must exist in your program, it should take a list of numbers as input, and it should output the result of multiplying each number in turn with the following number.
* isiteven(num) - this function must exist in your program, it should take a single number as input, and it should output a boolean value - True if the number is an even, whole number, False otherwise.
* isitaninteger(num) - this function must exist in your program, it should take a single number as input, and it should output a boolean value - True if the number is an integer, False otherwise. '''