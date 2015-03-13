from django.http import HttpResponse, Http404
from django.shortcuts import render
from mediaplayer.models import Video

def index(request):
	video_list = Video.objects.order_by('-pub_date')[:5]
	context = {'video_list': video_list}

	return render(request, 'mediaplayer/index.html', context)


def play(request, video_id):
	try:
		video = Video.objects.get(pk=video_id)
	except Video.DoesNotExist:
		raise Http404("Video does not exist")

	return render(request, 'mediaplayer/player.html', {'video': video})