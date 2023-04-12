"""
[5-3] 阿能寫作文
Description

此題為填空題。

阿能文筆很不好，每次寫作文都都要善用各種標點符號幫忙湊篇幅。像底下那個例子：

s1 = "I Have a Dream"

s2 = "是1960年代的美國黑人民權運動領袖馬丁·路德·金恩博士一場極為著名演講的稱呼"

阿能希望寫的時候，可以用雙引號包住字串 s1 ，之後再與字串 s2 串接在一起。這樣就可以多 2 格的篇幅了！


Input
此題無輸入。


Output
輸出為 1 行，請輸出第一個字串加上雙引號後，與第二個字串串接的結果


Sample Input 1 

 
Sample Output 1
"I Have a Dream"是1960年代的美國黑人民權運動領袖馬丁·路德·金恩博士一場極為著名演講的主題

Hint
請於作答區底線處，填入正確內容，完成題目要求。
作答時請將底線移除，替換成正確內容。
雙引號" 為python中用來標示字串的特殊字，因此若輸出的內容中，希望包含雙引號，則需使用跳脫字元
字串間可以使用 + 進行連接

Source
ccClub Judge
"""

s1 = "I Have a Dream"
s2 = "是1960年代的美國黑人民權運動領袖馬丁·路德·金恩博士一場極為著名演講的主題"

# 字串串接
# s = "__" + s1 + "__" + s2
s = "\"" + s1 + "\"" + s2

# 輸出
print(s)
# 輸出結果應為: "I Have a Dream"是1960年代的美國黑人民權運動領袖馬丁·路德·金恩博士一場極為著名演講的主題