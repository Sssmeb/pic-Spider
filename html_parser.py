from lxml import etree
class HtmlParser():

    def parse(self, html_cont):
        selector = etree.HTML(html_cont)
        #提取出文本中的图片张数
        tnum = selector.xpath('//header[@class="listing-header"]/h1[1]/text()')
        snum = str(tnum[0])
        lnum = list(filter(str.isdigit, snum))      #筛选出文本中的数字
        fnum = ""
        for item in lnum:
            fnum += item
        num = int(fnum)
        return num




