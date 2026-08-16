menu={
    "鱼香肉丝":15,
    "宫保鸡丁":20,
    "红烧肉":30,
    "水煮鱼":40
}
#利用循环输出字典
print(menu)
for i in menu:#一次一个，把 menu 左边所有的 “键”，挨个取出来，放进 i 里面
    print(i,menu[i])
    #i是键，menu[i]是值
money=float(input("请输入你的余额："))
if money>=15:
    print("你可以选择的菜品有：")
    print("鱼香肉丝",menu["鱼香肉丝"])
    if money>=20:
        print("宫保鸡丁",menu["宫保鸡丁"])
        if money>=30:
            print("红烧肉",menu["红烧肉"])
            if money>=40:
                print("水煮鱼",menu["水煮鱼"])
else:
    print("你的余额不足，请充值！")
