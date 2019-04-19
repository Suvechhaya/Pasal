from django.http import HttpResponse
from django.shortcuts import render


from register.models import Register, Login


def registerForm(request):
    print('hello')

    if request.method == "GET":
        return render(request, 'register/register.html')
    elif request.method== "POST":
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm-password']
            print(username)
            register = Register(username=username, email=email, password=password,confirm_password=confirm_password)
            register.save()

            print("name = " + username)
            # context = {
            #     'message': 'Registered successfully.Please log in'
            # }
            return render(request, 'register/register.html')
        except Exception as e:
            print("error in request")
            return  render(request, 'register/register.html', {'success': False})


def loginForm(request):
    if request.method == "GET":
        return render(request, 'register/register.html')
    elif request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
            #remember = request.POST['remember']
            user = Register.objects.get(username=username, password=password)
            return render(request, 'categories/categories.html', {'success': True, 'user': user})
            #return HttpResponse('logged in')

            #return render(request,'register/register.html')
        except Register.DoesNotExist:
            return HttpResponse('Please register first.')
            return render(request, 'register/register.html', {'success': False})


