'''
This Python program finds and displays all prime numbers between 1 and a user-defined number n. 
It checks each number from 2 up to n and determines whether it is a prime number.
All prime numbers found are stored in a list and then displayed at the end.
A prime number is a number greater than 1 that can only be divided evenly by 1 and itself.
'''

n = int(input("Enter a number : "))
prime_numbers = []

for  num in range(2, n+1):
    is_prime = True
    for  j in range(2, num):
        if num % j == 0:
            is_prime = False
            break
    
    if is_prime:
        prime_numbers.append(num)
    

print(f"The prime numbers  from  1 to  {n} are/is:  \n{prime_numbers}")
