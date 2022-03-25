# 文件打开
f = open('test.txt', 'w')

# 文件读写write(), read()
f.write('addsd')

# 文件关闭
f.close()

# r 如果文件不存在就会报错， 不允许写入，表示只读
# f = open('test1.txt', 'r')  # 报错


# w 只写，
