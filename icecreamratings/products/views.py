from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


# def home(request):
#     return render(request,'home.html')


class home(View):
    

    def get(self,request,*args, **kwargs):

        return HttpResponse("Hello")



class about_us(TemplateView):

    template_name = 'about.html'




    
