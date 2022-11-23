from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
# # def demo(request):
# #     return HttpResponse("<h1>Enter ur Values</h1>")
# # def home(request):
# #     return render(request, 'home.html')
# # def contact(request):
# #     return render(request, 'contact.html')
# # def thanks(request):
# #     return render(request, 'thanks.html')
# # def about(request):
# #     return HttpResponse("HELLO....THIS IS ABOUT Pge")
# # def details(request):
# #     return HttpResponse("HELLO...THIS IS DETAILS PAGE")
#
#
#
#
# def math(request):
#     return render(request,'home.html')
# def math1(request):
#     x=int(request.GET['n1'])
#     y=int(request.GET['n2'])
#     addi=x+y
#     subt=x-y
#     mult=x*y
#     divi=x/y
#     return render(request,'result.html',{'add':addi,'sub':subt,'mul':mult,'div':divi})
# from django.http import HttpResponse
# from django.shortcuts import render
# # Create your views here.
from . models import Team


def demo(request):
    obj=Team.objects.all()
    return render(request,"index.html",{"result":obj})
