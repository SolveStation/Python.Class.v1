from calculator import Calculator


class Animal:
    total_count = 0

    def __init__(self, name, age: int, gender):
        self.name = name
        self.gender = gender
        self.age = age
        Animal.total_count += 1

    def walk(self):
        print(f"{self.name} is Walking")

    def speak(self):
        print("I am speaking")


# goat = Animal("GOAT", 12, "Male")
# goat.walk()
# goat.speak()
# print(f"The Current Total Count is {goat.total_count}")

# cow = Animal("COW", 12, "Male")
# cow.walk()
# print(f"The Current Total Count is {Animal.total_count}")

Calculator.addition()
