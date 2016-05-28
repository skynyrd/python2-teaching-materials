#parameterless, returns void
def print_hello():
    print "Hello"
    
print_hello()

#takes parameters, returns a value
def bmi(weight, height):
    return weight / (height * height);
    
bmi_of_anil = bmi(83, 1.83)
print(bmi_of_anil)

#optional parameter
def multiply_by_pi(value, pi = 3.14159265359):
    return value * pi
    
print "********"
print(multiply_by_pi(5))
print(multiply_by_pi(5, pi = 3.14))

#anonymous function, lambda
sum = lambda x,y: x+y
return_five = lambda: 5

print(sum(5,6))
print(return_five())
