from django.http import HttpResponse
from django.shortcuts import render_to_response
import json
import postlist_crawler
import postdetail_crawler
def single_board(request, board):

	inlist = [board]
	outdata = postlist_crawler.get_result(inlist)
	outdata = outdata.items()

	#title = outdata[0][1][0]['title']
	return render_to_response('postlists.html', {'board_posts':outdata})

def post_detail(request, board, pid):
	outdata = postdetail_crawler.get_postdetail(board,pid)
	return HttpResponse(json.dumps(outdata).decode('unicode_escape'))

def multiple_board(request):
	boards = request.GET.getlist('board')
	outdata = postlist_crawler.get_result(boards,2)
	outdata = outdata.items()
	outdata = [('pic','ture'),('girls','boys')]
	return render_to_response('postlists.html', {'board_posts':outdata})

