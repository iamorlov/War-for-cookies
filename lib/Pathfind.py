# -*- coding: cp1251 -*-
import lib, numpy#волновой алгоритм
def pathfind(matrix, x1,y1,x2,y2,steps):#matrix-карта проходимости. области со своей и вражьей армией также пометить непроходимыми!
    #непроходимые ячейки - 0, проходимые - 1
    n=len(matrix)
    m=len(matrix[0])#длинна и ширина массива
    for i in range (n):
        for j in range (m):
            wavematrix[i][j] = 0
    wavematrix[x1][y1] = -1
    xb[1]=x1
    yb[1]=y1
    k=0
    lenmas=1
    flag=false
    for z in range (30): #максимальная длинна волны
        waveitems=0 #кол-во клеток, задетых волной.
        nextx = []
        nexty = []
        for j in range(lenmas):
            for i in range (xb[j]-1,xb[j]+1): #1 этап, пускаем волну
                if i<0 or i>n:
                    continue #ну или как там ход цикла пропустить
                temp=(z+1)*matrix[i][yb[j]]
                if wavematrix[i][yb[j]]>temp or wavematrix[i][yb[j]]==1:
                    wavematrix[i][yb[j]]=temp
                    waveitems++
                    nextx.append(i)
                    nexty.append(yb[j])
            for i in range (yb[j]-1,yb[j]+1): #1 этап, пускаем волну
                if i<0 or i>m:
                    continue #ну или как там ход цикла пропустить
                temp=(z+1)*matrix[x1][y1]
                if wavematrix[x1][i]==1 or wavematrix[x1][i]>temp:
                    wavematrix[x1][i]=temp
                    waveitems++
                    nextx.append(x1)
                    nexty.append(y1)
            for i in range (waveitems):
                if nextx[i] == x2 and nexty[i] == x2:#если дошли до нужной точки
                    flag=true#флаг на выход
                    u=z#записали длину волны
        if flag:
            break
        lenmas=waveitems           
        xb=nextx
        yb=nexty
    if !flag:
        #сообщение об ошибке, жень сделай красиво через пугейм
    trase = [][]
    retmove = [][]
    trase[0][0]=x2
    trase[0][1]=y2
    for i in range(1,u):
        if wavematrix[(trase[i-1][0])-1][trase[i-1][1]] == wavematrix[trase[i-1][0]][trase[i-1][1]]-1:
            trase[i][0] = trase[i-1][0]-1
            trase[i][1] = trase[i=1][0]
        elif wavematrix[(trase[i-1][0])+1][trase[i-1][1]] == wavematrix[trase[i-1][0]][trase[i-1][1]]-1:
            trase[i][0] = trase[i-1][0]+1
            trase[i][1] = trase[i=1][0]
        elif wavematrix[(trase[i-1][0])][trase[i-1][1]-1] == wavematrix[trase[i-1][0]][trase[i-1][1]]-1:
            trase[i][0] = trase[i-1][0]
            trase[i][1] = trase[i=1][0]-1
        elif wavematrix[(trase[i-1][0])][trase[i-1][1]+1] == wavematrix[trase[i-1][0]][trase[i-1][1]]-1:
            trase[i][0] = trase[i-1][0]
            trase[i][1] = trase[i=1][0]+1
        #все, обратная дорожка получена.
    for i in range (steps):
        retmove[i][0] = trase[u-i][0]#переворачиваем трассу обратно, и отрезаем по кол-ву шагов
        retmove[i][1] = trase[u-i][1]
