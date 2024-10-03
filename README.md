  # ADOPTDOG PROJECT https://www.adoptdog.co.uk
  
  # Contents 
 - [ADOPTDOG PROJECT https://www.adoptdog.co.uk](#adoptdog-project-https---wwwadoptdogcouk)
- [Contents](#contents)
  * [1. OVERVIEW](#1-overview)
    + [Target Audience](#target-audience)
  * [2. USER STORIES](#2-user-stories)
    + [Epic](#epic)
    + [Site User](#site-user)
    + [Future Site User Stories](#future-site-user-stories)
    + [Site Admin or Staff User](#site-admin-or-staff-user)
    + [Future Site Admin stories](#future-site-admin-stories)
  * [3. SITE OWNER GOALS](#3-site-owner-goals)
  * [4. FEATURES](#4-features)
    + [Navigation Bar](#navigation-bar)
    + [Nav Logo](#nav-logo)
    + [Menu Links](#menu-links)
    + [Search Sanctuaries](#search-sanctuaries)
    + [Logged in/Logged out Notification](#logged-in-logged-out-notification)
    + [Footer](#footer)
    + [Landing Page](#landing-page)
    + [About Page](#about-page)
    + [Registration Page](#registration-page)
    + [Sign in Page](#sign-in-page)
    + [Tabular Display of Information from Database](#tabular-display-of-information-from-database)
    + [Comments with CRUD functionality for Dogs and Site](#comments-with-crud-functionality-for-dogs-and-site)
    + [Collaboration form](#collaboration-form)
    + [Admin Panel](#admin-panel)
  * [Future Features](#future-features)
    + [Dark/Light Theme](#dark-light-theme)
    + [Email Registration and Authentication using SendGrid](#email-registration-and-authentication-using-sendgrid)
  * [5. UX/UI](#5-ux-ui)
    + [AdoptDog CSS Colors](#adoptdog-css-colors)
    + [Fonts](#fonts)
    + [Navbar](#navbar)
    + [Footer](#footer-1)
    + [Borders](#borders)
  * [User Experience Design](#user-experience-design)
    + [Navigation](#navigation)
    + [User Authentication](#user-authentication)
    + [Pagination](#pagination)
    + [Notification of Viewing text box](#notification-of-viewing-text-box)
  * [6. WIRE FRAMES](#6-wire-frames)
    + [AdoptDog Landing Page](#adoptdog-landing-page)
    + [AdoptDog Selection-view](#adoptdog-selection-view)
    + [AdoptDog Registration](#adoptdog-registration)
    + [AdoptDog Search](#adoptdog-search)
  * [7. ENTITY RELATIONSHIP DIAGRAMS](#7-entity-relationship-diagrams)
    + [Full Entity relationship Diagram of Django Models](#full-entity-relationship-diagram-of-django-models)
    + [AdoptDog Draw.io Entity Relationship Diagram V1.6](#adoptdog-drawio-entity-relationship-diagram-v16)
  * [8. TESTING](#8-testing)
  * [9. DEPLOYMENT](#9-deployment)
  * [Database](#database)
  * [Deploying to Heroku](#deploying-to-heroku)
  * [10. TECHNOLOGIES](#10-technologies)
    + [Hosting](#hosting)
    + [Languages](#languages)
    + [Frameworks, Libraries, API's and other Programs/Websites Used](#frameworks--libraries--api-s-and-other-programs-websites-used)
  * [Software](#software)
  * [11. MEDIA](#11-media)
- [END OF README.md](#end-of-readmemd)



<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

<div>
<img src="documentation/images/adoptdog-screens.webp" alt="AdoptDog U-DEV">
</div>


## 1. OVERVIEW

Twenty thousand dogs are euthanized a year in the UK,  the majority of these dogs are unwanted pets that have ended up in a dog sanctuary,  Due to this complete waste of animal life, I decided to create https://www.adoptdog.com.  This site will try to address this problem by having the functionality to show pictures of dogs that are in sanctuaries.  So I can give details of where they are being kept,  at first for the Berkshire area, and if the site goes viral throughout the UK.  This site will give the ability for a user to see a picture of a dog and add a comment , find contact details, search for a sanctuary and navigate through to a dog that is housed there, and leave a message for the administrators of this site.

This site will for the duration of the project hold fictitious sanctuaries and dogs until the project is marked,  potentially after the marking the site can be populated with real data.

I hope to actively help in finding dogs new homes where they can become part of a new family.  As through no fault of their own, if they do not gain new owners the dogs will be destroyed. 

******

### Target Audience

adoptdog.co.uk aim is to provide information on dogs that have not got homes, for the following criteria,

- Stray Dogs that have been picked up by services such as the RSPCA
- Unwanted pets that have been given to a sanctuary
- Dogs that have not got on with there before family and have been sent to a sanctuary
- Dogs that have been sent to a sanctuary for financial reasons

- The audience is families that are looking to get a new pet dog that are willing to try a sanctuary first before going
to a pet shop,  authorised breeder etc.

- Single adults looking to get a pet dog who can't afford breeders fees for purchase
- For professional services looking to acquire a dog 

The site can be used for 
a). Sanctuaries looking to add their sanctuary and dogs that they currently have for a wider audience on the internet, basically to make a connection to the WebP large image of the animal to a new owner.

b). Families or singletons interested in finding a home for a pet dog(s) that is not working out in their home.  


## 2. USER 

**PROJECT BOARD:** <a href="https://github.com/users/StaysafeUK/projects/10/views/1" target="_blank">Adoptdog Kanban Project Board link </a>

### Epic

- **As a User I want to be able to find a rescue dog:** 
As a User I can find a rescue dog so that I can select a new pet from available dogs that are due to be destroyed

### Site User

- **View lists of Posts:** As a site user I can view a paginated list of posts so that I can select which post I want to view.

- **Open a Post:** As a site user I can click on a post so that I can read the text displayed from the database.

- **View Comments:** As a site user I can view comments on a dog so that users comments can be seen and the site admin can view the conversation.

- **Account Registration:** As a site user I can register an account so that I can comment on a dog so that I can express interest in the animal and start a conversation with the site.

- **Comment on a dog with create, edit and delete operation:** As a site user I can modify or delete my comment so that I can be in control of my conversations to the site.

- **Read about the Site:** As a site user I can read about the site so that I can click on the about link and read about the site producer.

- **View the dogs location and contact details:** As a site user I can read about the location of the dog so that I can contact the sanctuary owner and find the location.

- **As a user I want a friendly website address:** As a user I can go to a friendly url so it is easy to find so that I can use the address in social media and by word of mouth or find the site address in search engines.

- **I can search for Sanctuaries near me:** As a user I can search for sanctuaries near me  so that I know what dogs are local for me to take home.

###  Future Site User Stories

- **As a user I can select A Light or Dark Theme:** As a User I can Select a Dark or Light Theme on the Site so that I can use a display preference


### Site Admin or Staff User

- **create, modify and delete Dogs as a SuperUser:** As a Staff User I can create, modify and delete dogs so that I can administer the dogs on the site.

- **Manage Posts:** As a Site Admin I can create, read, update and delete posts so that I can manage the Dogs content.

- **Create, drafts:** As a Site Admin I can create draft posts so that I can finish the content later so that I have a draft.

- **Approve Comments:** As a site admin I can approve or disapprove comments so that I can filter out objectionable comments 

- **Add and update the text to About page:** As a Site Admin I can create or update the about page content so that it is available on the about us page and is easy to edit.

- **Ability to contact the site owner as a dog sanctuary owner for use of this site:** As a potential staff user I can contact the site owner or SuperAdmin so that I can leave a message about potential collaboration.

### Future Site Admin stories

- **I want users to leave real email addresses when they register an account:** As a Admin I can confirm whom is making account so that I do not receive robotic accounts and keep hacking to a minimum

*******

## 3. SITE OWNER GOALS

- The site owners goal is to have a clean site running on the Django framework with PostGresSQL database,  hosted on Heroku running Javascript for CRUD (Create, Read, Update, Delete) operation that has the ability to create well formatted posts showing images and important information regarding the Dog specified so information can quickly be asatained  regarding that animal.

- The site owners goal is to have a site that can receive comments from the public,  or collaboration requests for sanctuaries or dog owners that want to move their pet dog onto another family for whatever reason.

- The site owners goal is to give the ability to search for a Sanctuary based on name to show dogs that are located at that vicinity.

******

## 4. FEATURES

### Navigation Bar

The navigation bar is displayed across all major pages,  the navbar is reduced to a Burger Bar using Bootstrap where the menu items are displayed below.

<div>
<img src="documentation/images/navbar-adopdog.webp" alt="AdoptDog NavBar">
</div>

### Nav Logo

The navigation logo uses CSS to give it a distinctive personalisation using CSS, when clicked the logo takes the user back to the home page.

<div>
<img src="documentation/images/nav-logo-adoptdog.webp" alt="AdoptDog NavLogo">
</div>

### Menu Links

Menu links are shown on the Above image in navigation bar and the burger bar showing the user where he can click to access the pages on the site.  Clearly giving navigation to the About page and access to Search Sanctuary,  Note:  Signup page is not showing as the user is logged in at the time this image was created.

<div>
<img src="documentation/images/menu-links-adoptdog.webp" alt="AdoptDog Menu-Links">
</div>


### Search Sanctuaries 

The search facility gives a user the ability to search on sanctuary which if listed in the database returns information about the sanctuary and the dogs that are homed at that location.  The data is clearly displayed in a tabular format.

<div>
<img src="documentation/images/search-sanctuary-adoptdog.webp" alt="AdoptDog Search sanctuaries">
</div>

### Logged in/Logged out Notification

The Logged in/Logged out notification clearly shows if the user is Logged in & displays the username, if the user is not logged in this is shown.

<div>
<img src="documentation/images/loggedin-adoptdog.webp" alt="AdoptDog Login notification">
</div>

### Footer 

The footer shows clearly the social media site connections with A HREFS to selected social media sites and details of the site creator.

<div>
<img src="documentation/images/footer-adoptdog.webp" alt="AdoptDog Footer">
</div>

### Landing Page 

The landing page shows dogs that are available pulled from the Elephant PostGresSQL database,  on cards that display the sanctuary where the dog is housed. Upon clicking the page is redirected to a Post_detail view where more information is available regarding the specific dog.

<div>
<img src="documentation/images/landingpage-adoptdog.webp" alt="AdoptDog Landing Page">
</div>

### About Page

The about page shows information about the site creator and also has a collaborator form where members of the public can ask to collaborate on the site i.e asking if they can add there sanctuary and dogs to the site.  This form is available to view as an admin user through the admin portal.  The about page also has a comments section about the site where comments can be left about the overall site experience with CRUD functionality.

<div>
<img src="documentation/images/aboutpage-adoptdog.webp" alt="AdoptDog About page">
</div>

### Registration Page

The registration page is where users sign up to the site so they have the ability to leave comments for the site admins about the dogs or the site itself.

<div>
<img src="documentation/images/registrationpage-adoptdog.webp" alt="AdoptDog Registration page">
</div>

### Sign in Page 

The sign in page is so users can be authenticated to the site so they have the ability to leave comments for dogs or the site.  I started to add email authentication using SendGrid relay and Django-Auth for additional security however this is now a future and will NOT be included in the three iterations for this project.  This will be discussed further in the Future Features Section.

<div>
<img src="documentation/images/signinpage-adoptdog.webp" alt="AdoptDog Signin ">
</div>

### Tabular Display of Information from Database

One of the best features of the site is the tabular display of information presented from the PostGresSQL database into a table.  The example below shows information from the search function in the Navbar.  Another example of this is from clicking on a dog and seeing the information provided in a table.


<div>
<img src="documentation/images/tabulardisplay-adoptdog.webp" alt="AdoptDog Tabular display of Dog(s) information">
</div>
 
### Comments with CRUD functionality for Dogs and Site

As mentioned above the site includes the ability to have:
- comments approved, by the site admin for a permanent display to the site to control unwanted comments
- Gives the user an ability to add, edit and delete comments once signed in CRUD functionality for Dogs and the Site.

- Comments for specific Dog
<div>
<img src="documentation/images/commentsdog-adoptdog.webp" alt="AdoptDog Comments about a dog">
</div>

- Comments about the Site

<div>
<img src="documentation/images/commentsabout-adoptdog.webp" alt="AdoptDog Comments about the site">
</div>

### Collaboration form 

The collaboration form gives the public the ability to get in touch regarding adding a new potential sanctuary and dogs that can be displayed for people to get in touch with the site admins regarding the dogs the sanctuary holds.  The collaboration form has required fields which must be filled out with verification that the fields are correct entities. for example the email field must have a valid email address i.e have an @ sign.

<div>
<img src="documentation/images/collaboration-adoptdog.webp" alt="AdoptDog Collaboration form">
</div>

### Admin Panel

The admin panel is available only to site administrators,  this is a standard feature of Django.  However this has been extended to include SummerNote which gives Rich Text Formatting RTF to the majority of the database fields of TextField. This is so the Site Administrators or SuperUsers can use RTF to write fully formatted text. 

<div>
<img src="documentation/images/admin-adoptdog.webp" alt="AdoptDog Admin-Panel">
</div>

## Future Features

### Dark/Light Theme

I would like the site in a future iteration to include the ability to switch from a light themed CSS to a Dark themed CSS,  I started work on this however due to using Bootstrap predominantly and default settings through Class tags this makes it increasingly difficult to switch between light and dark in CSS. As this is rapid development it therefore should be understood that this was not complete due to timescales. 

### Email Registration and Authentication using SendGrid

I managed to get email authentication working locally from my GitPod environment using SendGrid API,  As this project would receive  no additional credit for using SendGrid to authenticate users,  i.e send a confirmation email and use the email address throughout the Python Django code for authentication,  I have commented out the code in view.py and deleted the new crispy form for authenticating by email.  When reviewing the code base on Github you will see where the code has been commented out that gives the email auth/Send Grid API the ability to send mail and authenticate. 


## 5. UX/UI

### AdoptDog CSS Colors 

The colors used for this site are bright and user friendly to the eye for an enjoyable user experience,  Colors are also derived from Bootstrap such as WARNING, ERROR and SUCCESS.  These colors are used for CRUD information messages on operations. From a UI perspective I wanted to keep the site clean and uncluttered.  

**Text color scheme:   #4b4b4f**
**light background:    #fff**
**Dark Background:     #445261**
**Main Background:     #F9FAFC**
**Card:                Transparent**
**image notification:  #18815c**
**Author Box Text:     #fff**
**Page-Link Hover is:  #E84610**
**Button Sign is:      #23BBBB** 
**link:                #23BBBB**
**Button Like:         #E84610**
**Button Hover:        #f22009**
**Approval:            rgb(232, 36, 22)**

<div>
<img src="documentation/diagrams/adoptdog-css-color.webp" alt="AdoptDog CSS Colors Diagram">
</div>

### Fonts 

Google Fonts have been used through this site to give the text a unique, readable fonts that add to the design. I opted for Inter Sans Serif, review the CSS to see the weighting of the font displayed.  

**Font family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900**

### Navbar 

The Navbar uses **bootstrap@5.0.1 navbar-light navbar-expand-lg background light**,  the thinking here was bootstrap provides good viewpoint features when viewing on different device sizes. Therefore bootstrap has been used throughout this project.

### Footer 

The footer uses footer **mt-auto py-3 dark-bg** with favicons for the social media links **font-awesome/5.15.3**.  The text color is white.  

### Borders 

Borders are displayed around the card-text using **border p-2** 

********** 

## User Experience Design

### Navigation

Navigation is key to well defined user friendly site,  all pages on the site can be accessed from the navbar defined in Base.html which extends to each of the templates on the About and Blog application.  On smaller screens such as mobile,  the burger bar comes into play where the links are listed.

### User Authentication

User Authentication has been used throughout this project from the onset, defined in the DTL (Django Template Language) to give access once the users has been logged in,  such as leaving comments about dogs or the site.  Once a user is authenticated they have the ability to leave, edit and delete a comment.

### Pagination 

Pagination is used to allow multiple database entries of Posts/Dogs using the Previous and Next Buttons,  this enables the user not to get over whelmed with the potential of having hundreds/thousands of Dogs to view.

### Notification of Viewing text box

When a user is accessing a text field this is highlighted to show what field is active, this comes into play when using the edit button to edit a comment on the comments for dogs or leavecomment for the website.

## 6. WIRE FRAMES

The wire frames below are the initial design conception before coding began,  These diagrams show two different view points.

- Mobile Display 
- Full screen Web Browser

The wire frame images have not been updated since coding began, and throughout the coding experience some features where added during the coding stage,  such as the search sanctuaries tabular display.  The leavecomments model was also added after the Wire frame stage to include custom CRUD manipulation of data provided by a user comment for the About Application.


### AdoptDog Landing Page

<div>
<img src="documentation/wireframes/adoptdog-landingpage.webp" alt="AdoptDog Landing page wire frame">
</div>

### AdoptDog Selection-view

<div>
<img src="documentation/wireframes/adoptdog-selection-view.webp" alt="AdoptDog Selection-view wire frame">
</div>

### AdoptDog Registration

<div>
<img src="documentation/wireframes/adoptdog-registration.webp" alt="AdoptDog Registration page wire frame">
</div>

### AdoptDog Search

<div>
<img src="documentation/wireframes/adoptdog-search.webp" alt="AdoptDog Registration page wire frame">
</div>

## 7. ENTITY RELATIONSHIP DIAGRAMS

### Full Entity relationship Diagram of Django Models

The entity diagram was created at the design phase of the project,  As mentioned above an additional model of leavecomments has been added during the User Story phase to give the ability for CRUD functionality,  this was achieved by creating an independent table with no foreign keys. The footer has also been modified to show Font Awesome Icons of clickable links to the various social media platforms.

Below are The ERD Diagrams created on Code Institute's Elephant PostGresSQL Database,  The Sanctuary model has a one to many relationship, extending the Post Model to have the ability to select a Sanctuary for a Dog when created in the Admin Portal.

<div>
<img src="documentation/diagrams/erd_models.webp" alt="AdoptDog Full Entity Relationship Diagram">
</div>


### AdoptDog Draw.io Entity Relationship Diagram V1.6
<div>
<img src="documentation/diagrams/adoptdog-erd_1.6.webp" alt="AdoptDog Entity Relationship Diagram">
</div>

## 8. TESTING

### HTML W3C Testing
<a href="https://validator.w3.org/" target="_blank">W3C Validator Link</a>

The following section details the HTML testing using W3C Markup Validation service,  As Django uses DTL Django template language the HTML has to be validated after it is rendered on a page.  Below are the results

**Landing Page**

The landing page HTML W3C Validator passed with no errors

<div>
<img src="documentation/Testing/landing-page-HTMLChecker.webp" alt="Landing Page HTML W3C Validator">
</div>

**PostDetail Page**

Post DetailPage HTML W3C Validator recorded one Error no p element but a p end tag seen,  I have looked for this error but cannot see where Django is getting this HTML,  due to time restraints I will try to solve at the end of the project if possible.

<div>
<img src="documentation/Testing/PostDetail-page-HTMLChecker.webp" alt="PostDetail Page HTML W3C Validator">
</div>

**Search Results Page**

Search results page using the HTML W3C validator has detected one error, The center element is obsolete USe CSS instead, due to the rapid turn around of this project I will leave this for now, and try to resolve by end of the project deadline.

<div>
<img src="documentation/Testing/Search-pageHTMLChecker.webp" alt="Search Results Page HTML W3C Validator">
</div>

**Login Page**

Login Page results for the HTML W3C Validator passed with no errors

<div>
<img src="documentation/Testing/LoginHTMLChecker.webp" alt="Login Page HTML W3C Validator">
</div>

**Sign Up Page**

The Signup Page results for HTML W3C Validator had four errors, due to the tight timescales of this project these errors will be resolved at a later date.

1. End tag p implied, but there were open
2. Unclosed element span
3. Stray end tag span
4. No p element in scope but a p end tag

<div>
<img src="documentation/Testing/signupHTMLChecker.webp" alt="Sign Up Results Page HTML W3C Validator">
</div>

**About Page**

The About page has 6 Errors and 4 Warnings for the HTML W3C Validator

1 8 Bad value 85% for attribute width on element img : Expected a digit but saw % instead : *This error I will try and correct before the project deadline*
2 Duplicate ID: _ (4)  *The Duplicate ID errors are due to the collaboration form using the same fields such as. id_name and id_email as the leavecomments* 
form.  *These errors do not effect the workings of the site and can be written off due to the extra form for leavecomments.*     

2.1  Duplicate ID div_id_name:
2.2  Duplicate ID id_name.
2.3  Duplicate ID div_ id_email
2.4  Duplicate ID id_email.
3 V Attribute method not allowed on element a at this point. *This attribute is used by javascript for the CRUD Function*

<div>
<img src="documentation/Testing/About-PageHTMLChecker.webp" alt="About Page HTML W3C Validator">
</div>

### CSS Validator###

The CSS Validator had a few errors which I corrected such as elements not being in alphabetical order, I have resolved these issues now and the CSS passes, 
see image below.

<div>
<img src="documentation/Testing/CSSValidator.webp" alt="CSS W3C Validator">
</div>



### JavaScript Validator ###
<a href="https://jshint.com/" target="_blank">JS Hint Link</a>

**comments.js JS Validator**

<div>
<img src="documentation/Testing/commentsJSValidator.webp" alt="AdoptDog Search sanctuaries">
</div>



**leavecomments.js JS Validator**

<div>
<img src="documentation/Testing/leavecommentsJSValidator.webp" alt="AdoptDog Search sanctuaries">
</div>

























## 9. DEPLOYMENT

## Deploying to Heroku

## 10. TECHNOLOGIES

### Hosting 
Heroku is used for Hosting the Django site and is deployed from Gitpod IDE where the site has been viewed rendered throughout this development process using *python3 manage.py runserver* initiating Gunicorn webserver.  Cloudinary is used for dynamic images through the Cloudinary API. 

### Database 



## env.py

The secrets needed to run this Django site including database strings, cloudinary API strings and passwords, Django secrets, etc.  Are stored in .env.py which is added to gitignore and not uploaded to the Github respository.  In *settings.py*   

*if os.path.isfile('env.py'):*
                *import env* 

the secrets are called by the  *os.environ.get* method.  

The Django secret key has been changed from the default key to a new secure key and has not been uploaded to this repository.

### Languages
- <a href="https://dev.w3.org/html5/spec-LC" target="_blank">HTML 5</a>
- <a href="https://www.w3.org/Style/CSS/Overview.en.html" target="_blank">CSS3</a> 
- <a href="https://docs.djangoproject.com/en/5.1/ref/templates/language" target="_blank">Django Template Language</a>
- <a href="https://en.wikipedia.org/wiki/Markdown" target="_blank">Markdown Language</a>
- <a href="https://jquery.com/" target="_blank">Jquery</a>
- <a href="https://www.python.org/" target="_blank">Python</a>

### Frameworks, Libraries, API's and other Programs/Websites Used

- <a href="https://asgi.readthedocs.io/en/latest/" target="_blank">asgiref = 3.8.1</a>
- <a href="https://balsamq.com" target="_blank">Balsamiq</a>
- <a href="https://cloudinary.com/" target="_blank">Cloudinary = 1.36.0</a>
- <a href="https://django-crispy-forms.readthedocs.io/en/latest/" target="_blank">Crispy bootstrap5 = 0.7</a>
- <a href="https://cloudinary.com/" target="_blank">dj3-cloudinary-storage = 0.0.6</a>
- <a href="https://www.djangoproject.com/" target="_blank">Django = 4.2.16</a>
- <a href="https://www.djangoproject.com/" target="_blank">django-allauth = 0.57.2"</a>
- <a href="https://www.djangoproject.com/" target="_blank">django-allauth = 0.57.2</a>
- <a href="https://django-crispy-forms.readthedocs.io/en/latest/" target="_blank">django-crispy-forms = 2.3</a>
- <a href="https://www.djangoproject.com/" target="_blank">django-extensions = 3.2.3</a>
- <a href="https://www.djangoproject.com/" target="_blank">django-phone-field = 1.8.1</a>
- <a href="https://www.djangoproject.com/" target="_blank">django-phonenumber-field = 8.0.0</a>
- <a href="https://www.djangoproject.com/" target="_blank">django-phonenumbers = 1.0.1</a>
- <a href="https://www.djangoproject.com/" target="_blank">django-summernote = 0.8.20.0</a>

- <a href="https://app.diagrams.net/" target="_blank">Draw.io</a>
- <a href="https://git-scm.com/" target="_blank">Git</a>
- <a href="https://github.com/" target="_blank">Github</a>
- <a href="https://heroku.com" target="_blank">Heroku</a>

- <a href="https://docs.gunicorn.org/en/20.1.0/" target="_blank">gunicorn = 20.1.0</a>
- <a href="https://oauthlib.readthedocs.io/en/latest/" target="_blank">oauthlib = 3.2.2</a>

- <a href="https://pypi.org/project/phonenumbers/" target="_blank">phonenumbers = 8.13.45</a>
- <a href="https://pypi.org/project/psycopg2/" target="_blank">psycopg2 = 2.9.9</a>
- <a href="https://pypi.org/project/pydotplus/" target="_blank">pydotplus = 2.0.2</a>
- <a href="https://pypi.org/project/PyJWT/" target="_blank">PyJWT = 2.9.0</a>
- <a href="https://pypi.org/project/pyparsing/" target="_blank">pyparsing = 3.1.4</a>
- <a href="https://pypi.org/project/python-http-client/" target="_blank">python-http-client = 3.3.7</a>
- <a href="https://pypi.org/project/python3-openid/" target="_blank">python3-openid = 3.2.0</a>
- <a href="https://pypi.org/project/requests-oauthlib/" target="_blank">requests-oauthlib = 2.0.0</a>
- <a href="https://pypi.org/project/sendgrid/" target="_blank">sendgrid = 6.11.0</a>
- <a href="https://pypi.org/project/sqlparse/" target="_blank">sqlparse = 0.5.1</a>
- <a href="https://pypi.org/project/starkbank-ecdsa/" target="_blank">starkbank-ecdsa = 2.2.0</a>
- <a href="https://pypi.org/project/urllib3/" target="_blank">urllib3 = 1.26.20</a>
- <a href="https://pypi.org/project/whitenoise/" target="_blank">whitenoise = 5.3.0</a>

## Software

## 11. MEDIA

# END OF README.md