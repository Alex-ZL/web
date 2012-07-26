from django.http import HttpResponse
import json
import postlist_crawler
import postdetail_crawler
def single_board(request, board):

	inlist = [board]
	outdata = postlist_crawler.get_result(inlist)
	return HttpResponse(json.dumps(outdata).decode('unicode_escape'))

def post_detail(request, board, pid):
	outdata = postdetail_crawler.get_postdetail(board,pid)
	return HttpResponse(json.dumps(outdata).decode('unicode_escape'))

def multiple_board(request):
	boards = request.GET.getlist('board')
	outdata = postlist_crawler.get_result(boards,2)
	return HttpResponse(json.dumps(outdata).decode('unicode_escape'))
