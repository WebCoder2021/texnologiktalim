from django.shortcuts import render
from .models import *
# Create your views here.
def test(request):
    context = {}
    context['tests'] = TestQuestion.objects.all()
    if request.method == "POST":
        result = UserTestResult.objects.create(user=request.user)
        for test in TestQuestion.objects.all():
            print(test.id,request.POST.get(str(test.id),False))
            ts = UserTest.objects.create(question_id=int(test.id),answer_id=int(request.POST.get(str(test.id),False))) 
            ts.save()
            
            result.tests.add(ts)
            result.save()
            context['result'] = result
            

    return render(request,'test/test.html',context)