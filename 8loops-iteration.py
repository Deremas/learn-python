# Loops and Iteration
# For Loop
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number) # Output: 1, 2, 3, 4, 5 (iterating over a list)

# Break and Continue
# Break: The break statement is used to exit a loop prematurely when a certain condition is met.
for number in numbers:
    if number == 3:
        break  # Exit the loop when number is 3
    print(number) # Output: 1, 2 (iterating over a list and breaking the loop when number is 3)

# Continue: The continue statement is used to skip the rest of the code inside a loop for the current iteration and move to the next iteration.
for number in numbers:
    if number == 3:
        continue  # Skip the rest of the loop when number is 3
    print(number) # Output: 1, 2, 4, 5 (iterating over a list and skipping the number 3)
# Nested Loops
# Nested loops are loops that are contained within another loop. The inner loop is executed for each iteration of the outer loop.
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f'i: {i}, j: {j}')  # Output: i: 1, j: 1; i: 1, j: 2; i: 1, j: 3; i: 2, j: 1; i: 2, j: 2; i: 2, j: 3; i: 3, j: 1; i: 3, j: 2; i: 3, j: 3 (iterating over a range of numbers with nested loops)

# While Loop
# A while loop is a control flow statement that allows code to be executed repeatedly based on a given boolean condition. The loop will continue to execute as long as the condition is true.
# The syntax of a while loop is:
  # while condition:
  #     # code to execute

count = 0
while count <10:
    # if count == 5:
    #     break  # Exit the loop when count is 5
    print(count) # Output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (iterating while count is less than 10)
    count += 1