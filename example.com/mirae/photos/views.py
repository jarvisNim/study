from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from django.shortcuts import get_object_or_404

# Create your views here.

def hello(req):
    return HttpResponse('Hello there.')

def index(req):
    return HttpResponse('Home Page.')

def detail(req,photo_id):
    try:
        #photo = Photo.objects.get(pk=photo_id)
        photo = get_object_or_404(Photo,pk=photo_id)
    except Photo.DoesNotExist:
        return HttpResponse("사진이 없습니다.")

    msg = (
        '<p>{}번 사진 보여줄께요.</p>'.format(pk=photo_id),
        '<p>주소는 {url}</P>'.format(url=photo.image.url),
        '<p><img src="{url}" /></p>'.format(url=photo.image.url),
    )
    return HttpResponse('\n'.join(msg))
