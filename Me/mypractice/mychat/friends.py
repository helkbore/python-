import itchat
from pandas import DataFrame

# itchat.login()
itchat.auto_login(hotReload=True)

friends = itchat.get_friends(update=True)[0:]
# print(friends)


# 初始化计数器
male = female = other = 0
# for i in friends:
#     print(i)

for i in friends[1:]:
    sex = i['Sex']
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

# 计算朋友总数
total = len(friends[1:])

# 打印出自己的好友性别比例
print("%s 一共有 %d 名好友" % (friends[0]['NickName'],total))
print("男性好友: %.2f%%" % (float(male)/total * 100) + "\n" +
      "女性好友: %.2f%%" % (float(female) / total * 100) + "\n" +
      "不明性别好友: %.2f%%" % (float(other) / total * 100) + "\n"
      )

# 定义一个函数，用来爬取各个变量
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable


# 省份分析
df_friends = DataFrame(friends)
Province = df_friends.Province
Province_count = Province.value_counts()
Province_count = Province_count[Province_count.index!=''] #有一些好友地理信息为空，过滤掉这一部分人。

# 城市
City = df_friends.City #[(df_friends.Province=='北京') | (df_friends.Province=='四川')]
City_count = City.value_counts()
City_count = City_count[City_count.index!='']


msg_body = '你的朋友主要来自省份：%s(%d)、%s(%d)和%s(%d)。\n\n' %(Province_count.index[0],Province_count[0],Province_count.index[1],Province_count[1],Province_count.index[2],Province_count[2]) + \
           '主要来自这些城市：%s(%d)、%s(%d)、%s(%d)、%s(%d)、%s(%d)和%s(%d)。'%(City_count.index[0],City_count[0],City_count.index[1],City_count[1],City_count.index[2],City_count[2],City_count.index[3],City_count[3],City_count.index[4],City_count[4],City_count.index[5],City_count[5])


print(msg_body)
# itchat.send_msg(msg_body, toUserName='filehelper')




#调用函数得到各变量，并把数据存到csv文件中，保存到桌面
NickName = get_var('NickName')
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')




data = {'NickName': NickName, 'Sex': Sex, 'Province': Province,
        'City': City, 'Signature': Signature}
frame = DataFrame(data)
frame.to_csv('data.csv', index=True)


import re
siglist = []
for i in friends:
    signature = i["Signature"].strip().replace("span","").replace("class","").replace("emoji","")
    rep = re.compile("1f\d+\w*|[<>/=]")
    signature = rep.sub("", signature)
    siglist.append(signature)
text = "".join(siglist)

import jieba
wordlist = jieba.cut(text, cut_all=True)
word_space_split = " ".join(wordlist)



import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image
coloring = np.array(Image.open("/Users/apple/Desktop/wechat.jpg"))
my_wordcloud = WordCloud(background_color="white", max_words=2000,
                         mask=coloring, max_font_size=60, random_state=42, scale=2,
                         font_path="/Library/Fonts/Microsoft/SimHei.ttf").generate(word_space_split)

image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()