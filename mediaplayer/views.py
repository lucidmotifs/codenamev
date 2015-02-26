from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the MediaPlayer index.")


def play(request, video_id):
	response = "You're watching the video %s."
	return HttpResponse(response % video_id)