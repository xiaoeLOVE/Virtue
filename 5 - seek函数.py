'''
文件对象.seek(偏移量，起始位置)  0 开头 1 当前位置 2 结尾
'''

f = open('test.txt', 'a+')
f.seek(3, 0)
con = f.read()
print(con)
f.close()
