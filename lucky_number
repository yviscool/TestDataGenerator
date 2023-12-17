

def 数字变换(t):
    if t == 0:
        return 0
    return (t * 7 - 1) % 9 + 1

def 是否为幸运数(x):
    sum = 0
    d = 1
    while x > 0:
        t = x % 10
        if d % 2 == 0:
            sum += t
        else:
            sum += 数字变换(t)
        d += 1
        x //= 10
    return sum % 8 == 0

def 生成幸运数(count):
    幸运数列表 = []
    while count > 0:
        potential_number = random.randint(1, 10**12)
        if 是否为幸运数(potential_number):
            幸运数列表.append(potential_number)
            count -= 1
    return 幸运数列表


def 生成幸运数测试数据():
    total_cases = 10
    
    for i in range(1, total_cases + 1):  # 生成 10 组测试数据
        io = IO(file_prefix="", data_id=i)

        if i <= 5:
            n = random.randint(2, 10)
        else:
            n = random.randint(11, 20)

        幸运数集 = 生成幸运数(random.randint(1, n))

        随机数字集 = []
        for j in range(n - len(幸运数集)):
            num = random.randint(1, 10**6)
            随机数字集.append(num)

        io.input_writeln(n)
        for l in 幸运数集 + 随机数字集:
            io.input_writeln(l)

        os_name = os.name
        if os_name == 'nt':  # Windows
            io.output_gen("std.exe")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
        else:  # Linux
            io.output_gen("./std")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
