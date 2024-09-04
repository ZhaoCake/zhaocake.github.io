from tqdm import tqdm

url = 'https://api.iw233.cn/api.php?sort=pc'
# 这个链接跳转后会到一个图片上，然后就下载这张图片

import requests
import os

def get_img(url):
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.content

def save_img(path, img):

    with open(path, 'wb') as f:
        f.write(img)
        f.close()

def main(i):
    path = f"./{i}.jpg"
    img = get_img(url)
    save_img(path, img)

if __name__ == '__main__':
    # for i in tqdm(range()):
    main(7)