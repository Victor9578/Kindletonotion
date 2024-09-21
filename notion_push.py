import requests


class HighlightPush:
    def __init__(self, boo_title, highlights) -> None:

        self.book_title = boo_title
        self.highlights = highlights
        self.NOTION_SECERT = "secret_q6bYrvxOZGUnaH4xCfN0bsJiO2RxcdCkGmxb68PGBji"
        self.NOTION_DATABASE_ID = "107bb40bdcf2808390cdd3337ec4de94"
        self.headers = {
            "Authorization": f"Bearer {self.NOTION_SECERT}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        }

    def push(self):
        url = f"https://api.notion.com/v1/pages"

        for highlight in self.highlights:
            # 构建 Notion API 请求数据
            data = {
                "parent": {"database_id": self.NOTION_DATABASE_ID},
                "properties": {
                    "Book": {"title": [{"text": {"content": self.book_title}}]},
                    "Loc": {
                        "rich_text": [{"text": {"content": highlight["loc"]}}]
                    },
                    "Highlight": {
                        "rich_text": [{"text": {"content": highlight["content"]}}]
                    },
                },
            }

            response = requests.post(url, headers=self.headers, json=data,verify=False)

            if response.status_code == 200:
                print(f"Uploaded highlight at {highlight['loc']} successfully.")
            else:
                print(
                    f"Failed to upload highlight. Status code: {response.status_code}, Response: {response.text}"
                )
