from django.http import HttpResponse
from django.shortcuts import render
from news.models import Event,Post
from .models import Questionnaire
# Create your views here.
def home (request):
    events = Event.objects.all().order_by('-created')[:6]
    posts = Post.objects.all().order_by('-created')[:4]
    questionnaire = Questionnaire.objects.filter(publish=True).first()
    context = {
        'events':events,
        'posts': posts,
        'questionnaire': questionnaire,

    }
    if request.method == 'POST':
        q = request.POST.get('q',False)
        print(questionnaire.res1)
        if q:
            if q == questionnaire.ans1:
                questionnaire.res1 +=1 
            elif q == questionnaire.ans2:
                questionnaire.res2 +=1
            elif q == questionnaire.ans3:
                questionnaire.res3 +=1
            elif q == questionnaire.ans4:
                questionnaire.res4 +=1
            elif q == questionnaire.ans5:
                questionnaire.res5 +=1
            elif q == questionnaire.ans6:
                questionnaire.res6 +=1
            questionnaire.save()
            
    return render(request,'index.html',context)


def library(request):
    return render(request,'library.html')
def resurs(request):
    return render(request,'resurs.html')
def video_lesson(request):
    return render(request,'video_lesson.html')