def is_prime(x):
    if x < 2:
        return False
    for d in range(2, int(x**0.5)+1):
        if x%d == 0:
            return False
    return True
        
n = int(input())
count = 0
num = 2
super_count = 0
while True:
    if is_prime(num):
        count+=1
        if is_prime(count):
            super_count+=1
            if super_count == n:
                print(num)
                break
    num+=1