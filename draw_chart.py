import csv
from datetime import datetime
from matplotlib import pyplot as plt

def draw_chart(filename):
    # 从文件里获取记录，日期，现价和投入
    #filename = 'myFundTotal.csv' #统计信息存到这个文件啦
    with open(filename,'r') as f:
        reader = csv.reader(f)
        header_row = next(reader)  # 获取每一行文件的数据

        dates, returns, my_input = [], [], []  # 创建空列表
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[2])
            except ValueError:
                print(current_date, 'missing data')  # 打印报错信息
            else:
                dates.append(current_date)
                returns.append(high)
                my_input.append(low)

    # 填充数据
    fig = plt.figure(dpi=128, figsize=(10, 6))
    # 加图例，设置label参数
    line1 = plt.plot(dates, returns, c='red',label ="Current")
    line2 = plt.plot(dates, my_input, c='blue',label ="Input")
    plt.fill_between(dates, returns, my_input, facecolor='blue', alpha=0.1)
    # 显示图例，位置及字体大小
    plt.legend(loc="upper right",fontsize=10)

    # 绘制
    title = "My Funds ROI"
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Balance", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    #plt.ylim(10, 120)
    plt.flag()
    # 展示
    plt.show()
