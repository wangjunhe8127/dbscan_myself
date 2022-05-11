# encoding: utf-8
'''''
author:王竣禾
time：2019.12.1下午-2019.12.2上午
describe：dbscan基于密度的聚类，且此处定义了就是两类，实际上真正的dbscan不需要定义，且中间有参数需奥根据观察到的数据设置，如point的初始值，需要根据r中第一个不为0的k设置
后期还有待完善：参数完善更好，更合适的程序代码，自动分类
'''''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
data=pd.read_csv('/home/xiaoshumiao/PycharmProjects/dbscan/data0.csv').values
# # #先看大致分布，确定初始点
# plt.plot(data[:,0],data[:,1],'bo')
# plt.show()
r=[1]*len(data)
hh=[0]
tt=[0]
c=np.array([0,0])
cc=np.array([0,0])
ccc=np.array([0,0])
d=0
e=0
f=0
gg=0
t=0.3
plt.subplot(1,2,1)
#将不同类型的点分入不同的矩阵
for i in range(len(data)):
    n = 0
    for j in range(len(data)):
        if np.linalg.norm(data[i]-data[j])<t:
            n=n+1
    if n>=6:
        if f==0:
            c=c+data[i]
        else:
            c=np.vstack((c,data[i]))
        f=f+1

    elif (n<6)&(n>3):
        if e==0:
            cc=cc+data[i]
        else:
            cc=np.vstack((cc,data[i]))#边缘点拼成新矩阵
        e=e+1
        r[i]=0
        plt.plot(data[i:i + 1, 0], data[i:i + 1, 1], 'yo')#画出这两类点
    else:
        r[i] = 0
        d=d+1
        plt.plot(data[i:i + 1, 0], data[i:i + 1, 1], 'bo')
point=1#观擦第一个不是0的

hh[0]=hh[0]+1#观察第一个不是0的

ll=0#判断是不是没有单个可到达
p=0#hh中的位置
print r
print len(data)
yy=0


print d+e+f
#r[k]=0的是边界点和噪声点
#等于point判定放在前面，要不可能先判断不等于0就不进循环了
for u in range(2):
    for i in range(len(c)):
        k=0
        gg=0
        ll=0
        if r[point]!=0:
            while (k==point)|(r[k]==0):#既不等又不等于0
                k = k + 1
                while r[k] == 0:

                    k = k + 1
            if k >= len(c):  # 超过大小限制
                gg = 1
                if u == 0:
                    for j in range(len(hh)):  # 如果新的没有可以满足条件的，从之前的中找。
                        if (np.linalg.norm(c[hh[j]] - c[point]) < t):
                            ll = 1
                            p = j
                            break
                else:
                    for j in range(len(tt)):  # 如果新的没有可以满足条件的，从之前的中找。
                        if (np.linalg.norm(c[tt[j]] - c[point]) < t):
                            ll = 1
                            p = j
                            break
            while (np.linalg.norm(c[point]-c[k])>=t)&(gg==0):#如果不满足半径条件就加大k，找满足条件的 核心点
                k = k + 1
                while (k == point)|(r[k]==0):
                    k = k + 1
                    while r[k] == 0:
                        k = k + 1

                if k>=len(c):#超过大小限制
                    gg=1
                    if u==0:
                        for j in range(len(hh)):#如果新的没有可以满足条件的，从之前的中找。
                            if np.linalg.norm(c[hh[j]] - c[point]) < t:
                                gg=0
                                ll=1
                                p=j
                                break
                    else:
                        for j in range(len(tt)):#如果新的没有可以满足条件的，从之前的中找。
                            if np.linalg.norm(c[tt[j]] - c[point]) < t:
                                gg=0
                                ll=1
                                p=j
                                break
                    break
            if gg==0:#排除怎么也找不到同一类的点
                if u==0:

                   plt.plot(data[point:point+ 1, 0], data[point:point + 1, 1], 'ro')
                else:
                    plt.plot(data[point:point + 1, 0], data[point:point + 1, 1], 'go')
                if ll==0:#如果是新的点就把它加到类中，并用k更新point
                    r[point] = 0
                    point=k
                    if u==0:
                        hh=np.vstack((hh,k))#一直一类点的索引
                    else:
                        tt=np.vstack((tt,k))
                else:#否则就只是置0,并且这样更新
                    r[point] = 0
                    if u ==0:
                        point=int(random.choice(hh))#注意变成标量！！！！！   ！！！！！！！！！！！！！！！！！随机从中选点   需要确定的每次便利吗？？？？？？ 实验发现迭代次数没关系，而且注意这里可以迭代不知len（c）次
                    else:
                        point = int(random.choice(tt))
                    r[point] = 1#为了保证下一次可以进去if
    for pp in range(len(data)):
        if r[pp]!=0:
            if pp not in hh:
               point = pp
               break
            else:
                pp = pp + 1
    tt[0] = tt[0] +pp

for i in range(len(cc)):
    minh=np.linalg.norm(cc[i]-hh[0])
    mint=np.linalg.norm(cc[i]-hh[0])
    for j in range(len(hh)):
        if minh>np.linalg.norm(cc[i]-hh[j]):
            minh=np.linalg.norm(cc[i]-hh[j])
    for k in range(len(tt)):
        if mint>np.linalg.norm(cc[i]-tt[k]):
            mint=np.linalg.norm(cc[i]-tt[k])
    if minh>mint:
        plt.plot(cc[i:i + 1, 0], cc[i:i + 1, 1], 'go')
    else:
        plt.plot(cc[i:i + 1, 0], cc[i:i + 1, 1], 'ro')
plt.subplot(1,2,2)
plt.plot(data[:,0],data[:,1],'bo')
plt.show()