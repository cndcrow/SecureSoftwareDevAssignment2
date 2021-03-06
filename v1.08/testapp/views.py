from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, UserManager
from testapp.forms import register_form

def index(request):
    context = RequestContext(request)

    user_list = User.objects.order_by('first_name')
    list = {'list': user_list}

    return render_to_response('testapp/index.html', list, context)

def about(request):
    context = RequestContext(request)
    context_dict = {'message': "IM ALL ABOUT KIBA!!!"}
    return render_to_response('testapp/about.html', context_dict, context)

def addUser(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
	form = register_form(request.POST)

        if form.is_valid():
            user = form.save()

            user.set_password(form.passwd)
            user.save()
            registered = True

        else:
            print form.errors

    else:
        form = register_form()

    return render_to_response(
            'testapp/register.html', {'register_form': register_form}, context)

def login(request):
	
    context = RequestContext(request)
    form = register_form()
    #return render_to_response('testapp/login.html', {'form': form}, context)
    
    if request.method =='POST':

	email=request.POST['email']
	password=request.POST['passwd']

	user = authenticate(username=email, password=password)

	if user:
	    if user.is_active:
		login(user)
		return HttpResponse('working')
        else:
	    return HttpResponse('borked')

    return render_to_response('testapp/login.html', {'form': form}, context)

