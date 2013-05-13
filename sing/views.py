from sing.models import *
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import logging

logger = logging.getLogger(__name__)
IP = 'http://71.190.160.148:5000'

@require_http_methods(["GET"])
def view(request):
	songs = Songs.objects.all().order_by('-created')

	return render_to_response('main.html', {'songs': songs})

@csrf_exempt
@require_http_methods(["POST"])
def callin(request):
	xml = '''
		<Response>
			<Gather action="/stepone" finishOnKey="12">
				<Say>Hello. Thanks for calling stranger.</Say>
		    	<Say>Press one to record a song.</Say>
	        	<Say>Press two and listen to a song.</Say>
    		</Gather>
    		<Redirect>%s</Redirect>
		</Response>
	      ''' % (IP)

	return HttpResponse(xml, mimetype="text/xml")

@csrf_exempt
@require_http_methods(["POST"])
def stepone(request):
	digits = request.POST.get('Digits')

	if digits == '1':
		xml = '''
			<Response>
				<Say>Press any key to stop recording.</Say>
				<Record action="/record" playBeep="true" />
			</Response>
			  '''

	elif digits == '2':
			xml = '''
				<Response>
					<Redirect>%s/play</Redirect>
				</Response>
				  ''' % (IP)

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

	xml = '''
		<Response>
			<Say>Thanks!</Say>
			<Redirect>%s/callin</Redirect>
		</Response>
		  ''' % (IP)

	return HttpResponse(xml, mimetype="text/xml")

@csrf_exempt
@require_http_methods(["POST"])
def play(request):
	# Todo - make this so we don't need to get them all
	songs = Songs.objects.all()
	song = choice(songs)

	xml = '''
		<Response>
			<Play>%s</Play>
			<Redirect>%s/callin</Redirect>
		</Response>
		  ''' % (song.url, IP)

	return HttpResponse(xml, mimetype="text/xml")
