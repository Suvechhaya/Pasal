from django.shortcuts import render
from contact.models import Contact

# def showContact(request):
#     return render(request,"contact/contact.html")

def contactForm(request):
    if request.method == "GET":
        return render(request, 'contact/contact.html')
    elif request.method== "POST":
        try:
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            contact = Contact(name=name, email=email,subject=subject, message=message)
            contact.save()
            print("name = " + name)
            return render(request, 'contact/contact.html', {'success' : True})
        except Exception as e:
            print("error in request")
            return  render(request, 'contact/contact.html', {'success': False})

