from django.shortcuts import render
from .models import *
# Create your views here.
def test(request):
    context = {}
    context['tests'] = TestQuestion.objects.all()
    context['old_results'] = UserTestResult.objects.filter(user=request.user)
    if request.method == 'GET':
        start = request.GET.get('start',False)
        if start:
            context['start'] = True
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