import sys
n = int(sys.stdin.readline().strip())  # 获得窗口输入的单个输入
# if __name__ == "__main__":              主函数的使用方法
for i in range(2):                     # 获得，几行的输入，并将每行的输入转化为list，例子是两行
    line = sys.stdin.readline().strip('')  #删除字符串中的某一种字符
    line = sys.stdin.readline().strip('[')  # 删除字符串中的某一种字符
    values = list(map(int, line.split()))   # split默认的分隔符只有空格( )、换行(\n)、制表符(\t)或者（.）
    if i == 0:
        M = values
    elif i == 1:
        N = values

