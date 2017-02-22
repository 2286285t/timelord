from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from timelord.forms import UserForm, UserAccountForm
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    context_dict = {'boldmessage': "manage time"}
    return render(request, 'timelord/index.html', context=context_dict)
    #return HttpResponse("Hi there<br /><a href='/timelord/login/'>Login</a>")

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserAccountForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserAccountForm()

    return render(request,
                  'timelord/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'timelord/timetable.html', {'username': username})
                #return HttpResponseRedirect(reverse('timetable'))
            else:
                return HttpResponse("Your Timelord account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'timelord/login.html', {})

@login_required
def timetable(request):
    context_dict = {'boldmessage': "manage time"}
    return render(request, 'timelord/timetable.html', context=context_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


