# -*- coding: utf-8
import locale

locale.setlocale(locale.LC_COLLATE, 'zh_CN.UTF-8')
names = ["阿强", "张伟", "李华", "夏洛", "王刚"]
print(sorted(names, key=locale.strxfrm))
print(names)
print(list(map(lambda x: x.encode('utf-8'), names)))
# sort没有按照拼音来排序，反而是按照utf-8编码来排序的
print(bytearray(bytes("阿强", encoding='utf-8')))
