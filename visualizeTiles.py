
# coding: utf-8
import requests, time
from selenium import webdriver

start_url = 'http://csc-thays10d/server_wa/rest/services/Anson_5ft_2ft/MapServer/tile/13/3238/2268'
end_url = 'http://csc-thays10d/server_wa/rest/services/Anson_5ft_2ft/MapServer/tile/13/3250/2278'
tile_url = 'http://csc-thays10d/server_wa/rest/services/Anson_5ft_2ft/MapServer/tile/13/'

xmin = int(start_url.split('/')[-1])
ymin = int(start_url.split('/')[-2])

xmax = int(end_url.split('/')[-1])
ymax = int(end_url.split('/')[-2])

x_len = xmax - xmin
y_len = ymax - ymin
print(x_len, y_len)
total = x_len * y_len
print(total)

driver = webdriver.Chrome()

n = 0
for x in range(xmin, xmax):
    for y in range(ymin, ymax):
        url = tile_url + str(y) +'/' + str(x)
        driver.get(url)
        time.sleep(.3)
        n += 1
        print('{}% done'.format(str(n/total*100)))
