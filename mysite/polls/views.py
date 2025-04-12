
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
import subprocess


def command_injection(request):
    hostname = request.GET.get('hostname', '')
    output = None
    
    if hostname:
        try:
            # Intentionally vulnerable - command injection
            # User input is directly passed to a shell command without sanitization
            command = f"ping -c 1 {hostname}"
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            output = e.output
    
    return render(request, 'polls/command_injection.html', {
        'hostname': hostname,
        'output': output
    })


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

def lfi_vulnerable(request):
    file_path = request.GET.get('file', '')
    content = None
    error = None
    
    if file_path:
        try:
            # Intentionally vulnerable - no path validation or sanitization
            # This allows path traversal and reading any file on the system
            with open(file_path, 'r') as f:
                content = f.read()
        except Exception as e:
            error = str(e)
    
    return render(request, 'polls/lfi.html', {
        'file_path': file_path,
        'content': content,
        'error': error
    })

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
