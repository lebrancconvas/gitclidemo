# Finding GCD (Greatest Common Divisor)
def gcd(num1,num2):
    if(num1 == num2):
        return num1
    if(num1 > num2):
        return gcd(num1-num2,num2)
    return gcd(num1,num2-num1)

# Finding LCM (Lowest Common Multiple)
def lcm(num1,num2):
    return (num1*num2) / gcd(num1,num2)