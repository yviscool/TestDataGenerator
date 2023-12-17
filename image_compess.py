# 检查灰阶数量
def count_gray_levels(inputs):
    gray_levels = {}
    for line in inputs:
        pixels = [line[i:i+2] for i in range(0, len(line), 2)]  # Split the string into pairs of characters
        for pixel in pixels:
            if pixel in gray_levels:
                gray_levels[pixel] += 1
            else:
                gray_levels[pixel] = 1
    
    sorted_gray_levels = sorted(gray_levels.items(), key=lambda x: x[1], reverse=True)
    return sorted_gray_levels

# Test data inputs example
# inputs = [
#     "00FFCFAB00FFAC09071B5CCFAB76",
#     "00AFCBAB11FFAB09981D34CFAF56",
#     "01BFCEAB00FFAC0907F25FCFBA65",
#     "10FBCBAB11FFAB09981DF4CFCA67",
#     "00FFCBFB00FFAC0907A25CCFFC76",
#     "00FFCBAB1CFFCB09FC1AC4CFCF67",
#     "01FCCBAB00FFAC0F071A54CFBA65",
#     "10EFCBAB11FFAB09981B34CFCF67",
#     "01FFCBAB00FFAC0F071054CFAC76",
#     "1000CBAB11FFAB0A981B84CFCF66",
# ]

# result = count_gray_levels(inputs)
# for gray_level, count in result:
#     print(f"{gray_level}: {count}")


def generate_test_data():
    

    total_cases = 10
    
    for i in range(1, total_cases + 1):  # 生成 10 组测试数据
        io = IO(file_prefix="", data_id=i)

        if i == 1:
            io.input_writeln("10")
            io.input_writeln("00FFCFAB00FFAC09071B5CCFAB76")
            io.input_writeln("00AFCBAB11FFAB09981D34CFAF56")
            io.input_writeln("01BFCEAB00FFAC0907F25FCFBA65")
            io.input_writeln("10FBCBAB11FFAB09981DF4CFCA67")
            io.input_writeln("00FFCBFB00FFAC0907A25CCFFC76")
            io.input_writeln("00FFCBAB1CFFCB09FC1AC4CFCF67")
            io.input_writeln("01FCCBAB00FFAC0F071A54CFBA65")
            io.input_writeln("10EFCBAB11FFAB09981B34CFCF67")
            io.input_writeln("01FFCBAB00FFAC0F071054CFAC76")
            io.input_writeln("1000CBAB11FFAB0A981B84CFCF66")
        else:
            n = random.randint(10, 20)  # Random number of images
            io.input_writeln(n)
            pixel_list = []

            gray_levels  = count_gray_levels(pixel_list)
            # 确保灰阶数量 大于 16 种
            if len(gray_levels) <= 16:
                pixel_list = []
                for _ in range(n):
                    img_size = random.randint(2, 20) * 2  # Random image size between 2 and 20, even number
                    pixels = ''.join([random.choice("0123456789ABCDEF") for _ in range(img_size)])  # Random pixels
                    pixel_list.append(pixels)
                gray_levels  = count_gray_levels(pixel_list)

            # print( '灰阶数量', len(gray_levels), gray_levels)

            io.input_writeln('\n'.join(pixel_list))

        os_name = os.name
        if os_name == 'nt':  # Windows
            io.output_gen("std.exe")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
        else:  # Linux
            io.output_gen("./std")  # 调用 C++ 可执行文件生成输出文件
            print(f"生成测试数据 {i}")
