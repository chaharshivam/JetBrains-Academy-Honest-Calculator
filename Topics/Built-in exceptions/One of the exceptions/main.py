choice = True
while choice:
    try:
        n = int(input())
    except ValueError:
        print("provide a valid integer")
    else:
        print(dir(locals()['__builtins__'])[n])
    finally:
        print("showed what was required")
        print("do you want to try again, yes/no")
        userChoice = input()
        if userChoice == "no":
            choice = False

