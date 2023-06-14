class  Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print("bow bow!")

# main function

sohan = Dog("rocky",4)

print(sohan.name)
print(sohan.age)

sohan.bark()
