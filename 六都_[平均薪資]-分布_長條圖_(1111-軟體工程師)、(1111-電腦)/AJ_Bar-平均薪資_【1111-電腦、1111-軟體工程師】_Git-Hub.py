# 1111 平均薪資-長條圖
import pandas as pd
import re
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import fontManager
print()

def transfer(strSalary):  #轉換薪資為月薪，單位為「元」
    sal = float(strSalary)
    if sal < 20:  #薪資單位為「萬」
        sal = sal * 10000
    elif sal <300:  #日薪
        sal = sal * 8 * 22
    return sal

# 加入中文字型設定：翰字鑄造-台北黑體
fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
matplotlib.rc('font', family='Taipei Sans TC Beta')

#  1111 電腦_長條圖
df5 = pd.read_excel('1111_電腦_data.xlsx')
city = ['台北', '新北', '桃園', '台中', '台南', '高雄']  #六都
salarylist = []
for i in range(len(city)):
    df = df5[(df5['工作地點'].str.contains(city[i]))]
    indexlist = df.index  #取得資料索引
    total = 0  #薪資總額
    for j in range(len(df)):
        salarytem = df['薪資'][indexlist[j]].replace(',', '')  #以資料索引取得資料
        salanum = re.findall(r"\d+\.?\d*",salarytem)  #取出資料中的數值
        if len(salanum) == 1:  #若是1個數值即為薪資
            salary = transfer(salanum[0])
        else:  #若是2個數值則取平均數
            salary = (transfer(salanum[0])+transfer(salanum[1]))/2
        total += salary
    salarycity = int(total/len(df))  #平均薪資
    salarylist.append(salarycity)

ser = pd.Series(salarylist, index=city)  #串列轉Series
print(ser)
plt.figure(num='1111_電腦')  # 建立 1111 圖表視窗
plt.ylabel('單位：元')
ser.plot(kind='bar', title='六都_電腦_職缺薪資', figsize=(6, 6))  #繪製長條圖
print()

#  1111 軟體工程師_長條圖
df3 = pd.read_excel('1111_軟體工程師_data.xlsx')

city2 = ['台北', '新北', '桃園', '台中', '台南', '高雄']  #六都
salarylist2 = []
for i in range(len(city2)):
    df2 = df3[(df3['工作地點'].str.contains(city2[i]))]
    indexlist2 = df2.index  #取得資料索引
    total2 = 0  #薪資總額
    for j in range(len(df2)):
        salarytem2 = df2['薪資'][indexlist2[j]].replace(',', '')  #以資料索引取得資料
        salanum2 = re.findall(r"\d+\.?\d*",salarytem2)  #取出資料中的數值
        if len(salanum2) == 1:  #若是1個數值即為薪資
            salary2 = transfer(salanum2[0])
        else:  #若是2個數值則取平均數
            salary2 = (transfer(salanum2[0])+transfer(salanum2[1]))/2
        total2 += salary2
    salarycity2 = int(total2/len(df2))  #平均薪資
    salarylist2.append(salarycity2)

ser2 = pd.Series(salarylist2, index=city2)  #串列轉Series
print(ser2)
plt.figure(num='1111_軟體工程師')  # 建立 1111 圖表視窗
plt.ylabel('單位：元')
ser2.plot(kind='bar', title='六都_軟體工程師_職缺薪資', figsize=(7, 6))  #繪製長條圖
print()

plt.show()
print()
