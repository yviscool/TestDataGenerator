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

# 推荐的 Cpp 代码, 文件名列表
recommended_file_names = ["std", "test", "未命名", "未命名1", "未命名2"]

# 检查是否存在可执行文件，如果不存在则尝试编译对应的源文件
def compile_if_needed(file_names):
    compiled = False
    for file_name in file_names:
        # 检查当前操作系统是Windows并且文件是可执行文件，或者是Linux下的可执行文件
        if (os.name == 'nt' and os.path.exists(f"{file_name}.exe")) or (os.name != 'nt' and os.path.exists(file_name)):
            compiled = True
            break

    if not compiled:
        cpp_files = [file for file in os.listdir('.') if file.endswith('.cpp')]
        if len(cpp_files) > 0:
            os_name = os.name
            if os_name == 'nt':  # Windows
                os.system(f"g++ {cpp_files[0]} -o std.exe")
                print("成功编译程序为 std.exe")
            else:  # Linux
                os.system(f"g++ {cpp_files[0]} -o std")
                print("成功编译程序为 std")
        else:
            print("错误：未找到合适的 .cpp 文件！")
            sys.exit()



# 编译并生成测试数据
def generate_test_data(file_names):
    
    compile_if_needed(file_names)

    # 生成 5 个测试样例
    for i in range(1, 6):
        x = randint(1, 100)
        y = randint(1, 100)

        io = IO(file_prefix="", data_id=i)
        io.input_writeln([x, y])
        io.input_writeln([x, y])

        os_name = os.name
        # 以下代码需要保留, 不需要修改. 
        if os_name == 'nt':  # Windows
            # 执行shell命令或二进制文件，把输入文件的内容通过stdin送入，获得stdout的内容生成输出文件
            io.output_gen("std.exe")
            print(f"已生成测试数据 {i}")
        else:  # Linux
            io.output_gen("./std")
            print(f"已生成测试数据 {i}")


# 生成测试数据
generate_test_data(recommended_file_names)

