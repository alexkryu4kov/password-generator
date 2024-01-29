# Password Generator

The system to generate and store passwords for different websites

# Use Case

Registration on new website requires a password. 
It's much more safe to separate passwords for different resources and generate a new one for new registration.
This app allows to generate passwords for specific site based on such criterias: length, are symbols/numbers/upper case required

Also, you can get list of all passwords for your websites

# Safety Concerns

Passwords stores as hashes in database and 'master-password' is using for decode them. 
'master-password' NEVER EVER saved anywhere and even doesn't send to backend part, 
so no risks to lost it during http request. It uses strictly on browser side

# Technologies

Flask (+gunicorn)
Vanilla JavaScript for password generation
MySQL for storing the passwords

# How to run

Set environment variables for .env file - look at env.example
docker build -t password_app && docker run -p 5000:5000 password_app

# Plans

Make a simple interface for users to access for their passwords