import feedgenerator
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# arXiv API 请求
url = "https://export.arxiv.org/api/query?search_query=cat:hep-ph&sortBy=lastUpdatedDate&sortOrder=descending&max_results=50"
response = requests.get(url)
soup = BeautifulSoup(response.content, "xml")

# 创建 RSS Feed
feed = feedgenerator.Rss201rev2Feed(
    title="arXiv hep-ph (New)",
    link="https://arxiv.org/list/hep-ph/new",
    description="Latest papers in hep-ph (sorted by announcement date)",
)

# 解析 arXiv API 结果并添加到 RSS Feed
for entry in soup.find_all("entry"):
    title = entry.title.text
    link = entry.id.text
    description = entry.summary.text
    pubdate_str = entry.published.text  # 获取日期字符串
    pubdate = datetime.strptime(pubdate_str,
                                "%Y-%m-%dT%H:%M:%SZ")  # 转换为 datetime 对象
    feed.add_item(
        title=title,
        link=link,
        description=description,
        pubdate=pubdate,
    )

# 输出 RSS Feed
with open("hep-ph_rss.xml", "w") as f:
    f.write(feed.writeString("utf-8"))
