def lcm(n1,n2):
    x = n1
    while(x % n2) != 0:
                x += n1
    return x

print("What's your name?")
name = input()
print(name + ' has ' + str(len(name)) + ' letters in it')
num1 = int(input(name + ", Enter first number: "))
num2 = int(input(name + ", Enter second number: "))

print(name + ", the LCM of the two numbers is " + str(lcm(num1,num2)))
