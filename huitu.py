# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:44:55 2019
@author: SAIC_G7066
"""
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
#plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题
plt.figure(figsize=(5,5))

X = np.linspace(-np.pi,np.pi,25)
C,S = np.cos(X),np.sin(X)

plt.plot(X,C)


plt.plot(X,C,label = 'COS', color = 'red', linewidth = 3,Marker = 'o', linestyle = '-')
plt.plot(X,S,label = 'SIN', color = 'blue', linewidth = 3,Marker = 'D', linestyle = ':')
plt.legend(['a','b'])
for x,y in zip(X,C):
    plt.text(x, y+0.05, '%.3f' % y, ha='center', va= 'bottom',fontsize=11)
for x,y in zip(X,S):
    plt.text(x, y+0.05, '%.3f' % y, ha='center', va= 'bottom',fontsize=11)
ticks = np.linspace(-np.pi,np.pi,5)
plt.xticks(ticks)
plt.yticks([-1,0,1],['b','c','d'])
plt.xlabel('x取值范围',{'size': 13})
plt.ylabel('y取值范围',{'size': 13})
plt.title('绘图')
#####################################################
import matplotlib.pyplot as plt
import numpy as np 
x = np.arange(10) 
ax = plt.subplot(111) 
for i in range(15):    
    ax.plot(x, i * x, label='$y = %ix$' % i) 
    plt.show()
    plt.legend() 
    plt.pause(0.3)

plt.xticks(np.linspace(0,8,3),['a','s','c'])
plt.yticks(np.linspace(0,35,5))
###########################################################
fig = plt.figure()
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
ax1.plot(X,C,label = 'COS', color = 'red', linewidth = 3,Marker = 'o', linestyle = '-')
ax2.plot(X,S,label = 'SIN', color = 'blue', linewidth = 3,Marker = 'D', linestyle = ':')
ax1.legend()
ax2.legend()
ticks = np.linspace(-np.pi,np.pi,5)
plt.xticks(ticks)
plt.yticks([-1,0,1],['b','c','d'])
plt.xlabel('x取值范围',{'size': 13})
plt.ylabel('y取值范围',{'size': 13})
plt.title('绘图')
###########################################################
plt.subplot(211)
plt.plot(X,S,linewidth = 3 , linestyle = ':')
plt.title('xxxxxxxxx')
plt.legend('sin')
plt.subplot(212)
plt.plot(X,C)
plt.title('yyyyyyyy')
plt.legend('cos')
###########################################################
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax4 = fig.add_subplot(2,2,4)
ax3 = fig.add_subplot(2,2,3)
ax2 = fig.add_subplot(2,2,2)
ax1 = fig.add_subplot(2,2,1)
ax4.plot([1.5,3.5,-2,1.6])
ax1.hist(np.random.randn(100),bins=20,color='k',alpha=0.3)
ax2.scatter(np.arange(30),np.arange(30) + 3 * np.random.randn(30))
ax3.plot(np.random.randn(50).cumsum(),'k--')
###########################################################
x = np.random.randn(10000)
a = np.array([3,2,3,4])
a.cum()
###########################################################
#plt.hist(x, bins=30, normed=1, alpha=0.5, histtype='stepfilled',cumulative=True); 
x = np.random.randn(100000)
#plt.bar(list(range(len(x))), x)
bins = np.linspace(-4,4,9)
plt.hist(x, normed = 1,bins = bins, color = 'r',label = 'sss')
###########################################################
x = [1,3,4,6,13,4]
y = 'a','b','c','d','e','f'
plt.pie(x,labels = y,explode = (0.1,0.1,0,0,0,0),autopct='%1.1f%%',shadow=True)
