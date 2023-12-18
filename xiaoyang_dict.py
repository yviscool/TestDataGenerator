def generate_test_data():
    total_cases = 10
    
    for i in range(1, total_cases + 1):  # 生成 10 组测试数据
        io = IO(file_prefix="", data_id=i)
        
        if i <= 3:
            N = randint(2, 9)  # 词典中的条目数 N，范围为 2 到 9
        else:
            N = randint(10, 20)  # 词典中的条目数 N，范围为 10 到 99
        
        io.input_writeln(N)
        
        dictionary = {}
        for _ in range(N):
            if i <= 3:
                A = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', randint(2, 5)))  # 随机生成 A 语言单词
                B = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', randint(2, 5)))  # 随机生成 B 语言翻译
            else:
                A = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', randint(1, 10)))  # 随机生成 A 语言单词
                B = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', randint(1, 10)))  # 随机生成 B 语言翻译
            io.input_writeln(f"{A} {B}")
            dictionary[A] = B
        
        S = ""
        words_count = randint(2, 5)  if i <= 3 else randint(20, 30) 
        for _ in range(words_count):
            if random.randint(1, 10) <= 7:  # 70% 概率生成词典中存在的单词
                word = random.choice(list(dictionary.keys()))
            else:
                word = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', randint(1, 10)))  # 生成不存在于字典中的单词
            S += word + ''.join(random.sample('.!,()-[]{}\\|;:\'",./?<>', randint(1, 3)))  # 在单词后添加标点符号

        io.input_writeln(S)

        os_name = os.name
        if os_name == 'nt':  # Windows
            io.output_gen("std.exe")  # 调用C++可执行文件生成输出文件
            print(f"已生成测试数据 {i}")
        else:  # Linux
            io.output_gen("./std")  # 调用C++可执行文件生成输出文件
            print(f"已生成测试数据 {i}")
