from bs4 import BeautifulSoup

class HttpSoup():

    def __init__(self):
        pass

    def get_text(self, html, tag_name, class_name):
        soup = BeautifulSoup(html, 'lxml')
        return soup.find_all("a", "cp-feedback")