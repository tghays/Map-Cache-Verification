# coding: utf-8
import requests, sys
from PIL import Image
from PIL import ImageOps
from IPython.display import clear_output

start_url = 'http://csc-thays10d/server_wa/rest/services/Anson_5ft_2ft/MapServer/tile/13/3238/2268'
end_url = 'http://csc-thays10d/server_wa/rest/services/Anson_5ft_2ft/MapServer/tile/13/3250/2278'
tile_url = 'http://csc-thays10d/server_wa/rest/services/Anson_5ft_2ft/MapServer/tile/13/'

out_dir = r'C:\Users\Tyler\Desktop\dev\\'
file_name = 'L13.png'

xmin = int(start_url.split('/')[-1])
ymin = int(start_url.split('/')[-2])

xmax = int(end_url.split('/')[-1])
ymax = int(end_url.split('/')[-2])

x_len = xmax - xmin
y_len = ymax - ymin
x_len, y_len

# create main image frame
width = x_len * 100
height = y_len * 100
retimg = Image.new('RGB', (width, height))
width, height

n = 0

imgs = {}
x_loc = 0
y_loc = 0
n_x = 0
n_y = 0

for x in range(xmin, xmax):
    for y in range(ymin, ymax):
        url = tile_url + str(y) +'/' + str(x)

        resp = requests.get(url, stream=True)
        resp.raw.decode_content = True

        img = Image.open(resp.raw)
        img.thumbnail((100,100))

        #bord_img = ImageOps.expand(img,border=5,fill=128)
        imgs[x,y] = img
        retimg.paste(img, (x_loc, y_loc))

        n_y += 1
        print('\r', 'image {} complete in column {}'.format(n_x, n_y), end='')
        #clear_output(wait=True)
        y_loc += 100

        #break
    print('\n', 'column {} complete, url = {}'.format(n_x, url))
    n_x += 1
    n_y = 0
    x_loc += 100
    y_loc = 0
    n += 1

# save image
retimg.save(out_dir + file_name)

