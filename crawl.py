#coding:utf-8
import requests
import json
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pprint
import datetime
import csv




class Crawl:

	def __init__(self):

		
		#crawling data
		self.title = []
		self.popular = []
	

	def crawling(self):
		url = 'https://www.reddit.com/r/all/?count=0'
		for i in range(140):
			print i
			
			res_news = requests.get(url, headers = {'User-agent': 'your bot 0.1'})
			#print res_news
			soup_news = BeautifulSoup(res_news.text.encode('utf8'), "html.parser")
			wholeBody = soup_news.find_all('div',attrs={"class":"entry unvoted"})
			for item in wholeBody:
				title = item.find('p',attrs={"class":"title"}).text.encode('utf-8')
				liFirst = item.find('li',attrs={"class":"first"}).text.encode('utf-8').split(' ')
				if(len(liFirst) < 2):
					number = 0
				else:
					number = int(item.find('li',attrs={"class":"first"}).text.encode('utf-8').split(' ')[0])
				#print title
				#print number
				self.title.append(title)
				if number >= 50:
					self.popular.append(1)
				if number < 50:
					self.popular.append(0)
			url = soup_news.find_all('span',attrs={"class":"next-button"})[0].find('a').attrs['href'].encode('utf-8')
			#print url
		#print self.title
		#print self.popular
		print len(self.title)
		print len(self.popular)
		with open ('train.csv', mode='w') as write_file:
			writer = csv.writer(write_file)
			writer.writerow(["title","popular"])
			for i in range(len(self.popular)):
				writer.writerow([self.title[i],self.popular[i]])
		

		

			

if __name__ == "__main__":
	crawlInstance = Crawl()
	crawlInstance.crawling()