import argparse

from douban_get_book_rate import get_douban_rating
from goodread_get_book_rate import get_goodreads_rating


def __main__():
    # 创建解析器对象
    parser = argparse.ArgumentParser(description="查询书籍在豆瓣和 GoodReads 的评分")

    # 添加命令行参数
    parser.add_argument("-b", "--book", type=str, help="要查询的书籍名称")
    args = parser.parse_args()

    if args.book == None or args.book.strip() == "":
        print("请输入书籍名称")
        print(parser.format_usage())
        return
    rate_douban = get_douban_rating(args.book)
    rate_goodreads = get_goodreads_rating(args.book)

    print(args.book)
    print(f"豆瓣评分：{rate_douban}")
    print(f"Goodreads评分：{rate_goodreads}")


__main__()
