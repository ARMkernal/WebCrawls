import requests
from lxml import etree

hea = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; '
                     'x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}


def getData(url):
    r = requests.get(url, headers=hea)
    sel = etree.HTML(r.text)
    for module in sel.xpath('//*[@id="rankWrap"]/div[2]/ul/li'):
        rank_raw = module.xpath('span[3]/strong/text()')
        if len(rank_raw) == 0:
            rank = module.xpath('span[3]/text()')[0].strip()
        else:
            rank = rank_raw[0]
        sss = module.xpath('a/text()')
        time = module.xpath('span[4]/span/text()')[0].strip()
        try:
            sli = str(sss[0]).split('-')
            singer = sli[0].strip()
            song = sli[1].strip()
        except:
            pass
        data = {
            'rank': rank,
            'singer': singer,
            'song': song,
            'time': time
        }
        print(data)


for a in range(1, 24):
    url = 'https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(a)
    getData(url)
