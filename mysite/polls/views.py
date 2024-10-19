
from django.http import HttpResponse
from django.db import connection



def vulnerable_query(request):
    question_text = request.GET.get('q', '')
    query = f"SELECT * FROM polls_question WHERE question_text = '{question_text}'"
    
    with connection.cursor() as cursor:
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except Exception as e:
            result = str(e)
    
    return HttpResponse(result)
'''
from django.shortcuts import render
from django.http import HttpResponse

def vulnerable_query(request):
    user_input = request.GET.get('q', '')
    
    return render(request, 'polls/vulnerable.html', {'user_input': user_input})
'''

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
