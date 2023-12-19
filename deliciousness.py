def generate_test_data():
    
    total_cases = 10
    
    generated_combinations = set()
    
    for i in range(1, total_cases + 1):  # 生成 10 组测试数据
        io = IO(file_prefix="", data_id=i)
        
        if i <= 2:
            N = randint(1, 10)
        elif i < 8:
            N = randint(1, 100)
        else:
            N = randint(1, 1000)

        
        io.input_writeln(N)
        

        delicious = []
        for _ in range(N):
            if i <= 4:
                a_i = randint(0, 10)
            elif i < 6:
                a_i = randint(0, 100)
            else:
                a_i = randint(0, 1000)
            delicious.append(a_i)

        io.input_writeln(delicious)


        os_name = os.name
        if os_name == 'nt':  # Windows
            io.output_gen("std.exe")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
        else:  # Linux
            io.output_gen("./std")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
