first_num = int(input())
operation = input()
second_num = int(input())


all_ops = ["*", "/", "+", "-"]
if operation in all_ops:
    print(eval(str(first_num) + operation + str(second_num)))