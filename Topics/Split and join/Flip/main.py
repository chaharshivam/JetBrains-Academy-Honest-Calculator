numeric_sequence = input().split()
new_numeric = list()
for num in numeric_sequence:
    new_numeric.append(int(num))

new_numeric.reverse()
for n in new_numeric:
    print(n, end=" ")