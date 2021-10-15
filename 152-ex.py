def print_line(char,times):

    print(char * times)

def print_lines():
    """打印单行分隔线
    
    :param char 打印的字符参数
    :param times 打印出来的次数
    """
    row = 0

    while row <= 5:

        print_line("+",50)

        row += 1

# print_lines()

def print_liness(char , times):

    row = 0

    while row <= 5:

        print_line(char , times)

        row += 1

print_line("+", 6)
