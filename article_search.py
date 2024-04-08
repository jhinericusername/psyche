from tavily import TavilyClient
from datetime import datetime


def dict_to_utf8(old_dict):
    new_dict = {}
    for k, v in old_dict.items():
        if isinstance(k, str):
            k = k.encode(encoding='utf-8', errors="replace")
        if isinstance(v, str):
            v = v.encode(encoding='utf-8', errors="replace")
        
        new_dict[k] = v
    return new_dict


api_key = "API-KEY-HERE"

tavily = TavilyClient(api_key=api_key)

response = tavily.search(query="Give me the links to 15 articles about the 2024 election", search_depth="basic", max_results=15)

results = [dict_to_utf8(old) for old in response["results"]]

context = [{"url": obj[b"url"], "content": obj[b"content"]} for obj in results]

now = datetime.now()

filename = "article_generation/" + now.strftime("%d-%m-%Y_t%H-%M-%S") + ".txt"

f = open(filename, 'w')

for article in context:
    f.write("URL: " + str(article["url"]) + "\n")
    f.write("Content: " + str(article["content"]) + "\n\n")

f.close()
