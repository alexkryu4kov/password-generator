# Password Generator

A system to generate and store passwords for different websites

# Use Case

When registering on a new website, a password is required.   
It's much safer to use separate passwords for different resources and to generate a new one for each registration.   
This app allows the generation of passwords for a specific site   
based on criteria such as length, and the inclusion of symbols, numbers, and uppercase letters.

Additionally, you can retrieve a list of all your passwords for various websites.

# Safety Concerns

Passwords are stored as hashes in the database, and a 'master password' is used to decode them.  
The 'master password' is NEVER saved anywhere and is not transmitted to the backend,   
so there's no risk of losing it during an HTTP request.   
It is used strictly on the browser side.

# Technologies

Flask (with Gunicorn)
Vanilla JavaScript for password generation
MySQL for storing passwords

# How to run

Set environment variables according to the .env file (see env.example).
docker-compose up --build

# Plans

Develop a simple interface for users to access their passwords