# learngit
my git learning
- [x] This is a complete item
- [ ] This is an incomplete item


```python
import jieba
txt = open("test.txt", "r", encoding='gbk').read()
words = jieba.lcut(txt)
print("/".join(words))
```
