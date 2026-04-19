def get_num():
    return float(input("Enter a number: "))


def calc(num0, num1):
    if num1 == 0:
        res4 = None
    else:
        res4 = num0 / num1

    print(f"""{num0} + {num1} = {num0 + num1}
    {num0} - {num1} = {num0 - num1}
    {num0} * {num1} = {num0 * num1}
    {num0} / {num1} = {res4}
    """)


x = get_num()
y = get_num()
calc(x, y)