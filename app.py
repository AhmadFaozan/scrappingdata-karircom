import requests
import bs4 as bs
import csv
from datetime import datetime

while True:
    job = input('Isi Job :')
    if job != '':
        print('searcing job :',job)
        break

url = 'https://www.karir.com/search?q={}&page='.format(job)
now = datetime.now()
dt_string = now.strftime("%H-%M-%S")
datas = []
for page in range(1, 35):
    print('retrive data ', job)
    source = requests.get(url+str(page))
    soup = bs.BeautifulSoup(source.text,'html.parser')
    items = soup.findAll('div','row opportunity-box')
    for it in items:
        name = it.find('h4','tdd-function-name --semi-bold --inherit').text
        pt = it.find('div', 'tdd-company-name h8 --semi-bold').text
        lok = it.find('span', 'tdd-location').text
        exp = it.find('span', 'tdd-experience').text
        gaji = it.find('span', 'tdd-salary').text
        datas.append([name,pt,lok,exp,gaji])

body = ['Nama','Perusahaan', 'Lokasi', 'Pengalaman','Upah']

writer = csv.writer(open('results/{}-{}.csv'.format(job,dt_string),'w',newline=''))
writer.writerow(body)

for d in datas:writer.writerow(d)