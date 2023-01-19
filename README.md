# Hounds Hotels


![Hounds Hotel mockup images](assets/.jpg)


Hounds Hotel is a business created to for dog owners to have a safe and homely space for their furry family members to stay whilst they go away.

The main objective of the site is to provide the user with information on the services provided and enable them to make a booking.

Visit the deployed website [here](https://.com).


## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Strategy](#strategy)
        1. [Project Goals](#project-goals)
        2. [User Goals](#user-goals)
        3. [Strategy Table](#strategy-table)
    2. [Scope](#scope)
        1. [User Stories](#user-stories)
    3. [Structure](#structure)
    4. [Skeleton](#skeleton)
    5. [Surface](#surface)
2. [Features](#features)
    1. [General](#general)
    2. [Home Page](#home-page)
    3. [About Page](#about-page)
    4. [Search Results Page](#search-results-page)
    5. [Question Detail Page](#question-detail-page)
    6. [Ask Question Page](#ask-question-page)
    7. [Leave Reply Page](#leave-reply-page)
    8. [Edit Question Page](#edit-question-page)
    9. [Delete Question Page](#delete-question-page)
    10. [Edit Reply Page](#edit-reply-page)
    11. [Delete Reply Page](#delete-reply-page)
    12. [Authentication Pages](#authentication-pages)
3. [Technologies Used](#technologies-used)
    1. [Languages Used](#languages-used)
    2. [Libraries and Frameworks](#languages-and-frameworks)
    3. [Packages / Dependecies Installed](#packages--dependecies-installed)
    4. [Database Management](#database-management)
    5. [Tools and Programs](#tools-and-programs)
4. [Testing](#testing)
    1. [Go to TESTING.md](https://github.com/josswe26/c/blob/main/TESTING.md#-testing)
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

* Site users are able to open an account in order to make a booking.

* Site users are able to create an account and make a booking.


#### User Goals

* As a Site Admin,  .................

* As a Site User, I want to be able to interact with the content.

* As a Site User, I want the information to be easy to find and read.

* As a Dog Parent, I want to be able to create an account.

* As a Dog Parent, I want to be able to Sign in using User Name & Password.

* As a Dog Parent, I can update my account information.

* As a Dog Parent, I want the information to be easy to find and read.

* As a Dog Parent, I want to be able to make a booking for my dog.


#### Strategy Table

Opportunity / Problem   Importance  Viability / Feasibility
--- | --- | ---
Responsive design   | 5 | 5
Account Creation    | 5 | 5
Ability to sign-in  | 5 | 5
Create, edit and delete personal info | 5 |4
Create, edit and delete booking | 5 | 4
Ability to search for information | 5 | 3
Social Media Icons | 3 | 5
        
**Total** | **33**  |  **28**



### Scope

According to the strategy table, not all features can be implemented in the first release of the project. For this reason, the project will be divided in multiple phases. The first phase will include the features that have been identified in order to build the minimum viable product.

**First Phase**

* Responsive design

* Menu 

* Account registration

* Booking Form

* 

* 

**Second Phase**

* Ability to add reviews 

* Social media signup

* Extra Services, Grooming, extra playtime, Treats, Massages


#### User Stories

GitHub projects was used as my project management tool to track user stories. Using a Kanban board helped to focus on specific tasks and track the project progress.

**Start**
![User Stories Progress - Start](assets/)

**Week 1**
![User Stories Progress - Week 1](assets/)

**Week 2**
![User Stories Progress - Week 2](assets/)

**Week 3**
![User Stories Progress - Week 3](assets/)


### Structure

The website has been organized in a Hierarchical Tree Structure to ensure the site user navigates through the site effortlessly and intuitively. Here you can you can find the website map design.

![website map](assets/)

* Header, footer and navigation bar are consistent through all pages.

* Links and forms provide clear feedback to the site user.

* The opportunity to add additional content to the website is provided for the site user once they register an account.

* A 404-error page is available.


#### Database Model

The database model has been designed using [drawsql](https://drawsql.app/). The type of database being used for the is relational database being managed using [PostgreSQL](https://www.postgresql.org/).

![website map](assets/)

**Question Model**



**Reply Model**

* 




### Skeleton

#### Wireframes

[Balsamiq](https://balsamiq.com/) has been used to showcase the appearance of the site and display the placement of the different elements whitin the pages.

Page | Desktop Version | Mobile Version
--- | --- | ---
Index / User Logged Out | ![Desktop index / user logged out wireframe image](assets/) | ![Mobile index / user logged out wireframe image](assets/wireframes/)
Sign Up | ![Desktop sign up wireframe image](assets/wireframes/signup_dektop.png) | ![Mobile sign up wireframe image](assets/wireframes/signup_mobile.png)
Log In | ![Desktop log in wireframe image](assets/wireframes/login_dektop.png) | ![Mobile log in wireframe image](assets/wireframes/login_mobile.png)
Index / User Logged In | ![Desktop index / user logged in wireframe image](assets/wireframes/index_dektop_logged_in.png) | ![Mobile index / user logged out wireframe image](assets/wireframes/index_mobile_logged_in.png)
Ask Question | ![Desktop ask question wireframe image](assets/wireframes/ask_question_desktop.png) | ![Mobile ask question wireframe image](assets/wireframes/ask_question_mobile.png)
Open Question | ![Desktop open question wireframe image](assets/wireframes/question_dektop.png) | ![Mobile open question wireframe image](assets/wireframes/question_mobile.png)
Leave Reply | ![Desktop leave reply wireframe image](assets/wireframes/leave_reply_desktop.png) | ![Mobile leave reply wireframe image](assets/wireframes/leave_reply_mobile.png)


### Surface

#### Color Scheme

![Color scheme image](assets/)

The colors used in the website are a middle red (#CA8471) for secondary buttons, navbar links, as well as for main buttons and links transitions. Charcoal (#253A47) is used for the main text, footer background, main buttons and secondary buttons and links transitions.

A brown sugar (#C37046) for the navigation bar and card footers background, footer and buttons content. A Thistle color (#E3C7E9) is also used in the main background and cards footer as well as for input fields.

The colors are were chosen keeping in mind simplicity but also providing the website a modern design. This in order to keep the focus on the content but also appealing for the users.


#### Typography

The main font being used in the site is Nunito, with sans-serif as a fallback in case Nunito doesn't get imported correctly. Roboto, with sans-serif as a fallback is used mainly for headings and the logo has been given the Quicksand font, with sans-serif as a fallback.

Nunito and Roboto were chosen after some research on fonts that are better for reading. Specially Nunito which has been used as main font. Quicksand was used for the logo for design purposes.

[Back to top ⇧](#hounds-hotel)


## Features

### General

* The website has been designed from a mobile first perspective.

* Responsive design across all device sizes.

* Navigation Bar
![ Navigation Bar image](assets/readme_files/_navbar.png)

    *  Contains the main logo and section links.

    * The navigation bar contains links to all sections to facilitate navigation across the site. It also has a hover effect that changes color to provide feedback to the Site User for a better user experience.

* Search bar
![Search Bar image](assets/readme_files/search_bar.png)

    * Provide the Site User an input field and a Search button to be able to search for specific questions.

* Footer
  ![ Footer image](assets/readme_files/_footer.png)

    * The footer includes a logo and link to social media channels.


### Home Page

* Question list



### About Page

![CAbout Page image](assets/readme_files/_about.png)

* Provide relevant information about the website's objective.


### Search Results Page
![ About Page image](assets/readme_files/_search_results.png)

* Display information about the Search being handled

* Display a paginated list of the questions matching the search and its relevant information for the user to identify.


### Question Detail Page
![ Question Detail Page image](assets/readme_files/_question_detail.png)

* Display the full question a well as a list of its replies.

* Question and reply scores as well as voting possibilities for registered users is provided next to each item.

* For registered users, a Leave Reply button is provided to allow the user to access the Leave Reply page to create a new reply to the question.

 * Edit and Question buttons are provided for the questions and replies the registered Site User has created.


### Ask Question Page
![ Ask Question Page](assets/readme_files/ask_question.png)

* Provide a form to allow registered Site Users to create a new question.

### Leave Reply Page
![Leave Reply Page](assets/readme_files/_leave_reply.png)

* Provide a form to allow registered Site Users to create a new reply to the questions.


### Edit Question Page
![ Edit Question Page](assets/readme_files/cedit_question.png)

* Provide a prepopulated form to allow the Site User to edit a question they created.


### Delete Question Page
![ Edit Question Page](assets/readme_files/cdelete_question.png)

* Provide a form to allow the Site User to delete a question they created.


### Edit Reply Page
![ Edit Question Page](assets/readme_files/_edit_reply.png)

* Provide a prepopulated form to allow the Site User to edit a reply they created.


### Delete Reply Page
![ Edit Question Page](assets/readme_files/delete_reply.png)

* Provide a form to allow the Site User to delete a reply they created.


### Authentication Pages

Page | Purpose | Image |
--- | --- | --- |
Register | Allow the Site User to sign up an account for the website. | ![ Sign Up Page](assets/readme_files/co_sing_up.png) |
Login | Allow the Site User to sign in with their account. | ![ Sign In Page](assets/readme_files/_sign_in.png) |
Logout | Allow the Site User to sign out from their account. | ![ Sign Out Page](assets/readgn_out.png) |


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

* [Summernote](https://summernote.org/) 
    * Summernote has been used as WYSIWYG editor.

* [Cloudinary](https://cloudinary.com/)
    * Cloudinary has been used as image management solution

### Database Management
* [Heroku Postgres](https://www.heroku.com/postgres)   
    * Heroku Postgres database was used in production, as a service based on PostgreSQL provided by Heroku.



