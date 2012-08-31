#!usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re
import time, datetime


# convert date format from 'Wed Jul 25 16:20:20 2012' to '2012-07-25T16:20:00'
def date_format_convert(s_date):
	temp = time.strptime(s_date, "%a %b %d %H:%M:%S %Y")
	return  time.strftime("%Y-%m-%dT%H:%M:%S", temp)


def get_postdetail(board, pid):
	post_url = 'http://bbs.nju.edu.cn/bbstcon?board=' + board + '&file=M.' + pid + '.A'

	try:
		content = urllib2.urlopen(post_url).read().decode('gb2312','ignore')
	except urllib2.URLError:
		except_message = "Unable reach URL: "+ post_url
		return [except_message]

	#content = urllib2.urlopen(post_url).read().decode('gb2312','ignore')
	soup = BeautifulSoup(content)

	postdetail_list = []
	
	for item in soup.findAll('a', href=re.compile('^bbsqry.*')):
		postdetail_dict = {}
	
		postdetail_dict['author'] = item.contents[0]
		post = str(item.parent.parent.parent.contents[1].contents).decode('utf-8')
	
		text_board =u"信区:"
		text_title =u"标  题:"
		text_date =u"发信站: 南京大学小百合站"
		text_tail =u"--"
		#print isinstance(text,unicode)
		#print post
	
		pos_board = post.find(text_board)
		pos_title = post.find(text_title)
		pos_date = post.find(text_date)
		pos_tail = post.rfind(text_tail)
	
		#print 'board:', post[pos_board+4 : pos_title-1]
		postdetail_dict['board'] = post[pos_board+4 : pos_title-1]
	
		#print 'title:', post[pos_title+6 : pos_date-1]
		postdetail_dict['title'] = post[pos_title+6 : pos_date-1]
	
		#print 'date:', post[pos_date+15 : pos_date+39]
		postdetail_dict['date'] = date_format_convert(post[pos_date+15 : pos_date+39])
	
		#print 'body:', post[pos_date+42 : pos_tail]
		postdetail_dict['body'] = post[pos_date+42 : pos_tail]
	
		postdetail_list.append(postdetail_dict)
	
	return postdetail_list


if __name__ == '__main__':
	import json
	postdetail_list = get_postdetail('Girls','1343222805')
	print json.dumps(postdetail_list).decode('unicode_escape') 
