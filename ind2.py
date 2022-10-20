# В списке, состоящем из вещественных элементов, вычислить:
#     1) сумму отрицательных элементов списка;
#     2) произведение элементов списка, расположенных между максимальным и минимальным
#     элементами.
# Упорядочить элементы списка по возрастанию.

import random

l = []

for x in range(10):
    l.append(random.randint(-10, 10))

print(l)

summ = 0
for x in l:
    if x < 0:
        summ += x

product = 1
min_el = min(l)
max_el = max(l)

min_id = 0
max_id = 0

for x in range(len(l)):
    if l[x] == min_el:
        min_id = x
    elif l[x] == max_el:
        max_id = x

new_l = []
if min_id > max_id:
    new_l = l[max_id+1:min_id]
elif min_id < max_id:
    new_l = l[min_id+1:max_id]

for x in new_l:
    product *= x

print('Сумма отрицательных элементов:', summ)
print('произведение элементов списка, расположенных между максимальным и минимальным', product)
l.sort()
print('Упорядоченный список:')
print(l)