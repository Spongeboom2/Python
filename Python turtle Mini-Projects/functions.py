#print("Hello Bob")
#print("Hello Alice")
#print("Hello John")

#Function to say hello to name passed as parameter
def say_hello(name):
    print("Hello " + name)

#Calling the function with different names
say_hello("Bob")
say_hello("Alice")
say_hello("John")

#function showing return value
def add_numbers(a, b):
    sum = a + b
    print("The sum is: " + sum)
    return sum

num = add_numbers(150, 2063)
print(num)



