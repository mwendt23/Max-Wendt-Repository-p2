primelist = []
n = 1

def primseive(n):
    for i in range (2, n - 1):
        if n % i == 0:
          return false
        return true
        
while n <= 600851475143:
    n += 1
    if 600851475143 % n == 0:
         if n % 2 != 0:
             if primseive(n) == true:
                 primlist.append(n)

print(max(primelist))


   
        
