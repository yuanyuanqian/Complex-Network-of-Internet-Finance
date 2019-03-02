import networkx
import matplotlib.pyplot as plt
#G = networkx.read_adjlist("C:\\Users\\86138\\Desktop\\factor1.adjlist", "rb", encoding="utf-8-sig")
DG = networkx.DiGraph()
DG.add_edges_from([("H1", "H2"), ("H1","H3"), ("H1","H4"), ("H1","H7"), ("H1","H8"), ("H1","H10"), ("H1","F8"), ("H1","F9"),
                   ("H2","H5"),("H2","H7"),("H2","H8"),("H2","H9"),("H2","F3"),
                   ("H3","H2"),("H3","H5"),("H3","H7"),("H3","H8"),("H3","H9"),("H3","F3"),
                   ("H4","H1"),("H4","H5"),("H4","H7"),("H4","H8"),("H4","H9"),("H4","F3"),("H4","F8"),("H4","F9"),
                   ("H5","H7"),("H5","H8"),("H5","H9"),("H5","F3"),("H5","F8"),("H5","F9"),
                   ("H6", "H1"),("H6","H4"),("H6","H4"),("H6","H7"),("H6","H8"),("H6","H10"),
                   ("H7", "H8"),("H7", "H9"),("H7", "F3"),("H7", "F9"),
                   ("H8", "H9"),("H8", "F3"),("H8", "F9"),
                   ("H9", "H7"),("H9", "F3"),("H9", "F8"),("H9", "F9"),
                   ("H10", "F1"),("H10", "F3"),("H10", "F5"),
                   ("H11", "F3"),("H11", "F7"),
                   ("H12", "H13"),("H12", "F3"),("H12", "F9"),
                   ("H13", "F3"),("H13", "F7"),("H13", "E7"),
                   ("H14", "H15"),("H14", "F3"),("H14", "F6"),("H14", "F7"),
                   ("H15", "F3"),("H15", "F6"),("H15", "F7"),
                   ("H16", "F3"),("H16", "E7"),
                   ("H17", "F3"),("H17", "E10"),
                   ("H18", "F3"),("H18", "F7"),
                   ("F1", "F3"),("F1", "F4"),
                   ("F2", "F3"),("F2", "F5"),
                   ("F3", "F4"),
                   ("F6", "F3"),
                   ("F7", "F3"),
                   ("F10", "F11"), ("F10", "F12"), ("F10", "F13"), ("F10", "F14"),
                   ("F11", "E7"),
                   ("F13", "E8"),
                   ("E1", "F3"),("E1", "F4"),
                   ("E2", "F3"), ("E2", "F4"),
                   ("E3", "F3"), ("E3", "F4"),
                   ("E4", "F3"), ("E4", "F4"),
                   ("E5", "F3"), ("E5", "F4"),
                   ("E6", "F3"), ("E6", "F4"),
                   ("E7", "F3"),
                   ("E8", "F3"),
                   ("E9", "F14"),
                   ("E10", "F3"), ("E10", "E8"),
                   ("E11", "F3"),("E11", "F6"),
                   ("E12", "F3"),("E12", "F4"),
                   ("E13", "F3"),
                   ("M1", "H1"),("M1", "M4"),("M1", "M5"),("M1", "M7"),("M1", "M8"),("M1", "M10"),("M1", "M11"),
                   ("M2", "H8"),("M2", "F3"),
                   ("M3", "F8"),("M3", "F9"),("M3", "F10"),("M3", "M4"),
                   ("M5", "H1"),("M5", "H2"),("M5", "H3"),("M5", "H5"),("M5", "H10"),
                   ("M6", "H3"), ("M6", "H7"), ("M6", "H8"),
                   ("M7", "H1"), ("M7", "H7"), ("M7", "H8"),
                   ("M8", "M4"),("M8", "M10"),("M8", "F1"),("M8", "F3"),("M8", "F5"),("M8", "F8"),("M8", "F9"),("M8", "F10"),
                   ("M9", "F1"), ("M9", "F2"), ("M9", "F3"),
                   ("M10", "F2"),("M10", "F5"),
                   ("M11", "M2"),("M11", "M4"),("M11", "M5"),("M11", "M6"),("M11", "M7"),("M11", "M8"),("M11", "M10"),("M11", "M12"),
                   ("M12", "H3"),("M12", "H5"),("M12", "H2")])
pos = networkx.circular_layout(DG)

print("边数：", networkx.number_of_edges(DG))
print("节点数：", networkx.number_of_nodes(DG))
print("平均聚集系数：", networkx.average_clustering(DG))

list_2 = dict(networkx.shortest_path_length(DG))
base_1 = 0
for bb in list_2:
    for cc in list_2[bb]:
        base_1 += list_2[bb][cc]
# print("==========================")
result = 2*base_1/(len(list_2)*(len(list_2)-1))
print("平均最短路径", result)

print("平均最短路径：", networkx.average_shortest_path_length(DG))
networkx.draw(DG,
              pos,
              node_color="#304554",
              alpha=0.9,
              node_size=300,
              linewidths=0,
              width=1,
              style="solid",
              # arrows=True,
              edge_color="#8bb1cc",
              font_size=6,
              font_weight=800,
              font_color="#ffffff",
              with_labels=True)
plt.show()

list_1 = networkx.degree(DG)
base1 = 0
for a in list_1:
    base1 += a[1]
print("总度平均值：", base1/len(list_1))
print("总度：", DG.degree)

list_2 = DG.out_degree
base2 = 0
for b in list_2:
    base2 += b[1]
print("出度平均值：", base2/len(list_2))
print('出度：', DG.out_degree)

list_3 = DG.in_degree
base3 = 0
for c in list_3:
    base3 += c[1]
print("入度平均值：", base3/len(list_3))
print('入度：', DG.in_degree)

degree = networkx.degree_histogram(DG)#返回图中所有节点的度分布序列
# out_degree = networkx.degree_histogram(DG.out_degree)

# out
print("===========")
arr = []
y_arr = []
for zz in DG.out_degree:
    arr.append(zz[1])
for zx in range(max(arr)+1):
    x_arr = range(0, zx+1)
    y_arr.append(arr.count(zx)/len(arr))
print("===========")
# in
print("===========")
arr2 = []
y_arr2 = []
for zc in DG.in_degree:
    arr2.append(zc[1])
for zv in range(max(arr2)+1):
    x_arr2 = range(0, zv+1)
    y_arr2.append(arr2.count(zv)/len(arr2))
print("===========")


x = range(len(degree))#生成X轴序列，从1到最大度
y = [z/float(sum(degree))for z in degree]#将频次转化为频率，利用列表内涵

print("x", x)
print("x_arr", x_arr)
print("y", y)
print("y_arr", y_arr)
# y_out = [k/float(sum(out_degree))for k in out_degree]
plt.scatter(x_arr, y_arr, color="#8BC34A", linewidth=2, alpha=0.5)#在双对坐标轴上绘制度分布曲线
plt.scatter(x_arr2, y_arr2, color="#FFC107", linewidth=2, alpha=0.5)#在双对坐标轴上绘制度分布曲线
plt.scatter(x, y, color="#304554", linewidth=2, alpha=0.5)#在双对坐标轴上绘制度分布曲线
plt.show()#显示图表

# print("H1-M2",networkx.shortest_path(DG, source="H1", target="M2"))

