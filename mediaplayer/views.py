from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from mediaplayer.models import Video, Comment
from datetime import datetime

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


def comment(request, video_id):
	video = get_object_or_404(Video, pk=video_id)
	try:
		comment_text = request.POST['comment']
	except (KeyError, Video.DoesNotExist):
		# Display error message
		return render(request, 'mediaplayer/player.html', {'video': video, 'error_message': "You didn't select a choice."})
	else:
		c = Comment()
		c.text = comment_text
		c.video = video
		c.created = datetime.datetime.now()
		c.modified = datetime.now()
		c.save()
		return HttpResponseRedirect(reverse('mc:play', args=(video.id,)))
