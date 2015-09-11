## Step #4

<<<<<<< HEAD
### Implement a login function and logged in decorator
- Create the login page
  - Login form
  - Login html
  - login_success temporary page
  - Add db check of credentials
  - Add user to the session
  - Add error message to login page

- Create a login decorator
  - Add user decorators.py
  - Import user.decorators login_required to user and add to login_success
  - Add next query param to session
  - Add check if next session to redirect there
  - Add login_required decorator to /admin
=======
### Create the blog models.py
- Create a blog class with the name and admin
- Add an email field to the author form
- Add blog.models and run dbinit

### Create the admin route and check if there's a blog
- If not, present a form to create the blog and admin
- Create a template/blog/admin.html and add a flashed message iterator
>>>>>>> step-3
