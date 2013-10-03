from sing.models import *
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from random import choice
import logging

logger = logging.getLogger(__name__)
# IP = 'http://71.190.160.148:5000'
IP = 'http://songline.herokuapp.com'

@require_http_methods(["GET"])
def view(request):
	songs = Songs.objects.all().order_by('-created')

	return render_to_response('main.html', {'songs': songs})

@csrf_exempt
@require_http_methods(["POST"])
def callin(request):
	greeting = 'https://dl.dropboxusercontent.com/u/2094414/Welcome.mp3'

	xml = '''
		<Response>
			<Gather action="/stepone">
				<Play loop="10">%s</Play>
    		</Gather>
    		<Redirect>%s</Redirect>
		</Response>
	      ''' % (greeting ,IP)

	return HttpResponse(xml, mimetype="text/xml")

@csrf_exempt
@require_http_methods(["POST"])
def stepone(request):
	digits = request.POST.get('Digits')

	if digits == '*':
		message = 'https://dl.dropboxusercontent.com/u/2094414/Record.mp3'
		xml = '''
			<Response>
				<Play>%s</Play>
				<Record action="/record" playBeep="true" />
			</Response>
			  ''' % (message) #Press any key to stop recording.

	else:
		message = 'https://dl.dropboxusercontent.com/u/2094414/ListentoSong.mp3'
		xml = '''
			<Response>
				<Play>%s</Play>
				<Redirect>%s/play</Redirect>
			</Response>
			  ''' % (message, IP)

	return HttpResponse(xml, mimetype="text/xml")

@csrf_exempt
@require_http_methods(["POST"])
def record(request):
	url = request.POST.get('RecordingUrl')
	length = request.POST.get('RecordingDuration')
	phone_number = request.POST.get('Caller')

	song = Songs()
	song.url = url
	song.phone_number = phone_number
	song.length = int(length)
	song.save()

	message = 'https://dl.dropboxusercontent.com/u/2094414/Thanks.mp3'

	xml = '''
		<Response>
			<Play>%s</Play>
			<Redirect>%s/callin</Redirect>
		</Response>
		  ''' % (message, IP)

	return HttpResponse(xml, mimetype="text/xml")

@csrf_exempt
@require_http_methods(["POST"])
def play(request):
	# Todo - make this so we don't need to get them all
	songs = Songs.objects.all()
	song = choice(songs)

	xml = '''
		<Response>
			<Gather action="/play">
				<Play>%s</Play>
			</Gather>
			<Redirect>%s/play</Redirect>
		</Response>
		  ''' % (song.url, IP)

	return HttpResponse(xml, mimetype="text/xml")
