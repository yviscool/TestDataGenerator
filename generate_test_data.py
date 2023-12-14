#!/usr/bin/env python
import os
import sys
from cyaron import *

# cyaron 文档说明 https://github.com/luogu-dev/cyaron/wiki

# IO库的方法主要有以下几种：
# io = IO("test1.in", "test1.out") # 先新建一组数据
# io.input_write(1, 2, 3) # 写入1 2 3到输入文件
# io.input_writeln(4, 5, 6) # 写入4 5 6到输入文件并换行
# io.output_write(1, 2, 3) # 写入1 2 3到输出文件
# io.output_writeln(4, 5, 6) # 写入4 5 6到输出文件并换行
# io.input_write([1, 2, 3]) # 写入1 2 3到输入文件
# io.output_write(1, 2, [1, 2, 3], [4]) # 写入1 2 1 2 3 4到输出文件
# io.input_write(1, 2, 3, separator=',') # 写入1,2,3,到输入文件，目前版本尾部会多一个逗号，之后可能修改行为
# io.output_gen("~/Documents/std") # 执行shell命令或二进制文件，把输入文件的内容通过stdin送入，获得stdout的内容生成输出
# io.output_gen("C:\\Users\\Aqours\\std.exe") # 当然Windows也可以

# CYaRon 提供了一些常用的常数。

# PI
# 即圆周率的值。3.1415926...

# E
# 即自然底数的值。2.7182818...

# ALPHABET_SMALL
# 一个字符串，包含所有的小写字母。"abcdefghijklmnopqrstuvwxyz"

# ALPHABET_CAPITAL
# 一个字符串，包含所有的大写字母。"ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# ALPHABET
# 一个字符串，包含所有的字母。"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# NUMBERS
# 一个字符串，包含所有的数字。"0123456789"

# str = String.random(5) # 生成一个5个字母的单词，从小写字母中随机选择
# str = String.random((10, 20), charset="abcd1234") # 生成一个10到20个字母之间的单词，从abcd1234共8个字符中随机选择
# str = String.random(10, charset="#######...") # 生成一个10个字母的只有'#'和'.'组成的字符串，'#'的可能性是70%，'.'可能30%。
# str = String.random(None, charset=["foo", "bar"]) # 从foo、bar两个单词中随机选择一个返回
# # charset参数对于以下所有指令也有效。

# str = String.random_sentence(5) # 生成一个5个单词的句子，以空格分割，第一个单词首字母自动大写，结尾有句号或感叹号，每个单词3到8个字母长
# str = String.random_sentence((10, 20), word_separators=",;", sentence_terminators=None, first_letter_uppercase=False, word_length_range=(2, 10), charset="abcdefg") # 生成一个10到20个单词的句子，以逗号或分号随机分割，第一个单词首字母不大写，结尾没有任何符号，每个单词2到10字母长，从abcdefg共7个字符中随机选择
# # 以上所有参数，对于以下所有指令也有效

# str = String.random_paragraph((3, 10)) # 生成一个3到10个句子的段落，句子之间以句号或感叹号分割，小句之间以逗号或分号分割，句子和小句结束后均接有一个空格，句子开头首字母大写而小句开头首字母不大写。生成句子的可能性为30%而小句的可能性为70%。
# str = String.random_paragraph(6, sentence_joiners="|", sentence_separators=",", sentence_terminators=".?", termination_percentage=0.1) # 生成一个6个句子的段落，句子之间以句号或问号号分割，小句之间以逗号分割，句子和小句结束后均接有一个"|"号，句子开头首字母大写而小句开头首字母不大写。生成句子的可能性为10%而小句的可能性为90%。

# # 注意：如果您需要以两个空格分割单词，应该使用如下写法：
# str = String.random_sentence(5, word_separators=["  "]) # 以两个空格分割单词
# # 而不是：
# str = String.random_sentence(5, word_separators="  ") # 这会导致从两个空格中随机选择一个，也就是只有一个空格

# 生成测试数据的核心规则和要点主要包括以下几个方面：

# 1. **问题理解**：理解问题的输入输出格式、约束条件和要求。这对于正确生成测试数据至关重要。

# 2. **随机性和覆盖性**：在生成测试数据时，确保随机性和覆盖性。随机性保证测试数据的多样性，覆盖性则确保测试覆盖到各种可能的情况，包括边界情况和特殊情况。

# 3. **边界条件**：对于输入的边界条件，例如最小值、最大值、特殊情况等，需要特别关注。确保生成的测试数据涵盖这些边界条件，这有助于验证算法或程序的健壮性。

# 4. **数据合法性**：确保生成的数据符合输入约束和问题描述的要求。在生成随机数据时，需要验证生成的数据是否合法，并且不违反问题的约束条件。

# 5. **多样性和复杂性**：生成多样性的测试数据，包括不同规模、不同特征的数据。这样能够更全面地测试算法或程序的性能和正确性。

# 6. **自动化**：尽可能地将测试数据生成过程自动化。编写脚本或程序来生成测试数据可以提高效率，并确保数据的一致性和准确性。

# 总的来说，生成测试数据需要考虑问题的要求，确保测试数据的合法性、多样性和覆盖性。随机性和边界条件的考虑能够有效地测试算法或程序的各种情况，帮助发现潜在的问题。


# 推荐的 Cpp 代码, 文件名列表
recommended_file_names = ["std", "test", "未命名", "未命名1", "未命名2"]


# 总是检查是否存在可执行文件，总是编译对应的源文件
def compile_if_needed(file_names):
    compiled = False
    for file_name in file_names:
        # 检查当前操作系统是Windows并且文件是可执行文件，或者是Linux下的可执行文件
        if (os.name == 'nt' and os.path.exists(f"{file_name}.exe")) or (os.name != 'nt' and os.path.exists(file_name)):
            compiled = True
            break

    cpp_files = [file for file in os.listdir('.') if file.endswith('.cpp')]

    if not compiled:
        if len(cpp_files) <= 0:
            print("错误：未找到合适的 .cpp 文件！")
            sys.exit()
            
    os_name = os.name
    if os_name == 'nt':  # Windows
        os.system(f"g++ {cpp_files[0]} -o std.exe")
        print("成功编译程序为 std.exe")
    else:  # Linux
        os.system(f"g++ {cpp_files[0]} -o std")
        print("成功编译程序为 std")


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



# 编译并生成测试数据
def generate_test_data(file_names):

    compile_if_needed(file_names)
    
    armstrong_numbers = [153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725, 4210818, 9800817, 9926315, 24678050, 24678051, 88593477]

    for i in range(1, 11):  # 生成10组测试数据
        io = IO(file_prefix="", data_id=i)

        M = randint(1, 50)  # 随机生成1到100之间的整数，表示待判断的正整数个数
        io.input_writeln(M)  # 写入待判断的正整数个数

        armstrong_count = randint(2, len(armstrong_numbers)-1)  # 随机生成自幂数的个数，确保不超过待判断的正整数个数
        non_armstrong_count = M - armstrong_count  # 计算非自幂数的个数

        armstrong_numbers_subset = random.sample(armstrong_numbers, armstrong_count)  # 随机选取自幂数的子集
        non_armstrong_numbers = []

        while non_armstrong_count > 0:
            n = randint(1, 10**8)  # 随机生成小于10^8的整数
            if n not in armstrong_numbers and n not in non_armstrong_numbers:
                non_armstrong_numbers.append(n)
                non_armstrong_count -= 1

        numbers = armstrong_numbers_subset + non_armstrong_numbers
        random.shuffle(numbers)  # 将数字列表打乱顺序

        for n in numbers:
            io.input_writeln(n)  # 写入待判断的正整数

        os_name = os.name
        if os_name == 'nt':  # Windows
            io.output_gen("std.exe")  # 调用C++可执行文件生成输出文件
            print(f"已生成测试数据 {i}")
        else:  # Linux
            io.output_gen("./std")  # 调用C++可执行文件生成输出文件
            print(f"已生成测试数据 {i}")


# 生成测试数据
generate_test_data(recommended_file_names)

