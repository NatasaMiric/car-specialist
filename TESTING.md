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



## Testing user Stories
## Bugs

### Fixed Bugs

* The submission of booking form did not work, it was not saved to database and it reported an error message about a field in the form. The error is fixed by removing the 'user' from the form fields and instead user data will be automatically retrieved when he loggs in.