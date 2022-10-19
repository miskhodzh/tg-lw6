# Ввести список А из 10 элементов, найти наибольший элемент и переставить его с первым
# элементом. Преобразованный массив вывести.

A = []

for x in range(10):
    A.append(int(input('Ввдеите число >>> ')))

print(A)

m_elem = max(A)
for x in range(len(A)):
    if A[x] == m_elem:
        A.pop(x)
        A.insert(0, m_elem)
        A.insert(x+1, A[1])
        A.pop(1)

print(A)