Firstly I have setup django framework
Then I have installed rest_framework
Then add rest_framework to INSTALLED_APPS of settings.py in my project
Then I have created a separate app name user.
In User app I have created model for Profile which inherits User of django.contrib.auth
Inside Profile i created a extra boolean fields which differentiates between member and librarian
I have installed PyJWT library for JWT token
I have created different apies for all operations of users apps in urls.py and write their business logics in views.py of users app.
Firstly New user will register himself using a username and password, then he also have to pass a boolean variable, is_librarian, set True if the registering user is librarian else False.
Then User will login to project with username and password, as he will login, a JWT token will be created by encoding to his userid, the same token will be stored in cookie of the browser so, that in each operaion that JWT tokwen will authenticate the user.
As User will logout, JWT will be removed from cookies.
Then, i created a another app named library which handles each and every operation of libary.
Created model for it which contains various field i.e, book name, price, auther, status, issued_by
Then created serializer for both the apps or model to serialeze the object data
Then created all apies for all operations like create, update, view, issue or submit books in urls.py
I have created a different class to check the authentication of requested user and also to check is he librarian or not.
Tested all the operations by using postman.