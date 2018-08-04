import myrequests
import parser
import csv
import time


urls = {
    "all":["https://github.com/trending/?since=monthly"], 
    "rust":["https://github.com/trending/rust?since=monthly"], 
    "javascript":["https://github.com/trending/javascript?since=monthly"], 
    "python":["https://github.com/trending/python?since=monthly"], 
    "golang":["https://github.com/trending/go?since=monthly"], 
    "css":["https://github.com/trending/css?since=monthly"], 
    "php":["https://github.com/trending/php?since=monthly"], 
    }


trendingData = []
for item in urls:
    for i in myrequests.gets(urls[item]):
        if i["response"].status_code == 200:
            proList = parser.text(i["response"].text, "ol:first>li")

            for rl in proList.items():
                data = parser.getTrendingData(rl)
                trendingData.append(data)

        else:
            print("url: %s 请求响应失败， code：%i" % (i["url"], i["response"].status_code) )

    if (len(trendingData) > 0):
        csv.write("github-Trending-%s.csv" % item, trendingData)    
    else:
        print("%s 数据拉取失败" % item)

    time.sleep(60)