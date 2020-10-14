#这是注释
'''
练习
多行注释
print()
type()
input()#z这里只表示字符类型，需要强制转换
每一个运算符前需要一个缩进，规范
命令变量时，可采用下划线
'''
name = input("名字：")
student_no = int(input("学号："))
price = int(input("价格："))
weight = int(input("重量："))
scale = float(input("数据对比："))
money = price * weight
print("我的名字叫 %s" % name)
print("我的学号 %06d" % student_no)
print("苹果单价 %.02f, 购买 %.02f, 价格 %.02f" % (price,weight,money))
print("数据对比：%.02f%%" % scale)