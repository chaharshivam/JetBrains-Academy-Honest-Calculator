# put your python code here
sequence = input().split()
num_list = list()
for num in sequence:
    num_list.append(int(num))
x = int(input())
counter = 0
found = False
for number in num_list:
    if number == x:
        print(counter, end=" ")
        found = True
    counter += 1
if not found:
    print("not found")
