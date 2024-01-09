

def generate_symmetric_integers(count):
    symmetric_integers = []
    for _ in range(count):
        # 生成对称的32位二进制序列
        symmetric_binary = '0' + ''.join(random.choice('01') for _ in range(15))
        symmetric_binary += symmetric_binary[::-1]  # 添加对称的部分
        symmetric_integers.append(int(symmetric_binary, 2))  # 转换为整数并加入列表
    return symmetric_integers

# 生成三个内码对称的整数
symmetric_numbers = generate_symmetric_integers(3)

# 打印生成的整数
for index, num in enumerate(symmetric_numbers, start=1):
    print(f"对称整数 {index}: {num}")
