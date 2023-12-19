
def generate_test_data():
    
    total_cases = 10
    
    generated_combinations = set()
    
    for i in range(1, total_cases + 1):  # 生成 10 组测试数据
        io = IO(file_prefix="", data_id=i)
        
        N = randint(1, 10000)
        M = randint(1, 100)
        
        if i <= 2:  # For 20% of cases, M = 1
            M = 1
            N = randint(1, 20)
        
        if i > 2 and i <= 6:  # For 40% of cases, N <= 20 and M <= 2
            N = randint(1, 20)
            M = randint(1, 2)
        
        io.input_writeln(N, M)
        
        transitions = [randint(1, N) for _ in range(M)]
        io.input_writeln(*transitions)
        
        if i<=6 :
            scores = [randint(-3, 10) * 10 for _ in range(N)]
        else:
            scores = [randint(-100, 1000) for _ in range(N)]
        io.input_writeln(*scores)
        

        os_name = os.name
        if os_name == 'nt':  # Windows
            io.output_gen("std.exe")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
        else:  # Linux
            io.output_gen("./std")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
