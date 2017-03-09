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

def about(request):
    response = render(request, 'timelord/about.html')
    return response

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
                #return render(request, 'timelord/timetable.html', {'username': username})
                return HttpResponseRedirect(reverse('timetable'))
            else:
                return HttpResponse("Your Timelord account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'timelord/login.html', {})

@login_required
def timetable(request, user_name):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # TODO  un comment once we have timetable items model
    # try:
        # Try to find timetable items for given user
        # timetable_items = TimetableItem.objects.filter(owner = user_name)

    # TODO uncomment once we have models
    # context_dict = {'boldmessage': "manage time", 'days': days, 'timetable_items': timetable_items}
    context_dict = {'boldmessage': "manage time", 'days': days}
    print context_dict
    return render(request, 'timelord/timetable.html', context=context_dict)

@login_required
def view_account(request):
    response = render(request, 'timelord/account.html')
    return response

@login_required
def create_task(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        # Check that form is valid
        if form.is_valid():
            # Save the new timetable item to the database
            form.save(commit=True)
            # Redirect user to index page
            return index(request)
        else:
            # The supplied form contains errors, print to terminal
            print(form.errors)

    return render(request, 'timelord/create_task.html', {'form': form})

@login_required
def edit_task(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return edit_task(request)
        else:
            print(form.errors)

    return render(request, 'timelord/edit_task.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def edit_categories(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return edit_categories(request)
        else:
            print(form.errors)

    return render(request, 'timelord/edit_categories.html')


