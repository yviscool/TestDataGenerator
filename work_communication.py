def generate_test_data():
    
    total_cases = 10
    
    generated_combinations = set()
    
    for i in range(4, total_cases + 1):  # 生成 10 组测试数据
        io = IO(file_prefix="", data_id=i)
        
        N = randint(3, 50) if i > 5 else randint(3, 10)
        f = [0] + [0] * (N - 1)
        
        for j in range(1, N):
            leaders = random.sample(range(0, j), 1) # 从 0 到 j-1 中随机选择领导
            f[j] = leaders[0]
        
        io.input_writeln(N)
        io.input_writeln(*f[1:])
        
        Q = randint(1, 10) if i < 5 else randint(1, 20)
        io.input_writeln(Q)

        for _ in range(Q):
            m = randint(2, N-1)
            employees = random.sample(range(1, N), m)
            employees.insert(0, m)
            io.input_writeln(employees)

        os_name = os.name
        if os_name == 'nt':  # Windows
            io.output_gen("std.exe")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
        else:  # Linux
            io.output_gen("./std")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
