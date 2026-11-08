#引入
import random
import time

#设置变量
name_boy=input("请输入男方的姓名：")
name_gril=input("请输入女方的姓名：")
num=random.randint(1,100)
#输出
print(f"您的姓名：{name_boy }，您和{name_gril}的缘分指数：{num}")
time.sleep(1)
if num>85:
    print("你们很有缘分，天作之合")
elif num>60:
    print("你们缘分还行，继续努力")
elif num<61:
    print("你们没有缘分，洗洗睡吧")

