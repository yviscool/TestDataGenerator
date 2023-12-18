def generate_test_data():
    total_cases = 10
    
    for i in range(1, total_cases + 1):  # 生成 10 组测试数据
        io = IO(file_prefix="", data_id=i)
        
        if i <= 3:
            N = randint(1, 10)  # 随机生成马匹数量 N
        else:
            N = randint(10, 50)  # 随机生成马匹数量 N
            
        io.input_writeln(N)
        
        horses = list(range(1, 2 * N + 1))  # 生成所有马匹的速度列表，1 到 2N
        
        random.shuffle(horses)  # 随机打乱速度列表
        
        your_horses = horses[:N]  # 你的马匹列表为前 N 个马匹
        vj_horses = horses[N:]  # 田忌的马匹列表为后面的马匹
        
        io.input_writeln(' '.join(map(str, your_horses)))
        io.input_writeln(' '.join(map(str, vj_horses)))
        
        os_name = os.name
        if os_name == 'nt':  # Windows
            io.output_gen("std.exe")  # 调用C++可执行文件生成输出文件
            print(f"已生成测试数据 {i}")
        else:  # Linux
            io.output_gen("./std")  # 调用C++可执行文件生成输出文件
            print(f"已生成测试数据 {i}")
