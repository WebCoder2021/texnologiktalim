from django.shortcuts import render
from .models import *
# Create your views here.
def test(request):
    context = {}
    context['tests'] = TestQuestion.objects.all()
    print('test')
    if request.method == "POST":
        print('post')
        for test in TestQuestion.objects.all():
            print(request.POST.get(str(test.id),False)) 

    return render(request,'test/test.html',context)