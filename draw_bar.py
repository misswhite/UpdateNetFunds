import matplotlib.pyplot as plt
import numpy as np
import csv


def draw_bar(filename="FUNDS.csv"):
    # 从文件里获取记录，日期，现价和投入
    # filename = 'myFundTotal.csv' #统计信息存到这个文件啦
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header_row = next(reader)  # 获取每一行文件的数据

        funds, returns, my_input = [], [], []  # 创建空列表
        for row in reader:
            try:
                fund = row[1]
                high = int(row[3])
                low = int(row[6])
            except ValueError:
                print('missing data')  # 打印报错信息
            else:
                funds.append(fund)
                returns.append(high)
                my_input.append(low)

    plt.rcdefaults()
    fig, ax = plt.subplots()

    ax.barh(funds, returns, height=0.3, color='red',align='edge')
    ax.barh(funds, my_input,height=0.3, color='blue', align='center')

#    ax.set_yticks(np.arange(100000))
    ax.set_yticklabels(funds)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('balance')
    ax.set_title('How fast do you want to go today?')

    plt.show()

if __name__ == '__main__':
    draw_bar("FUNDS.csv")
