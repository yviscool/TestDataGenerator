
def 检查密码规范(s):
    l = len(s)
    if l < 6 or l > 12:
        return False

    hasC = any(c.isupper() for c in s)
    hasL = any(c.islower() for c in s)
    hasD = any(c.isdigit() for c in s)
    hasS = any(c in "!@#$" for c in s)

    if not hasS:
        return False

    if sum([hasC, hasL, hasD]) < 2:
        return False

    return True

def 生成密码规范检查测试数据(file_names):
    compile_if_needed(file_names) 

    total_cases = 10
    
    for i in range(1, total_cases + 1):  # 生成 10 组测试数据
        io = IO(file_prefix="", data_id=i)
        
        # 生成随机密码，确保至少一个符合规范
        passwords = []
        for _ in range(random.randint(5, 8)):
            length = random.randint(6, 13)
            password = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$", k=length))
            passwords.append(password)
        
        compliant_passwords = [pw for pw in passwords if 检查密码规范(pw)]
        
        # 确保至少一个密码符合规范
        while len(compliant_passwords) < random.randint(1, total_cases):
            length = random.randint(6, 13)
            compliant_password = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$", k=length))
            if 检查密码规范(compliant_password):
                passwords.append(compliant_password)
                break
        
        io.input_writeln(','.join(passwords))  # 将生成的密码作为输入
        
        os_name = os.name
        if os_name == 'nt':  # Windows
            io.output_gen("std.exe")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
        else:  # Linux
            io.output_gen("./std")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
