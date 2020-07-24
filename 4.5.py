# coding_utf-8 -*-
print(open('cafe.txt', 'w', encoding='utf-8').write('café+中文测试'))
print(open('cafe.txt', 'r').read())
