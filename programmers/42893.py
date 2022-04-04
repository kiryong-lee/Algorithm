
import re

def solution(word, pages):
    word = word.lower()
    page_dict = dict()
    content_list = []
    for page in pages:
        page = page.lower()
        content = re.search('<meta.+content="\S+"', page).group(0)[33:-1]
        basic = 0
        for w in re.findall('[a-z]+', page):
            if w == word:
                basic += 1

        content_list.append(content)
        if content in page_dict:
            page_dict[content] += basic
        else:
            page_dict[content] = basic

        hrefs = re.findall('a href="\S+"', page)
        for href in hrefs:
            href = href[8:-1]
            if href in page_dict:
                page_dict[href] += basic / len(hrefs)
            else:
                page_dict[href] = basic / len(hrefs)
    
    max_index = 0
    max_value = 0
    for i, content in enumerate(content_list):
        if max_value < page_dict[content]:
            max_index = i
            max_value = page_dict[content]
    
    return max_index
