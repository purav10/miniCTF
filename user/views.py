from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.views.decorators.csrf import csrf_exempt

  
@csrf_exempt
#################### index#######################################
def index(request):
    return render(request, 'user/index.html', {'title':'index'})
  
########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to Login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'register here'})
  
################ login forms###################################################
@csrf_exempt 
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        # user = authenticate(request, username = username, password = password)
        str = 'N0tSoE#5Y'
        if(username != 'admin'):
            messages.info(request, f'Username is not admin')
            return render(request, 'user/login.html', {'form':AuthenticationForm(), 'title':'Login'})
        elif(len(password) != 9):
            messages.info(request, f'Length of password is not 9')
            return render(request, 'user/login.html', {'form':AuthenticationForm(), 'title':'Login'})
        elif(password != str):
            for i in range(9):
                if(str[i] != password[i]):
                    messages.info(request, f'Password at {i} index is incorrect')
                    return render(request, 'user/login.html', {'form':AuthenticationForm(), 'title':'Login'})



        else :
            # form = login(request, user)
            messages.success(request, f"flag{{L3aky_Err0r_M355age5}}")
            return render(request, 'user/login.html', {'form':AuthenticationForm(), 'title':'Login'})
    #     else:
    #         messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'Login'})