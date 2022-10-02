# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
operators = ["+", "-", "*", "/"]


def check(v1, v2, v3):
    msg = ""
    msg_9 = "You are"
    v1 = float(v1)
    v2 = float(v2)
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8
    if msg != "":
        msg_9 += msg
        print(msg_9)


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    else:
        return False


memory = 0
while True:
    try:
        print(msg_0)
        calc = input()
        x, op, y = calc.split()
        if x == "M":
            x = memory
        else:
            x = float(x)
        if y == "M":
            y = memory
        else:
            y = float(y)
    except ValueError:
        print(msg_1)
    else:
        if op not in operators:
            print(msg_2)
        else:
            check(x, y, op)
            if op == "+":
                result = x + y
                print(result)
            elif op == "-":
                result = x - y
                print(result)
            elif op == "*":
                result = x * y
                print(result)
            elif op == "/":
                try:
                    result = x / y
                except ZeroDivisionError:
                    print(msg_3)
                    continue
                else:
                    print(result)
    print(msg_4)
    answer = input()
    if answer == "y":
        msg_index = 10
        if is_one_digit(result):
            while msg_index < 13:
                if msg_index == 10:
                    print(msg_10)
                elif msg_index == 11:
                    print(msg_11)
                elif msg_index == 12:
                    print(msg_12)
                save_answer = input()
                if save_answer == "y":
                    msg_index += 1
                else:
                    break
        else:
            memory = result
        if msg_index == 13:
            memory = result
    print(msg_5)
    answer = input()
    if answer != "y":
        break




