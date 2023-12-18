def generate_test_data():
    
    total_cases = 10
    
    generated_combinations = set()
    
    for i in range(1, total_cases + 1):  # 生成 10 组测试数据
        io = IO(file_prefix="", data_id=i)
        
        while True:
            N = randint(1, 9)  # 生成小猫数量 N，范围为 1 到 9
            i_value = randint(0, N - 1)  # 生成每次扔到海里的鱼的数量 i，范围为 0 到 N-1
            
            if (N, i_value) not in generated_combinations:
                generated_combinations.add((N, i_value))
                break
        
        io.input_writeln(N)
        io.input_writeln(i_value)


        os_name = os.name
        if os_name == 'nt':  # Windows
            io.output_gen("std.exe")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
        else:  # Linux
            io.output_gen("./std")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
