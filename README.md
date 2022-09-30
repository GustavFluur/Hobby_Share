# Hobby Share

Hobby Share is a community where people are able and willing to share their interests - or hobbies. It creates a streamline of information for user to create, and interact with various of posts from other hobby enthusiasts. Where all the uploaded news and sharing messages are their for peoples disposal.  

![Responsitive Image](static/readme-images/readme.main.png)


# Database Schema: 

![Database Diagram](static/readme-images/database_readme.png)

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

# Bugs

# 1

#### create_post.html

##### Error
    form class="create-post" id="create_post_form" method="post" action="{% url 'create_post' %}"

The data wasn't registrated from the form and the images wasn't uploaded to the home page. However, in the database demonstrated from tableplus it was registrated there and as well as in the django administration page. 

##### Fixed Error
    form class="create-post" id="create_post_form" method="post" enctype="multipart/form-data" action="{% url 'create_post' %}"

The issue was resolved by adding the enctype attribute and everything was finally added into the data, which the user was now able to post images related to their blogpost. It was required to have this feature cause without it would create a bad user experience and the purpose of the website wouldn't meet up to its expectations.   

# 2

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


##### Fixed Error

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

# 3

## settings.py
The user was unable to register a new account due in the settings.py

### First Issue: 
ACCOUNT_EMAIL_VERIFICATION = False

### First change & failed: 
ACCOUNT_EMAIL_VERIFICATION = True

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



# Credits

- [I think and therefore I blog - Walkthrough Project](https://github.com/Code-Institute-Solutions/Django3blog/tree/master/12_final_deployment) & [Website: ](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/)
- [Django Blog Application - Full Tutorial 2022](https://www.youtube.com/watch?v=I8TRkEcw9Mg)
- [Django For Everybody - Full Python University Course](https://www.youtube.com/watch?v=o0XbHvKxw7Y)
- [Build a Social Media App with Django – Python Web Framework Tutorial](https://www.youtube.com/watch?v=xSUm6iMtREA)

# Media 

- [Pexels](https://www.pexels.com/)
- [Main Photo](https://images.pexels.com/photos/5973966/pexels-photo-5973966.jpeg?auto=compress&cs=tinysrgb&w=1600)
- [Blog1 Post](https://images.pexels.com/photos/5644638/pexels-photo-5644638.jpeg?auto=compress&cs=tinysrgb&w=1600)
- [Blog2 Post](https://images.pexels.com/photos/1040157/pexels-photo-1040157.jpeg?auto=compress&cs=tinysrgb&w=1600)
