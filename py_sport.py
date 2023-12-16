#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..')
from base.spider import Spider
import json
import base64
import random
import requests
import urllib.parse
import re

class Spider(Spider):  # 元类 默认的元类 type
	def getName(self):
		return "体育直播"
	def init(self,extend=""):
		print("============{0}============".format(extend))
		pass
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def homeContent(self,filter):
		result = {}
		cateManual = {
			"体育直播": "全部"
		}
		classes = []
		for k in cateManual:
			classes.append({
				'type_name':k,
				'type_id':cateManual[k]
			})
		result['class'] = classes
		if(filter):
			result['filters'] = self.config['filter']
		return result

	def homeVideoContent(self):
		result = {}
		return result 

	def categoryContent(self,tid,pg, filter,extend):
		result = {}
		if int(pg) > 1:
			return result
		rsp = self.fetch('http://itiyu5.tv/spweb/schedule', headers=self.header)
		root = self.html(self.cleanText(rsp.text))
		dataList = root.xpath("//div[@class='fixtures']/div[@class='box']")
		dateList = root.xpath("//div[contains(@class,'subhead')]")
		videos = []
		#utc_offset = self.fetch('http://worldtimeapi.org/api/timezone/Australia/Sydney', headers=self.header).json()['utc_offset']
		#hour_offset = int(utc_offset.split(':')[0][1:]) - 8
		hour_offset = 3
		for data in dataList:
			pos = dataList.index(data)
			for video in data.xpath(".//div[@class='list']/ul/li"):
				infosList = video.xpath(".//div[@class='team']/div")
				stime = video.xpath(".//p[@class='name']/span/text()")[0].strip()
				sdate = dateList[pos].xpath('.//text()')[0].split()[0].strip()
				hour = stime.split(':')[0]
				if int(hour) < hour_offset:
					sdate = sdate.replace(sdate[3:-1], str(int(sdate[3:-1]) - 1))
					stime = str(24 - hour_offset + int(hour)) + ':' + stime.split(':')[1]
				else:
					hour = str(int(hour) - hour_offset)
					if len(hour) == 1:
						hour = '0' + hour
					stime = hour + ':' + stime.split(':')[1]
				rid = video.xpath(".//p[contains(@class,'btn')]/a/@href")[0]
				state = video.xpath(".//p[contains(@class,'btn')]/a/text()")[0].strip()
				if len(infosList) != 2:
					home = infosList[0].xpath('.//span/text()')[0].strip()
					away = infosList[2].xpath('.//span/text()')[0].strip()
					cover = infosList[0].xpath('.//img/@src')[0]
					name = home + 'VS' + away
				else:
					#cover = 'https://s1.ax1x.com/2022/10/07/x3NPUO.png'
					cover = 'http://gdown.baidu.com/img/0/3200_3200/3962f019ca2c9d6785851b01193facb8.png'
					name = infosList[1].xpath('.//text()')[0].strip()
				if state != '已结束':
					videos.append({
						"vod_id": rid,
						"vod_name": name,
						"vod_pic": cover,
						"vod_remarks": '[{}]|{}'.format(sdate, stime)
					})
		result['list'] = videos
		result['page'] = pg
		result['pagecount'] = 9999
		result['limit'] = 90
		result['total'] = 999999
		return result

	def detailContent(self, array):
		#array = ['/spweb/live/mid/62821']
		html_content = self.fetch('http://itiyu5.tv{}'.format(array[0]), headers=self.header)
		#print(html_content.text)
		matches = re.findall("/spweb/live/mid/", html_content.text)
		if len(matches) >0:
			playurl = ''
			for i in range(1, len(matches)+1):
				rsp = self.fetch('http://itiyu5.tv{}/vid/{}'.format(array[0], i), headers=self.header)
				if 'vid/{}'.format(i) not in rsp.text or not '\'url\': ' in rsp.text:
					title = '比赛尚未开始'
					purl = 'http://0.0.0.0'
				else:
					purl = self.regStr(reg=r"\'url\': \"(.*?)\"", src=rsp.text)
					title = self.regStr(reg=r"\"title\": \"(.*?)\"", src=rsp.text)
					if purl == '':
						rid = self.regStr(reg=r'config\.iurl = \"(.*?)\"', src=rsp.text)
						if '.m3u' in rid:
							if rid.count('http') != 1:
								replstr = self.regStr(reg=r'(http.*?)http', src=rid)
								purl = rid.replace(replstr, '')
					if i == 1:									
						playurl = '直播1$' + purl
					else:
						playurl = playurl + '#直播{}$'.format(i) + purl
			playfrom = title							
		else:
			title = '比赛尚未开始'
			playurl = 'http://0.0.0.0'

			#if '.m3u' in purl or purl == 'http://0.0.0.0':
				#break
		vod = {
			"vod_id":array[0],
			"vod_name":title,
			#"vod_pic":'https://s1.ax1x.com/2022/10/07/x3NPUO.png',
			"vod_pic":'http://gdown.baidu.com/img/0/3200_3200/3962f019ca2c9d6785851b01193facb8.png',
			"type_name":'',
			"vod_year":'',
			"vod_area":"",
			"vod_remarks":'',
			"vod_actor":"",
			"vod_director":'',
			"vod_content":""
		}
		
		vod['vod_play_from'] = playfrom
		vod['vod_play_url'] = playurl
		result = {
			'list':[
				vod
			]
		}
		
		print(vod)
		return result

	def searchContent(self,key,quick):
		result = {
			'list':[]
		}
		return result
	def playerContent(self,flag,id,vipFlags):
		result = {}
		result["parse"] = 0
		result["playUrl"] = ''
		result["url"] = id
		result["header"] = ''
		return result

	config = {
		"player": {},
		"filter": {}
	}
	header = {
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36"
	}

	def localProxy(self,param):
		return [200, "video/MP2T", action, ""]
