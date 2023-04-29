from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    return render(request, 'daarulhalaalapp/index.html')

def course_registration(request):
    if request.method == 'POST':
        html = render_to_string('daarulhalaalapp/email_template.html', {
            'Phone_Number': request.POST['number'],
            'First_Name': request.POST.get('first-name'),
            'Middle_Name': request.POST.get('middle-name'),
            'Last_Name': request.POST.get('last-name'),
            'Country': request.POST.get('country'),
            'City': request.POST.get('city'),
            'Course': request.POST.get('courses'),
        })
        send_mail(
                'Course registration',
                'Course registration',
                request.POST.get('email'),
                ['DarulHalaalmadrasah@gmail.com'],
                html_message=html)
        return render(request, 'daarulhalaalapp/success.html')
    else:
        return render(request, 'daarulhalaalapp/register.html')
    
def about_view(request):
    return render(request, 'daarulhalaalapp/about.html')