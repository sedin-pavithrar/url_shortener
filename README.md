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



1. Web Frontend (Browser Links)
Home Page (URL Shortener Form): http://localhost:8000/
Dashboard (Manage URLs & Statistics): http://localhost:8000/dashboard/
Short URL Redirect Link: http://localhost:8000/<short_code>

2. REST API Endpoints
All API endpoints are under the /api/ prefix:

Create Short URL
URL: POST http://localhost:8000/api/shorten
Payload Format:
json
{
  "url": "https://www.example.com/some/long/url"
}
Retrieve Short URL Information

URL: GET http://localhost:8000/api/shorten/<short_code>

Update Short URL
URL: PUT http://localhost:8000/api/shorten/<short_code>
Payload Format:
json
{
  "url": "https://www.example.com/some/updated/url"
}
p
Delete Short URL
URL: DELETE http://localhost:8000/api/shorten/<short_code>
Get URL Statistics
URL: GET http://localhost:8000/api/shorten/<short_code>/stats
12:02 AM
