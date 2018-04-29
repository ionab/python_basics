def say_hello():
    print("Hello World!")

say_hello()

def greet(name):
    if(name) == "Ally":
        print("Hi, " + name)
    else:
        print("I don't know you!")


greet("Ally")
greet("Kelsie")


favourite_foods = ["Pizza", "Cake", "Falafel"]
print(favourite_foods[0])
print(favourite_foods.pop())
print(favourite_foods.count("Pizza"))
print(len(favourite_foods))
print("Pizza" in favourite_foods)

for food in favourite_foods:
    print(food)
print("Loop has finished")

# python doesnt have an end funtion
import numpy as np
array1 = np.array([2,4,6])
array2 = np.array([1,3,5])
print(array1*array2)

person = {
    "name": "Kelsie",
    "favourite_foods": ["Pizza", "Cake", "Falafel"]
}

print(person["name"])

for food in person["favourite_foods"]:
    print food
