# HMvuln - SQLite Injection Challenge

A deliberately vulnerable Django application designed to teach SQL injection techniques in a safe and controlled environment. This application simulates a CTF (Capture The Flag) style challenge similar to those found on TryHackMe or HackTheBox.

## Disclaimer

``` bash
This application is intentionally vulnerable for educational purposes only. Do not deploy this in a production environment or on a publicly accessible server.
```

## Challenge Overview

This application contains multiple intentional vulnerabilities that allow you to:

- SQL Injection: Extract hidden data from the database and discover hidden tables
- Local File Inclusion (LFI): Access sensitive system files through path traversal
- Command Injection: Execute arbitrary system commands on the server
- Find multiple flags to complete the challenge

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

6. Access the vulnerable applications at:

   ```bash
   http://localhost:8000/polls/vulnerable/  # SQL Injection Challenge
   http://localhost:8000/polls/lfi/         # Local File Inclusion Challenge
   http://localhost:8000/polls/ping/        # Command Injection Challenge
   ```

## Challenge Goals

### SQL Injection Challenge

1. Find a way to exploit the SQL injection vulnerability
2. Enumerate the database schema to discover hidden tables
3. Extract the flag from the hidden table
4. Submit the flag (format: FLAG{...})

### Local File Inclusion Challenge

1. Exploit the file inclusion vulnerability to access sensitive system files
2. Try to access the application's configuration files to find credentials
3. Find a way to read the database file directly
4. Discover the hidden flag file on the system

### Command Injection Challenge

1. Bypass the ping functionality to execute arbitrary system commands
2. Enumerate the server's file system and users
3. Discover environment variables and configuration details
4. Find the hidden flag in the server's file system

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

## Contributions

Contributions are welcome! If you'd like to improve the challenges, fix bugs, or add new features:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
