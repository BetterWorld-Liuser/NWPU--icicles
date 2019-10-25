#在做作业的时候没有发现很好的参考资料，大多数同学都是直接拿学长的copy一下，自己什么却都不太懂
#尤其是在我的同学给我了一份说是上届同学自己编的代码，却满是漏洞，没有包，使用python2，没有预先定义的变量，就这说是他自己写的，我是不信的。
#自认为这不是一个很好的学习状态，故作此篇教程希望各位同学能在借鉴的同时还能有所收获。


#此篇教程以python3语言为主干
#例题为第2题
#参数设置为6-A,6-B,6-C的参数
#如果你还没看题目，希望你先去看看这一题，用书上说的解析法过一遍再来看，会好理解很多

#为了便于新手理解，一些地方的代码没有用程序员的方式写，大佬轻喷
#我的作品绝非绝对正确，请以批判的眼光看待，如果能改正则更好

#导入一些数学处理的常用包，如果你不知道如何安装这些包，建议给懂的同学看，并让他教你，你就放弃这篇教程吧，不太适合你。
#或者你也可以去学习一下python3，对你以后都有帮助。
from scipy.optimize import fsolve
import numpy as np
from math import cos,sin,pi
from matplotlib import pyplot as plt 
import matplotlib
#这里的设置是为了让表里标题的中文能正常显示，如果你不懂复制就好。如果你想了解更多，百度这个函数名，会有相关解释。
matplotlib.rcParams["font.family"]="Microsoft YaHei"



#这个地方就是参数设置的地方，对，我的名字叫刘政东
#LAB即是6-A的参数
LAB = 220

#这里设置最后导出图像文件的名字
name = "张勉之"

#这里是非线性方程解法的初始值的全局参数，不懂没关系，接着看。
parameter1=100
parameter2=0
parameter3=0
parameter4=-500
parameter5=700


#这个是我自编写的修复函数的精准度的调和值，值越小，修复程度越高，图像损失程度越大。
#其实在大部分题目里应该是不需要使用修复函数的。
accuracy = 50


#定义函数
#功能：根据主动件角度c1解出各个杆的相关值
#参数：c1为主动件初始角度值

#输出：
#s1为滑块B到D的长度
#C2为杆DC与水平方向的夹角
#c3为杆ED与水平方向的夹角
#lc0为c点距离y轴的长度
#s2为滑块B到C的长度
#result为这五个数组成的数组


#LAB是上面设置的全局变量，这样设置的好处是，方便修改到6-B，6-C的参数，以便带带同组成员
def getResult(c1,LAB):

    #python3的特性，如果想在函数内更改全局变量，必须global声明一下
    global parameter1,parameter2,parameter3,parameter4,parameter5
    

    #为了观看方便，我把c1默认的单位设定为°，在下面函数默认使用弧度制，所以这里需要转换一下
    #讲角度制转成弧度制，因为下面函数计算默认使用弧度制。
    #pi就是π
    c1 = pi/180*c1


    #再到这里比较难理解
    #再定义一个函数，构造了等式，这是scipy包中解非线性方程的固定格式
    def structureEquation(x):
        
        #这里的变量在上面有说明
        s1=x[0]
        c2=x[1]
        c3=x[2]
        lc0=x[3]
        s2=x[4]
        
        
        #这里其实就是五个等式，他们后面都有 =0，这样好理解一些吧？式子建议写在纸上，对照题目看一下就很容易理解
        return[
               120+LAB*cos(c1)-s1*cos(c2)-160*cos(c3),
               460+LAB*sin(c1)-s1*sin(c2)-160*sin(c3),
               160*cos(c3)+960*cos(c2)-lc0,
               160*sin(c3)+960*sin(c2)-900,
               960-s1-s2
              ]
        #所以这个函数实际上就是传入一个数组，然后把这个数组组合一下再传出去。
        
        
    
    #fsolve的的作用是解非线性方程，第一个参数是构造非线性方程组的函数（也就是上面的函数），第二个参数是给与非线性方程组运算的初始值。
    #可以看到这里就用上了上面预先定义的全局变量

    #事实上fsolve利用的就是牛顿法（还不去百度！）求解的
    #牛顿法简单理解就是用计算机凑答案，而既然要凑答案，你就需要给计算机一个凑的起点，这个起点就是这五个参数。
    #牛顿法其实并不需要你掌握，但你要知道它大概是怎样的，建议去百度一下，但是掌握了更好
    #老师提到用高斯法求解线性方程，这个在部分题型中可能会用到，但我的题目中全都是非线性方程
    #线性方程和非线性方程的区别，以及具体定义，你要理解清楚，还不去百度！
    result = fsolve(structureEquation,[parameter1,parameter2,parameter3,parameter4,parameter5])
    
    
    
    
    #这里我们再将求得的值赋给这些全局变量
    #为的是下次求解的时候能尽可能接近下一次的结果
    #前面讲了计算机的答案是凑的，如果你给的参数接近真实答案，那么理论上，计算机就会凑得更快更准
    parameter1,parameter2,parameter3,parameter4,parameter5 = result
    


    #构造数组
    #现在我们返回我们求到的几个数并把弧度制再转为角度制
    result = [
              result[0],
              (result[1]*180/pi),
              (result[2]*180/pi),
              result[3],
              result[4]
             ]
    return result


#修复受损函数图像
#作用：把数组中一些看起来就差很多的值转为正常值的平均值
#为什么会出现数值的受损啊？
#因为牛顿法使用的凑的方法，凑就有凑不出来的情况，导致数值远远偏离
#原理我不打算细讲了，你知道这个功能就完事儿，如果想看就看一看。
def repair(v):
    hold=0
    get=0
    cur=0
    while(True):
        if cur==len(v)-1:
            break
        cur=cur+1
        if abs(v[cur]-v[hold])>=accuracy and cur<len(v)-1:
            continue
        
        elif(cur-hold>=2 or cur==len(v)-1):
            #print(cur-1)
            get=cur
            space_cur = get-hold
            space = v[get]-v[hold]
            k=space/space_cur
            for i in range(1,space_cur):
                v[hold+i]=k*i+v[hold]
            hold=get
        else:
            hold=cur
                        
    return v



#现在就是重复上面的步骤了R为第一个函数的结果数组，看到后面你会明白，i也是
def getResult_v(c1,LAB,R,i):

    #全局变量声明
    global parameter1,parameter2,parameter3,parameter4,parameter5

    

    c1=c1*pi/180
    s1=R[0][i]
    c2=R[1][i]/180*pi
    c3=R[2][i]/180*pi
    
    

    #这里就开始构造第二个线性方程
    #这个方程需要你手动求导然后填进去
    #这其实是个线性方程，但牛顿法也能求，我图省事，就一直用牛顿法求了。
    #建议你们不要学
    def structureEquation_v(x):


        s1_v =x[0]#s1的速度
        w2=x[1]#θ1角速度
        w3=x[2]#θ2角速度
        v0=x[3]#C点速度


        return [
               -LAB*sin(c1)    -  s1_v*cos(c2)         +       s1*w2*sin(c2)      +   160*w3*sin(c3),
                LAB*cos(c1)    -  s1_v*sin(c2)         -       s1*w2*cos(c2)      -   160*w3*cos(c3),
               -160*w3*sin(c3)  -   960*w2*sin(c2)     - v0,
                160*w3*cos(c3)  +   960*w2*cos(c2)
              ]
    



    result=fsolve(structureEquation_v,[parameter1,parameter2,parameter3,parameter4])
    
    result = [
        result[0],
        result[1]*180/pi,
        result[2]*180/pi,
        result[3]
        
    ]
    
    return result



#接下来就一样了
def getResult_a(c1,LAB,r,w,i):
    global parameter1,parameter2,parameter3,parameter4,parameter5
    
    c1=c1*pi/180
    
    
    s1=r[0][i]
    c2=r[1][i]/180*pi
    c3=r[2][i]/180*pi
    
    
    s1_v=w[0][i]
    w2=  w[1][i]/180*pi
    w3=  w[2][i]/180*pi
    
    
    
    def structureEquation_a(x):
        s1_a =x[0]
        p2=x[1]
        p3=x[2]
        a0=x[3]
        return[
               -LAB*cos(c1)-s1_a*cos(c2)+s1_v*w2*sin(c2)+s1_v*w2*sin(c2)+s1*p2*sin(c2)+s1*(w2**2)*cos(c2)+160*p3*sin(c3)+160*(w3**2)*cos(c3),
               -LAB*sin(c1)-s1_a*sin(c2)-s1_v*w2*cos(c2)-s1_v*w2*cos(c2)-s1*p2*cos(c2)+s1*(w2**2)*sin(c2)-160*p3*cos(c3)+160*(w3**2)*sin(c3),
               -160*p3*sin(c3)-160*(w3**2)*cos(c3)-960*p2*sin(c2)-960*(w2**2)*cos(c2) - a0,
                160*p3*cos(c3)-160*(w3**2)*sin(c3)+960*p2*cos(c2)-960*(w2**2)*sin(c2)
        ]
    
    #fsolve的的作用是解非线性方程，第一个参数是构造非线性方程组的函数，第二个参数是给与非线性方程组运算的初始值。
    #如果有疑问请看下面的补充说明
    result = fsolve(structureEquation_a,[parameter1,parameter2,parameter3,parameter4])
    
    result = [
        result[0],
        result[1]*180/pi,
        result[2]*180/pi,
        result[3]
        
    ]
    
    return result







#重头戏
#这里生成一个0，1，2，3 ... 359的数组
c = np.arange(0,360,1)


#分别定义第一次结果的数组，第二次结果的数组，第三次结果的数组
r0,r1,r2,r3,r4 = [],[],[],[],[]
w0,w1,w2,w3 = [],[],[],[]
A0,A1,A2,A3 = [],[],[],[]


#每个角度都调用一次函数计算，然后加入到数组里

for x in c:
    k = getResult(x,LAB)
    r0.append(k[0])
    r1.append(k[1])
    r2.append(k[2])
    r3.append(k[3])
    r4.append(k[4])

r0=repair(r0)
r1=repair(r1)
r2=repair(r2)
r3=repair(r3)
r4=repair(r4)

R =[r0,r1,r2,r3,r4]
for x in range(len(c)):
    
    k=getResult_v(c[x],LAB,R,x)
    w0.append(k[0])
    w1.append(k[1])
    w2.append(k[2])
    w3.append(k[3])

w0=repair(w0)
w1=repair(w1)
w2=repair(w2)
w3=repair(w3)

W =[w0,w1,w2,w3]
for x in range(len(c)):
    k=getResult_a(c[x],LAB,R,W,x)
    A0.append(k[0])
    A1.append(k[1])
    A2.append(k[2])
    A3.append(k[3])

A0=repair(A0)
A1=repair(A1)
A2=repair(A2)
A3=repair(A3)




#画图
#这是定义图像的参数，写累了，不想写了，自己百度一下他们的意思吧，挺简单的...
plt.rcParams['figure.figsize'] = (10.0, 15.0)
plt.subplots_adjust(hspace = 0.5,wspace = 0.5)

plt.subplot(621)
plt.plot(c,r0)
plt.title("s1长度随主动件角度变化")

plt.subplot(622)
plt.plot(c,r1)
plt.title("θ2角度随主动件角度变化")

plt.subplot(623)
plt.plot(c,r2)
plt.title("θ3角度随主动件角度变化")


plt.subplot(624)
plt.plot(c,r3)
plt.title("C加随主动件角度变化")

plt.subplot(625)
plt.plot(c,w0)
plt.title("s1速度随主动件角度变化")

plt.subplot(626)
plt.plot(c,w1)
plt.title("θ2角速度随主动件角度变化")

plt.subplot(627)
plt.plot(c,w2)
plt.title("θ3角速度随主动件角度变化")


plt.subplot(628)
plt.plot(c,w3)
plt.title("C加速度随主动件角度变化")

plt.subplot(629)
plt.plot(c,A0)
plt.title("s1加速度随主动件角度变化")

plt.subplot(6,2,10)
plt.plot(c,A1)
plt.title("θ2角加速度随主动件角度变化")

plt.subplot(6,2,11)
plt.plot(c,A2)
plt.title("θ3角加速度随主动件角度变化")


plt.subplot(6,2,12)
plt.plot(c,A3)
plt.title("C加速度随主动件角度变化")

plt.savefig('./图-'+name)
plt.show()









