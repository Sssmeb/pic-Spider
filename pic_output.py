import requests
from lxml import etree
import random
import threading
import queue

class PicOutPut():

       def lget(self, page, keyWord):
            # 提取出原图的链接
            purl = ("https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc&page={}").format(keyWord, page)
            try:
                __response = requests.get(purl)
                selector = etree.HTML(__response.text)
                lpic = selector.xpath('//a[@class="jsAnchor thumb-tags-toggle tagged"]/@href')
                return lpic
            except Exception as e:
                print(e, "②")

       def output_pic(self, num, keyWord, filePath):
                page = int(num / 24 + 1)
                __count = 0
                q = queue.Queue()
                for i in range(page):
                    purl = self.lget(i + 1, keyWord)

                    for item in purl:
                        num = item.strip("https://alpha.wallhaven.cc/wallpaper/").strip("/thumbTags")
                        html = "http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-" + num + ".jpg"   #拼接出大图的地址
                        q.put(html)
                semaphore = threading.BoundedSemaphore(3)          #计线程数，最大不超过3

                def download(html,__count):
                    semaphore.acquire()
                    pic_path = (filePath + keyWord + str(__count) + ".jpg")
                    ua_list = (
                           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
                           "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
                           "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
                           "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
                           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
                       )

                    headers = {"User-Agent": random.choice(ua_list)}
                    try:
                           pic = requests.get(html, headers=headers)
                           with open(pic_path, "wb") as f:             #利用with open ，当写入结束后，自动关闭文件
                               f.write(pic.content)
                           print("pic {} download succeed".format(__count))

                    except Exception as e:
                        print(e, "③")


                    semaphore.release()        #释放后会检测线程数是否到达最大量

                while not q.empty():
                    __count += 1
                    worker = threading.Thread(target=download, args=(q.get(), __count))
                    worker.start()

