class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

Josh = Person("Josh", 24)
Bob = Person("Bob", 30)

print(Josh.name)
print(Josh.age)

Josh.greet()

print(Bob.name)
print(Bob.age)

Bob.greet()