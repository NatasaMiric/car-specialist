# TESTING

* [Manual testing](#Manual-testing)
* [Validator Testing](#Validator-testing)
    * [Lighthouse](#Lighthouse) 
* [Testing User Stories](#Testing-user-stories)
* [Bugs](#Bugs)



## Manual testing
## Validator testing

The [W3C validator](https://validator.w3.org/) was used to validate all HTML pages and [Jigsaw](https://jigsaw.w3.org/css-validator/) to validate CSS. As the site is created with Django and utilises Django templating language within the HTML, I have checked the HTML by inspecting the page source and then running this through the validator.

* HTML

| Page | Result | Evidence |
| :--- | :--- | :---: |
| Home Page | Pass| [Home Page Validation](docs/testing/validation/homepagevalidation.png) |
| Services Page | Pass | [Services Page Validation](docs/testing/validation/servicespagevalidation.png) |
| Contact Us Page | Pass | [Contact Us Page Validation](docs/testing/validation/contactpagevalidation.png) |
| Book a Service Page | Pass | [Book a Service Page Validation](docs/testing/validation/bookservicevalidation.png) |
| My Bookings | Pass |[My Bookings Page Validation](docs/testing/validation/mybookingspagevalidation.png) |
| Update Booking Page | Pass | [Update Booking Validation](docs/testing/validation/updatepagevalidation.png)|
| Delete Booking Page| Pass | [Delete Booking Page Validation](docs/testing/validation/deletepagevalidation.png) |
| Register Page | Pass | [Register Page](docs/testing/validation/registerpagevalidation.png) |
| Login Page | Pass | [Login Page](docs/testing/validation/loginpagevalidation.png) |
| Logout Page | Pass | [Logout Page](docs/testing/validation/logoutvalidation.png) |
| Success Page | Pass | [Success Page](docs/testing/validation/successpagevalidation.png) |
| 404 error Page | Pass | [404 error Page](docs/testing/validation/404validation.png) |

* CSS

    * It passes the validation [CSS validation](docs/testing/validation/cssvalidation.png)

### Lighthouse

I have used Googles Lighthouse testing to test the performance, accessibility, best practices and SEO of the site.

* Desktop results

| Page | Result |
| :--- | :--- |
| Home Page | ![Home Desktop Lighthouse Testing](docs/testing/lighthouse/desktophome.png) |
| Services Page | ![Services Desktop Lighthouse Testing](docs/testing/lighthouse/desktopservices.png) |
| Contact Page | ![Contact Desktop Lighthouse Testing](docs/testing/lighthouse/desktopcontact.png) |
| Book a service Page | ![ Book a service Desktop Lighthouse Testing](docs/testing/lighthouse/desktopbooking.png) |
| My Bookings Page | ![ My Bookings Desktop Lighthouse Testing](docs/testing/lighthouse/desktopmybookings.png)|
| Update Page | ![ Update Desktop Lighthouse Testing](docs/testing/lighthouse/desktopupdate.png) |
| Delete Page | ![ Delete Desktop Lighthouse Testing](docs/testing/lighthouse/desktopdelete.png) |
| Register Page | ![ Register Desktop Lighthouse Testing](docs/testing/lighthouse/desktopregister.png) |
| Login Page | ![ Login  Desktop Lighthouse Testing](docs/testing/lighthouse/desktoplogin.png) |
| LogoutPage | ![ Logout Desktop Lighthouse Testing](docs/testing/lighthouse/desktoplogout.png) |



* Mobile results

| Page | Result |
| :--- | :--- |
| Home Page | ![Home Mobile Lighthouse Testing](docs/testing/lighthouse/mobilehome.png) |
| Services Page | ![Services Mobile Lighthouse Testing](docs/testing/lighthouse/mobileservices.png) |
| Contact Page | ![Contact Mobile Lighthouse Testing](docs/testing/lighthouse/mobilecontact.png) |
| Book a service Page | ![ Book a service Mobile Lighthouse Testing](docs/testing/lighthouse/mobilepbooking.png) |
| My Bookings Page | ![ My Bookings Mobile Lighthouse Testing](docs/testing/lighthouse/mobilemybookings.png)|
| Update Page | ![ Update Mobile Lighthouse Testing](docs/testing/lighthouse/mobileupdate.png) |
| Delete Page | ![ Delete Mobile Lighthouse Testing](docs/testing/lighthouse/mobiledelete.png) |
| Register Page | ![ Register Mobile Lighthouse Testing](docs/testing/lighthouse/mobileregister.png) |
| Login Page | ![ Login  Mobile Lighthouse Testing](docs/testing/lighthouse/mobilelogin.png) |
| LogoutPage | ![ Logout Mobile Lighthouse Testing](docs/testing/lighthouse/mobilelogout.png) |



## Testing User Stories

| As a/an | I want to be able to ... | So that I can... | How is this achieved? | Evidence |
| :--- | :--- | :---| :--- | :---: |
| Registered user | book a service |  book the time for service | If the user is logged in, he should be able to click on Book Now button that is located on the landing page or click on Booking that is located in navbar and then click on Book a service. This action will take the user to the page where is located the booking form. User should fill out all the details and click on Book button below the form. In case the user is not logged in and goes to Book a service page, he will be redirected to login page | :---: |
| Registered user | choose a service type from the list when creating a booking |  I have a better overview of all services provided in the workshop | When the user clicks on the service type field in the Book a service form, then appears a list where he can select the desired service | :---: |
| Registered user | to choose a time in my booking | choose the time to drive my car to the service that suits me best| User can choose a date and select offered time when he click on time field in Book a service form | :---: |
| Registered user | see my bookings  | remind myself and check booking details | If the user is logged in, he should be able to click on Booking in navbar and then choose and click on My bookings where he will find all requested bookings | :---: |
| Registered user | update my booking | make necessary changes in booking details and change date, time or type of service that I want | User should be able to click on My bookings page where he will find all his bookings and click on Update button on the booking that he wants to change and each field can be changed to another value | :---: |
| Registered user | delete my booking | cancel my booking| User should be able to click on My bookings page where he will find all his bookings and click on Delete button that will lead user to the page on which he will be prompt if he is sure that he wants to delete booking and he will see all booking details | :---: |
| Registered or anonymous user | contact the workshop | send a message through the website to the workshop and get the information that I need | There is a link in navbar with the name Contact Us where the user should click and he will be redirected to contact page where is the contact form. User should fill out all required details and click on Send button underneath the message field  | :---: | 
| Registered user |log in to my account | manage my bookings| User should be able to find the Login link in navbar and when he click on it he will see the sign in form where he should fill all required fields and click on Sign in | :---: |
| Anonymous user |  register an account  | manage my bookings | User should be able to find the register link in navbar and when he click on it he will see the sign up form where he should fill all required fields and click on Sign up | :---: |
| Admin | approve or disapprove bookings | manage all the appointments| Admin should go to admin page,log in and he will see admin panel where he should be able to click on Bookings. On Bookings page should be listed all registered bookings and when the admin clicks on certain booking, he will see all the details and on the bottom is approved checkbox where he should click if he wants to approve the booking and then click save. There is also an option for approval above the booking list which gives possibility to select several bookings from the list and approve them in the same time by clicking on that empty field, click on approved and then click 'go' | :---: |

## Bugs

### Fixed Bugs

* The submission of booking form did not work, it was not saved to database and it reported an error message about a field in the form. The error is fixed by removing the 'user' from the form fields and instead user data will be automatically retrieved when he loggs in.