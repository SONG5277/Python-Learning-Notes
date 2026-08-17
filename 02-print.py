print("Hello World")
print('Hello World')

#转义字符 \
#print(" 莎士比亚说:“to be or not to be ,that's the question" ")会报错
print("1.莎士比亚说:\"to be or not to be ,that's the question\"")
print('2.莎士比亚说:“to be or not to be ,that\'s the question"')

#一行打印多个数据

#1. + 拼接：只能【字符串 + 字符串】
#+ 拼接运算，要求两边必须是「同一种类型」
print("2023"+"2024"+"2025")
print(123 + 456)#做算术求和
# 报错 print(123 + "abc")

# 2. 逗号分隔多个参数：自动在内容中间加【空格】
print("2023","2024","2025")

# 3. sep = 自定义分隔符（sep = separator分隔符）
print("2023","2024","2025",sep='->')

#   +：拼接，把几段文字粘成一整个字符串，只允许同一种类型串相加
#   ,：向 print 传入多个独立数据，自动空格，不同类型数据可以一起放
print("A","B","C", sep="|", end="。")
print("\n1"+"2","3"+"4", sep="~")
print(123, "abc")

#print函数默认end值为\n(换行）
print("2023")
print("2024")
print("2025")

print("2026",end="和")
print("2027",end="和")
print("2028",end="和")

#一个print函数打印多行文本
#print（“蒹葭苍苍
#        白露为霜“）
#python解释器逐行翻译，会报错
print("\n蒹葭苍苍\n白露为霜")
print(''' 
 蒹葭苍苍
      白露为霜
 ''')
#三引号保持格式不变

