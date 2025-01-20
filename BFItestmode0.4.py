import random
import datetime

#問項
ques= [
'充滿活力',
'有非常多熱情',
'喜歡外出、好社交的',
'樂於助人且無私的',
'有寬容本質',
'幾乎對所有人體貼且仁慈的',
'可信賴的工作者',
'會堅持到工作完成',
'做事有效率的',
'擔心很多的',
'情緒不穩定的',
'容易感到緊張的',
'具有生動想像力',
'有創造力的',
'重視藝術及美學經驗']

con = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","0"]


ans = [["充滿活力(e)",],
["有非常多熱情(e)",],
["喜歡外出、好社交的(e)",],
["樂於助人且無私的(a)",],
["有寬容本質(a)",],
["幾乎對所有人體貼且仁慈的(a)",],
["可信賴的工作者(c)",],
["會堅持到工作完成(C)",],
["做事有效率的(C)",],
["擔心很多的(N)",],
["情緒不穩定的(N)",],
["容易感到緊張的(N)",],
["具有生動想像力(O)",],
["有創造力的(O)",],
["重視藝術及美學經驗(O)",]]

#for i in range(1,16):
#    ques.append(input())

#隨機出題
uuu = 1
path = 'result.txt'
path2 = 'latestrd.txt'
with open(path,'a') as f:
    name = input('\n請輸入姓名:')
    print(name,':\n',file=f)

    
while len(con) > 0:
    nn = int(random.randint(0,14))
    if str(f'{nn}') in con:
        print(f'第{uuu}題:',ques[int(f'{nn}')])
        locat = ques[int(f'{nn}')]
        print('輸入分數一到五:')
        print()
        inp =int(input())
        #儲存答案
        ans[int(f'{nn}')].append(inp)
        con.remove(f'{nn}')
        uuu += 1
        print()

        
#計算分數
o = ans[12][1]+ans[13][1]+ans[14][1]
c = ans[6][1]+ans[7][1]+ans[8][1]
e = ans[0][1]+ans[1][1]+ans[2][1]
a = ans[3][1]+ans[4][1]+ans[5][1]
n = ans[9][1]+ans[10][1]+ans[11][1]
print(f"o:{o},c:{c},e:{e},a:{a},n:{n}",
"https://www.airitilibrary.com/Article/Detail/16094905-202012-202102010013-202102010013-271-299")
print()


#紀錄時間
now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))

#寫入紀錄

with open(path,'a') as f:
    print(now.strftime('%Y/%m/%d %H:%M:%S'),f"o:{o},c:{c},e:{e},a:{a},n:{n}\n",file=f)
    print(ans,'\n\n',file=f)
    print(now.strftime('%Y/%m/%d %H:%M:%S'),f"o:{o},c:{c},e:{e},a:{a},n:{n}\n")

 
with open(path2,'w') as f:
    print(now.strftime('%Y/%m/%d %H:%M:%S'),f"o:{o},c:{c},e:{e},a:{a},n:{n}\n",file=f)
    print(ans,'\n\n',file=f)
    

input()


"""
充滿活力
有非常多熱情
喜歡外出、好社交的
樂於助人且無私的
有寬容本質
幾乎對所有人體貼且仁慈的
可信賴的工作者
會堅持到工作完成
做事有效率的
擔心很多的
情緒不穩定的
容易感到緊張的
具有生動想像力
有創造力的
重視藝術及美學經驗
"""







"""
充滿活力(E)
有非常多熱情(E)
喜歡外出、好社交的(E)
樂於助人且無私的(A)
有寬容本質(A)
幾乎對所有人體貼且仁慈的(A)
可信賴的工作者(C)
會堅持到工作完成(C)
做事有效率的(C)
擔心很多的(N)
情緒不穩定的(N)
容易感到緊張的(N)
具有生動想像力(O)
有創造力的(O)
重視藝術及美學經驗(O)
"""
