#Maior e menor valores em Tupla

import random

n1 = random.randint(1, 20)
n2 = random.randint(1, 20)
n3 = random.randint(1, 20)
n4 = random.randint(1, 20)
n5 = random.randint(1, 20)

nums = (n1, n2, n3, n4, n5)

print('Os números informados foram: ', end = '')

for num in nums:
    print(num, end = ', ')
print('FIM')

print('-'*25)
print(f'O maior número é {max(nums)}')
print(f'O menor número é {min(nums)}')
print('-'*25)


