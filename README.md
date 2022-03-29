# Django Interview Assignment
A django rest framework based web api's application that will be used by our candidates to implement interview assignment.

## Dependencies
This project relies mainly on Django. Mainly:
  - Python 3.8+
  - Django 3+ or 4+
  - Django Rest Framework

## Requirements:
  - Candidates expected to implement required features for a library management system based on provided scenario
  - Candidates have to implement web REST api's for each required action related to scenario
  - Proper [JWT][1] based authentication should be implemented in each protected web api endpoint
  - Ensure an user can only perform actions using apis which are allowed to the role assigned to that user


### Scenario
The are two roles in the system; `LIBRARIAN` and `MEMBER`

### As a User
  - I can signup either as `LIBRARIAN` and `MEMBER` using username and password
  - I can login using username/password and get JWT access token

#### As a Librarian
  - I can add, update, and remove Books from the system
  - I can add, update, view, and remove Member from the system
  
#### As a Member
  - I can view, borrow, and return available Books
  - Once a book is borrowed, its status will change to `BORROWED`
  - Once a book is returned, its status will change to `AVAILABLE`
  - I can delete my own account

## Nice to Have:
It will be an advantage for candidates to demonstrate the following:
  - Proper usage of Http Methods and REST practices
  - Understanding of [SOLID Principle][2]
  - Understanding of Design patterns
  - Understanding of TDD and BDD
  - Each implementation should be equipped with unit tests
  - Integration tests are require to demonstrate API usages

## **Instructions**
- [ ] Follow these steps for submission:
  1. Fork the repository in your github account
  1. Create issues and work on them in their respective branches
  1. Complete the tasks while following all instructions
  1. Create MRs and merge into main branch
  1. When done, Test if all task requirements are met and instructions followed
  1. Push code to github
  1. Deploy/Host your solution
  1. Reply to the same email with the URLs for **repo**, **hosted API** and **hosted documentation**
- [ ] `setup_instructions.md` should have all the details and instructions like how to setup and run the project
- [ ] Repo should not contain irrelevant folders/files like cache files, build/dist directories etc.
- [ ] Create API documentation using Swagger or similar framework
- For any queries please email us at [hiring@truevalueaccess.com](mailto:hiring@truevalueaccess.com)

[1]: https://jwt.io/introduction
[2]: https://en.wikipedia.org/wiki/SOLID