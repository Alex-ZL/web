#!usr/bin/env python
#coding = utf-8
import urllib2
from bs4 import BeautifulSoup
import re
import time, datetime
from threading import Thread
import Queue

class Crawler(Thread):

	def __init__(self, name, board_queue, post_lists_queue):
		Thread.__init__(self)
		self.board_queue = board_queue
		self.post_queue = post_lists_queue
		self.name = name
		self.start()


	def run(self):
		while 1:
			if self.board_queue.empty():
				break

			cur_board = self.board_queue.get()
			temp_dict = {}

			cur_url = 'http://bbs.nju.edu.cn/board?board=' + cur_board
			content = urllib2.urlopen(cur_url).read().decode('gb2312','ignore')
			soup = BeautifulSoup(content)
			cur_postlist = self.get_postlist(soup)

			temp_dict[cur_board] = cur_postlist
			#temp_list.append(cur_postlist)

			self.post_queue.put(temp_dict)
			
			print 'Crawler' + self.name + 'finish the board: ' + cur_board
			self.post_queue.task_done()
			self.board_queue.task_done()


		# convert date format from 'Jul 25 16:20' to '2012-07-25T16:20:00'
		# to avoid crash caused by time.strptime, change to handling strings directly.
	def date_format_convert(self, s_date):
		month_dict = {'Jan':'01','Feb':'02','Mar':'03', 'Apr':'04', 'May':'05',
		              'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10',
		              'Nov':'11', 'Dec':'12'}

		month = month_dict[s_date[:3]]
		day = s_date[4:6]
		hour_min = s_date[7:12]
		return  str(datetime.datetime.now().year) + '-' +month+ '-' +day+ 'T' +hour_min+ ':00'


	def get_postlist(self,soup):
		""" Use beautiful soup to get postlist in one board"""
		postlist = []
		for item in soup.findAll('a', href=re.compile('^bbsqry.*')):
	
			##only fetch the item with 4 or 5 digits PostID.
			if len(item.parent.parent.contents[0].contents[0]) in (4,5):
				record = item.parent.parent.contents
				dict_record = {}
				if len(record) == 6:

					#print record[0].contents[0]
					dict_record['num'] = record[0].contents[0]

					#print record[2].contents[0].contents[0]
					dict_record['author'] = record[2].contents[0].contents[0]

					#print date_format_convert(record[3].contents[0])
					dict_record['date'] = self.date_format_convert(record[3].contents[0])

					#print record[4].contents[0].contents[0]
					dict_record['title'] = record[4].contents[0].contents[0]

					#print record[5].contents[0].contents[0]
					dict_record['replyCount'] = record[5].contents[0].contents[0]

					#print record[5].contents[2].contents[0]
					dict_record['viewCount'] = record[5].contents[2].contents[0]

				else:

					#print record[0].contents[0]
					dict_record['num'] = record[0].contents[0]

					#print record[2].contents[0].contents[0]
					dict_record['author'] = record[2].contents[0].contents[0]

					#print record[4].#contents[0].contents
					dict_record['date'] = self.date_format_convert(record[4].contents[0].contents[0])
					
					#print record[4].contents[0].contents[1].contents[0].contents[0]
					dict_record['title'] = record[4].contents[0].contents[1].contents[0].contents[0]

					#print record[4].contents[0].contents[2].contents[0].contents[0]
					dict_record['replyCount'] = record[4].contents[0].contents[2].contents[0].contents[0]

					dict_record['viewCount'] = 'N/A'
	
				postlist.append(dict_record)
		return postlist

def get_result(boardlist, crawler_num = 1):
	"""use boardlist to fetch data from boards, then return result in the form of dict."""
	post_lists_dict={}
	board_queue = Queue.Queue()
	post_lists_queue = Queue.Queue()
	
	for board in boardlist:
		board_queue.put(board)
	
	for i in range(crawler_num):
		threadName = 'num'+str(i)
		Crawler(threadName, board_queue, post_lists_queue)
	
	#time.sleep(2)
	while 1:
		item = post_lists_queue.get()
		post_lists_dict = dict(item.items() + post_lists_dict.items())
		if len(post_lists_dict) == len(boardlist):
			break
	
	post_lists_queue.join()
	board_queue.join()
	return post_lists_dict



if __name__ == "__main__":

	import json
	boardlist = ['pictures', 'girls', 'Chat']
	#boardlist = ['pictures']
	result = get_result(boardlist,2)
	result = result.items()
	print type(result)
	print len(result)
	#print result
	#data = json.dumps(result)
	#print type(data)
	#print data.decode('unicode_escape')
