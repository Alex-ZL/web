#!/usr/bin/python
## test view in reading django book
#from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context
from django.http import HttpResponse
import MySQLdb
import datetime

def book_list(request):
	db = MySQLdb.connect(user='me', db='mydb',passwd='secret',host='localhost')
	cursor = db.cursor()
	cursor.execute('SELECT name FROM books ORDER BY name')
	names = [row[0] for row in cursor.fetchall()]
	db.close()
	return render_to_response('book_list.html',{'names': names})

def todolist1(request):
	list =['get up without any hesitation', 
			'read python practice book',
			'coding and coding',
			'do anything to make improve yourself quickly',
			"don't let she wait too long time",
			'life is 10% what happens to you, and 90% how you react to it.',
			'breakfast']
	
	return render_to_response('to-do-list1.html',{'task_list':list,})

def musicians(request):
	MUSICIANS = [
	{'name': 'Django Reinhardt', 'genre': 'jazz'},
	{'name': 'Jimi Hendrix',     'genre': 'rock'},
	{'name': 'Louis Armstrong',  'genre': 'jazz'},
	{'name': 'Pete Townsend',    'genre': 'rock'},
	{'name': 'Yanni',            'genre': 'new age'},
	{'name': 'ella Fitzgerald',  'genre': 'jazz'},
	{'name': 'Wesley Willis',    'genre': 'casio'},
	{'name': 'Jonh Lennon',      'genre': 'rock'},
	{'name': 'Bono',             'genre': 'rock'},
	{'name': 'Garth Brooks',     'genre': 'country'},
	{'name': 'Duke Ellington',   'genre': 'jazz'},
	{'name': 'William Shatner',  'genre': 'spoken work'},
	{'name': 'Madonna',          'genre': 'pop'},
	]
	musicians = []
	has_pretentious = False
	for m in MUSICIANS:
		if ' ' not in m['name']:
			has_pretentious = True

		musicians.append({
			'name': m['name'],
			'genre': m['genre'],
			'is_important': m['genre'] in ('rock','jazz'),
			'is_pretentious': ' 'not in m['name'],
		})

	return render_to_response('musicians.html',{'musicians':musicians, 'has_pretentious':has_pretentious,})

def current_datetime(request):
	now = datetime.datetime.now()
	#t = get_template('current_datetime.html')
	#html = t.render(Context({'current_date':now}))
	return render_to_response('current_datetime.html',{'current_date':now})

def hours_ahead(request,offset):
	offset = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = 'In %s hour(s), it will be %s.' % (offset, dt)
	return HttpResponse(html)

def hour_offset(request,flag, offset):
	offset = int(offset)
	if offset == 1:
		hours = 'hour'
	else:
		hours = 'hours'
	
	if flag == 'plus':
		dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
		html = 'In %s %s, it will be %s.' % (offset,hours,dt)
	else: 
		dt = datetime.datetime.now() - datetime.timedelta(hours=offset)
		html = '%s %s ago, it was %s.' % (offset,hours,dt)
	return HttpResponse(html)
