  def generate_isbn():
            # 生成首位数字（语言代码）
            language_code = random.randint(0, 9)
            isbn = str(language_code)

            # 生成出版社代码
            publisher_code = ''.join(str(random.randint(0, 9)) for _ in range(3))
            isbn += f"-{publisher_code}"

            # 生成出版编号
            publication_code = ''.join(str(random.randint(0, 9)) for _ in range(5))
            isbn += f"-{publication_code}"

            # 计算识别码
            weights = [i + 1 for i in range(9)]
            identifier = sum(int(digit) * weight for digit, weight in zip(isbn.replace('-', ''), weights)) % 11
            identifier = 'X' if identifier == 10 else str(identifier)

            isbn += f"-{identifier}"
            return isbn
