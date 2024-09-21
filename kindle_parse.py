import os
from bs4 import BeautifulSoup


class Highlights:
    def __init__(self, html) -> None:
        self.book_title = ""
        self.highlights = []
        with open(html, "r", encoding="utf-8") as f:
            self.soup = BeautifulSoup(f, "html.parser")

    def parse(self):

        # 提取书名
        self.book_title = self.soup.find("div", class_="bookTitle").text.strip()

        # 提取所有高亮
        note_headings = self.soup.find_all("div", class_="noteHeading")
        note_texts = self.soup.find_all("div", class_="noteText")

        for heading, text in zip(note_headings, note_texts):

            # 提取位置 (loc)
            loc = heading.text.split(" ")[-1].strip()

            # 提取高亮内容
            content = text.text.strip()

            self.highlights.append({"loc": loc, "content": content})

        # 打印解析结果
        print(f"Book Title: {self.book_title}")
        # for highlight in self.highlights:
        #     print(f"Location: {highlight['loc']}, Content: {highlight['content']}")
