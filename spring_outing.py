

def 生成春游测试数据(file_names):
    总测试点数 = 10
    全员到达测试点数 = 3
    
    for i in range(1, 总测试点数 + 1):  # 生成10组测试数据
        io = IO(file_prefix="", data_id=i)

        N = randint(2, 1000)  # 随机生成学生数量
        M = randint(2, 1000)  # 随机生成报到的学生数量

        io.input_writeln(N, M)  # 写入学生数量和报到的学生数量

        # 从0到N-1随机生成报到的学生编号
        reported_ids = [randint(0, N - 1) for _ in range(M)]

        # 确保三个测试点所有学生都到达
        if i <= 全员到达测试点数:
            reported_ids = random.sample(range(N), N)  # 所有学生都到达

        for report_id in reported_ids:
            io.input_writeln(report_id)  # 写入报到的学生编号

        os_name = os.name
        if os_name == 'nt':  # Windows
            io.output_gen("std.exe")  # 调用C++可执行文件生成输出文件
            print(f"生成测试数据 {i}")
        else:  # Linux
            io.output_gen("./std")  # 调用C++可执行文件生成输出文件
            print(f"生成测试数据 {i}")
