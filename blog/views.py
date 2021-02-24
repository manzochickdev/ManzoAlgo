from django.shortcuts import render
from django.http import HttpResponse

#https://www.youtube.com/watch?v=1PkNiYlkkjo&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=4

posts = [
    {
        'author':'Anh Pham Tuan',
        'title':'About',
        'content':'Professional Algo Trader',
        'date_posted':'02/22/2021'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context=context)

def about(request):
    return render(request,'blog/about.html')

