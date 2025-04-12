
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection


def vulnerable_query(request):
    user_input = request.GET.get('q', '')
    result = None
    
    if user_input:
        # Intentionally vulnerable SQL query construction
        query = f"SELECT * FROM polls_question WHERE question_text LIKE '%{user_input}%'"
        
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                result = cursor.fetchall()
            except Exception as e:
                result = str(e)
    
    return render(request, 'polls/vulnerable.html', {'user_input': user_input, 'result': result})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
