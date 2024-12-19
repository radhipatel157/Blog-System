from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import login,Blog
from django.views.decorators.cache import never_cache
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = login.objects.get(email=email)
            if user.passw == password:
                # Create a session for the user
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                messages.success(request, 'Login successful!')
                return redirect('index')
            else:
                messages.error(request, 'Invalid login credentials. Please try again.')
        except login.DoesNotExist:
            messages.error(request, 'Invalid login credentials. Please try again.')
        
        return redirect('login_view')
    return render(request, 'login.html')

def signup(request):
     if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if login.objects.filter(email=email).exists():
            messages.error(request,'this email already exits')
            return redirect('signup')
        user=login(email=email,passw=password)
        user.save()
        request.session['user_id'] = user.id
        request.session['user_email'] = user.email
        messages.success(request, 'Signup successful!')
        return redirect('index')
     return render(request, 'signup.html')
@never_cache
def logout_view(request):
    auth_logout(request)
    request.session.flush() 
    messages.success(request, 'You have been logged out.')
   
    return redirect('login_view')


def save_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            try:
                
                user_email = request.session.get('user_email')
                if not user_email:
                    messages.error(request, 'User is not logged in.')
                    return redirect('login_view')
                
                
                user = login.objects.get(email=user_email)
                
                new_blog = Blog(user=user, title=title, content=content)
                new_blog.save()
                messages.success(request, 'Your blog has been successfully submitted!')
                return redirect('save_blog')  
            except login.DoesNotExist:
                messages.error(request, 'User does not exist.')
        else:
            messages.error(request, 'Title and content are required.')

    return render(request, 'index.html')

def saved_blog(request):
    # Ensure the user is logged in
    if 'user_email' not in request.session:
        messages.error(request, 'You need to log in to view your saved blogs.')
        return redirect('login_view')
    
    try:
        # Retrieve the logged-in user
        user_email = request.session.get('user_email')
        user = login.objects.get(email=user_email)
        
        # Fetch blogs for the logged-in user
        mydata = Blog.objects.filter(user=user)
        
        return render(request, 'saved_blog.html', {'res': mydata})
    except login.DoesNotExist:
        messages.error(request, 'User not found.')
        return redirect('login_view')

def edit_blog(request,blog_id):
     user_email = request.session.get('user_email')
     user = login.objects.get(email=user_email)
     blog = get_object_or_404(Blog, id=blog_id, user=user)
     if request.method == "POST":
        blog.title = request.POST.get('title')
        blog.content = request.POST.get('content')
        blog.save()
        return redirect('saved_blog')  
     return render(request, 'edit_blog.html', {'blog': blog})

def delete_blog(request,blog_id):
    user_email = request.session.get('user_email')
    user = login.objects.get(email=user_email)
    blog = get_object_or_404(Blog, id=blog_id, user=user)
    if request.method == "POST":
        blog.delete()
        return redirect('saved_blog')  
    return render(request, 'delete_blog.html', {'blog': blog})