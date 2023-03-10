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
| Home Page | Pass| [Home Page Validation](docs/images/homepagevalidation.png) |
| Services Page | Pass | [Services Page Validation](docs/images/servicespagevalidation.png) |
| Contact Us Page | Pass | [Contact Us Page Validation](docs/images/contactpagevalidation.png) |
| Book a Service Page | Pass | [Book a Service Page Validation](docs/images/bookservicevalidation.png) |
| My Bookings | Pass |[My Bookings Page Validation](docs/images/mybookingspagevalidation.png) |
| Update Booking Page | Pass | [Update Booking Validation](docs/images/updatepagevalidation.png)|
| Delete Booking Page| Pass | [Delete Booking Page Validation](docs/images/deletepagevalidation.png) |
| Register Page | Pass | [Register Page](docs/images/registerpagevalidation.png) |
| Login Page | Pass | [Login Page](docs/images/loginpagevalidation.png) |
| Logout Page | Pass | [Logout Page](docs/images/logoutvalidation.png) |
| Success Page | Pass | [Success Page](docs/images/successpagevalidation.png) |

* CSS

    * It passes the validation [CSS validation](docs/images/cssvalidation.png)

### Lighthouse
## Testing user Stories
## Bugs

* The submission of booking form did not work, it was not saved to database and it reported an error message about a field in the form. The error is fixed by removing the 'user' from the form fields and instead user data will be automatically retrieved when he loggs in.