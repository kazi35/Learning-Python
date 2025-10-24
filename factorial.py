#WAF to calculate Factorial of n 

def factorial_cal(n):
    fact=1
    for i in range(1,n+1):
        fact*= i
    print(fact)

factorial_cal(5)