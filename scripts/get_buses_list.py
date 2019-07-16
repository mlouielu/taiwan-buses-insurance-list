from urllib.parse import urljoin

import requests
from lxml import etree


cookies = {
    'ASP.NET_SessionId': 'dl04l0cad5j1hgjq55dzquyn',
    '_ga': 'GA1.3.552341003.1563268676',
    '_gid': 'GA1.3.1060446820.1563268676',
    '_gat_gtag_UA_81912319_12': '1',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Origin': 'https://www.thb.gov.tw',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'https://www.thb.gov.tw/sites/ch/modules/businesscoach/businesscoach_list',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}

data = {
  '__EVENTTARGET': '',
  '__EVENTARGUMENT': '',
  '__VIEWSTATE': '',
  '__VIEWSTATEGENERATOR': '32D45FFB',
  '__EVENTVALIDATION': '',
  'ctl00_ctl00_ctl00_main_lsvMegaMenu_ctrl0_lsvSiteMap_ClientState': '',
  'ctl00_ctl00_ctl00_main_lsvMegaMenu_ctrl1_lsvSiteMap_ClientState': '',
  'ctl00_ctl00_ctl00_main_lsvMegaMenu_ctrl2_lsvSiteMap_ClientState': '',
  'ctl00_ctl00_ctl00_main_lsvMegaMenu_ctrl3_lsvSiteMap_ClientState': '',
  'ctl00_ctl00_ctl00_main_lsvMegaMenu_ctrl4_lsvSiteMap_ClientState': '',
  'ctl00_ctl00_ctl00_main_lsvMegaMenu_ctrl5_lsvSiteMap_ClientState': '',
  'ctl00_ctl00_ctl00_main_lsvMegaMenu_ctrl6_lsvSiteMap_ClientState': '',
  'ctl00_ctl00_ctl00_main_lsvMoblieMenu_ctrl0_lsvSiteMap_ClientState': '',
  'ctl00_ctl00_ctl00_main_lsvMoblieMenu_ctrl1_lsvSiteMap_ClientState': '',
  'ctl00_ctl00_ctl00_main_lsvMoblieMenu_ctrl2_lsvSiteMap_ClientState': '',
  'ctl00_ctl00_ctl00_main_lsvMoblieMenu_ctrl3_lsvSiteMap_ClientState': '',
  'ctl00_ctl00_ctl00_main_lsvMoblieMenu_ctrl4_lsvSiteMap_ClientState': '',
  'ctl00_ctl00_ctl00_main_lsvMoblieMenu_ctrl5_lsvSiteMap_ClientState': '',
  'ctl00_ctl00_ctl00_main_lsvMoblieMenu_ctrl6_lsvSiteMap_ClientState': '',
  'ctl00_ctl00_ctl00_main_lsvHotKeyword_ClientState': '',
  'ctl00$ctl00$ctl00$main$main$content$ddlOrgUnit': '',
  'ctl00$ctl00$ctl00$main$main$content$ddlType': '',
  'ctl00$ctl00$ctl00$main$main$content$ddlSearchField': '0',
  'ctl00$ctl00$ctl00$main$main$content$txbKeyword': '',
  'ctl00_ctl00_ctl00_main_main_content_lsvList_ClientState': '',
  'ctl00_ctl00_ctl00_main_lsvFatFooterSiteMap_ClientState': ''
}

URL = 'https://www.thb.gov.tw/sites/ch/modules/businesscoach/businesscoach_list'


def get_state(r=None):
    if not r:
        r = requests.get(URL)
    root = etree.HTML(r.text)
    viewstate = root.xpath('id("__VIEWSTATE")')[0].get('value')
    eventvalidation = root.xpath('id("__EVENTVALIDATION")')[0].get('value')
    return viewstate, eventvalidation


def fill_state(data, r=None):
    viewstate, eventvalidation = get_state(r)
    data['__VIEWSTATE'] = viewstate
    data['__EVENTVALIDATION'] = eventvalidation


class Pager:
    def __init__(self):
        self.data = data
        self.headers = headers
        self.session = requests.Session()
        self.r = None

    def next_page(self):
        key = 'ctl00$ctl00$ctl00$main$main$content$lsvList$pagList$ctl02$ctl00'
        if self.r and key not in self.data:
            self.data[key] = ''
        fill_state(self.data, self.r)
        self.r = self.session.post(URL, headers=self.headers, data=self.data)
        return etree.HTML(self.r.text)


def get_link(root):
    for i in root.xpath('//tr/td[1]/a'):
        print(','.join([i.get('title'), urljoin(URL, i.get('href'))]))


if __name__ == '__main__':
    p = Pager()
    while True:
        get_link(p.next_page())
