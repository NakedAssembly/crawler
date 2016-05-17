# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import csv
import time

def main(num, url, csv_writer, name):
    for idx in range(1,80):
        url = 'http://watch.peoplepower21.org/?mid=Member&member_seq={}&page={}'.format(row[2], idx)

        try:
            req = requests.get(url)
            soup = BeautifulSoup(req.text,'html.parser')
            frame = soup.find_all('div',{'class':'panel panel-default'})[2]
            table = frame.find('div',{'id':'attend_sangim'}).find('tbody')
            for tr in table.find_all('tr'):
                date = tr.find_all('td')[0].text
                commitee_name = tr.find_all('td')[1].text
                period = tr.find_all('td')[2].text
                result = tr.find_all('td')[3].text.replace(" ","")
                csv_writer.writerow([date, commitee_name.encode('utf-8'), period.encode('utf-8'), result.encode('utf-8')])
                
        except IndexError:
            pass

    print num, name
    time.sleep(2)





if __name__ == '__main__':
    fr = open('member_parameter.csv', 'rb')
    csv_reader = csv.reader(fr)
    fw = open('sangim_attend.csv','wb')
    csv_writer = csv.writer(fw)
    for row in csv_reader:
        main(row[0], row[2], csv_writer, row[1])
    fr.close()
    fw.close()
