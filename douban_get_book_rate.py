import requests


def get_douban_rating(book_title):
    api_key = "0ac44ae016490db2204ce0a042db2916"
    api_url = f"https://frodo.douban.com/api/v2/search/weixin?q={book_title}&start=0&count=20&apikey={api_key}"

    headers = {
        "Host": "frodo.douban.com",
        "referer": "https://servicewechat.com/wx2f9b06c1de1ccfca/91/page-frame.html",
        "xweb_xhr": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/6.8.0(0x16080000) NetType/WIFI MiniProgramEnv/Mac MacWechat/WMPF XWEB/30515",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Accept-Language": "zh-CN,zh",
    }
    # 发起API请求
    response = requests.get(api_url, headers=headers)
    data = response.json()

    # 检查是否找到书籍
    if data["count"] > 0:
        # 获取第一本书的评分
        rating = data["items"][0]["target"]["rating"]
        max = rating["max"]
        value = rating["value"]
        return f"{value}/{max}"
    else:
        return "-1"


def example():
    # 示例用法
    book_title = (
        "Stolen Focus: Why You Can't Pay Attention- and How to Think Deeply Again"
    )
    rating = get_douban_rating(book_title)
    print(f"{book_title} 的评分：{rating}")
