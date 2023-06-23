import requests
from bs4 import BeautifulSoup


def get_goodreads_rating(book_title):
    # 替换为你的Goodreads搜索URL
    search_url = f"https://www.goodreads.com/search?q={book_title}"

    # 发起搜索请求
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # 获取搜索结果中的第一本书的URL
    first_book_link = soup.find("a", class_="bookTitle")["href"]
    book_url = f"https://www.goodreads.com{first_book_link}"

    # 发起书籍详情页请求
    response = requests.get(book_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # 获取书籍评分
    rating_element = soup.find("div", class_="RatingStatistics__rating")

    if rating_element:
        rating = rating_element.text
        return f"{rating}/5"
    else:
        return "-1"


def example():
    # 示例用法
    book_title = (
        "Stolen Focus: Why You Can't Pay Attention- and How to Think Deeply Again"
    )
    rating = get_goodreads_rating(book_title)
    print(f"{book_title} 的评分：{rating}")
