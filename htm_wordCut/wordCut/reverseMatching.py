test_file = '300.txt'  # 词典
test_file2 = 'test.txt'  # 测试语料

def get_dic(test_file):  # 读取文本返回列表
    with open(test_file, 'r', encoding='utf-8', ) as f:
        try:
            file_content = f.read().split('\n')
        finally:
            f.close()
    chars = list(file_content)
    return chars
dic = list(get_dic(test_file))

def readfile(test_file2):
    with open(test_file2, 'r', encoding='gbk', ) as f:
        content=f.read()
        my_list=[]
        while len(content)>0:
            tryWord=content[-20:]
            while tryWord not in dic:
                if len(tryWord) == 1:
                    break
                tryWord = tryWord[1:]
            my_list.append(tryWord)
            content=content[0:len(content)-len(tryWord)]
    my_list.reverse()
    return my_list
print('/'.join(readfile(test_file2)))


