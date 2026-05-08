# Task 1: Function
def hello():
    print("Hello, World!")

# Task 2: Function with Parameters
hello()
def info():
    name = input("Enter your name: ")
    email = input("Enter your Email: ")
    print("Hello, " + name + "!" + "\n" "Email" + email)
info()    

# Task 3: Function with Return Value
def sum(a,b):
    return a+b 
print(sum(5,10)) 


def sum(c,d):
    return c+d
print(sum(c=1,d=2))


def sum(c,d):
    return c+d
c=1
d=2
print(sum(c,d))

# Task 4: Built-in Functions
print(len("Hello, World!"))
print(max(5,10))
print(min(5,10 ))
print(type(5))

# Task 5: Data Types 
def check_data_type(value):
    if value.isdigit():
        return "Integer"
    
    try:
        float(value)
        return "Float"
    except:
        pass

    if value.lower() == "true" or value.lower() == "false":
        return "Boolean"

    return "String"
data = input("Enter something: ")
result = check_data_type(data)
print("The data type is:", result)

# Task 6: Greet Person Function
def greet_person(name, roll_number):
    print(f"Hello, My Love, {name}!{roll_number},How are you?")
greet_person("Adnan", 39)
greet_person("Ali", 35)
greet_person("Latif", 42)
greet_person("Ahmed", 2)    
