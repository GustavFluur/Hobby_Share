# Hobby Share

Hobby Share is a community where people are able and willing to share their hobbies with others. Likewise it creates a streamline of information for the users to see what categories there are, thus encouraged to feel willing to create, and interact with various of posts from other hobby enthusiasts. Where all the uploaded and inspiring messages are their for peoples disposal. It's a representation of who you are and what interests you represents.  

![Responsitive Image](static/readme-images/readme.main.png)
[Live link to the webpage:](https://sharehobbies.herokuapp.com/)

This project is dedicated to all ages who are keen to see what kind of hobbies there are out there, the reason behind this is due to overwhelming information regular internet users are interact with on daily basis. That leads to an overload and people becomes quite depressed and having difficulties to process information out there on the internet spectrum. What Hobby Share is a platform for one category that is the share of your interests or hobbies. It's great for both young and old groups to see what kind of interests there - perhaps they all be interesting to create a sense of community on a digital platform. E.g., as it was during the launch of Facebook or Instagram, there no advertisement and other information that especially children or younger people feeling stressed about. On Hobby Share you don't need to feel stressed at all and the only thing Hobby Share want you do know is to inspire other with our own curiosity. 

## Table of Contents

* Disclaimer, there were a lack of time to make a Table of Content. That will be fixed for later, pardon for that inconvience. 

1. [User stories](#user-stories)

2. [Database Schema](#database-schema)

3. [Design Plan](#design-plan)

4. [Color Scheme](#color-scheme)

5. [Typography](#typography)

6. [Imagery](#imagery)

7. [Media](#media)

8. [Features](#features)

9. [CRUD: Create, Read, Update and Delete](#crud-create-read-update-and-delete)

10. [Bugs Report](#bugs-report)

11. [Validator Test](#validator-test)

12. [Technologies Used](#technologies-used)

13. [Deployment](#deployment)

14. [Installed Packages](#installed-packages)

15. [Features Left to Implement](#features-left-to-implement)

16. [Credits](#credits)

17. [Credits to my mentor](#credits-to-my-mentor)


# User stories: 

User Stories
Not all stories have been implemented. Some have been left for future implementations as the site grows and expands.

## Admin stories:
### As an admin:
1. I can create blog post, delete comments, users and look through all the uploads etc. 
- Story points: 3
2. I cannot grant a blog comment. 
- Story points: 2
3. I can create a log in / sign up page so that potential users can sign up to the site.
- Story points: 1
4. I must be accessible for the users to reach out to me in case of problems|issues. 
- Story points: 1
## Blogger stories:
### As an blogger:
1. I can create a user profile so that I can be found & viewed on the site.
- Story points: 2
2. I can upload blog posts so that I can share it with hobby enthusiasts.
- Story points: 4
3. I can create a post of my interest, comment and like an other user's post.
- Story points: 1
4. I can post, edit and delete my blog uploads.
- Story points: 1
5. I can add an image, write a bio and edit my profile.
- Story points: 1
6. I can easily orientate and contact the admin if any issues|problems emerges.
- Story points: 4

## Visitor stories:
### As a visitor:
1. I can visit the blog so that I can see what is new.
- Story points: 1
2. I can look see the topic and read the posts.
- Story points: 2
3. I can visit a blogger's profile site and read its bio.
- Story points: 2
4. I can orientate myself to the about page to see the purpose of website.
- Story points: 4
5. I can easily register myself to website, thus start blogging and sharing with others. 
- Story points: 1

# Database Schema

![Database Diagram](static/readme-images/database_readme.png)
- [Database diagram was made from the interactive site Creately](https://app.creately.com/d/usBCZwL48oY/edit)


# Design Plan:

The design of the Hobby Share changed along the the way but importantly is the outcome and the functions behind the webpage. 

*Disclaimer my knowledge of Balsamiq was limited for this project when it comes to the true present webpage's design. Many Apologies for that.... Both in the plan and final result of the design. 

## Homepage:

The homepage was designed like this because I wanted to create a perfect introdution for the user to feel a sense of welcome once they are visiting the page: 

![Plan Design Homepage](static/readme-images/Plan-Design-homepage.png)


### Updated & final design: 

![Updated Design Homepage](static/readme-images/update-homepage.jpg)


### About page: 

![Plan Design - About](static/readme-images/plan-design-about.png)

In the about page of my design plan I wanted to create a word art where peoples posts coherent with their categories where uploaded here. But some changes where made and I redirected my focus on wanted to create a regular about page. It became a very one and it could have become better - but it's a representation of what Hobby Share want to signaling with its target audience: 

### Updated & final design: 

![Design - About](static/readme-images/Updated-design-about.jpg)


### Login Page:

![Plan Design - Log in](static/readme-images/plan-design-sign-in.png)

The log-in page hasn't been updated nor changed when it comes to its design. 

### BlogPost:

![Plan Design Blogpost](static/readme-images/plan-design-blogpost.png)

### Updated & final design: 

![Updated Design Blogpost](static/readme-images/Update-BlogPost.jpg)

### Color Scheme:

![Color Palette](static/readme-images/color-palette.png)

# Typography:
All fonts were obtained from the Google font & Bootstrap. I chose the following fonts for the page:

[Bootstrap](https://getbootstrap.com/docs/5.0/content/typography/) & 'Times New Roman', Times, serif: 

- heading/logo, Blog & print titles
- navigation & site buttons [w3schools](https://www.w3schools.com/css/css3_shadows_box.asp)

# Imagery:

All photography for the fictional "posts" from the users, were imported from [Tomi Tokko](https://github.com/tomitokko/django-social-media-website) with [freecodecamp](https://www.freecodecamp.org/) free course on [youtube](https://www.youtube.com/watch?v=xSUm6iMtREA).

Likewise from [Pexels](https://www.pexels.com/). 

# Media 

- [Pexels](https://www.pexels.com/)
- [Main Photo](https://images.pexels.com/photos/5973966/pexels-photo-5973966.jpeg?auto=compress&cs=tinysrgb&w=1600)
- [Blog1 Post](https://images.pexels.com/photos/5644638/pexels-photo-5644638.jpeg?auto=compress&cs=tinysrgb&w=1600)
- [Blog2 Post](https://images.pexels.com/photos/1040157/pexels-photo-1040157.jpeg?auto=compress&cs=tinysrgb&w=1600)


# Features
### Existing Features:

Homepage|Uploaded Posts page: 

![Hompage1](static/readme-images/hompage.jpg)
![Hompage2](static/readme-images/hompeage2.jpg)

Paignation function:

![paignation](static/readme-images/paignation-oage.png)

Navigation Bar:

Desktop: 
![Navbar](static/readme-images/navbar-desktop.jpg)

*Disclaimer, navbar for the mobile phone was unfortunately failed cause the uploaded posts fall off, and that will be changed for later.

![Navbar-mobile](static/readme-images/navbar.mobile.jpg)

About page: 

About page with closed-Accordion:

![Aboutpage-closed-Accordion](static/readme-images/aboutpage.1.jpg)

About page with open-Accordion:

![Aboutpage-open-Accordion](static/readme-images/aboutpage.full.png)

# CRUD: Create, Read, Update and Delete

## Create: 

Only signuped users are able to create posts and profiles at Hobby Share: 

Create Post:
![Create_Post](static/readme-images/create_post.png)
* It's important to click on status button to make published:

![Test Post](static/readme-images/testpost.png)

Once you are logged into the page you can only edit & delete your own posts, there are unfortunately no warnings once you decide to remove them. Yet you can create or edit you own posts as much as you want: 

## READ

- Both visitors & logged-in members are able to orientate themselves across the website.

![read1](static/readme-images/read.1.png)

- Once you select an article of your interest e.g. "6 Reasons Why Hunting Can Be A Great Hobby to Take Up"

![read2](static/readme-images/read.2.png)
 

![read.blogpost1](static/readme-images/read.blogpost.1.png)
![read.blogpost2](static/readme-images/read.blogpost.2.png)
- You are able to read the whole blog post and see the whole content what the blogger has created. In this example it has been taking from how it is on a desktop.

![read.blogpost3](static/readme-images/read.blogpost.3.png)

- However, in this example above it being presented of a user who is logged in to Hobby Share. You are unable to comment, edit and delete the post until you register yourself to the website. 

- Please look at the example below: 

![read.no-comment](static/readme-images/read.no-comment.png)

## EDIT/Update

Once you click on the edit button you come to this page:
![status-publish](static/readme-images/status-publish.png)

![Edit Post](static/readme-images/EditPost.png)

Once you want to delete a post, you will redirected to the home page or uploaded posts:

Before you have pressed delete button: 

![Delete Post](static/readme-images/beforedelete.png)

After you have pressed delete button:

![After Delete Post](static/readme-images/afterdelete.png)

## Contact|Support Page:

![Contact|Support Page](static/readme-images/contact%7Csupport.oage.png)

Profile Page:

![Profile Page](static/readme-images/Profile%20Page.png)

Logout Page:

![Logout Page](static/readme-images/Logoutpage.png)

Register Page:

![SignUp](static/readme-images/signup-register.png)


# Bugs Report

# 1.

A common mistake is to type the right commands in the terminal and have the files in the project. That mistake can be done easily once you are typing all the commands into the terminal that is necessary for making the website work. 

### The message you receive in the terminal : 
    django.core.exceptions.ImproperlyConfigured: In order to use cloudinary storage, you need to provide CLOUDINARY_STORAGE dictionary with CLOUD_NAME, API_SECRET and API_KEY in the settings or set CLOUDINARY_URL variable (or CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET variables).

### If you lose the workspace on gitpod it can sometimes be very problematic since you need to restart the working process and adding all the important elements, files, imports etc. into the workspace all over again.

### In the env.py file (which is secret for non-authorized developers can't access to) must add these into the file:

        import os

        os.environ["envpy_test"] = 'envpy'
        os.environ["DATABASE_URL"] = "postgres://################################################################"
        os.environ["SECRET_KEY"] = "##############################"
        os.environ["CLOUDINARY_URL"] = "cloudinary://####################################"

The env.py file wasn't added into this workspace thus the error emerged. Besides I used wrong command and missed "runserver" => python3 manage.py runserver.

# 2.

## In the file: create_post.html

###   Error
    form class="create-post" id="create_post_form" method="post" action="{% url 'create_post' %}"

The data wasn't registrated from the form and the images wasn't uploaded to the home page. However, in the database demonstrated from tableplus it was registrated there and as well as in the django administration page. 

### Fixed Error
    form class="create-post" id="create_post_form" method="post" enctype="multipart/form-data" action="{% url 'create_post' %}"

The issue was resolved by adding the enctype attribute and everything was finally added into the data, which the user was now able to post images related to their blogpost. It was required to have this feature cause without it would create a bad user experience and the purpose of the website wouldn't meet up to its expectations.   

# 3.

#### views.py

#### Errors
##### CRUD: 
class CreatePost(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "create_post.html", 
            {
                "form": PostForm()
            },
        )
        

    def post(self, request, *args, **kwargs):

        post_form = PostForm(request.POST)

Related to the issue above in terms of uploading and creating posts, it was unable to pin a image into the your own blog. Thanks to no request.FILES where added in the function. That generated the problems to store data for user's benefit and see were it went. 


## Fixed Error

class CreatePost(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "create_post.html", 
            {
                "form": PostForm()
            },
        )
        

    def post(self, request, *args, **kwargs):

        post_form = PostForm(request.POST, request.FILES)

By added request.FILES in the post form it was finally resolved by adding this missing feature. Once something is missing it creates error and thanks to the documentation from the terminal it gave the path of a good result to determine where the bug was. 

# 4.


In the register page of the Hobby Share, it created an error due some issues regards to the settings.py file and that led to some errors along the way of project's process:

- The a new potential user is trying to set up a new account:

![Typing in the email](static/readme-images/error-try-signup-with-email.png)
- Error message:

![Error Message](static/readme-images/error-message-after-signup.png)

## settings.py

### First Issue: 
ACCOUNT_EMAIL_VERIFICATION = False

### First change & failed: 
ACCOUNT_EMAIL_VERIFICATION = True

### Result: 

![ConnectionRefusedError:](static/readme-images/error_message.no-signup-with-email.png)

### Final and solution: 
ACCOUNT_EMAIL_VERIFICATION = 'none'

##### Another error of the CRUD

While working with CRUD function it was some issues to add the delete one, since I was doing the same changes and added the same functions with different attributes, names etc it gave me an error. It send the information on my website: http 405 which meant that no right method has been used and the website crashed. It also was a late night and it led on layers of more issues and a sense of feeling that you were stuck in a loop of bad repetion. 

#### Error:


class PostDelete(View):

    def get(self, request, id, *args, **kwargs):
        post = get_object_or_404(post.id)
        post.delete()

        return HttpResponseRedirect(reverse('home'))
    
##### Fixed Error

    class PostDelete(View):

        def get(self, request, id, *args, **kwargs):
            post = get_object_or_404(Post, id=id)
            post.delete()

            return HttpResponseRedirect(reverse('home'))

# Validator Test

- [Pep8online](http://pep8online.com/) is unfortunately unaccessible at this time, the only source of test I was able to make for this project was look through my terminal or the installed pep8 compliant. (Directed from the Tut support)

- ![In the termial it shown only 9 problems](static/readme-images/pep8-from-terminal.jpg) but it won't affect the workspace nor the function of the code. Because the characters of the text is too long but it the final result is acting as expected, therefore reach up to its goal of this project. 

All html files were passed by [W3C Validator](https://validator.w3.org/)

- Errors that were discovered were the {%%} & {{}} tags. Those are required to make the webpage work. As well as other errors that won't hurt the projects main objective, e.g. "Non-space characters found without seeing a doctype first. Expected". These can be changed but the outcome to make the page work with all its functions is the main goal here. 

- CSS file didn't detect any errors either in [Jigsaw validator](https://jigsaw.w3.org/css-validator/), since I am Swedish and Jigsaw seems to only show messages on my language at this time - (don't know how to change it) - I swear it says that no error are shown in the css file: 

![JigSaw-Validator-image](static/readme-images/Jigsaw%20validator-swedish.jpg)

* Hobby Share was demonstraded and portrayed these stats in Lighthouse:

![Lighthouse-stats](static/readme-images/lighthouse-stat.jpg)

# Technologies Used

### Main Languages Used
- HTML5
- CSS3
- Javascript
- Python
- Django
- SQL - Postgres

### Frameworks, Libraries & Programs Used
- Google Fonts - for the font families:
- [Font Awesome](https://fontawesome.com/icons) - to add icons to the social links in the footer element.
- GitPod - to create my html files & styling sheet before pushing the project to Github.
- GitHub - to store my repository for submission.
- [Balsamiq](https://balsamiq.com/) - were used to create mockups of the project prior to starting.
- [Am I Responsive?](https://ui.dev/amiresponsive) - to ensure the project looked good across all devices.
- [Favicon](https://icons8.com/icons/set/lightbulb) - to provide the code & image for the icon in the tab bar.
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Database Design Tool | Creately](https://creately.com/diagram-type/database-design/)
- Preview (macOS) was used for this README.md file and its design features for images only 


# Deployment
### The site was deployed to Heroku. The steps to deploy are as follows:

# GitHub|GitPod Terminal

- Install Django & Gunicorn: pip3 install 'django<4' gunicorn
- Install Django database & psycopg: pip3 install dj_database_url psycopg2
- Install Cloudinary: pip3 install dj3-cloudinary-storage
- Creating the requirements.txt file with the following command: pip3 freeze --local > requirements.txt
    a django project was created using: django-admin startproject printstatements .
    the blog app was then created with: python3 manage.py startapp blog
    which was then added to the settings.py file within our project directory.
- The changes were then migrated using: python3 manage.py migrate

# Heroku part 1

- Heroku & created a new app called Share_Hobby added the Heroku Postgres database to the Resources tab.

The Settings Tab, to add the following key/value pairs to the configvars:
key: SECRET_KEY | value: randomkey
key: PORT | value: 8000
key: CLOUDINARY_URL | value: API environment variable
key: DATABASE_URL | value: value supplied by Heroku

# GitPod: env.py file

1. added the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the env.py file

2. added the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the settings.py file

3. add an import os statement for the env.py file.

4. added Heroku to the ALLOWED_HOSTS in settings.py

# Procfile

created the Procfile

pushed the project to Github

# Heruko part 2

connected my github account to Heroku through the Deploy tab

connected my github project repository, and then clicked on the "Deploy" button

The live link for "Hobby Share" can be found HERE

# Installed Packages:

#### One you install all the packages on the terminal you need to use "pip3 install" and please follow all the steps below:   
#

1. pip3 install 'django<4' gunicorn

2. pip3 install dj_database_url psycopg2 [More info:](https://pypi.org/project/dj-database-url/)

3. pip3 install dj3-cloudinary-storage [More info:](https://pypi.org/project/dj3-cloudinary-storage/)

4. pip install django-allauth [More info:](https://django-allauth.readthedocs.io/en/latest/installation.html)

5. pip install django-summernote [More info:](https://summernote.org/) 

6. pip install django-crispy-forms [More info:](https://django-crispy-forms.readthedocs.io/en/latest/index.html)

7. pip install Pillow [More info:](https://pypi.org/project/Pillow/)



# Features Left to Implement

## Home page:
### Users will be able to:

- search hobbies from a search bar.
- use tags.
- see what is trending.  

## Profile page:
### Users will be able to:

- chat, follow - and unfollow others.
- see how many followers and posts you a user has on its profile.
- see on a user's profile page which uploaded posts are related to them.
- delete their profile.

## Register page: 
### select more categories:

- Nationality
- Gender
- Signup page goes align with creating a profile page.
- Structurized design regards to the about and profile page.  



# Credits

- [I think and therefore I blog - Walkthrough Project](https://github.com/Code-Institute-Solutions/Django3blog/tree/master/12_final_deployment) & [Website: ](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/)
- [Django Blog Application - Full Tutorial 2022](https://www.youtube.com/watch?v=I8TRkEcw9Mg)
- [Django For Everybody - Full Python University Course](https://www.youtube.com/watch?v=o0XbHvKxw7Y)
- [Build a Social Media App with Django – Python Web Framework Tutorial](https://www.youtube.com/watch?v=xSUm6iMtREA)
- [Codemy.com -Create A Simple Django Blog ](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)


# Credits to my mentor
I want to thank my mentor on Code Institute, who guide me to build a new and structured Codeblock. Without her support, advice and inspiration it would have been much harder to understand what I missed:

- Martina Terlevic






