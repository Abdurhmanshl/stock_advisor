from django.http import HttpResponse

def home(request):
    return HttpResponse("مرحباً في المستشار المالي")
