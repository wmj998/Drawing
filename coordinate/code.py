import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决plt中文显示的问题
plt.rcParams['axes.unicode_minus'] = False    # 解决plt负号显示的问题

# 坐标
x = ['0~100','100~200','200~300','300~400','400~500','500~600','600~700','700~800','800~900','900~1000','1000以上']
y = [15, 18, 16, 10, 7, 16, 14, 5, 2, 14, 83]

# plt.figure(figsize = (18,10)) #改变画布大小（长，宽）

# 设置坐标轴字体大小
# plt.xticks(fontsize=25)
# plt.yticks(fontsize=25)

# plt.subplot(2,2,1)   # 不同图在同一画布中的位置
plt.figure()  # 图在不同窗口显示
plt.title("标题")
plt.xlabel("价格")
plt.ylabel("数量")
# plt.scatter(x,y)  # 散点图
plt.plot(x,y,label='价格',color='b',linewidth=1,linestyle='-.')  # 折线图
plt.legend()  # 线条标签
# plt.grid()  # 添加网格

# plt.subplot(2,2,2)
plt.figure()
plt.title("标题")     # plt.title("标题",fontsize=50)
plt.xlabel("价格")    # plt.xlabel("价格",fontsize=25)
plt.ylabel("数量")    # plt.ylabel("数量",fontsize=25)
plt.bar(x,y,label='价格')  # 柱状图
plt.legend()  # 线条标签
# plt.grid()  # 添加网格

# plt.subplot(2,2,3)
plt.figure()
plt.title("各价格段所占比例",fontsize=20)  # figsize大小，fontweight粗细，fontstyle字体类型
explode = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]   # 各模块顶点距圆心的距离
plt.pie(y,explode,x,autopct='%.2f%%')  # 饼状图
plt.show()
