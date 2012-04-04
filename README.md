Welcome to Project Conga
=========================

Hi! We're working on "EngSci Courses", codenamed *Project Conga*. In a sense, it's the spiritual successor to
engsci.unavoidable.ca (which I'm sure you guys have used before). 

Our first launch of Project Conga will be focused on providing a hassle-free, dead-easy note-sharing experience
for all of us EngScis. We hope to get this up by Saturday. So we *need* your help!

If you're here, you've probably been "recruited" here through other means. So you know what to do next.

So have fun everyone!

[What the site looks like for now](http://i.imgur.com/E31Ek.jpg)

Instructions to demo the site on a local dev server.

1. To run this site, install python and django per the instructions on this site: https://docs.djangoproject.com/en/1.3/intro/install/

2. Install django registration from http://bitbucket.org/ubernostrum/django-registration/ and follow the built in docs to install it.

3. Install django filetransfer from http://www.allbuttonspressed.com/projects/django-filetransfers and follow the documentation on the site to install it.

4. download and unzip this repo onto your computer.

5. in the folder you unziped to, create three new folders, one named mediafiles, another named database, and one named dev. Then create a folder called email_output in dev.

6. run the manage.py file with the command line argument: syncdb.

7. follow the command line instructions to create your admin account.

8. run the manage.py file with the command line argument: runserver.

9. go to http://127.0.0.1:8000/ and http://127.0.0.1:8000/admin/ to try things out. login with the admin account you just created.
