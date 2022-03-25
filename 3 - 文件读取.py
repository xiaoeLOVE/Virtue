# read(num)函数是文件读取函数，能够获得文件的字节数,num表示可以获得的字节数，不写的就是读取所有的文件内容

# 文件换行也是一个字节'\n', 读出来的参数和看到的不匹配，因为有换行符
f = open('test.txt', 'r')
# jj = f.read(6)
# print(jj)  # 读取的是 add'\n'aa


# readlines(): readlines可以按照⾏的⽅式把整个⽂件中的内容进⾏⼀次性读取，并且返回的是⼀个列表，其中每⼀⾏的数据为⼀个元素。
# gg = f.readlines()
# print(gg)


# readline() readline()⼀次读取⼀⾏内容。
jj = f.readline()
print(f'第一行{jj}')

jj = f.readline()
print(f'第二行{jj}')


f.close()