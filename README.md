# Car Specialist

Car Specialist is a website that provides all the information about the car workshop. The site will be targeted towards the people who need car repair services and it will deliver all necessary information about the range of services provided by the service as well as the possibility to book, update and delete an appointment. To be able to do all these booking actions, customers will first need to create an account and log in.


[Visit Car Specialist](https://car-specialist.herokuapp.com/)

## Table of Content

* [UX](#UX) 
    * [User Stories](#User-Stories)          
    * [Wireframes](#Wireframes)
    * [Colour Scheme](#Color-Scheme)
    * [Typography](#Typography)
    * [Agile Methodology](#Agile-methodology)

* [Features](#Features)
  * [Existing features](#Existing-features)
  * [Future Features](#Future-features)
  
* [Technologies Used](#Technologies-Used)
  * [Languages Used](#Languages)
  * [Frameworks, Libraries & Programs](#Frameworks-Libraries-Programs) 

* [Testing](#Testing)

* [Deployment](#Deployment)

* [Credits](#Credits)
    * [Content](#Content)
    * [Media](#Media)
    
----------------------------
## UX
### User Stories          
### Wireframes

Wireframes were created for desktop and mobile devices. Each page is individually presented for mobile and desktop screens in the following links.

[Home page](docs/wireframes/home.png)

[Services page](docs/wireframes/services.png)

[Contact page](docs/wireframes/contact.png)

[Booking page](docs/wireframes/bookingpage.png)

[My Bookings page](docs/wireframes/mybookings.png)

[Update booking](docs/wireframes/updatebooking.png)

[Delete booking](docs/wireframes/deletebooking.png)

[Register](docs/wireframes/register.png)

[Login](docs/wireframes/login.png)

### Color Scheme

The color scheme is chosen based on some car service website designs founded on [Pinterest](https://www.pinterest.com/pin/163537030209768423/) that seemed suitable for the website theme.

[Color Scheme](docs/images/colorscheme.jpeg)

### Typography

[Google Fonts](https://fonts.google.com/) was used for the following fonts: 
  * Racing Sans One for the logo on the website.
  * Roboto for the body text on the website. 

### Agile methodology

## Features
### Existing features

**Logo**

  * It is featured on all three pages on the website and is fully responsive. It allows users to go back to the home page by clicking on it. 

**Navigation bar**

  * It is featured on all three pages on website, is fully responsive and includes links to Home page, Services, Contact, Booking, Register, and Login page.  
  * Fixed on top of all three pages to allow the user to easily navigate from page to page across all devices without having to revert to the previous page via the back button or scroll up.
  * Sorted out according to priority and it is consistent in style and color to enable easy navigation.
  * To fit in one row, navigation links are in the dropdown menu on smaller screen sizes while on larger screens there is text. 
  * On larger screens, there is a row with text above the navbar which contains information about the opening time of the service and a link for booking a service. 

**The Landing Page Image**

  * The image is consistent with the theme and contains text that motivates people to use the services and has a button that leads to booking services. 

**Our services section**
  * Provides insight into the type of services that the Car Specialist provides to customers. Each type of service is presented with an icon and text. Below these icons is a link that leads to the page where the other services provided by the company are listed.
  * On the larger screens icons are positioned in one row and on smaller screens one below the other.
   
**About Section**

 * The about section will allow users to find out some information about the company and highlight its qualities, which should motivate the customers to choose this service.
  
**The Footer**

  * It is featured on all three pages on website.
  * The footer section includes a Car Specialist logo and again motivational description, useful links which lead to important pages of this webpage for easier navigation, contact information and 
  links to relevant social media sites. The social links will open to a new tab to allow easy navigation for the user.
  * The footer is valuable to the users as it provides useful links and information, and encourages them to keep connected via social media where they can be constantly updated.

**Services page**

* Follows the style from the home page and it consists of the landing image as well. It contains text which highlights the expertise and affordable prices. 
* Below the landing image is the description and a full list of services that Car Specialist provides to the customers. 

**Contact us page**
* In the upper part of the page is a contact form where the user can send a message to the Car Specialist and contact information about address, email, phone, and opening times. 
* In the lower part, there is a map that shows the (fictitious) location of the Car Specialist. 

**Book a service or when the user is logged in -> Booking dropdown menu which contains: Book a service and My bookings page**

* In case the user is not logged in, the page will show a sign-in page that informs the user to sign in to be able to make a booking.
* The logged-in user has the access to a Booking form where she/he should fill out the details about phone number, service type, day, time, and description of the issue with the car.
* All fields in the form are required and if any of them is omitted, a message is displayed. 
* In case the user chooses an already occupied time, he receives a notification to choose another. 
* Every booking needs to be approved by the admin to be valid.

**My Bookings Page**

* It shows all the bookings that the user has requested and it provides booking details: type of service, day, time, and approval status.
* On each booking, there is an option to update or delete the booking. 

**Update Booking Page**

* It provides the user with the ability to change the booking details. If the user decides to change the time, he will be informed if he has chosen an unavailable time.
* If the user changes the booking, it needs to be approved by the admin again. 
* After the changes have been made, the user will receive a success message.


**Delete Booking Page**

* If the user decides to delete the booking and clicks on the button provided on the my bookings page in booking details, 
the user will be redirected to the page which will present all booking details and will prompt the user if he is sure that he wants to delete it.
* After the changes have been made, the user will receive a success message.

**Register page**

* It allows the user to register an account. It is required that the user writes a username and password whereas the email is optional.
* It is a necessary step if the user wants to make a booking. 
* The user will receive a success message after registration. 

**Login**

* It allows the user to sign in to the account to be able to make a booking. 
* It is a necessery step if the user wants to make a booking, update or delete a booking. 
* The user will receive a success message after logging in.

### Future features

## Technologies Used

* Python version 3.8.11 - the main language used to build the back-end
* HTML- markup language used to build the front-end templates
* CSS- to style the content and provide the layout
* [Django](https://www.djangoproject.com/) - Python-based web framework that follows the model–template–views architectural pattern.
* [Bootstrap 5.3](https://getbootstrap.com/) - for customizing the webpage and making it responsive
* [Cloudinary](https://cloudinary.com/) - for cloud-based image and video management services
* [PostgreSQL](https://www.postgresql.org/) - used as a database management system
* GitHub - project repository
* Gitpod - version control
* Heroku - cloud platform for deployment, management, and scaling of the app
* [ElephantSQL](https://www.elephantsql.com/) - PostgreSQL database hosting service.
* Code Institute GitPod Full Template - Using the GitPod Full Template from the Code Institute for my project.
* [Font Awesome](https://fontawesome.com/)- used for importing the icons.
* [Tiny PNG](https://tinypng.com/)- was used to compress images.
* [Balsamiq](https://balsamiq.com/)- was used to create wireframes.
* [Google Fonts](https://fonts.google.com/) - was used to import the fonts used on the website.
* Google Dev Tools - to troubleshoot and test features, solve issues with responsiveness and styling


## Testing

  The testing document can be found [here](TESTING.md).

## Deployment

The project is deployed using Heroku. To deploy the project:


### Step 1: Installing Django and supporting libraries in the terminal:

  1. Install Django and gunicorn: `pip3 install 'django<4' gunicorn`
  2. Install supporting libraries:  `pip3 install dj_database_url==0.5.0 psycopg2`
  3. Install Cloudinary Libraries: `pip3 install dj3-cloudinary-storage`
  4. Create requirements file `pip3 freeze --local > requirements.txt`
  5. Create project(carspecialist): `django-admin startproject carspecialist . `
  6. Create App (workshop): `python3 manage.py startapp workshop`  
  7. Add to installed apps in setting.py(Save file)
  8. Migrate changes `python3 manage.py migrate`
  9. Run Server to Test `python3 manage.py runserver`

### Step 2: Deploying an app to Heroku
**Create a new external Database**

The sqlite3 database was used in the development, however, this is only available for use in development so It was required to create a new external database that can be accessed by Heroku.

  10.  Go to the ElephantSQL.com, log in, and go to the dashboard and click the create new instance button on the top right.
  11.  Name the plan (your project name is a good choice), select the tiny turtle plan (this is the free plan) and choose the region that is closest to you then click the review button.
  12.  Check the details are all correct and then click create instance in the bottom right.
  13.  Go to the dashboard and select the database just created.
  14.  Copy the URL (you can click the clipboard icon to copy).

**Heroku app setup**

  15.  From the Heroku dashboard, click the new button in the top right corner and select create new app.
  16.  Give your app a name (this must be unique), select the region that is closest to you and then click the create app button bottom left.
  17.  Open the settings tab and create a new config var of DATABASE_URL and paste the database URL you copied from elephantSQL into the value (the value should not have quotation marks around it).
  
**Attach the Database:**
  * Gitpod: 
  18. Create new env.py file on top level directory in gitpod
  * In env.py: 
  19. Import os library(import os)
  20. Set environment variables(os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL")
  21. Add in secret key(os.environ["SECRET_KEY"] = "Make up your own randomSecretKey")
  * In Heroku app:
  22. Add Secret Key to Config Vars(SECRET_KEY, “randomSecretKey”)

**Prepare our environment and settings.py file:**
  * In settings.py:
  23. Reference env.py (import os)
  24. Remove the insecure secret key and replace - links to the SECRET_KEY variable on Heroku (SECRET_KEY = os.environ.get('SECRET_KEY')
  25. Comment out the old DataBases Section and add new DATABASES Section (`DATABASES = {
   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}`)
  * In terminal:
  26. Save all files and Make Migrations `python3 manage.py migrate`

**Get our static and media files stored on Cloudinary:**
  * In Cloudinary.com: (Note: must be logged in):
  27. Copy your CLOUDINARY_URL e.g. API Environment Variable.
  * In env.py(Gitpod):
  28. Add Cloudinary URL to env.py - be sure to paste in the correct section of the link (`os.environ["CLOUDINARY_URL"] = "cloudinary://************************"`)
  * In Heroku: 
  29. Add Cloudinary URL to Heroku Config Vars
  30. Add DISABLE_COLLECTSTATIC to Heroku Config Vars (temporary step for the moment, will be removed before deployment) `e.g. DISABLE_COLLECTSTATIC, 1`
  * Gitpod
  - In setting.py: 
  31. Add Cloudinary Libraries to installed apps `INSTALLED_APPS = [ …,'cloudinary_storage',
    'django.contrib.staticfiles','cloudinary',…,]`
  32. Tell Django to use Cloudinary to store media and static files( `STATIC_URL = '/static/'
  STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
  MEDIA_URL = '/media/'
  DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'`)
  33. Link file to the templates directory in Heroku `TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')`
  34. Change the templates directory to TEMPLATES_DIR `TEMPLATES = [{…,'DIRS': [TEMPLATES_DIR], …,],},},]`
  35. Add Heroku Hostname to ALLOWED_HOSTS `ALLOWED_HOSTS = ["carspeacialist.herokuapp.com", "localhost"]`  
  36. Create procfile on the top level directory (Gitpod) and add:`web: gunicorn carspecialist.wsgi`  
  37. Add, Commit and Push
  * Heroku
  38. Deploy Content manually through Heroku (Github as deployment method,enable automatic deployments,deploy on main branch)


## Credits
### Content 

Content for the website was taken from: 
* https://www.johanssoncarservice.se/bilverkstad-stockholm-sodermalm/
* https://preview.themeforest.net/item/car-service-mechanic-auto-shop-wordpress-theme/full_screen_preview/12777824?_ga=2.233172310.978326925.1675884526-1535900306.1675677744

* Footer example borrowed from: https://mdbootstrap.com/docs/standard/navigation/footer/
* Solution on how to make the footer stay on the bottom of the page: 
(https://radu.link/make-footer-stay-bottom-page-bootstrap/)
* Solution on how to make alert message for class based view-DeleteView : https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown?noredirect=1&lq=1
* Creating a custom 404 error page : (https://stackoverflow.com/questions/17662928/django-creating-a-custom-500-404-error-page)

### Media

Photos were taken from: 
* Hero image/home page: https://images.hdqwalls.com/download/black-ford-mustang-4k-2020-e7-1920x1080.jpg
* Picture on the home page: https://www.freepik.com/premium-photo/car-lifting-equipment-garage-being-repair-fix_5034140.htm
* Hero image/services page: https://unsplash.com/photos/oNnl9IYzbug
* Image on services page: https://www.pexels.com/photo/mechanic-checking-the-engine-of-a-car-6870313/

The color scheme was inspired by these HTML template design: 
(https://creativemarket.com/etheme2/2938419-Car-Repair-Service-HTML-Template?u=ohlove&epik=dj0yJnU9SWlrRHhZOFctOENiQlBwaUN5MTd3YmU3Um1IZ0JiOGQmcD0wJm49M2JlSllfdGxQQjlsUXZTTzNrSGo1USZ0PUFBQUFBR1BnMUo4)

