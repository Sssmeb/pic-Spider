import os
import html_downloader
import html_parser
import pic_output

class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = pic_output.PicOutPut()
        self.filePath = ("/spider-work/pic-spider/pic." + keyWord + "/")

    def file(self):
        filePath = self.filePath
        if not os.path.exists(filePath):
            os.makedirs(filePath)           #递归创建目录树

    def craw(self, root_url):
        self.file()
        try:
            html_cont = self.downloader.download(root_url)
            num = self.parser.parse(html_cont)
            if num != 0:
                print("total:", num, "*"*20)
                self.outputer.output_pic(num, keyWord, self.filePath)
            else: print("find nothing……")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    keyWord = input("please input the keyWord:")
    root_url = ("https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc").format(keyWord)
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
