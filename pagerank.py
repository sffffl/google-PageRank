from numpy import *

a = array([[0, 1, 1, 0],   #根据转移图得到的矩阵，竖着看，第一列表示从A可以转移到B，C，D；第二列表示可以从B转移到A,D...
           [1, 0, 0, 1],
           [1, 0, 0, 1],
           [1, 1, 0, 0]], dtype=float)  # dtype指定为float


def graphMove(a):  # 构造转移矩阵
    b = transpose(a)  # b为a的转置矩阵     #对a矩阵转置之后，再根据每一行求和，得到的是从不同的页面转移出去的次数和，分别是3，2，1，2，分别表示从A,B,C,D页面转移出的次数
    c = zeros((a.shape), dtype=float)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            c[i][j] = a[i][j] / (b[j].sum())  # 完成初始化分配
    # print c,"\n===================================================="
    return c


def firstPr(c):  # pr值的初始化     假设所有页面出现的概率相等
    pr = zeros((c.shape[0], 1), dtype=float)  # 构造一个存放pr值的矩阵
    for i in range(c.shape[0]):
        pr[i] = float(1) / c.shape[0]
    # print pr,"\n==================================================="
    return pr


def pageRank(p, m, v):  # 计算pageRank值
    while ((v == p * dot(m, v) + (1 - p) *v ).all() == False):  # 判断pr矩阵是否收敛,(v == p*dot(m,v) + (1-p)*v).all()判断前后的pr矩阵是否相等，若相等则停止循环
        # print v
        v = p * dot(m, v) + (1 - p) *v       # print (v == p*dot(m,v) + (1-p)*v).all()
    return v


if __name__ == "__main__":
    M = graphMove(a)   #转移概率矩阵
    pr = firstPr(M)  #初始PR值
    p = 0.8  # 引入浏览当前网页的概率为p,假设p=0.8
    print(pageRank(p, M, pr))  # 计算pr值