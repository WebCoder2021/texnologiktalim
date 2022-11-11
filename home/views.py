from django.http import HttpResponse
from django.shortcuts import render
from news.models import Event,Post
from modul.models import Module
from .models import Books, InternetResources, Questionnaire, VideoCategory, VideoLessons
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
    context['modules'] = Module.objects.all().order_by('order')
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


def about(request):
    context = {}
    context['modules'] = Module.objects.all().order_by('order')
    return render(request,'about.html',context)
def contact(request):
    context = {}
    context['modules'] = Module.objects.all().order_by('order')
    return render(request,'contact.html',context)

def library(request):
    context = {}
    context['modules'] = Module.objects.all().order_by('order')
    context['books'] = Books.objects.all()
    return render(request,'library.html',context)
def resurs(request):
    context = {}
    context['modules'] = Module.objects.all().order_by('order')
    context['resurs'] = InternetResources.objects.all()
    return render(request,'resurs.html',context)
def video_lesson(request):
    context = {}
    context['modules'] = Module.objects.all().order_by('order')
    context['videos_category'] = VideoCategory.objects.all()
    return render(request,'video_lesson.html',context)