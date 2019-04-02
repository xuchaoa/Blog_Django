from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegisterForm,UserProfileForm,UserForm,UserInfoForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile,UserInfo
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.


def user_login(request):
    # next = request.GET.get('next','')
    print(next)
    if request.method == "POST":

        login_form = LoginForm(request.POST)    #request.POST  或者 request.GET都是字典类对象，可以用request.GET.get('name')  获取value
        if login_form.is_valid():  #判断是否合法
            dic_user = login_form.cleaned_data  #返回from表单提交的字典类型
            user = authenticate(username = dic_user['username'],password = dic_user['password'])  #判断用户名密码返回user对象，否则None
            if user:
                login(request,user)  #真正的登陆，生成session
                # return HttpResponse('login successfully')
                if next == '':
                    # return HttpResponseRedirect(reversed('blog:blog_title'))
                    return HttpResponse("successfully")
                else:
                    # return HttpResponseRedirect(next)
                    return HttpResponse(str(next))
            else:
                return HttpResponse('username or password is not right')

        else:
            return HttpResponse('invalid login')

    if request.method == 'GET':
        login_form = LoginForm()
        return render(request,'account/login2.html',{'form':login_form})


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() & userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            UserInfo.objects.create(user=new_user)  #同时在account_userinfo表中写入信息
            return HttpResponseRedirect(reverse('account:auth_login'))
        else:

            return HttpResponse('sorry')
    else:
        user_form = RegisterForm()
        userprofile_form = UserProfileForm()
        return render(request,"account/register.html",{'form':user_form,'profile':userprofile_form})

@login_required(login_url='account/login/')
def myself(request):
    # print(dir(request.user))
    userprofile = UserProfile.objects.get(user=request.user) if hasattr(request.user,
                                                                        'userprofile') else UserProfile.objects.create(user=request.user)
    # HttpRequest.user实际上是由一个定义在django.contrib.auth.models 中的  user model  类  所创建的对象。
    # 该类有许多字段，属性和方法,详细属性见数据库
    # 与user关联的数据库account_profile有则直接使用，没有则新创建关联
    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user,
                                                                  'userinfo') else UserInfo.objects.create(user=request.user)
    return render(request, "account/myself.html",
                  {"user": request.user, "userinfo": userinfo, "userprofile": userprofile})


@login_required(login_url='/account/login/')
def myself_edit(request):
    userprofile = UserProfile.objects.get(user=request.user) if hasattr(request.user,'userprofile') else UserProfile.objects.create(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user,'userinfo') else UserProfile.objects.create(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST)  #eamil
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid() & userinfo_form.is_valid() & userprofile_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            request.user.email = user_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']
            userinfo.school = userinfo_cd['school']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['profession']
            userinfo.address = userinfo_cd['address']
            userinfo.aboutme = userinfo_cd['aboutme']
            request.user.save()
            userprofile.save()
            userinfo.save()
        return HttpResponseRedirect('/account/my_information')

    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={'birth':userprofile.birth,
                                                    'phone':userprofile.phone})
        userinfo_form = UserInfoForm(initial={'school':userinfo.school,
                                                    'company':userinfo.company,
                                                    'profession':userinfo.profession,
                                                    'address':userinfo.address,
                                                    'aboutme':userinfo.aboutme})
        return render(request,'account/myself_edit.html',{'user_form':user_form,
                                                          'userprofile_form':userprofile_form,
                                                          'userinfo_form':userinfo_form})


def my_image(request):
    if request.method == 'POST':
        img = request.POST['img']
        print(request.user)
        print(request.user.id)
        userinfo = UserInfo.objects.get(user_id=request.user.id)  #勘误
        userinfo.photo = img
        userinfo.save()
        return HttpResponse('1')
    else:
        return render(request,'account/imagecrop.html')

