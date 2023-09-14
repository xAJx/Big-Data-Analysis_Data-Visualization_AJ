import pandas as pd
import re
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import fontManager
print()

# 加入中文字型設定：翰字鑄造-台北黑體
fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
matplotlib.rc('font', family='Taipei Sans TC Beta')

# 1111 圓餅圖
df = pd.read_excel('1111data.xlsx')
city = ['台北', '新北', '桃園', '台中', '台南', '高雄']  #六都
citycount = []  #存六都工作職缺數量的串列
for i in range(len(city)):
    df1 = df[df['工作地點'].str.contains(city[i])]  #取出包含指定地點的資料
    indexlist = df1.index  #取得資料索引
    total = 0  #職缺總額
    for j in range(len(df1)):
        personnum = re.findall(r"\d+\.?\d*",df1['應徵人數'][indexlist[j]])  #取出資料中的數值
        if len(personnum) == 1:  #若是1個數值即為人數
            person = int(personnum[0])
        else:  #若是2個數值則取平均數
            person =int((int(personnum[0])+int(personnum[1]))/2)
        total += person
    citycount.append(total)

ser = pd.Series(citycount, index=city)  #串列轉Series
print(ser)
plt.figure(num='1111')  # 建立 1111 圖表視窗
plt.axis('off')
ser.plot(kind='pie', title='1111_六都(電腦)職缺數量', figsize=(6, 6))  #繪製圓餅圖
print()
#plt.figure(6)

# 104 圓餅圖
df3 = pd.read_excel('104_ThreadPoolExecutor-submit_51~75_page_500-data_職缺清單2023-08-26.xlsx')
city2 = ['台北', '新北', '桃園', '台中', '台南', '高雄']  #六都
citycount2 = []  #存六都工作職缺數量的串列
for i in range(len(city2)):
    df2 = df3[df3['工作地點'].str.contains(city2[i])]  #取出包含指定地點的資料
    indexlist2 = df2.index  #取得資料索引
    total2 = 0  #職缺總額
    for j in range(len(df2)):
        personnum2 = re.findall(r"\d+\.?\d*",df2['應徵人數'][indexlist2[j]])  #取出資料中的數值
        if len(personnum2) == 1:  #若是1個數值即為人數
            person2 = int(personnum2[0])
        else:  #若是2個數值則取平均數
            person2 =int((int(personnum2[0])+int(personnum2[1]))/2)
        total2 += person2
    citycount2.append(total2)

ser2 = pd.Series(citycount2, index=city2)  #串列轉Series
print(ser2)
plt.figure(num = '104') # 建立 104 圖表視窗
plt.axis('off')
ser2.plot(kind='pie', title='104_六都(Python)職缺數量', figsize=(6, 6))  #繪製圓餅圖

plt.show()  # 顯示 已繪製的 (多張)圖表
print()


