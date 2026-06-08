# Write a code to print all the prime numbers between 1 and *n*


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
