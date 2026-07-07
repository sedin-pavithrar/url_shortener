Development Plan

Phase 1 – Setup
Create Django project
Create shortener app
Configure templates and static files
Create the ShortURL model
Run migrations
Register the model in the admin
created superuser

Phase 2 – URL Creation
Build a form to accept a URL
Validate the URL
Generate a unique short code
Save it to the database

Phase 3 – Redirect
Look up the short code
Increment the click count
Redirect using Django's redirect() function

Phase 4 – Dashboard
Display all shortened URLs
Show:
Original URL
Short URL
Click count
Creation date

Phase 5 – Update & Delete
Edit the original URL
Delete a short URL

Phase 6 – Enhancements
Search
Pagination
Custom aliases
QR code generation
Expiration dates
User login (so each user manages only their own links)

User enters
        │
        ▼
https://www.google.com/maps
        │
        ▼
Generate a unique short code
        │
        ▼
aB3xY9
        │
        ▼
Save both values to the database
        │
        ▼
Display the shortened URL