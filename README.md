## FIFTH TASTE
### Contents

1. [Project Overview](#project-overview)
2. [Rationale](#rationale)
3. [Planning](#planning)
4. [Schema](#schema)
5. [Security Features](#security-features)
6. [Deployment](#deployment)
7. [Testing](#testing)
8. [Credits](#credits)

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
The site has been deployed using Code Institute's mock terminal for Heroku. I deployed early and consistently to check for any deployment errors. 

<hr>

### Testing and Validation
#### Validation
- Bootstrap's built-in form validation for client-side validation 
- Django's clean() method for server-side validation to ensure that the data entered by users is both accurate and secure before being saved to the database.
  
#### Manual Testing
- Django Shell: Initially, I used the Django shell to manually test key functions and methods to ensure they were working as expected. This allowed for quick and direct feedback on the behavior of models, views, and other backend logic.
- CSS, HTML, and JavaScript Validators: I validated HTML using `djhtml` and CSS using [W3C](https://validator.w3.org/). JavaScript was tested using console-based debugging during development, as well as [JSHint](https://jshint.com/) after completion.

#### Automated Testing
- I used Django's TestCase to test models and forms. I used it to check my Booking views were interacting with the database correctly (bookings can be created, updated and deleted). I also used it to check the contact form was validating data correctly, saving valid data to the database and providing correct feedback when invalid data is entered. 
  
<hr>

### Credits
- Stack Overflow was definitely my friend in this project. Here are two examples I needed it for: [Django ORM filter](https://stackoverflow.com/questions/10040143/and-dont-work-with-filter-in-django) and [Specific fields from querysets](https://stackoverflow.com/questions/7503241/how-to-obtain-a-queryset-of-all-rows-with-specific-fields-for-each-one-of-them)
- Django documentation was extremely helpful e.g. [understanding widgets](https://docs.djangoproject.com/en/5.1/ref/forms/widgets/), [CSRF](https://docs.djangoproject.com/en/5.1/howto/csrf/) and [form validation](https://docs.djangoproject.com/en/5.2/ref/forms/validation/)
- Images from [Unsplash](https://unsplash.com/)
- [Django-blog project](https://github.com/emilywade/django_blog/) - I used the walkthrough project to help with general project structure and the header and footer to get me started on templates. 
