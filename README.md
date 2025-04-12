# HMvuln - SQLite Injection Challenge

A deliberately vulnerable Django application designed to teach SQL injection techniques in a safe and controlled environment. This application simulates a CTF (Capture The Flag) style challenge similar to those found on TryHackMe or HackTheBox.

## Challenge Overview

This application contains intentional SQL injection vulnerabilities that allow you to:

- Extract hidden data from the database
- Discover hidden tables
- Find the flag to complete the challenge

**Difficulty**: Medium

## Prerequisites

- Python 3.8 or higher
- Django 4.0 or higher

## Setup Instructions

1. Clone this repository:

   ``` bash
   git clone https://github.com/yourusername/HMvuln.git
   cd HMvuln
   ```

2. Install required packages:

   ``` bash
   pip install -r requirements.txt
   ```

   (or simply install Django if requirements.txt is missing: `pip install django`)

3. Navigate to the mysite directory:

   ``` bash
   cd mysite
   ```

4. Set up the database and seed it with vulnerable data:

   ```bash
   python manage.py migrate
   python manage.py seed_db
   ```

5. Start the development server:

   ``` bash
   python manage.py runserver
   ```

6. Access the vulnerable application at:

   ``` bash
   http://localhost:8000/polls/vulnerable/
   ```

## Challenge Goals

1. Find a way to exploit the SQL injection vulnerability
2. Enumerate the database schema to discover hidden tables
3. Extract the flag from the hidden table
4. Submit the flag (format: FLAG{...})

## Hints

- The application is vulnerable to SQLite injection, which has slightly different syntax than MySQL or PostgreSQL
- Try basic SQL injection techniques first (quotes, comments, UNION statements)
- Explore the SQLite system tables to discover all tables in the database
- Remember that most SQL injection cheat sheets focus on MySQL, so you may need to adapt the techniques for SQLite

## Example Attack Path

1. Test for basic injection with: `' OR '1'='1`
2. Enumerate tables with: `' UNION SELECT name, NULL FROM sqlite_master WHERE type='table' --`
3. Further explore discovered tables and extract the flag

## Tools to Use

- Burp Suite (Community Edition is sufficient)
- OWASP ZAP
- SQLmap (though manual exploitation is recommended for learning)

## Educational Resources

- [OWASP SQL Injection Guide](https://owasp.org/www-community/attacks/SQL_Injection)
- [SQLite Injection Cheat Sheet](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md)
- [PortSwigger SQL Injection Tutorial](https://portswigger.net/web-security/sql-injection)

## Disclaimer

This application is intentionally vulnerable for educational purposes only. Do not deploy this in a production environment or on a publicly accessible server.

## Contributions

Contributions are welcome! If you'd like to improve the challenges, fix bugs, or add new features:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
