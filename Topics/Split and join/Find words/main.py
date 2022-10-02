n = int(input())
counter = 1
spaces = n - 1
while n != 0:
    inner_counter = 1
    inner_space = 1
    while inner_space <= spaces:
        print(" ", end=" ")
        inner_space += 1
    while inner_counter <= counter:
        print("*", end=" ")
        inner_counter += 1
    print()
    counter += 2
    n -= 1
    spaces -= 1

