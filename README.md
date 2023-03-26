# Hounds Hotels


![Hounds Hotel](static/img/home%20.png)


Hounds Hotel is a business created to for dog owners to have a safe and homely space for their furry family members to stay whilst they go away.

The main objective of the site is to provide the user with information on the services provided and enable them to make a booking.

Visit the deployed website [here](https://hounds-hotel.herokuapp.com/)


## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Strategy](#strategy)
        1. [Project Goals](#project-goals)
        2. [User Goals](#user-goals)
        3. [Strategy Table](#strategy-table)
    2. [Scope](#scope)
        1. [User Stories](#user-stories)
    3. [Structure](#structure)
        1. [Database Model](#database-model)
    4. [Skeleton](#skeleton)
        1. [Wireframes](#wireframes)
    5. [Surface](#surface)
        1. [Color Scheme](#color-scheme)
        2. [Typography](#typography)
2. [Features](#features)
    1. [General](#general)
    2. [Home Page](#home-page)
    3. [About Page](#about-page)
    12. [Authentication Pages](#authentication-pages)
3. [Technologies Used](#technologies-used)
    1. [Languages Used](#languages-used)
    2. [Libraries and Frameworks](#languages-and-frameworks)
    3. [Packages / Dependecies Installed](#packages--dependecies-installed)
    4. [Database Management](#database-management)
    5. [Tools and Programs](#tools-and-programs)
4. [Testing](#testing)
    1. [Go to TESTING.md](https://-testing)
5. [Deployment](#deployment)
6. [Finished Product](#finished-product)
7. [Credits](#credits)
8. [Known Bugs](#known-bugs)
9. [Acknowledgements](#acknowledgements)


***


## User Experience (UX)

### Strategy

#### Project Goals

* The website contains simple colors for a modern design and also to not draw attention from the content.

* Responsive design to make the website accessible on different screen sizes.

* Structure is easy to understand and navigates effortlessly.

* Site user are able to sign up & sign in 

* Site users can edit there personal info, but must contact admin to change there user name or email address.

* Site users are able to fill out a form and make a booking request.


#### User Goals

**Epic 1 - Admin Experience**

* As a Site Admin,  I want to view all user accounts.

* As a Site Admin,  I want to edit and delete all user accounts. 

* As a Site Admin,  I want to designate staff accounts to staff members.

* As a Site Admin,  I want to manage the appointment times.


**Epic 2 - User Experience**

* As a Site User, I want to be able to create a account.

* As a Site User, I want to be able to edit my personal account information.

* As a Site User, I want to be able to make a booking request.

* As a Site User, I want to be able find the company contact information and social media.

* As a Site User, I want the information to be easy to find and read.


**Epic 3 - Customer Experience**

* As a Customer, i want to know what services are available.

* As a Customer, i want to meet the staff and understand the experience they have.

* As a Customer, i want to read previous customer reviews.

* As a Customer, i want to send a quick message through a contact form.

#### Strategy Table

Opportunity / Problem | Importance | Viability / Feasibility
--- | --- | ---
Responsive design | 5 | 5
Account Sign up | 5 | 5
Edit User profile | 5 | 5
Make a booking | 5 | 5
Contact form | 5 | 5
Social media links | 5 | 5
Admin Manage bookings & edit accounts| 4 | 4
Staff pictures and bio| 4 | 4
Customer Reviews| 4 | 4
**Total** | **42** | **42**


### Scope

According to the strategy table, not all features can be implemented in the first release of the project. For this reason, the project will be divided in multiple phases. The first phase will include the features that have been identified in order to build the minimum viable product.


**First Phase**

* Responsive design

* Create, edit and delete accounts

* Account registration.

* Make a booking request.

* Edit User profiles.

* Social media links. 

* Contact form. 

* Reviews section carosel.

**Second Phase**

* Booking will be automatically confirmed.

* Rtes for rooms and additional services will be shown.

* Card payments will be accepted for bookings.

* Sign up for newsletter.


**Third Phase**

*  3d renderings of the grounds, rooms and facilitys.

*  Additional payment options.

*  Loyalty scheme.

#### User Stories

GitHub projects was used as my project management tool to track user stories. Using a Kanban board helped to focus on specific tasks and track the project progress.

**Start**
![User Stories Progress 1](static/img/HP4-USER-STORIES-1.png)

**Progress 1**
![User Stories Progress 2](static/img/HP4-USER-STORIES-2.png)

**Progress 2**
![User Stories Progress 3](static/img/HP4-USER-STORIES-3.png)

**Progress 3**
![User Stories Progress 4](static/img/HP4-USER-STORIES-4.png)



## Structure

The website has been organized in a Hierarchical Tree Structure to ensure the site user navigates through the site effortlessly and intuitively. Here you can you can find the website map design.

![Hounds website map](static/img/drwsql.png)

* Header and navigation bar are consistent through all pages.

* Links and forms provide clear feedback to the site user.

* New additional features are provided for the user once they register an account, such as make a booking.


#### Database Model

The database model has been designed using [drawsql](https://drawsql.app/). The type of database being used for the is relational database being managed using SQLite3 during development and deployed using [PostgreSQL](https://www.postgresql.org/).

![Hounds Database Model](static/img/drwsql.png)



### Skeleton

#### Wireframes

[Balsamiq](https://balsamiq.com/) has been used to showcase the appearance of the site and display the placement of the different elements in the pages.

Page | Desktop Version | Mobile Version
--- | --- | ---
Home Page | ![Desktop Home](static/img/WF-1.png) | ![Mobile Home](static/img/MOB-1.png)
Our Team | ![Desktop Team](static/img/WF-2.png) | ![Mobile Team](static/img/MOB-2.png)
Services| ![Desktop Services](static/img/WF-3.png) | ![Mobile Services](static/img/MOB-3.png)
Testimonies | ![Desktop Testimonies](static/img/WF-4.png) | ![Mobile Testimonies](static/img/MOB-4.png)
Contact Us | ![Desktop Contact Us](static/img/WF-5.png) | ![Mobile ](static/img/MOB-5.png)




### Surface

#### Color Scheme

![Color scheme image](static/img/color-pallette.png)

The colors used in the website are  Ecru (#B49E5C) for Service banner, send email button, social media icons & in the Booking form.   Silver Chalice (#AAAAAA) & Black (#000000) are  used for the main text, with White (#FFFFFF) asthe background

The colors are were chosen keeping in mind simplicity but also providing the website a modern design. This in order to keep the focus on the content but also appealing for the users.

#### Typography

The main font being used in the site is Source Sans Pro , with sans-serif as a fallback in case Source Sans Pro doesn't get imported correctly. 

Source Sans Pro  was chosen after some research on fonts that are better for reading. 

[Back to top ⇧](#hounds-hotel)


## Features

### General

* The website has been designed from a mobile first perspective.

* Responsive design across all device sizes.

* Navigation Bar
![ Navigation Bar image](static/img/nav.png)

    *  Contains the main logo and section links.

    * The navigation bar contains links to all sections to facilitate navigation across the site. It also has a hover effect that changes color to provide feedback to the Site User for a better user experience.



* Social Media Links
  ![Social](static/img/social.png)

    * The Contact Us section contain icons with embedded links to the social media sites


### Home Page


### Our Team

![team](static/img/team.png)

* Provide images, names & titles of our team.


### Services 
![Services](static/img/services.png)

* Display information about the Services on offer.

* Display images and short description.


### Testimonial
![Testimonies](static/img/testimonies.png)

* A image carosel

* 3 images of clients

* with a breif review and there name

### Contact Us
![contact us ](static/img/contact.png)

* Here is the business address, google map, social media links & send email form.

### Manage
![Leave Reply Page](static/img/manage.png)

* Allows the site admin to accept the booking



### Authentication Pages


[Back to top ⇧](#hounds-hotel)


## Technologies Used

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


### Libraries and Frameworks

* [Django](https://www.djangoproject.com/)   
    * Django was used as web framework.

* [Django Template](https://jinja.palletsprojects.com)  
    * Django Template was used as a templating language for Django to display backend data to HTML.
   
* [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)  
    * Bootstrap 5 was used throughout the website to help with styling and responsiveness.

* [Google Fonts](https://fonts.google.com)  
    * Google fonts was used to import the fonts into the html file, and were used on all parts of the site.

* [Font Awesome](https://fontawesome.com)  
    * Font Awesome was used throughout the website to add icons for aesthetic and UX purposes. 

* [jQuery 3.6.0](https://jquery.com/)  
    * jQuery was used as a JavaScript library to help writing less JavaScript code.  


### Packages / Dependecies Installed

* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)  
    * Django Allauth was used for user authentication, registration, and account management.

* [Django Crispy Form](https://django-crispy-forms.readthedocs.io/en/latest/)   
    * Django Crispy Form was used to control the rendering of the forms. 
 
* [Gunicorn](https://gunicorn.org/)  
    * Gunicorn was used as Python WSGI HTTP Server for UNIX to support the deployment of Django application.  


* [Cloudinary](https://cloudinary.com/)
    * Cloudinary has been used as image management solution

### Database Management
* [Heroku Postgres](https://www.heroku.com/postgres)   
    * Heroku Postgres database was used in production, as a service based on PostgreSQL provided by Heroku.



