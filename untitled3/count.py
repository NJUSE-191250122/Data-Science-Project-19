import csv
from pyhanlp import HanLP
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize as op

from scipy.optimize import leastsq
#@software{hanlp2,
#author = {Han He},
#  title = {{HanLP: Han Language Processing}},
#  year = {2020},
#  url = {https://github.com/hankcs/HanLP},
#}
#533,1561,1614,4209,379:17,799:16,1153:17,2339:14

def noComments(rootPath,desPath, length):
    wf = open(desPath, 'w+')
    with open(rootPath,'r')as f:
        reader=csv.reader(f)
        res=list(reader)
        for i in range(0,length):
            temp=HanLP.extractKeyword(res[i][0], 2)

            wf.write(",".join(temp))
            wf.write(",")
    wf.close()


def comments(rootPath,desPath,length,comLen):#源文件，目标文件地址，长度，评论个数
    wf = open(desPath, 'w+')
    with open(rootPath, 'r')as f:
        reader = csv.reader(f)
        res = list(reader)

        for i in range(0,length,2):
            for j in range(3, comLen, 1):
                try:
                    temp = HanLP.extractKeyword(res[i][j],2)
                    wf.write(",".join(temp))
                    wf.write(",")
                except:continue
    wf.close()

def count(rootPath,desPath):
    word_lst = []
    word_dict = {}
    with open(rootPath) as wf, open(desPath, 'w') as wf2:
        for word in wf:
            word_lst.append(word.split(','))
            for item in word_lst:
                for item2 in item:

                    if item2 not in word_dict:
                        word_dict[item2] = 1
                    else:
                        word_dict[item2] += 1
        wordOrder = sorted(word_dict.items(), key=lambda x: x[1], reverse=False)
        writer = csv.writer(wf2)
        try:
            writer.writerows(wordOrder)
        except UnicodeEncodeError:
            pass
def delete(rootPath,reslen):
    with open(rootPath, 'r') as f:
        reader = csv.reader(f)
        temp = list(reader)
        length=len(temp)
        count=-1
        res=[[0 for i in range(2)] for i in range(reslen)]
        for i in range(0,length,2):
            if (temp[i][0]!='#' and temp[i][0]!='@' and temp[i][0]!='%'):
                try:
                    count+=1
                    res[count][0]=temp[i][0]
                    res[count][1]=temp[i][1]
                except:continue
    wf=open(rootPath,'w+')
    writer = csv.writer(wf)
    try:
        writer.writerows(res)
    except UnicodeEncodeError:
        pass
def out(list1,path):
    with open(path,'w+') as wf:
        wf.write(",".join(list1))
        wf.write(",")


def sum(rootPath):
    sum=0
    with open(rootPath, 'r') as f:
        reader = csv.reader(f)
        temp = list(reader)
        length=len(temp)
        for i in range(0,length,2):
            sum+=int(temp[i][1])
    return sum
def get_psychology(set,int1):
    with open(r"res/res1.csv",'r')as f:
        reader=csv.reader(f)
        temp=list(reader)
        length=len(temp)
        for i in range(0, length, 2):
            if temp[i][2]==int1:
                set.add(temp[i][0])
    with open(r"res/res4.csv",'r')as f:
        reader=csv.reader(f)
        temp=list(reader)
        length=len(temp)
        for i in range(0, length, 2):
            if temp[i][2]==int1:
                set.add(temp[i][0])
    with open(r"res/res2.csv",'r')as f:
        reader=csv.reader(f)
        temp=list(reader)
        length=len(temp)
        for i in range(0, length, 2):
            if temp[i][2]==int1:
                set.add(temp[i][0])
    with open(r"res/res3.csv",'r')as f:
        reader=csv.reader(f)
        temp=list(reader)
        length=len(temp)
        for i in range(0, length, 2):
            if temp[i][2]==int1:
                set.add(temp[i][0])



    with open(r"res/comres1.csv",'r')as f:
        reader=csv.reader(f)
        temp=list(reader)
        length=len(temp)
        for i in range(0, length, 2):
            if temp[i][2]==int1:
                set.add(temp[i][0])
    with open(r"res/comres4.csv",'r')as f:
        reader=csv.reader(f)
        temp=list(reader)
        length=len(temp)
        for i in range(0, length, 2):
            if temp[i][2]==int1:
                set.add(temp[i][0])
    with open(r"res/comres2.csv",'r')as f:
        reader=csv.reader(f)
        temp=list(reader)
        length=len(temp)
        for i in range(0, length, 2):
            if temp[i][2]==int1:
                set.add(temp[i][0])
    with open(r"res/comres3.csv",'r')as f:
        reader=csv.reader(f)
        temp=list(reader)
        length=len(temp)
        for i in range(0, length, 2):
            if temp[i][2]==int1:
                set.add(temp[i][0])
    return set


def visualization(path,str):
    good=0
    bad=0
    neutral=0
    with open(path,'r')as f:
        reader = csv.reader(f)
        temp = list(reader)
        length = len(temp)
        for i in range(0,length,2):
            if temp[i][2]=='1':
                good+=1
            elif temp[i][2]=='-1':
                bad+=1
            elif temp[i][2]=='0':
                neutral +=1
        labels = ['Good', 'Bad', 'neutral']
        # 绘图显示的标签
        values = [good, bad, neutral]
        colors = ['b', 'm', 'y']
        explode = [0, 0.1, 0]
        # 旋转角度
        plt.title(str, fontsize=18)
        # 标题
        plt.pie(values, labels=labels, explode=explode, colors=colors,
                startangle=180,
                shadow=True, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()


def good_bad_ratio(path):
    good = 0
    bad = 0
    with open(path, 'r')as f:
        reader = csv.reader(f)
        temp = list(reader)
        length = len(temp)
        for i in range(0, length, 2):
            if temp[i][2] == '1':
                good += 1
            elif temp[i][2] == '-1':
                bad += 1
    ratio=good/bad
    return ratio


if __name__ == '__main__':
    #数据预处理
    noComments(r"data/2020-01-10~2020-01-22.csv", r'temp/first.csv', 533)
    count(r'temp/first.csv', "temp/resfir.csv")
    delete("temp/resfir.csv",609)
    noComments(r"data/2020-01-23~2020-02-07.csv", r"temp/second.csv", 1561)
    count(r"temp/second.csv", "temp/ressec.csv")
    delete("temp/ressec.csv",887)
    noComments(r"data/2020-02-10~2020-03-05.csv", r"temp/third.csv", 1614)
    count(r"temp/third.csv", "temp/resthird.csv")
    delete("temp/resthird.csv",1117)
    noComments(r"data/2020-03-10-~2020-05-31.csv", r"temp/forth.csv", 4209)
    count(r'temp/forth.csv', "temp/resfor.csv")
    delete("temp/resfor.csv",2340)

    comments(r"data/Comments 2020-01-10~2020-01-22.csv", r"temp/firstcom.csv",380, 10)
    count(r'temp/firstcom.csv', r"temp/comresfir.csv")
    delete(r"temp/comresfir.csv", 1437)
    comments(r"data/Comments 2020-01-23~2020-02-07.csv", r"temp/secondcom.csv", 800, 10)
    count(r'temp/secondcom.csv', r"temp/comressec.csv")
    delete(r"temp/comressec.csv", 2108)
    comments(r"data/Comments 2020-02-10~2020-03-05.csv", r"temp/thirdcom.csv", 1154, 10)
    count(r'temp/thirdcom.csv', r"temp/comresthird.csv")
    delete(r"temp/comresthird.csv", 2807)
    comments(r"data/Comments 2020-03-10~2020-05-31.csv", r"temp/forthcom.csv", 2340, 10)
    count(r'temp/forthcom.csv', r"temp/comresfor.csv")
    delete(r"temp/comresfor.csv", 5084)

    #求关键词总数
    sum1 = sum(r"res/res1.csv")
    sum2 = sum(r"res/res2.csv")
    sum3 = sum(r"res/res3.csv")
    sum4 = sum(r"res/res4.csv")
    comsum1 = sum(r"res/comres1.csv")
    comsum2 = sum(r"res/comres2.csv")
    comsum3 = sum(r"res/comres3.csv")
    comsum4 = sum(r"res/comres4.csv")
    # 获取心态词典
    good_psychology = set()
    bad_psychology = set()
    get_psychology(good_psychology, '1')
    get_psychology(bad_psychology, '-1')
    good1 = list(good_psychology)
    bad1 = list(bad_psychology)
    out(good1, r"res/good_psychology.csv")
    out(bad1, r"res/bad_psychology.csv")
    #获取数据并可视化
    visualization(r"res/res1.csv","Media Mentality from 2020-1-10 to 2020-1-22")
    visualization(r"res/res2.csv", "Media Mentality from 2020-1-23 to 2020-2-07")
    visualization(r"res/res3.csv", "Media Mentality from 2020-2-10 to 2020-3-05")
    visualization(r"res/res4.csv", "Media Mentality from 2020-3-10 to 2020-5-31")
    visualization(r"res/comres1.csv", "Common People Mentality from 2020-1-10 to 2020-1-22")
    visualization(r"res/comres2.csv", "Common People Mentality from 2020-1-23 to 2020-2-07")
    visualization(r"res/comres3.csv", "Common People Mentality from 2020-2-10 to 2020-3-05")
    visualization(r"res/comres4.csv", "Common People Mentality from 2020-3-10 to 2020-5-31")
    # 拟合
        #自变量：人民日报各阶段的积极/消极心态比
    x_group=np.array([good_bad_ratio("res/res1.csv"),good_bad_ratio("res/res2.csv"),good_bad_ratio("res/res3.csv"),good_bad_ratio("res/res4.csv")])
        #因变量：评论各阶段的积极/消极心态比
    y_group = np.array([good_bad_ratio("res/comres1.csv"), good_bad_ratio("res/comres2.csv"), good_bad_ratio("res/comres3.csv"),
                        good_bad_ratio("res/comres4.csv")])
    print(x_group)
    print(y_group)
    def f_1(params,x):
        A,B,C=params
        return A*x*x+ B*x+C
    # 误差函数，即拟合曲线所求的值与实际值的差
    def error(params, x, y):
        return f_1(params, x) - y


    # 对参数求解
    def slovePara():
        p0 = [1, 1, 1]
        Para = leastsq(error, p0, args=(x_group, y_group))
        return Para


    Para = slovePara()
    a, b, c = Para[0]
    print("a=", a, " b=", b, " c=", c)
    print("cost:" + str(Para[1]))
    print("求解的曲线是:")
    print("y=" + str(round(a, 2)) + "x*x+" + str(round(b, 2)) + "x+" + str(c))

    plt.figure(figsize=(8, 6))
    plt.scatter(x_group, y_group, color="green", label="sample data", linewidth=2)

    # 画拟合直线
    x = np.linspace(1, 3, 100)  ##在0-3直接画100个连续点
    y = a * x * x + b * x + c  ##函数式
    plt.plot(x, y, color="red", label="solution line", linewidth=2)
    plt.legend()  # 绘制图例
    plt.show()

    average=(x_group[0]+x_group[1]+x_group[2]+x_group[3])/4
    variance= np.math.sqrt((pow((x_group[0] - average), 2) + pow((x_group[1] - average), 2) + pow((x_group[2] - average), 2) + pow((x_group[3] - average), 2)) / 4)
