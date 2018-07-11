import requests

class HtmlDownloader():

    def download(self, url):
        if url is None:
            return
        try:
            __response = requests.get(url)
            html_cont = __response.text
            return html_cont
        except Exception as e:
                print(e)




