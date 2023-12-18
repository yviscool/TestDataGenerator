def generate_test_data():
    
    total_cases = 10
    
    generated_combinations = set()
    
    for i in range(1, total_cases + 1):  # 生成 10 组测试数据
        io = IO(file_prefix="", data_id=i)
        
        if i <= 4:
            N = randint(1, 9)  # 题目数量 N，范围为 1 到 9
        else:
            N = randint(10, 500)  # 题目数量 N，范围为 10 到 1000
        
        io.input_writeln(N)
        
        for _ in range(N):
            unit1 = random.choice(['km', 'm', 'kg', 'g'])  # 随机选择长度或重量单位
            if unit1 == 'km':
                unit2 = random.choice(['m', 'mm'])  # 如果是 km，则选择 m 或 mm
            elif unit1 == 'm':
                unit2 = 'mm'  # 如果是 m，则只能转换为 mm
            elif unit1 == 'kg':
                unit2 = random.choice(['g', 'mg'])  # 如果是 kg，则选择 g 或 mg
            elif unit1 == 'g':
                unit2 = 'mg'  # 如果是 g，则只能转换为 mg
            
            x = randint(1, 1000)  # x 为一个不超过 1000 的非负整数
            io.input_writeln(f"{x} {unit1} = ? {unit2}")

        os_name = os.name
        if os_name == 'nt':  # Windows
            io.output_gen("std.exe")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
        else:  # Linux
            io.output_gen("./std")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
