# Password Locker

### 22nd Oct. 2021

## Author

#### [Ezekiel Kibiego](https://github.com/ezekielkibiego)
### Description

This is an application that allows the user to store different accounts' Login Passwords by creating an account that securely stores those credentials. The user can store as many credentials as possible and can delete any or all of them at any time.

## Screenshot

<img src="assets/Screenshot from 2021-10-25 00-28-31.png">

## User Stories
The user would like to;
* To create an account for the application or log into the application.
* Store my existing acounts login details for various accounts that I have registered for.
* Generate new password for an account that I haven't registered for and store it with the account name.   
* Delete stored account login details that I do not want anymore.

## Setup Requirements

- Git
- Python3.8
- Pip

### Running the Application and cloning the repository

In your terminal:

```
git clone https://github.com/ezekielkibiego/Password-Locker.git
```

```
cd Password-Locker
```

```
chmod +x run.py
```

```
./run.py
```

## Behaviour Driven Development

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./run.py```|  <br>* ca ---  Create New Account * lg ---  login to your Account |
|Select  ca| input username and password| Bravo ```username```!, You've created Account successfully. lg to SignIn to your account
 Your password is: ```password```|
|Select lg | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new detail in the application| Enter ```1```|Enter Account, username, password<br>choose ```2``` to enter your password or ```1``` for the application to generate a password for you |
|Display all stored credentials | Enter ```2```|A list of all credentials that has been stored or ```Oops! No accounts saved yet!``` |
|Find a stored credential based on account name|Enter ```2```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```3```|Enter the account name of the Credentials you want to delete and returns Detail with media name '{account_name_to_delete}' has been deleted, if the account has been deleted and Detail with media name '{account_name_to_delete}' does not exist if the account doesn't exixt|
|Sign Out | Enter ```4```| You have successfully Signed out|
|Exit the application| Enter ```ex```| Thank you for using our app, Bye and the application exits |


### Technologies Used

- Python3.8

## Known Bugs

No known bugs so far

## Support and Contact Details

To make a contribution to the code used or for any queries feel free to contact me via my email addresses ezekiel.nyambane@student.moringaschool.com or kibiezekiel@gmail.com

## License

### MIT LICENCE

Copyright (c) 2021 Ezekiel Kibiego ~ Moringa School

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.