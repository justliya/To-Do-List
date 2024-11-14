#List of numbers from 1 to 10
numbers=list(range(1,11))
#List comprehension to create a list of squares
squares=[number**2 for number in numbers]
print(numbers)
print(squares)


number=int(input("Enter a number:"))

if number % 2 == 0:
    print(f'{number} is even.')
else:
    print(f"{number} is odd.")

    # Initialize an empty list to store toppings
toppings = []

# Loop to collect toppings from the user
while True:
    topping = input("Enter a pizza topping (or 'done' to finish): ")
    if topping.lower() == 'done':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza!")

# Print all the toppings entered
print("\nYour pizza toppings are:")
for topping in toppings:
    print(f"- {topping}")