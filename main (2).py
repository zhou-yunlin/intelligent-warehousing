import random
import numpy as np
import tkinter
import threading
from tkinter.constants import INSERT
import time

root = tkinter.Tk()  # 总画布


# 初始化仓库和堆垛机轨道
class cangku_innit:
    def __init__(self):
        self.cangku = [[] for j in range(10)]  # 仓库和堆垛机轨道的数组，双数行为仓库，单数行为堆垛机轨道
        for r in range(0, 8):  # r代表行
            for c in range(0, 9):  # c代表列
                if r % 2 != 1:  # 双数行为仓库
                    cell = tkinter.Text(root, width=10, height=2)
                    self.cangku[r].insert(c, cell)
                    self.cangku[r][c].insert(0.0, '000000')
                else:  # 单数行为堆垛机轨道
                    cell = tkinter.Text(root, width=10, height=1, background='black')
                    self.cangku[r].insert(c, cell)
                cell.place(x=75 * c, y=100 * r)

    def check(self, xn, yn):  # 检测货柜里的库存
        h = self.cangku[xn * 2][yn]
        hh = h.get("0.0", "end")  # 获取该文本框中的字符串
        return hh


    def denggai_cangchu(self, xn, yn):  # 更改货柜中的存储货物数据，由外界输入字符串，以及xn,yn坐标
        h = tkinter.Text(root, width=10, height=2)
        # self.cangku[xn*2][yn].delete("1.0", 'end')
        str_list = [ch for ch in self.check(xn, 8 - mar[xn].c)]
        if str_list[mar[xn].e] is '0':
            str_list[mar[xn].e] = '1'
        elif str_list[mar[xn].e] is '1':
            str_list[mar[xn].e] = '0'
        s = ""
        for i in str_list:
            s = "".join(str_list)
        self.cangku[xn * 2].insert(yn, h)
        self.cangku[xn * 2][yn].insert(0.0, s)
        h.place(x=75 * yn, y=200 * xn)

    def change_duiduoji(self, xn, yn, flag):  # xn,yn代表在数组中的堆垛机位置
        if flag == 1:  # 1表示有货物，涂成红色
            h = tkinter.Text(root, width=10, height=1, background='red')
            self.cangku[1 + 2 * xn].insert(yn, h)
            h.place(x=75 * (yn), y=100 * (1 + 2 * xn))
        if flag == 0:  # 0表示没有有货物，涂成黄色
            h = tkinter.Text(root, width=10, height=1, background='yellow')
            self.cangku[1 + 2 * xn].insert(yn, h)
            h.place(x=75 * (yn), y=100 * (1 + 2 * xn))
        if flag == 2:
            h = tkinter.Text(root, width=10, height=1, background='black')
            self.cangku[1 + 2 * xn].insert(yn, h)
            h.place(x=75 * (yn), y=100 * (1 + 2 * xn))


# 货柜出入点


class huogui_churu:
    def __init__(self):
        self.huoguichuru = tkinter.Text(root, width=10, height=1)  # 创建货柜出入点
        self.huoguichuru.place(x=75 * 8, y=720)
        self.huoguichuru.insert(0.0, 0)  # 货柜出入点列表

    def change(self):  # flag即为货物数量
        self.huoguichuru.delete(0.0, "end")
        self.huoguichuru.insert(0.0, out)


# 仓库出入点
class cangku_churu:
    def __init__(self):
        self.cangkuchuru = []  # 仓库出入点列表
        for r in range(0,20):
            c = tkinter.Text(root, width=2, height=1)  # 创建货柜出入点
            self.cangkuchuru.insert(r, c)
            c.place(x=75 * 15, y=40 * r)
            self.cangkuchuru[r].insert(0.0, 0)

    def change(self, n):
        self.cangkuchuru[n].delete(0.0, "end")
        self.cangkuchuru[n].insert(0.0, len(waitin[n]))


global i, j
i = 0
j = 0


# 小车轨迹初始化
class xiaoche_guiji_innit:
    def __init__(self):
        self.xiaoche_guiji = [[] for j in range(100)]
        for r in range(0, 47):  # r代表行
            for c in range(0, 21):  # c代表列
                cell = tkinter.Canvas(root, width=20, height=20, bg='pink')
                self.xiaoche_guiji[r].insert(c, cell)
                cell.place(x=700 + c * 20, y=20 * r)

    def change(self, xn, yn, flag):  # xn,yn代表在数组中的小车位置
        if car[flag].f == 0:
            h = tkinter.Text(root, width=2, height=1, bg='yellow')
            self.xiaoche_guiji[xn].insert(yn, h)
            self.xiaoche_guiji[xn][yn].insert(0.0,flag)
            h.place(x=703 + yn * 20, y=20 * xn+3)
        if car[flag].f == 1:
            h = tkinter.Text(root, width=2, height=1, bg='yellow')
            self.xiaoche_guiji[xn].insert(yn, h)
            self.xiaoche_guiji[xn][yn].insert(0.0,flag)
            h.place(x=703 + yn * 20, y=20 * xn+3)
        if car[flag].f== 2:
            h = tkinter.Text(root, width=2, height=1, bg='red')
            self.xiaoche_guiji[xn].insert(yn, h)
            self.xiaoche_guiji[xn][yn].insert(0.0, flag)
            h.place(x=703 + yn * 20, y=20 * xn + 3)
        if car[flag].f == 3:
            h = tkinter.Text(root, width=2, height=1, bg='yellow')
            self.xiaoche_guiji[xn].insert(yn, h)
            self.xiaoche_guiji[xn][yn].insert(0.0, flag)
            h.place(x=703 + yn * 20, y=20 * xn + 3)
        if car[flag].f == 4:
            h = tkinter.Text(root, width=2, height=1, bg='red')
            self.xiaoche_guiji[xn].insert(yn, h)
            self.xiaoche_guiji[xn][yn].insert(0.0, flag)
            h.place(x=703 + yn * 20, y=20 * xn + 3)
        if car[flag].f == 5:
            h = tkinter.Text(root, width=2, height=1, bg='yellow')
            self.xiaoche_guiji[xn].insert(yn, h)
            self.xiaoche_guiji[xn][yn].insert(0.0, flag)
            h.place(x=703 + yn * 20, y=20 * xn + 3)
        if car[flag].f == 6:
            h = tkinter.Text(root, width=2, height=1, bg='red')
            self.xiaoche_guiji[xn].insert(yn, h)
            self.xiaoche_guiji[xn][yn].insert(0.0, flag)
            h.place(x=703 + yn * 20, y=20 * xn + 3)
        if flag == -1:  # 涂成粉色
            h = tkinter.Canvas(root, width=18, height=18, bg='pink')
            self.xiaoche_guiji[xn].insert(yn, h)
            h.place(x=700 + yn * 20, y=20 * xn)

    def changee(self):
        global i, j
        hh = tkinter.text(root, width=18, height=18, bg='pink')
        self.xiaoche_guiji[i].insert(j, hh)
        hh.place(x=700 + j * 20, y=20 * i)
        if i < 40:
            i += 1
            h = tkinter.Canvas(root, width=18, height=18, bg='red')
            self.xiaoche_guiji[i].insert(j, h)
            h.place(x=700 + j * 20, y=20 * i)
        if j < 20:
            j += 1
            h.place(x=700 + j * 20, y=20 * i)
        root.after(1000, xiaocheguiji.changee)

class Car:  # 小车
    def __init__(self, a, b):
        self.x = a  # 长边位置点
        self.y = b  # 宽边位置点
        self.sx = a  # 当前所在x轴位置
        self.sy = b  # 当前所在y轴位置
        self.d = -1  # 目标点编号
        self.dx = 0  # 目标x轴位置
        self.dy = 0  # 目标y轴位置
        self.f = 0  # 当前状态，0空载起点等，1空载回，2负载回，3空载终点等，4负载终点等，5空载去，6负载去
        self.a = -1  # 长度
        self.c = -1  # 层数
        self.q=0 #小车方向

class Mar:  # 终点
    def __init__(self, a, b):
        self.x = a  # 长边位置点
        self.y = b  # 宽边位置点
        self.sx = a  # 当前所在x轴位置
        self.sy = b  # 当前所在y轴位置
        self.f = 0  # 当前状态，0空载起点等，1负载起点等，2空载去，3负载去，4空载回，5负载回
        self.c = -1  # 长度
        self.e = -1  # 层数


class Pak:  # 货物
    def __init__(self, a, b, d):
        self.a = a  # 堆垛机编号
        self.b = b  # 长度
        self.d = d  # 层数


class Waitin:  # 等待队列
    def __init__(self, a, b, d):
        self.a = a  # 目标堆垛机编号
        self.b = b  # 目标长度
        self.d = d  # 目标层数


class Waitout:  # 等待队列
    def __init__(self, a, b, d, e):
        self.a = a  # 堆垛机编号
        self.b = b  # 长度
        self.d = d  # 层数
        self.e = e  # 目标装载点


m = 20  # 货物装载点的个数，即小车个数
n = 4  # 货物入库点的个数，即堆垛机的个数
a = 45  # 随机小车运动区域长
b = 25  # 随机小车运动区域宽
c = 8  # 随机堆垛机运动区域长度
x = 1  # 小车速度
y = 1  # 堆垛机速度
time1 = 0  # 当前时间
cnt = 0  # 入库量
car = []
mar = []
pak = []
# 等待入库队列
waitin = [[] for i in range(25)]
# 等待出库队列
waitout = [[] for i in range(25)]
# 建立小车运动区域二维数组,一二维坐标，置1则此时这个点存在小车
p1 = np.zeros((a + 5, b + 5), dtype=np.int_)
# 建立货物区域三维数组,一维长度，二维上下,三维高度，置1则此位置存在货物
p2 = np.zeros((n + 5, c + 5, 10), dtype=np.int_)
# 建立堆垛机运动位置数组，一位编号，数值为位置
p3 = np.zeros((m), dtype=np.int_)
rk = []  # 入库量
ck = []  # 出库量
out=0

def checknumber():  # 查询指定时间内出入库情况，a标志出入库，b起始时间，c结束时间
    text4.delete(0.0, "end")
    a = int(text2.get(0.0,"end"))
    b = int(text3.get(0.0,"end"))
    if int(text1.get(0.0)) == 0:
        text4.insert("insert", ck[b] - ck[a])
    elif int(text1.get(0.0)) == 1:
        text4.insert("insert", rk[b] - rk[a])


class carThread(threading.Thread):  ##小车运行
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global time1, cnt, out
        while True:
            flag1 = 0
            flag2 = 0
            time.sleep(0.5)
            time1 += 1
            if time1 % 3 == 0:
                m0 = random.randint(0, m - 1)  # 随机装载点
                n0 = random.randint(0, n - 1)  # 随机入库点
                c1 = random.randint(1, c)  # 随机货架长度
                c3 = random.randint(0,5)  # 随机货架层数
                while p2[n0, c1, c3] != 0:
                    n0 = random.randint(0, n - 1)  # 随机入库点
                    c1 = random.randint(0, c)  # 随机货架长度
                    c3 = random.randint(0,5)  # 随机货架层数
                p2[n0, c1, c3] = 2
                waitin[m0].append(Waitin(n0, c1, c3))  # 入库申请加入队列
                cangkuchuru.change(m0)
                if time1 % 10 == 0 and cnt != 0:
                    k = random.randint(0, cnt - 1)  # 随机库存货物编号
                    m1 = random.randint(0, m - 1)  # 随机装载点
                    waitout[m0].append(Waitout(pak[k].a, pak[k].b, pak[k].d, m1))  # 出库申请加入队列
                    out+=1
                    huoguichuru.change()
                    cnt -= 1
                    del pak[k]
            # 小车执行活动
            for i in range(m):
                if car[i].f == 0:  # 空载起点等
                    if len(waitout[i]):  # 处理出库申请
                        n1 = waitout[i][0].a
                        car[i].d = n1
                        car[i].dx = mar[n1].x
                        car[i].dy = mar[n1].y
                        car[i].a = waitout[i][0].b
                        car[i].c = waitout[i][0].d
                        car[i].f = 5
                        del waitout[i][0]
                    elif len(waitin[i]):  # 处理入库申请
                        n1 = waitin[i][0].a
                        car[i].d = n1
                        car[i].dx = mar[n1].x
                        car[i].dy = mar[n1].y
                        car[i].a = waitin[i][0].b
                        car[i].c = waitin[i][0].d
                        car[i].f = 6
                        xiaocheguiji.change(car[i].x, car[i].y, i)  # 满载小车
                        del waitin[i][0]
                        cangkuchuru.change(i)
                elif car[i].f == 1 or car[i].f == 2:  # 空载回与负载回
                    if car[i].f == 1 and len(waitout[i]):  # 空载回的同时处理出库申请
                        n1 = waitout[i][0].a
                        car[i].d = n1
                        car[i].dx = mar[n1].x
                        car[i].dy = mar[n1].y
                        car[i].f = 5
                        del waitout[i][0]
                        continue
                    if car[i].sx < car[i].dx:  # 向右下走
                        if p1[car[i].sx, car[i].sy + 1] == -1 and car[i].sy + 1 <= car[i].dy and car[i].sy<i and car[i].q==0:  # 向右
                            p1[car[i].sx, car[i].sy] = -1
                            xiaocheguiji.change(car[i].sx, car[i].sy, -1)  #
                            p1[car[i].sx, car[i].sy + 1] = i
                            car[i].sy += 1
                            xiaocheguiji.change(car[i].sx, car[i].sy, i)
                        elif p1[car[i].sx + 1, car[i].sy] == -1 and car[i].sx + 1 <= car[i].dx:  # 向下
                            p1[car[i].sx, car[i].sy] = -1
                            xiaocheguiji.change(car[i].sx, car[i].sy, -1)
                            p1[car[i].sx + 1, car[i].sy] = i
                            car[i].sx += 1
                            xiaocheguiji.change(car[i].sx, car[i].sy, i)
                            car[i].q=0
                        else: #向右避让
                            if car[i].sy + 1 <=20  and p1[car[i].sx, car[i].sy+1] == -1:  # 向上
                                p1[car[i].sx, car[i].sy] = -1
                                xiaocheguiji.change(car[i].sx, car[i].sy, -1)
                                p1[car[i].sx, car[i].sy+1] = i
                                car[i].sy += 1
                                xiaocheguiji.change(car[i].sx, car[i].sy, i)
                                car[i].q=-1
                    elif car[i].sx > car[i].dx:  # 向右上走
                        if p1[car[i].sx, car[i].sy + 1] == -1 and car[i].sy + 1 <= car[i].dy and car[i].sy<i and car[i].q==0:  # 向右
                            p1[car[i].sx, car[i].sy] = -1
                            xiaocheguiji.change(car[i].sx, car[i].sy, -1)
                            p1[car[i].sx, car[i].sy + 1] = i
                            car[i].sy += 1
                            xiaocheguiji.change(car[i].sx, car[i].sy, i)
                        elif p1[car[i].sx - 1, car[i].sy] == -1 and car[i].sx - 1 >= car[i].dx:  # 向上
                            p1[car[i].sx, car[i].sy] = -1
                            xiaocheguiji.change(car[i].sx, car[i].sy, -1)
                            p1[car[i].sx - 1, car[i].sy] = i
                            car[i].sx -= 1
                            xiaocheguiji.change(car[i].sx, car[i].sy, i)
                            car[i].q=0
                        else: #向右避让
                            if car[i].sy + 1 <= 20 and p1[car[i].sx, car[i].sy + 1] == -1:  # 向上
                                p1[car[i].sx, car[i].sy] = -1
                                xiaocheguiji.change(car[i].sx, car[i].sy, -1)
                                p1[car[i].sx, car[i].sy + 1] = i
                                car[i].sy += 1
                                xiaocheguiji.change(car[i].sx, car[i].sy, i)
                                car[i].q=-1
                    else:
                        if p1[car[i].sx, car[i].sy + 1] == -1 and car[i].sy + 1 <= car[i].dy:  # 向右
                            p1[car[i].sx, car[i].sy] = -1
                            xiaocheguiji.change(car[i].sx, car[i].sy, -1)
                            p1[car[i].sx, car[i].sy + 1] = i
                            car[i].sy += 1
                            xiaocheguiji.change(car[i].sx, car[i].sy, i)
                    if car[i].sx == car[i].dx and car[i].sy == car[i].dy:  # 抵达目标的
                        if car[i].f == 1:
                            car[i].f = 0
                        elif car[i].f == 2:
                            if car[i].sx == car[i].x and car[i].sy == car[i].y:  # 目标点是归属点
                                car[i].f = 0
                            else:
                                car[i].dx = car[i].x
                                car[i].dy = car[i].y
                        flag2 += 1
                elif car[i].f == 3:  # 空载终点等
                    if mar[car[i].d].f == 0 or mar[car[i].d].f==3:
                        mar[car[i].d].c = car[i].a
                        mar[car[i].d].e = car[i].c
                        mar[car[i].d].f = 1
                    elif mar[car[i].d].f == 5:
                        car[i].dx = car[i].x
                        car[i].dy = car[i].y
                        car[i].f = 2
                        mar[car[i].d].f = 0
                        xiaocheguiji.change(car[i].sx, car[i].sy, i)
                        cangku.change_duiduoji(car[i].d, 8 - p3[car[i].d], 0)
                        out-=1
                        huoguichuru.change()
                elif car[i].f == 4:  # 负载终点等
                    if mar[car[i].d].f == 0:
                        mar[car[i].d].f = 2
                        mar[car[i].d].c = car[i].a
                        mar[car[i].d].e = car[i].c
                        car[i].dx = car[i].x
                        car[i].dy = car[i].y
                        car[i].f = 1
                        xiaocheguiji.change(car[i].sx, car[i].sy, i)
                        cangku.change_duiduoji(car[i].d, 8 - p3[car[i].d], 1)
                elif car[i].f == 5 or car[i].f == 6:  # 空载去和负载去
                    if car[i].sx < car[i].dx:  # 向左下
                        if p1[car[i].sx, car[i].sy - 1] == -1 and car[i].sy - 1 >= car[i].dy and car[i].sy>=i and car[i].q==0:  # 向左
                            p1[car[i].sx, car[i].sy] = -1
                            xiaocheguiji.change(car[i].sx, car[i].sy, -1)
                            p1[car[i].sx, car[i].sy - 1] = i
                            car[i].sy -= 1
                            xiaocheguiji.change(car[i].sx, car[i].sy, i)
                        elif p1[car[i].sx + 1, car[i].sy] == -1 and car[i].sx + 1 <= car[i].dx:  # 向下
                            p1[car[i].sx, car[i].sy] = -1
                            xiaocheguiji.change(car[i].sx, car[i].sy, -1)
                            p1[car[i].sx + 1, car[i].sy] = i
                            car[i].sx += 1
                            xiaocheguiji.change(car[i].sx, car[i].sy, i)
                            car[i].q=0
                        else: #向右避让
                            if car[i].sy + 1 <= 20 and p1[car[i].sx, car[i].sy + 1] == -1:  # 向上
                                p1[car[i].sx, car[i].sy] = -1
                                xiaocheguiji.change(car[i].sx, car[i].sy, -1)
                                p1[car[i].sx, car[i].sy + 1] = i
                                car[i].sy += 1
                                xiaocheguiji.change(car[i].sx, car[i].sy, i)
                                car[i].q=-1
                    elif car[i].sx > car[i].dx:  # 向左上
                        if p1[car[i].sx, car[i].sy - 1] == -1 and car[i].sy - 1 >= car[i].dy and car[i].sy>=i and car[i].q==0:  # 向左
                            p1[car[i].sx, car[i].sy] = -1
                            xiaocheguiji.change(car[i].sx, car[i].sy, -1)
                            p1[car[i].sx, car[i].sy - 1] = i
                            car[i].sy -= 1
                            xiaocheguiji.change(car[i].sx, car[i].sy, i)
                        elif p1[car[i].sx - 1, car[i].sy] == -1 and car[i].sx - 1 >= car[i].dx:  # 向上
                            p1[car[i].sx, car[i].sy] = -1
                            xiaocheguiji.change(car[i].sx, car[i].sy, -1)
                            p1[car[i].sx - 1, car[i].sy] = i
                            car[i].sx -= 1
                            xiaocheguiji.change(car[i].sx, car[i].sy, i)
                            car[i].q=0
                        else:  # 向右避让
                            if car[i].sy + 1 <= 20 and p1[car[i].sx, car[i].sy + 1] == -1:  # 向上
                                p1[car[i].sx, car[i].sy] = -1
                                xiaocheguiji.change(car[i].sx, car[i].sy, -1)
                                p1[car[i].sx, car[i].sy + 1] = i
                                car[i].sy += 1
                                xiaocheguiji.change(car[i].sx, car[i].sy, i)
                                car[i].q=-1
                    else:
                        if p1[car[i].sx, car[i].sy - 1] == -1 and car[i].sy - 1 >= car[i].dy:  # 向左
                            p1[car[i].sx, car[i].sy] = -1
                            xiaocheguiji.change(car[i].sx, car[i].sy, -1)
                            p1[car[i].sx, car[i].sy - 1] = i
                            car[i].sy -= 1
                            xiaocheguiji.change(car[i].sx, car[i].sy, i)
                    if car[i].sx == car[i].dx and car[i].sy == car[i].dy:  # 抵达目标位置
                        if car[i].f == 5:
                            car[i].f = 3
                        elif car[i].f == 6:
                            car[i].f = 4
            for i in range(n):
                if mar[i].f == 0:  # 空载等
                    continue
                elif mar[i].f == 1:  # 空载去
                    if mar[i].c == p3[i]:
                        mar[i].f = 4
                        p2[i, mar[i].c, mar[i].e] = 0
                        cangku.denggai_cangchu(i, 8 - mar[i].c)
                        cangku.change_duiduoji(i, 8 - p3[i], 1)
                        continue
                    cangku.change_duiduoji(i, 8-p3[i], 2)
                    if mar[i].c>=p3[i]:
                        p3[i] += 1
                    else:
                        p3[i]-=1
                    cangku.change_duiduoji(i, 8 - p3[i], 0)
                elif mar[i].f == 2:  # 负载去
                    if mar[i].c == p3[i]:
                        mar[i].f = 3
                        flag1 += 1
                        pak.append(Pak(i, mar[i].c, mar[i].e))
                        p2[i, mar[i].c, mar[i].e] = 1
                        cnt += 1
                        ##修改货舱
                        cangku.denggai_cangchu( i ,8-mar[i].c)
                        cangku.change_duiduoji(i, 8 - p3[i], 0)
                        continue
                    cangku.change_duiduoji(i, 8 - p3[i], 2)
                    p3[i] += 1
                    cangku.change_duiduoji(i, 8 - p3[i], 1)
                elif mar[i].f == 3:  # 空载回
                    if p3[i] == 0:
                        mar[i].f = 0
                        continue
                    cangku.change_duiduoji(i, 8 - p3[i], 2)
                    p3[i] -= 1
                    cangku.change_duiduoji(i, 8 - p3[i], 0)
                elif mar[i].f == 4:  # 负载回
                    if p3[i] == 0:
                        mar[i].f = 5
                        continue
                    cangku.change_duiduoji(i, 8 - p3[i], 2)
                    p3[i] -= 1
                    cangku.change_duiduoji(i, 8 - p3[i], 1)
                elif mar[i].f == 5:  # 负载等
                    continue
            rk.append(rk[time1 - 1] + flag1)
            ck.append(ck[time1 - 1] + flag2)

if __name__ == "__main__":
    root.geometry('1200x1000')  ## 规定窗口大小500*500像素
    root.resizable(False, False)  ## 规定窗口不可缩放
    cangku = cangku_innit()  # 初始化仓库和堆垛机轨道
    cangkuchuru = cangku_churu()  # 初始化仓库出入点
    huoguichuru = huogui_churu()  # 初始化堆垛机出入囤积的货物点
    xiaocheguiji = xiaoche_guiji_innit()  # 小车轨迹初始化
    for i in range(m):
        car.insert(i, Car(2*i, 20))
        xiaocheguiji.change(2*i, 20, i)  # 空载小车
    for i in range(n):  # 确定入库点
        mar.insert(i, Mar(5 + 10 * i, 0))
        cangku.change_duiduoji(i, 8, 0)  # 控制堆垛机位置和状态（空）
    for i in range(a + 5):
        for j in range(b + 5):
            p1[i, j] = -1
    for i in range(m):  # 起始小车停的位置
        p1[2*i, 20] = i  # 小车编号

    # 按钮响应
    label1 = tkinter.Label(root, width=15, height=1, text="出库(0)或入库(1)")
    label1.place(x=0, y=770)
    label2 = tkinter.Label(root, width=15, height=1, text="开始时间")
    label2.place(x=120, y=770)
    label3 = tkinter.Label(root, width=15, height=1, text="截止时间")
    label3.place(x=240, y=770)
    label4 = tkinter.Label(root, width=15, height=1, text="变化量")
    label4.place(x=360, y=770)
    text1 = tkinter.Text(root, width=15, height=2)
    text1.place(x=0, y=800)
    text2 = tkinter.Text(root, width=15, height=2)
    text2.place(x=120, y=800)
    text3 = tkinter.Text(root, width=15, height=2)
    text3.place(x=240, y=800)
    text4 = tkinter.Text(root, width=15, height=2)
    text4.place(x=360, y=800)
    button = tkinter.Button(root, width=15, height=1, text="计算", command=checknumber)
    button.place(x=480, y=800)
    rk.append(0)
    ck.append(0)
    thread1 = carThread("Thread-1")
    thread1.start()
    root.mainloop()
