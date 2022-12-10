from random import randint
import time
import sys
import random
'''
# 玩家
class Player:

    def __init__(self,stoneNumber,warriors):
        self.stoneNumber = stoneNumber # 灵石数量
        self.warriors = {}  # 拥有的战士，包括弓箭兵和斧头兵
'''
# 战士
class Warrior:
    name = '战士'
    # 初始化参数是生命值
    def __init__(self, strength):
        self.strength = strength

    # 用灵石疗伤
    def healing(self, stoneCount):
        # 如果已经到达最大生命值，灵石不起作用，浪费了
        if self.strength == self.maxStrength:
            return

        self.strength += stoneCount

        # 不能超过最大生命值
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength 
    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 20
        elif monster.typeName== '狼妖':
            self.strength -= 80
        else:
            print('未知类型的妖怪！！！')


# 弓箭兵 是 战士的子类
class Archer(Warrior):
    # 种类名称
    typeName = '弓箭兵'
    ArcherName='none'

    # 雇佣价 100灵石，属于静态属性
    price = 100

    # 最大生命值 ，属于静态属性
    maxStrength = 100

    @classmethod 
    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name


warriors={}
# 斧头兵 是 战士的子类
class Axeman(Warrior):
    # 种类名称
    typeName = '斧头兵'
    AxemanName='none'

    # 雇佣价 120灵石
    price = 120

    # 最大生命值
    maxStrength = 120


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

# 鹰妖
class Eagle():
    typeName = '鹰妖'

# 狼妖
class Wolf():
    typeName = '狼妖'

# 森林
class Forest():
    def __init__(self,monster):
        # 该森林里面的妖怪
        self.monster = monster
def hire(warrior):
    warriors[warrior.name] = warrior

print('''************************************游戏开始***************************************''')
username = input('请输入用户名:\n')
print('{},欢迎来到文字冒险游戏！'.format(username))
print('检测到新用户,正在为您生成属性')
stoneNumber=1000
#warriors={"您暂时没有雇佣战士"}
def message_属性():
    global message_属性1
    message_属性1 = ('{},你的属性为:灵石数量{},拥有的战士{}'.format(username,stoneNumber,warriors))
    print(message_属性1)
message_属性()

# 森林 列表
forestList = []
for i in range(7):
    # 产生 0 或 1 的随机数
    rand_num = random.randint(0, 1)
    # 如果 rand_num 等于 0，那么产生鹰妖
    if rand_num == 0:
        print("第 " + str(i+1) + " 座森林里有鹰妖")
        forestList.append( Forest(Eagle()))
    # 如果 rand_num 等于 1，那么产生狼妖
    if rand_num == 1:
        print("第 " + str(i+1) + " 座森林里有狼妖")
        forestList.append( Forest(Wolf()))
print('你有10秒钟的时间记忆，10秒钟就会消失，在记忆完成后才会触发下一事件\n')    
time.sleep(10)
cen=input('时间已到,是否继续(‘是’继续游戏但上述内容将会消失，‘否’退出游戏):\n')
if cen=='是':
    print('游戏继续进行')
    for i in range(20):
        print('\n')
else:
    sys.exit()

buying = 'none'
print('''进入战士商店,输入要购买的英雄,例:输入'弓箭兵':购买弓箭兵;输入'退出':退出商店
                             物品: 弓箭兵  斧头兵  
                             金钱:  {}      {}    
                                                退出'''.format(Archer.price,
                                                               Axeman.price))
if stoneNumber> 0:
    while buying != '退出':       
        buying = input('你有{}灵石,选择要雇佣的战士\n'.format(stoneNumber))
        if buying == '弓箭兵':
            ArcherNumber = int(input('选择要雇佣几位弓箭兵:\n'))
            if stoneNumber >= (Archer.price)*ArcherNumber:
                stoneNumber-= (Archer.price)*ArcherNumber
                for i in range(ArcherNumber):  
                    ArcherName=input('请给弓箭兵起一个名字:')
                    hire(Archer(ArcherName))
                    #warriors[Archer(ArcherName).name] = Archer(ArcherName)
                    #Archer.__init__(Archer.maxStrength)
                    #warriors["owner"] = "tyson" 
                print('雇佣成功')
            else:
                print('灵石不足')
        if buying == '斧头兵':
            AxemanNumber = int(input('选择要雇佣几位斧头兵:\n'))
            if stoneNumber >= (Axeman.price)*AxemanNumber:
                stoneNumber -= (Axeman.price)*AxemanNumber
                for i in range(AxemanNumber):
                    AxemanName=input('请给斧头兵起一个名字:')
                    hire(Axeman(AxemanName))
                    #warriors[Axeman(ArcherName).name] = Axeman(ArcherName)
                    #Axeman.__init__(Axeman.maxStrength)
                    #warriors.update({AxemanName})
                print('雇佣成功')
            else:
                print('灵石不足')
    
        if buying != '弓箭兵' and buying != '斧头兵' and buying != '退出':
                print('无法识别')
else:
    print('你并没有灵石,已自动退出。')
print('你目前麾下有:')
for i in warriors.keys():
    print(i)
next = input('输入\'前进\'可触发下一事件\n')
while next != '前进':
    if next == '属性':
        message_属性()
    next = input('你确定不触发任何事件?输入\'前进\'可触发下一事件\n')
def Adventure(warriors,forestList):
    if warriors:
        dispacth = input('请选择要派出的战士:')
        if dispacth in warriors:
            parameter = input('存在该英雄，是否确认派出该战士？(是or否)\n')
            if parameter == '是':
                warriors[dispacth].fightWithMonster(forestList[i].monster)
                print('你派出战士的血量为:{}'.format(warriors[dispacth].strength))
                if warriors[dispacth].strength > 0:               
                    print('恭喜你杀死{}'.format(forestList[i].monster.typeName))
                    print('你派出战士的血量为:{}'.format(warriors[dispacth].strength))
                    an=input('是否使用灵石给你的战士疗伤(是or否)：\n')
                    if an=='是':
                        ne = input('你要使用多少灵石给你的战士疗伤：')
                        warriors[dispacth].healing(int(ne))
                    else:
                        print('已放弃使用灵石给战士疗伤\n')
                else:                    
                    print('恭喜你的战士被{}杀死'.format(forestList[i].monster.typeName))
                    del warriors[dispacth]
                    if warriors:
                        print('请你派出下一个战士')
                        Adventure(warriors,forestList)
                    else:
                        print('你麾下没有战士，你被怪物杀死游戏结束！')
                        sys.exit()
            else:
            	Adventure(warriors,forestList)
if next == '前进':
    for i in range(7):
        print(f'你进入了第{i+1}座森林里面')
        Adventure(warriors,forestList)
    print('恭喜您成功通过所有关卡，你最后剩余的灵石数量为{}\n'.format(stoneNumber))
    print('你可以去参选国王啦！')



 

   