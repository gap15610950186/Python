data = input("请输入各科成绩，以空格隔开，空行回车结束输入：")
d = {}

while data:
    t = data.split()
    d[t[0]] = t[1]
    data = input()

ls = list(d.items())

ls.sort(key=lambda x:x[1], reverse=True)

s1,g1=ls[0]
s2,g2 =ls[len(ls)-1]

a = 0

for i in d.values():
    a = a+ int(i)

a = a/len(ls)

print("最高分课程是：{}{}, 最低分课程是：{}{}, 平均分是：{:.2f}".format(s1,g1,s2,g2,a))