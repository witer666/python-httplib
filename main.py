# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from toutiao.httplib import HttpLib
from toutiao.httpsoup import HttpSoup
def test_get():
    objHttpLib = HttpLib()
    data = objHttpLib.get('http://localhost:8080/get.php?a=1&b=1', '', {})
    print(data)

def test_post():
    objHttpLib  = HttpLib()
    data        = objHttpLib.post('http://localhost:8080/post.php', {"a":"1"}, {}, None)
    print(data)

def test_delete():
    objHttpLib = HttpLib()
    data = objHttpLib.delete('http://localhost:8080/delete.php', {"a": "1"}, {})
    print(data)

def test_head():
    objHttpLib = HttpLib()
    data = objHttpLib.head('http://localhost:8080/head.php', {"a": "1"}, {})
    print(data)

def test_options():
    objHttpLib = HttpLib()
    data = objHttpLib.options('http://localhost:8080/options.php', {"a": "1"}, {})
    print(data)

def test_soup():
    objHttpLib = HttpLib()
    data = objHttpLib.get('http://www.baidu.com', '', {})
    objHttpSoup = HttpSoup()
    elements    = objHttpSoup.get_text(data.get('body'), 'a', 'cp-feedback')
    print(elements[0].get_text())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_get()
    test_post()
    test_delete()
    test_head()
    test_options()
    test_soup()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
