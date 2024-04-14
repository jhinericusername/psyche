from tavily import TavilyClient
from datetime import datetime
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

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


response = tavily.search(query="Give me the links to 15 articles about the 2024 election", search_depth="advanced", max_results=100)

results = [dict_to_utf8(old) for old in response["results"]]

context = [{"url": obj[b"url"], "content": obj[b"content"]} for obj in results]

now = datetime.now()

filename = "article_generation/" + now.strftime("%d-%m-%Y_t%H-%M-%S") + ".txt"

f = open(filename, 'w')

for article in context:
    # write the url
    f.write("URL: " + str(article["url"])[2:-1] + "\n")

    # get content
    string_content = str(article["content"])[2:-1]

    # remove \n from content
    string_content = re.sub("\\\\n", " ", string_content)

    # remove html tags from content
    string_content = re.sub("\\\\...", " ", string_content)

    # remove non-alphanumeric characters from content
    string_content = re.sub("[|,./?\'\":;-]", "", string_content)

    # turn content into lowercase
    string_content = string_content.lower()

    # get nltk stopwords
    stop_words = set(stopwords.words("english"))

    # tokenize content
    word_tokens = word_tokenize(string_content)

    # filter out stopwords from content
    filtered = [w for w in word_tokens if not w.lower() in stop_words]

    # generate filtered sentence from filtered list
    filtered_sentence = ""
    for w in filtered:
        filtered_sentence = filtered_sentence + " " + w

    filtered_sentence = filtered_sentence[1:]

    # write filtered content to file
    f.write("Content: " + filtered_sentence + "\n\n")

f.close()
