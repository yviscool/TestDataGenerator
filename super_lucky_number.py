def generate_test_data():
    
    total_cases = 10
    
    generated_combinations = set()
    
    for i in range(1, total_cases + 1):  # 生成 10 组测试数据
        io = IO(file_prefix="", data_id=i)
        
        if i <= 3:
            a = randint(2, 100)
            x_range = 100
            N = randint(1, 100)
        elif i <= 6:
            a = randint(2, 1000)
            x_range = 10 ** 3
            N = randint(1, 1000)
        else:
            a = randint(2, 5000)
            x_range = 10 ** 6
            N = randint(1, 1000)
        
        io.input_writeln(a, N)
        
        
        for _ in range(N):
            if random.random() > 0.3:
                if a > 10000:
                    a /= 2
                x = randint(a, a * 10)
                io.input_writeln(x * 2)
            else:
                x = randint(1, x_range)
                io.input_writeln(x)

        os_name = os.name
        if os_name == 'nt':  # Windows
            io.output_gen("std.exe")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
        else:  # Linux
            io.output_gen("./std")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
