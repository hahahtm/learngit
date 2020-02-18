import jieba
txt = open("test.txt", "r", encoding='gbk').read()
words = jieba.lcut(txt)
print("/".join(words))