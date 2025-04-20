import re

def extract_markdown_images(text):
    matches = (re.findall(r"!\[([^\[\]]*)\]\(([^\]\)]*)\)?", text))
    match_list = list(matches)
    return match_list

def extract_markdown_links(text):
    matches = (re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text))
    match_list = list(matches)
    return match_list



# text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
# print(extract_markdown_links(text))