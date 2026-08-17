#打印购物小票
food1="薯片"
food2="雪碧"
num1=3
num2=1
price1=10.5
price2=3.5
total=num1*price1+num2*price2
print("商品名称 商品数量 商品单价")
print(food1,num1,price1)
print(food2,num2,price2)
print("总价：",total)
#有移位


print("商品名称 商品数量 商品单价")
print(food1,num1,price1,sep="     ")
print(food2,num2,price2,sep="     ")
print("总价：",total,sep="     ")

number=666
print("你的操作number")
# print("你的操作"+number) 变量是一个数字类型的变量，不能够使用加号拼接输出

#直接嵌入变量的输出方法
print(f"你的操作{number}") #可以用f-string方法5
print("你的操作",number)

#多个变量赋值
variable1,variable2=666,"苹果"#数字形式可以不用引号
print(variable1,variable2)
#print(variable1+variable2) 错误 v1整形，v2字符串，不同类型数据不能用+