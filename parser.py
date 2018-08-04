from pyquery import PyQuery
import re

reNumberInText = re.compile(r"^([0-9,]+)")

def text(text, selector = ""):
    html = PyQuery(text)
    return html(selector)


def getTrendingData(pq):
    data = {}
    subject = pq.find("h3>a")
    data["subject"] = subject.text()
    data["url"] = subject.attr("href")
    data["description"] = pq.find("p").text().strip()
    data["language"] = pq.find("span[itemprop=programmingLanguage]").text().strip()
    data["starts"] = pq.find("a.mr-3:nth-child(2)").text().strip()
    data["forks"] = pq.find("a.mr-3:nth-child(3)").text().strip()
    data["authors"] = getItemListAttr(pq.find("span.mr-3 > a.d-inline-block"), "href", "/")
    data["ups"] = getNumberFromText(pq.find("span.float-sm-right").text().strip())
    return data

def getItemListAttr(pq, name = "", strip = True):
    isText = name == "text"
    result = []
    for i in pq.items():
        if (isText):
            attr = i.text()
        else:
            attr = i.attr(name)
        if (strip):
            attr = attr.strip()
        if isinstance(strip, str):
            attr = attr.strip(strip)
        result.append(attr)
    return result

def getNumberFromText(text):
    m = reNumberInText.match(text)
    if (m == None):
        return None
    else:
        return m.group(0)