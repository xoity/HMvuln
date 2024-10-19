# HMvuln
HACK ME vulnerable application!

An app built with django that uses postgresql to make an easily hackable app. 

# How to Start

first enter the "mysite" directory and run:

`python manage.py runserver`

then visit: 

`http://localhost:8000/polls/vulnerable/`

from there you can give it some questions and it will return to you the database entry of that question, try this out!:

`http://localhost:8000/polls/vulnerable/?q=Is%20Django%20cool?`

now you can begin testing using ZAP, burp and more!

# Contributions

we are open to any form of contributions and help towards creating something that a django app shouldnt be!
