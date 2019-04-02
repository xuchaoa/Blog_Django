from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .forms import ImageForm
from .models import Image
from django.conf import settings
import os

@login_required(login_url='/account/login/')
@csrf_exempt
@require_POST
def upload_image(request):
    form = ImageForm(data=request.POST)
    if form.is_valid():
        try:
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()  #此时图片会被保存
            return JsonResponse({'status':"1"})
        except:
            return JsonResponse({'status':"0"})


@login_required(login_url='/account/login/')
def list_images(request):
    images = Image.objects.filter(user=request.user)
    return render(request,'image/list_images.html',{'images':images})


@login_required(login_url='/account/login/')
@csrf_exempt
@require_POST
def del_image(request):
    image_id = request.POST['image_id']
    try:
        image = Image.objects.get(id=image_id)
        base_path = settings.MEDIA_ROOT
        image_file = str(base_path)+str(image.image)
        if os.path.exists(image_file):
            os.remove(image_file)
        else:
            print('不存在文件')
        dir = image_file.rsplit('/',1)[0]
        if not os.listdir(dir):  #空文件夹则删除
            os.rmdir(dir)
        image.delete()
        return JsonResponse({'status':'1'})
    except:
        return JsonResponse({'status':2})

@login_required(login_url='/account/login/')
def falls_images(request):
    images = Image.objects.all()
    return render(request,'image/falls_images.html',{"images":images})

