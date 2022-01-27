from ssl import match_hostname
import urllib.request as url
import requests
import re
def Translate(DataStr,IsCustomDownload):
    pr = DataStr
    if (IsCustomDownload):
        data =  url.urlopen("https://soc.phreedom.club/api/v1/timelines/public",)
        pr = data.read().decode("utf-8")
    rssdata = '''<?xml version="1.0" encoding="UTF-8"?>
             <rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
             <channel>
             <atom:link href="https://phreedom.club/timeline.xml" rel="self" type="application/rss+xml" />
             <title>global fedi timeline</title>
             <link>https://soc.phreedom.club/main/all</link>
             <description>global fedi timeline</description>'''
    matchs = re.findall('{\"text\/plain\":\"[^}]+(?<!\"\")',str(pr))
    authors =re.findall("{\"account\":{\"acct\":\"[^\"]+",str(pr))
    uris = re.findall('(?<=\"uri\":\")[\w:\/.\-\d]+',str(pr))
    leng = min(len(matchs),len(authors))
    for i in range(leng):
        aut = authors[i][str(authors[i]).rfind('\"')+1:]
        curpost = str(matchs[i][str(matchs[i]).find('\"',13)+1:-1]).translate("utf-8")
        rssdata+= f"<item><guid>{uris[i]}</guid><title>{aut} said {curpost}</title><description>{curpost}</description></item>"
    rssdata+="</channel></rss>"
    return rssdata