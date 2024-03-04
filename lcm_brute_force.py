def lcm_brute_force(a, b):
    max_num = max(a, b)
    lcm = max_num

    while 1:
        if lcm % a == 0 and lcm % b == 0:
            return lcm
        lcm = lcm + max_num

num1 = int(input())
num2 = int(input())

result = lcm_brute_force(num1, num2)

print(f"The lcm of {num1} and {num2} via brute force method is {result}")