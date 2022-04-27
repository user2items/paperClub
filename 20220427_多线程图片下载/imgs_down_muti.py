from PIL import Image
from io import BytesIO
import random ,time
import os,base64,cv2
import requests as req
import pandas as pd
from tqdm import tqdm
from threading import Thread
import glob

def img_check(img_dir, file_type = '.jpg'):
    imgs = glob.glob(img_dir + "/*" + file_type)
    for imgfile in tqdm(imgs):
        try:
            src = cv2.imread(imgfile)
            gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            
        
        except Exception as ee:
            print(f"失败：{imgfile}, {ee}")
            os.remove(imgfile)



def img_download(url_data):
    img_dir = '/data/1_qunosen/2022/paddlerec/pinsage/dhome_style/images'
    (img_url, media_id) = url_data
    sleep_time = random.sample(list(range(1, 15)), 1)[0] /10.0
    save_file = os.path.join(img_dir, f"{media_id}.jpg")
    
    if not os.path.exists(save_file):
        try:
            time.sleep(sleep_time)
            response = req.get(img_url)
            ls_f = base64.b64encode(BytesIO(response.content).read())
            imgdata = base64.b64decode(ls_f)
            # print(save_file)
            with open(save_file,'wb') as f:
                f.write(imgdata)
            
        except Exception as ee:
            print(f"{media_id}, {ee}")
    
    else:
        pass



def multi_downs(urls:list, batch_size:int = 12):
    """ 分批下载图片：
        urls： 图片列表，batch_size 批次大小
    """
    for batch_index in tqdm(range(batch_size, len(urls), batch_size + 1)):
        start = batch_index - batch_size
        url_infos = urls[start: batch_index]
        
        works = []
        for url_info in url_infos:
            thread = Thread(target=img_download, args=[url_info ])
            thread.start()
            works.append(thread)

        for t in works:
            t.join()
            print(f"{t.name} 运行完成 ")

            # time.sleep(1)


projects =  pd.read_csv("/data/1_qunosen/2022/paddlerec/pinsage/dhome_style/origin_data/project.csv", sep='\t', names=['project_id', 'tags', 'urls', 'media_ids'])

down_urls = []
for line in projects.itertuples():
    project_id = line[1]
    tags = line[2]
    urls = eval(line[3])
    media_ids = eval(line[4])
    infos = [(url,id) for url,id in zip(urls, media_ids)]
    down_urls.extend(infos)


multi_downs(down_urls[::-1], 6)

# use_urls = down_urls[:30000]
# use_urls = down_urls[30000:50000]
# use_urls = down_urls[50000:80000]
# use_urls = down_urls[80000:100000]
# use_urls = down_urls[100000:120000]
# use_urls = down_urls[120000:150000]
# use_urls = down_urls[150000:180000]
# use_urls = down_urls[180000:200000]
# use_urls = down_urls[200000:220000]
# use_urls = down_urls[220000:240000]
# use_urls = down_urls[240000:]
# use_urls = down_urls[::-1][:20000]
# use_urls = down_urls[::-1][20000:40000]
# use_urls = down_urls[::-1][40000:60000]
# use_urls = down_urls[::-1][60000:80000]
# use_urls = down_urls[::-1][80000:100000]
# use_urls = down_urls[::-1][100000:120000]
# use_urls = down_urls[::-1][120000:160000]
# use_urls = down_urls[::-1][160000:180000]
# use_urls = down_urls[::-1][180000:200000]
# use_urls = down_urls[::-1][200000:220000]
# use_urls = down_urls[::-1][220000:]

# for url_data in tqdm(use_urls):
#     img_download(url_data)
    