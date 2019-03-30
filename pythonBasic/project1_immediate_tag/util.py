# 文本块生成器


# 在文件的最后追加一个空行
def lines(file):
    for line in file :
        yield line
        yield '\n'


# 当生成一个块之后，它里面的行会被连接起来，并且获得的字符串会被删除，得到一个代表块的字符串
# 同时，开始和结尾中多余的空格会被删除
def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
