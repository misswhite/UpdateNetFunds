#coding=utf-8
import csv
import shutil
import time
from random import random
from tempfile import NamedTemporaryFile
import draw_chart
import draw_bar

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_net(fundcode='000000'):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(argument="--headless")
    driver = webdriver.Chrome(options=chrome_options)
    url = 'http://fund.eastmoney.com/'+fundcode+'.html'
    driver.get(url)
    try:
    #  浏览器的xpath('// *[ @ id = "body"] / div[11] / div / div / div[3] / div[1] / div[1] / dl[2] / dd[1] / span[1]')
        net_fund = driver.find_element_by_xpath('//dd[1]/span[1]').text
   
    except:
       print('fail to locate: '+fundcode)
       net_fund = str(1.00)

    if net_fund=='0.00':
        try:
            net_fund = driver.find_element_by_xpath('//span[@class="ui-font-large"]').text
        except:
            print('Tried another way, still failed to locate: ' + fundcode)
            net_fund = str(1.00)

    driver.close()

    return net_fund


if __name__ == "__main__":
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    filename = 'FUNDS.csv'
    with open(filename, 'r+', newline='') as csvfile:
        spamreader = csv.reader(csvfile, dialect='excel')

# 忽略header
      #  next(spamreader,None)
        writer = csv.writer(tempfile)
        total_sum = 0
        total_input = 0
        for row in spamreader:
            row[5] = get_net(row[0])
            row[3] = int(float(row[4])*float(row[5]))
            row[7] = float(row[3])/float(row[6])
            row[7] = round(row[7],2)
            row[9] = row[3] - int(row[6])
            print(row)

            writer.writerow(row)
            total_sum += row[3]
            total_input += int(row[6])

        with open("myFundTotal.csv", 'a+', newline='') as totalfile:
            wr = csv.writer(totalfile)
            wr.writerow([(time.strftime('%Y-%m-%d',time.localtime())),str(total_sum),str(total_input),str(total_sum/total_input),str(total_sum-total_input)])
            totalfile.close()
        print("total:"+str(total_sum)+" input:"+str(total_input)+" rate:"+str(total_sum/total_input)+" balance:"+str(total_sum -total_input))

    csvfile.close()
    tempfile.close()

    shutil.move(tempfile.name, filename)

    draw_chart.draw_chart("myFundTotal.csv")
    draw_bar.draw_chart("FUNDS.csv")
