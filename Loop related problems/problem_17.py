n = int(input())

is_prime = True

if n < 2:
    is_prime = False

else:
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print('Prime')
else:
    print('Not Prime')