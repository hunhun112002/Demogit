from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Question
# Create your views here.




def index(request):
    taisan = ["dien thoai","dong ho ","xe may", "may tinh"] 
    context = {"taisan": taisan }
    return render(request, "polls/index.html" , context) 

def viewlist(request):
    list_questions = Question.objects.all()
    context  = {"dsquest": list_questions}
    return render(request, "polls/question_list.html", context)


def viewsdetail(request, question_id):
    q= Question.objects.get(pk=question_id)
    return render(request , "polls/viewsdetail.html", {"qs": q}) 








