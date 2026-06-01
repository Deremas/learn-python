# ==================================================
# PYTHON GENERATORS
# ==================================================

# A generator is a special function that produces values one at a time.
# Instead of creating and storing all values in memory, it gives one value only when needed.

# Normal function:
# - uses return
# - returns the final result
# - usually creates a full list before returning

# Generator function:
# - uses yield
# - gives one value at a time
# - pauses after each yield
# - continues from the same place when the next value is requested

import random
import time
import sys


# Sample data
names = ["John", "Jane", "Corey", "Travis", "Dave", "Kurt", "Neil", "Sam", "Steve", "Tom"]
majors = ["Math", "Engineering", "Computer Science", "Arts", "Business"]


# ==================================================
# LIST APPROACH
# ==================================================

# In the list approach:
# 1. We create an empty list.
# 2. We generate each item.
# 3. We append each item to the list.
# 4. We return the full list.

# This is good when:
# - the data is small
# - we need len()
# - we need indexing like people[0]
# - we need to reuse the data many times

# But it can use a lot of memory for large data.

def people_list(num_people):
    result = []

    for i in range(num_people):
        person = {
            "id": i,
            "name": random.choice(names),
            "major": random.choice(majors)
        }

        result.append(person)

    return result


# ==================================================
# GENERATOR APPROACH
# ==================================================

# In the generator approach:
# 1. We do not create an empty list.
# 2. We do not use append().
# 3. We use yield to return one item at a time.
# 4. Python pauses the function after each yield.
# 5. The next value is created only when requested.

# This is good when:
# - the data is large
# - we process one item at a time
# - we want to save memory
# - we are reading big files
# - we are streaming data

def people_generator(num_people):
    for i in range(num_people):
        person = {
            "id": i,
            "name": random.choice(names),
            "major": random.choice(majors)
        }

        yield person


# ==================================================
# RETURN VS YIELD
# ==================================================

# return:
# - sends back a value
# - ends the function completely

# yield:
# - sends back a value
# - pauses the function
# - continues later from the same place


# ==================================================
# TEST LIST VERSION
# ==================================================

print("LIST VERSION")
print("-" * 40)

start_time = time.perf_counter()

people = people_list(1_000_000)

end_time = time.perf_counter()

print(f"Time taken: {end_time - start_time:.4f} seconds")
print(f"Number of people: {len(people)}")
print(f"First person: {people[0]}")
print(f"List object size only: {sys.getsizeof(people)} bytes")


# ==================================================
# TEST GENERATOR VERSION
# ==================================================

print("\nGENERATOR VERSION")
print("-" * 40)

start_time = time.perf_counter()

people_gen = people_generator(1_000_000)

end_time = time.perf_counter()

print(f"Time taken to create generator: {end_time - start_time:.4f} seconds")
print(f"Generator object size: {sys.getsizeof(people_gen)} bytes")

print("\nGetting first 5 people from generator:")

for _ in range(5):
    print(next(people_gen))


# ==================================================
# IMPORTANT DIFFERENCE
# ==================================================

print("\nIMPORTANT DIFFERENCE")
print("-" * 40)
print("The list created and stored 1,000,000 people immediately.")
print("The generator did not create 1,000,000 people immediately.")
print("The generator creates each person only when we ask for the next item.")


# ==================================================
# SMALL SIMPLE EXAMPLE
# ==================================================

def number_list():
    result = []

    for i in range(5):
        result.append(i)

    return result


def number_generator():
    for i in range(5):
        yield i


print("\nSMALL LIST EXAMPLE")
print("-" * 40)

nums_list = number_list()

print(nums_list)
print(nums_list[0])
print(len(nums_list))


print("\nSMALL GENERATOR EXAMPLE")
print("-" * 40)

nums_gen = number_generator()

print(nums_gen)

for num in nums_gen:
    print(num)


# ==================================================
# IMPORTANT GENERATOR RULE
# ==================================================

# A generator can be used only once.
# After it has finished producing values, it becomes exhausted.
# To use it again, create a new generator object.

print("\nGENERATOR USED ONLY ONCE EXAMPLE")
print("-" * 40)

nums_gen = number_generator()

print("First loop:")
for num in nums_gen:
    print(num)

print("Second loop:")
for num in nums_gen:
    print(num)

print("The second loop prints nothing because the generator is already exhausted.")


# ==================================================
# FINAL SUMMARY
# ==================================================

# LIST:
# - uses return
# - creates all items immediately
# - stores all items in memory
# - can be reused
# - supports len()
# - supports indexing

# GENERATOR:
# - uses yield
# - creates one item at a time
# - saves memory
# - can be looped only once
# - does not support len() directly
# - does not support indexing directly

# Main idea:
# List      = build everything first, then use it.
# Generator = produce one item only when needed.
