"""
[11-1] 強強買東西
Description

強強很窮，可是他有很多東西想要買，所以他決定從便宜的先買，每次只買 3 項東西。如果想買的東西不到 3 項，就排序之後全都買。如果有相同價格，就依照輸入順序排序。


Input
輸入為 n + 1 行，前 n 行為想買的東西和其價格，東西和價格之間以逗號分隔。最後 1 行'end'，表示輸入結束。


Output
輸出為 3 行，第 1 行為最便宜的東西和其價格，第 2 行為第二便宜的東西和其價格，以此類推。東西和價格之間以空白分隔。


Sample Input 1 
戰術筆,85
傘繩31公尺,99
防刀衣,4500
軍用指北針,350
多功能鉗,900
尖嘴鉗,80
打火棒,38
迷你太陽能手電筒,200
求生毯,10
end

Sample Output 1
求生毯 10
打火棒 38
尖嘴鉗 80

Sample Input 2 
Python 自動化的樂趣：搞定重複瑣碎&單調無聊的工作(第二版),537
Effective Python中文版：寫出良好Python程式的90個具體做法(第二版),458
end

Sample Output 2
Effective Python中文版：寫出良好Python程式的90個具體做法(第二版) 458
Python 自動化的樂趣：搞定重複瑣碎&單調無聊的工作(第二版) 537

Hint
物品名稱保證不重複
本題可以用串列或字典來存資訊

Source
ccClub Judge
"""
dictItem = {}
ans = []
while True:
    s = input()
    if s == 'end':
        break
    name, price = s.split(',')
    price = int(price)
    dictItem[name] = price

sortedItem = {k: v for k, v in sorted(dictItem.items(), key=lambda item: item[1])}
if len(sortedItem) < 4:
  for i in range(len(sortedItem)):
    print(list(sortedItem)[i],list(sortedItem.values())[i])
else:
  for i in range(3):
    print(list(sortedItem)[i],list(sortedItem.values())[i])