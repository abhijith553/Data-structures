# used only when the greatest common factor of two numbers is given 
# formula : lcm = abs value of a x b / gcd of a, b

def gcd(a, b):
    while b:
        temp = a
        a = b
        b = temp%b
    return a

def lcm(a, b):
    return abs(a*b)//gcd(a, b)

num1 = int(input())
num2 = int(input())

result = lcm(num1, num2)

print(f"The lcm of {num1} and {num2} is {result}")