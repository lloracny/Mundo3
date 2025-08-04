num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 2)
num.remove(2) #-> Elimina o 1° 2
print(num)
print(f'Essa lista tem {len(num)} elementos')