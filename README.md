# Guest Review Management
### A Class 12 CS project

Guest review management in hotels is the process of collecting and analyzing feedback from guests about their stay at a hotel or other hospitality facility. This feedback can be used to identify areas for improvement and optimize the guest experience, as well as to build a positive reputation and attract new customers.

To manage guest reviews effectively, hotels can use a software solution that automates and streamlines the process of collecting and analyzing feedback. One way to develop such a solution is to use Python, a popular programming language, and MySQL, an open-source database management system.

# User Management

 - Super User 
 - House Keepers
 - Guest

# Working and setting up

**[1]  Initial Setup**

➔ **Super Admin End (Hotel)**

	○ The Super admin (Hotel Manager) should create an account

	○They should register the rooms within the account

	○Admin Should Register housekeepers (Staff) and assign rooms to them

	○Once this is finished, the hotel is equipped with Guest management system

➔ **User End (Guest)**

	○User should create an account

	○ They should choose which room are they staying in

	○ Now initial guest setup is done

**[2]  Giving Reviews**

	● This is done by the guest

	● They got 5 questions to rate the amenities + they can add more suggestion to the review

**[3]  Receiving and Analyzing Reviews**

	Once the review is done the Admin and housekeepers can view and analyze it through the admin dashboard

# Installation
First u have to create the databases in MySql by these Commands:
1.For The Reviews

    CREATE  TABLE reviews(
    review_uid VARCHAR(255) PRIMARY  KEY,
    hk_uid VARCHAR(255),
    sa_uid VARCHAR(255),
    dateAndTime DATETIME,
    room int,
    meal int,
    hospitality int,
    washroom int,
    overall int,
    remarks VARCHAR(255));

2.For Managing Users

    CREATE  TABLE userdetails(
    user_uid VARCHAR(255) PRIMARY  KEY,
    username VARCHAR(255) UNIQUE,
    password  VARCHAR(255),
    name  VARCHAR(255),
    user_role VARCHAR(255),
    sa_uid VARCHAR(255));

3.For Managing Different Hotels

    CREATE  TABLE hslocations(
    hsl_uid VARCHAR(255) PRIMARY  KEY,
    sa_uid VARCHAR(255) NOT  NULL,
    hk_uid VARCHAR(255),
    place_name VARCHAR(255) UNIQUE);

## Now Run the code(main.py) with python and :)
# Made with ❤️ by Rishi, Hamda, Leen, Sidhan, Ziya 
