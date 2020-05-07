#! /usr/bin/python3

import requests
from lxml import etree
import pandas

class GetUserAgent(object):

	"""docstring for GetUserAgen"""
	def __init__(self, url):

		super(GetUserAgent, self).__init__()

		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
           				'Accept':'application/json, text/javascript, */*; q=0.01'}
		self.url = url
		self.name = url.split('=')[-1]

	def GetBrowserAgent(self):

		'''Get Agent including Browser and Mobile Browser'''
		try:
			response = requests.get(self.url,self.headers,timeout = (3,60))
			response.encoding = response.apparent_encoding
			tree = etree.HTML(response.text)
			useragents = tree.xpath('//ul/li/a/text()')
			useragentlist =  [useragent for useragent in useragents if len(useragent)>80]
			df = pandas.DataFrame({'id':range(1,len(useragentlist)+1),'usergent':useragentlist})
			df.to_excel(self.name+'.xlsx',index=0)
			return len(useragentlist)
		except Exception :
			pass

if __name__ == '__main__':
	urllist = ['http://useragentstring.com/pages/useragentstring.php?typ=Browser','http://useragentstring.com/pages/useragentstring.php?typ=Mobile Browser']
	count = 0
	for url in urllist:
		print('正在爬取{0}的UserAgent...'.format(url))
		count = count + GetUserAgent(url).GetBrowserAgent()
	print('总共爬取{0}个UserAgent'.format(count))