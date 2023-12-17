def generate_test_data():
    
    armstrong_numbers = [153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725, 4210818, 9800817, 9926315, 24678050, 24678051, 88593477]

    for i in range(1, 11):  # 生成10组测试数据
        io = IO(file_prefix="", data_id=i)

        M = randint(1, 50)  # 随机生成1到100之间的整数，表示待判断的正整数个数
        io.input_writeln(M)  # 写入待判断的正整数个数

        armstrong_count = randint(2, len(armstrong_numbers)-1)  # 随机生成自幂数的个数，确保不超过待判断的正整数个数
        non_armstrong_count = M - armstrong_count  # 计算非自幂数的个数

        armstrong_numbers_subset = random.sample(armstrong_numbers, armstrong_count)  # 随机选取自幂数的子集
        non_armstrong_numbers = []

        while non_armstrong_count > 0:
            n = randint(1, 10**8)  # 随机生成小于10^8的整数
            if n not in armstrong_numbers and n not in non_armstrong_numbers:
                non_armstrong_numbers.append(n)
                non_armstrong_count -= 1

        numbers = armstrong_numbers_subset + non_armstrong_numbers
        random.shuffle(numbers)  # 将数字列表打乱顺序

        for n in numbers:
            io.input_writeln(n)  # 写入待判断的正整数

        os_name = os.name
        if os_name == 'nt':  # Windows
            io.output_gen("std.exe")  # 调用C++可执行文件生成输出文件
            print(f"已生成测试数据 {i}")
        else:  # Linux
            io.output_gen("./std")  # 调用C++可执行文件生成输出文件
            print(f"已生成测试数据 {i}")
