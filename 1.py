import networkx
import matplotlib.pyplot as plt
G = networkx.read_adjlist("/Volumes/Transcend/KONE计价工具/py/relation9.adjlist", "rb", encoding="UTF-8-sig")
create_using = networkx.Graph(G)
pos = networkx.spring_layout(G)
networkx.draw(G,
              pos,
              node_color="#304554",
              alpha=0.8,
              node_size=1,
              linewidths=0,
              width=1,
              style="solid",
              # arrows=True,
              edge_color="#8bb1cc",
              font_size=1,
              font_color="#304554",
              with_labels=True)
plt.savefig("dot.pdf")
plt.show()
plt.clf() # 清图。
plt.cla() # 清坐标轴。
print("边数：", networkx.number_of_edges(G))
print("节点数：", networkx.number_of_nodes(G))
print("平均聚集系数：", networkx.average_clustering(G))
list_1 = networkx.degree(G)
base = 0
for a in list_1:
    base += a[1]
print("度平均值：", base/len(list_1))


list_2 = dict(networkx.shortest_path_length(G))
base_1 = 0
for bb in list_2:
    for cc in list_2[bb]:
        base_1 += list_2[bb][cc]
    base_1 += 4*(len(list_2)-len(list_2[bb]))
# 最大距离为4
result = base_1/(len(list_2)*len(list_2))
print("平均最短路径", result)

# print("最长的最短路径：", networkx.diameter(G))
# print("所有节点的度分布序列:", networkx.degree_histogram(G))#返回图中所有节点的度分布序列（从1至最大度的出现频次）
degree = networkx.degree_histogram(G)#返回图中所有节点的度分布序列
x = range(len(degree))#生成X轴序列，从1到最大度
y = [z/float(sum(degree))for z in degree]#将频次转化为频率，利用列表内涵
plt.scatter(x, y, color="#304554", linewidth=1)#在双对坐标轴上绘制度分布曲线
# networkx.draw(G,
#               pos,
#               node_color="#304554",
#               alpha=0.8,
#               node_size=1,
#               linewidths=0,
#               width=1,
#               style="solid",
#               # arrows=True,
#               edge_color="#ffffff",
#               font_size=1,
#               font_color="#304554",
#               with_labels=True)
plt.savefig("degree.png")
plt.show()


#介数中心性
B = networkx.betweenness_centrality(G)  #计算每个节点的介数中心性，存储在字典中
m = max(list(B.values()))  #将字典转换成列表进行排序，取最大值
print("最大介数中心性", m)
N = networkx.number_of_nodes(G)
s = 0
k = 0
for i in B: #节点的遍历介数中心性
    k += 1
    s += m-B[i]
CPB = s/(N-1)
print('网络的中心点优势是:', CPB)