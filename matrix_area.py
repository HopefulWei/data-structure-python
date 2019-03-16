import sys
def search_row(M,I,J,line,n_max):
    for j1 in range(J,J+line):
        if M[I][j1] == 0:
            return I
    if (I + 1)<n_max:
        I = I + 1
        return search_row(M,I,J,line,n_max)
    else:
        return I + 1

def search_line(M,I1,J1,row,m_max):
    for i1 in range(I1,I1+row):
        if M[i1][J1] == 0:
            return J1
    if (J1 + 1) < m_max:
        J1 = J1 + 1
        return search_line(M,I1,J1,row,m_max)
    else:
        return  J1 + 1



Matrix = []
n = int(sys.stdin.readline().strip())  # 获得窗口输入的单个输入
# if __name__ == "__main__":              主函数的使用方法
for i in range(n):                     # 获得，几行的输入，并将每行的输入转化为list，例子是两行
    line = sys.stdin.readline().strip('')  #删除字符串中的某一种字符
    values = list(map(int, line.split()))   # split默认的分隔符只有空格( )、换行(\n)、制表符(\t)或者（.）
    Matrix.append(values)
m =len(Matrix[0])
Max = 0
for i in range(n):
    for j in range(m):
        if Matrix[i][j] == 1:
            row = search_row(Matrix,i,j,1,n)
            rowGap = row - i
            Line = search_line(Matrix,i,j,rowGap,m)
            LineGap = Line - j
            area1 = rowGap*LineGap

            Line1 = search_line(Matrix,i,j,1,m)
            LineGap1 = Line1 - j
            row1 = search_row(Matrix,i,j,LineGap1,n)
            rowGap1 = row1 - i
            area2 = rowGap1*LineGap1
            A=[area1,area2,Max]
            Max = max(A)
print (Max)