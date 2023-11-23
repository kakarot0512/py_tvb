#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider
#import json
import re
import requests



class Spider(Spider):
	def getName(self):
		return "btl"
	def init(self,extend=""):
		pass
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def homeContent(self,filter):
		result = {}
		return result
	def homeVideoContent(self):
		result = {}
		return result
	def categoryContent(self,tid,pg,filter,extend):
		result = {}
		return result

	def btl_get(self, url):
		# 创建一个 session 对象
		session = requests.Session()
		default_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}	
		# 发送第一次请求，获取HTML代码
		response1 = session.get(url, headers=default_headers)

		# 从HTML代码中提取cookie值
		cookie_pattern = re.compile(r'document\.cookie\s*=\s*"ge_js_validator_88=([^;]+)')
		match = cookie_pattern.search(response1.text)
		if match:
			cookie_value = match.group(1)
			# 模拟浏览器 reload()，发送第二次请求
			response2 = session.get(url, cookies={"ge_js_validator_88": cookie_value}, headers=default_headers)

			# 返回第二次请求的响应内容
			return response2.text
		else:
			return "Cookie未找到"	
  
	def detailContent(self,ids):
		aid = ids[0]			
		url = 'https://www.5bt0.com/mv/{0}.html'.format(aid)
		html = self.btl_get(url)
		
		title = re.search(r'info-title lh32">(.*?)</span>', html,re.S).group(1)
		area = re.search(r'上映地区:(.*?)</span>', html,re.S).group(1).strip()
		content = re.search(r'v:summary">(.*?)</span>', html,re.S).group(1).strip()

		dire = re.search(r'导演.*?<span itemprop="name">(.*?)</span>', html,re.S).group(1)
		actor_pattern1 = r'主演：</span>\s*<div class="tag-box">(.*?)</div>'
		actor_text = re.search(actor_pattern1, html, re.S).group(1)
		actor_pattern2 = re.compile(r'<span itemprop="name">(.*?)</span>', re.S)
		actor_matches = re.findall(actor_pattern2, actor_text)
		# 将演员名字合并成一个字符串，用逗号连接
		actors_combined = ','.join(actor_matches)
							
		vod = {
				"vod_id": aid,
				"vod_name": title,
				"vod_pic": '',
				"type_name": '',
				"vod_year": '',
				"vod_area": area,
				"vod_remarks": '',
				"vod_actor": actors_combined,
				"vod_director": dire,
				"vod_content": content
				}
		pattern = re.compile(r'class="h5">(.*?)</span>', re.S)
		sealists = re.findall(pattern, html)
		playfrom = ''
		playurl = ''
		for pf in sealists:
			playfrom = playfrom + '$$$' + pf
			    
			pattern_text = re.escape(pf)  # 使用re.escape确保变量中的特殊字符被转义
			pattern2 = re.compile(fr'text-center">{pattern_text}.*?(magnet:.*?)"><div', re.S)
			maglists = re.findall(pattern2, html)
			    
			for purl in maglists:
			      
			    playurl = playurl + '#磁力$' + purl
			playurl = playurl.strip('#磁力$') + '$$$'
		vod['vod_play_from'] = playfrom.strip('$$$')
		vod['vod_play_url'] = '磁力$' + playurl.strip('$$$')
			  
		result = {
		'list': [
			vod
				]
			}
		
		return result	
	def searchContent(self,key,quick):
		    
	    url = 'https://www.5bt0.com/search.php?sb={0}'.format(key)
	    html = self.btl_get(url)
	    	    
	    pattern = re.compile(r'<a href="./mv/(.*?).html.*?image:url\((.*?)\).*?<h5>(.*?)<span class="type--fine-print">\((.*?)\)</span></h5>', re.S)
	    sealists = re.findall(pattern, html)
	    
	    videos = []
	    for link, img, title, remark in sealists:
	        videos.append({
	            "vod_id": link,
	            "vod_name": title,
	            "vod_pic": img,
	            "vod_remarks": remark
	        })
	   	   	    
	    result = {
	        'list': videos
	    }
	    return result

	def playerContent(self,flag,id,vipFlags):
		result = {}
		url = id
		result["parse"] = 0
		result["playUrl"] = ''
		#result["url"] = 'magnet:?xt=urn:btih:{0}&tr=udp%3a%2f%2fopentracker.i2p.rocks%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.altrosky.nl%3a6969%2fannounce'.format(url)
		result["url"] = url
		result["header"] = {
			"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
		}
		result["contentType"] = ''
		return result
	config = {
		"player": {},
		"filter": {}
	}
	header = {}
	def localProxy(self,param):
		action = {
			'url':'',
			'header':'',
			'param':'',
			'type':'string',
			'after':''
		}
		return [200, "video/MP2T", action, ""]
