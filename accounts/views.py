from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login , logout

@csrf_exempt
def signup_view(request):
  if request.method == 'POST':
    signupForm = UserCreationForm(request.POST)
    if signupForm.is_valid():
      user = signupForm.save()
      # log the user in
      login(request, user)
      return redirect('articles:list')
  else:
    signupForm = UserCreationForm()
  return render(request, 'accounts/signup.html', {'form': signupForm})

def login_view(request):
  if request.method == 'POST':
    loginForm = AuthenticationForm(data=request.POST)
    if loginForm.is_valid():
      # log in the user
      user = loginForm.get_user()
      login(request, user)
      if 'next' in request.POST:
        return redirect(request.POST.get('next'))
      else:
        return redirect('articles:list')
  else:
    loginForm = AuthenticationForm()
  return render(request, 'accounts/login.html', {'login_Form': loginForm})

def logout_view(request):
  if request.method == 'POST':
    logout(request)
    return redirect('articles:list')