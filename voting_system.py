import sys
class VotingSystem:

    def __init__(self, name, age, number, address):
        self.name = name
        self.age = age
        self.number = number
        self.address = address

    def registration(self):
       pass


# try:
#     name = str(input("enter FullName :\t"))
#     age = int(input("enter Age:\t"))
# except :
#     print(f"invalid input {age} for age")
# else:
#     if age <= 17:
#         print(f"{name} You are not eligible for registeration, your age is {age}, minimus age required is 18")
#     else:
#         print(f"{name} You are eligible for registeration")
#         exit()
# finally:
#     pass

def validate(name, age):

    if age <= 17:
        print(f"{name} You are not eligible for registeration, your age is {age}, minimus age required is 18")
        return 1
    else:
        print(f"{name} You are eligible for registeration")
        return 0

def register():
    name = str(input("enter FullName :\t"))
    age = int(input("enter Age:\t"))
    validate(name, age)
    return 0


if __name__ == "__main__":
    print(__name__)
    try:
        reg = register()

    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye!")
        sys.exit(0)
    except ValueError:
        print("invalid input")
        sys.exit(1)
