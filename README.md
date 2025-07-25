## FIFTH TASTE
### Contents

1. [Project Overview](#project-overview)
2. [Rationale](#rationale)
3. [Planning](#planning)
4. [Schema](#schema)
5. [Key Features](#key-features)
6. [Security Features](#security-features)
7. [Deployment](#deployment)
8. [Testing](#testing)
9. [Credits](#credits)

<hr>

### Project Overview
Fifth Taste is a web-based restaurant booking system built using Django. The application allows users to reserve tables at restaurants, view restaurant details, and browse through available menus. Administrators can manage bookings, menus, and restaurants. The project is designed to enhance the dining experience by simplifying reservation processes for both customers and restaurant staff.

This project is intended for two primary groups:

### Restaurant Owners and Staff:

Restaurant owners and staff can manage their restaurant’s bookings, menus, and availability from a centralized dashboard.

In this application, both **owners** and **staff** users have identical access privileges - superusers. By implementing this approach, both owners and staff can efficiently manage the system without creating unnecessary barriers to accessing essential features or data. This is managed behind the scenes since the purpose of the website is not staff accounts - it is to showcase the restaurant to users, and allow them to book.

#### Customers:

Customers can check available time slots and make reservations directly from the website. Customers can also modify their booking details via the website.

<hr>

## Rationale

The primary goal of Fifth Taste is to streamline the process of making restaurant reservations and managing restaurant operations. 

- Providing Real-Time Availability: Customers can see the live availability of tables, reducing the chances of overbooking.
- Improving Restaurant Management: Restaurant owners can easily manage bookings, make adjustments to the menu, and track customer preferences.
- Customers get updated via website and email when their booking is changed/deleted. 

<hr>

## Planning
### Wireframe Design

To visualize the user interface (UI) and layout, I created a wireframe that helped to map out the structure and navigation of the application. This wireframe guided the design decisions throughout the development process, ensuring a user-friendly and organized experience.

You can view the wireframe design here: [Wireframe](https://wireframe.cc/U0hQ3v)

I only briefly planned the homepage as I knew the other pages would use the same header and footer and mostly follow form structures.

I knew I wanted to have 4 pages: 
1. Homepage with a jumbotron image and general info
2. Menu with dropdown sections for each course and some images to entice customers
3. Bookings page
4. Contact form 

### Lucidchart Planning Document

In addition to the wireframe, I thought about the structure of the project, since this was my first solo project using Django. I used Lucidchart to consider the data models and applications of the project. Whilst I diverted from the architecture slightly, this was extremely useful when creating my models as it allowed me to see the relationship between each table.

You can access the initial planning document here: [Lucidchart Planning Document](https://lucid.app/lucidchart/0c964fbb-9e59-4619-bf1c-b4e3ecfff5bb/edit?invitationId=inv_ecf3eb04-4041-4568-b217-d5c48ca4a0b2)

### Agile
I used an agile framework throughout this project. Before starting, I created a [project board](https://github.com/users/emilywade/projects/9) with user stories and well-defined acceptance criteria. This helped me focus on delivering specific features. 

<hr>

## Schema
The data schema for this project consists of three primary models: `ContactRequest`, `Table`, and `Booking`. These models are designed to handle different aspects of the application, including user interactions, table management, and booking information. 

### ContactRequest Model

This model is used to store messages sent by users through the contact form. It captures the user's name, email, message content, and the date the request was created. It has no relationship to the other models.

- name: Stores the name of the user making the request.
- email: Stores the email address of the user making the request.
- message: Stores the content of the user's message.
- created_at: Automatically stores the date and time when the request was created.

### Table Model
The Table model is used to manage the restaurant's tables. Each table is identified by a unique table number and has a defined seating capacity. This is an independent model which is referenced in the Booking model.

- table_number: A unique integer representing the table's number.
- capacity: A positive integer representing the number of guests the table can accommodate.

### Booking Model
The Booking model is used to store reservation details made by users. It includes information about the booking, such as the table reserved, the user's name, email, date and time of booking, the number of guests, special requests, and the booking's duration. This model has a one-to-many relationship this the Table model: each Booking is linked to one specific Table, but a Table can be associated with multiple Bookings. 

- booking_id: A unique UUID identifier for each booking.
- user: Username for each customer, set by the user at registration and used to login. 
- table_number: A foreign key linking the booking to a specific table from the Table model.
- name: The name of the person who made the booking.
- email: The email address of the person who made the booking.
- date: The date of the booking.
- time: The time of the booking.
- num_guests: The number of guests for the booking.
- special_requests: A field for any special requests made by the person booking.
- created_at: Automatically stores the date and time when the booking was created.
- duration: The default duration of the booking, set to 2 hours.

<hr>

### Key Features
This project includes several key features designed to provide a seamless user experience for managing bookings and customer inquiries:

- CRUD Functionality: Users are able to Create, Read, Update, and Delete their bookings. This allows for flexibility in managing booking information.
- Booking Availability Check: The system checks table availability in real-time to ensure that no double bookings occur. Users can only select available tables for their desired date and time. 
- No Overlapping Bookings: The system prevents overlapping bookings for the same table at the same time, ensuring that each table is booked for only one group at any given time.
- Email Confirmation: Upon successful booking, users receive an email confirmation detailing their booking information, including the table number, date, time, and any special requests made. This helps confirm their reservation and reduces the chance of mistakes.
- Manage Booking: Users can easily manage their bookings by viewing, updating, or cancelling their reservation. A link to manage their booking is provided as part of the email confirmation. I didn't want users to have to create an account in order to book with us - this annoys me with other restaurant websites - so I used the unique booking_id to access booking details. 

### Security Features
1. CSRF Protection
   Cross-Site Request Forgery (CSRF) protection is enabled for all forms to prevent malicious requests.
   I actually learnt about this by accident - when debugging in this project I came across [this site](https://docs.djangoproject.com/en/5.1/howto/csrf/) which explained the importance of this.
2.  Admin Panel Access
   Admin panel access is restricted to superusers only. Each must have their own account.
3. Database security
   All sensitive data is stored in config vars within Heroku.
4. UUID
   I generated booking IDs automatically using Python's UUID module. I knew this was something I wanted to use from the beginning after reading about it on [Stack Overflow](https://stackoverflow.com/questions/1210458/how-can-i-generate-a-unique-id-in-python)

<hr>

### Deployment
This project has been deployed to Heroku for live use. Check it out [here](https://the-fifth-taste-b8ef5776e3a8.herokuapp.com/)
Below is a breakdown of the steps I took to deploy the application and connect it to a remote database.

#### Initial Project Setup
- Created a new local folder.
- Opened the folder in VS Code.
- Created a new GitHub repository (without a README).
- Copied the GitHub repo commands into the VS Code terminal to initialise and connect the local repo.
- Verified the repository was connected by refreshing it on GitHub.
- Created a virtual environment:
```
python3 -m venv .venv
```
- Created a .gitignore file and added .venv to it.
- Installed Django:
```
pip3 install Django~=4.2.1
```
- Generated a requirements.txt file:
```
pip3 freeze --local > requirements.txt
```
- Started the Django project:
```
django-admin startproject fifth_taste .
```
- Verified the server was running locally:
```
python3 manage.py runserver
```

#### Steps Taken to Deploy to Heroku
1. Logged in to Heroku and created a new app.
2. In the app’s Settings > Config Vars, added the following:
	○ Key: DISABLE_COLLECTSTATIC, Value: 1
3. Installed Gunicorn (WSGI server for deployment):
`pip3 install gunicorn~=20.1`
4. Updated requirements.txt again:
`pip3 freeze --local > requirements.txt`
5. Created a Procfile in the project root (same level as requirements.txt):
`web: gunicorn my_project.wsgi`
6. In settings.py, updated the ALLOWED_HOSTS:
`ALLOWED_HOSTS = ['.herokuapp.com', '127.0.0.1']`
7. Set DEBUG = False for production use.
8. Committed and pushed all changes to GitHub.
9. In Heroku dashboard:
	○ Clicked on Deploy tab.
	○ Connected the app to the GitHub repository.
	○ Deployed the branch via Deploy Branch button.
10. In the Resources tab:
	○ Refreshed the page.
	○ Selected Eco dyno.
	○ Checked for existing Heroku Postgres add-ons and deleted any automatically added ones.
11. Verified the deployed app by opening the live link.

#### Connecting to POSTGRES
• Temporarily set DEBUG = True in settings.py.
• Created an env.py file at the project root and added it to .gitignore.
• Inside env.py, added: 
```
import os
os.environ.setdefault("DATABASE_URL", "<your-database-url>")
```
• Installed required packages:
```
pip3 install dj-database-url~=0.5 psycopg2~=2.9
pip3 freeze --local > requirements.txt
```
• In settings.py, added the following to the top:
```
import os
import dj_database_url

if os.path.isfile('env.py'):
    import env
```
• Replaced the default DATABASES config with:
```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```
• Ran the migrations:
```
python3 manage.py migrate
```
• Created a superuser:
```
python3 manage.py createsuperuser
```
• Set DEBUG = False again.
• Committed and pushed changes to GitHub.
• Back in Heroku:
	• In Settings > Config Vars, added a new key:
		○ DATABASE_URL with the value from your PostgreSQL host.
	• If Heroku added a Postgres database by default, went to Resources and deleted it.
• Deployed branch again via the Deploy tab.
• Opened the app to verify that it was connected to the live database.

<hr>

### Testing
#### Validation
- Bootstrap's built-in form validation for client-side validation 
- Django's clean() method for server-side validation to ensure that the data entered by users is both accurate and secure before being saved to the database.
  

#### Manual Testing
##### Django Shell
The Django shell was used extensively during development to test the behavior of models, particularly:

- Booking creation and retrieval
- Table availability logic
- User associations with bookings

For example:
```
from bookings.models import Booking, Table
Booking.objects.create(...)
```

##### HTML, CSS & JavaScript Validation
HTML: Validated using `djhtml`
CSS: Validated using [W3C CSS Validator](https://validator.w3.org/)
JavaScript: Tested using browser console and [JSHint](https://jshint.com/) to catch syntax and logic issues

##### Manual Test Cases
| Feature | Test Steps | Expected Outcome | Actual Outcome |
| ------- | ---------- | ---------------- | -------------- |
| Booking creation (logged in) | Log in → Submit valid form |	Booking is saved and confirmation shown |	As expected	|
| Booking creation (not logged in) | Try to access booking page without logging in | Redirected to login page | As expected |
| Edit own booking | Log in → Go to booking page → Update form → Submit | Booking is updated | As expected	|
| Edit someone else’s booking | Log in as User A → Try to access User B's booking via URL | 404 error shown | As expected	|
| Delete booking | Submit deletion form for own booking | Booking is deleted and cancellation message shown | As expected	|
| Contact form submission | Fill form with valid inputs and submit | "Message sent" success message appears | As expected	|
| Register with existing email | Try to register using an existing account email | Error message shown | As expected	|
| Invalid email input | Submit form with invalid email format | Form displays validation error | As expected	|
| Table availability check | Try to book more guests than any table can hold | Error message "no available tables" | As expected	|

##### Edge Cases Tested
- Booking within overlapping time windows
- Booking when no tables are available
- Attempting to book for a past date/time
- Submitting incomplete or invalid forms
- Accessing another user's booking (blocked via permissions)

#### Automated Testing
- I used Django's TestCase to test models and forms. I used it to check my Booking views were interacting with the database correctly (bookings can be created, updated and deleted). I also used it to check the contact form was validating data correctly, saving valid data to the database and providing correct feedback when invalid data is entered. 
  
<hr>

### Credits
- Stack Overflow was definitely my friend in this project. Here are two examples I needed it for: [Django ORM filter](https://stackoverflow.com/questions/10040143/and-dont-work-with-filter-in-django) and [Specific fields from querysets](https://stackoverflow.com/questions/7503241/how-to-obtain-a-queryset-of-all-rows-with-specific-fields-for-each-one-of-them)
- Django documentation was extremely helpful e.g. [understanding widgets](https://docs.djangoproject.com/en/5.1/ref/forms/widgets/), [CSRF](https://docs.djangoproject.com/en/5.1/howto/csrf/) and [form validation](https://docs.djangoproject.com/en/5.2/ref/forms/validation/)
- Images from [Unsplash](https://unsplash.com/)
- [Django-blog project](https://github.com/emilywade/django_blog/) - I used the walkthrough project to help with general project structure and the header and footer to get me started on templates. 
