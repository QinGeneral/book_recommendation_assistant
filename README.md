# 选书助手

选书助手项目旨在自动化获取一本书的价值。

图书价值 = 内容品质 + 版本价值 + 社会评价 + 内在动机

## 使用

> 目前实现了获取书籍豆瓣、GoodReads 评分的功能。

```bash
查询书籍在豆瓣和 GoodReads 的评分

options:
  -h, --help            show this help message and exit
  -b BOOK, --book BOOK  要查询的书籍名称
```

例子 1：
```bash
python get_book_level.py -b 如何阅读一本书
```

例子 2：
```bash
python get_book_level.py --book "Stolen Focus: Why You Can't Pay Attention- and How to Think Deeply Again"
```

## 方案 1：GPT + Browsering

```
Prompt：
一本图书价值 = 内容品质 + 版本价值 + 社会评价 + 内在动机，请根据这四点给出{BookName}的价值评分，0-10分
```

此方案下，大语音模型必须包含此图书数据，或能够根据网络搜索拿到此图书数据。

## 方案 2

根据图书价值公式的四点，分别打分。

1. 内容品质：GPT + Browsering；
2. 版本价值：GPT + Browsering；
3. 社会评价：豆瓣、Goodreads 等网站评分；
4. 内在动机。