"""
[6-2] 串列操作-2
Description

已知 my_lst 為一串列，該串列所包含的物件數量將大於 5 個。

輸出共有三行：

請輸出該串列中，第 1 個物件
取出該串列中第 2 個到第 5 個物件，以串列的型態輸出
請輸出該串列中最後一個物件

Input
輸入為一行包含數個字串以逗號分隔，經轉換後為一串列。


Output
輸出有三行。

第一行為該串列中，第 1 個物件。

第二行為該串列中第 2 個到第 5 個物件，以串列的型態輸出。

第三行為該串列中最後一個物件。


Sample Input 1 
1,2,3,4,5,6,7

Sample Output 1
1
[2, 3, 4, 5]
7

Sample Input 2 
a,b,c,d,e

Sample Output 2
a
['b', 'c', 'd', 'e']
e

Hint
在串列中，計算各物件的位置是從 0 開始，因此 lst[0] 將取到串列 lst 中的第一個物件， lst[1] 將取到串列 lst 中的第二個物件，以此類推。

Source
ccClub Judge
"""
# 此段程式碼不需特別了解, 該功能為將輸入的資料轉換為串列
# 只需知道 my_lst 為一串列, 即可對 my_lst 進行操作完成本題
my_lst = input().split(",")
print(my_lst[0])
print(my_lst[1:5])
print(my_lst[-1])

