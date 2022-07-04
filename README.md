# Tutotrial on Automating Testing with  Browserstack Automate  
### `We will be testing` https://bstackdemo.com/


#### Things to keep in mind while testing this website:

- This is targeted towards a `beginner level` audience
- You are using a `linux/debian` machine
- Language `Python`
- Web Automation Testing Framework `Selenium`
- Mobile Devicest being tested on: `iPhone 13 mini` and `Samsung Galaxy S20`
# Lets Go Step by Step 
## 0. Install minimum requirements
```
sudo apt-get install python3
sudo apt-get install pip
sudo apt-get update && apt-get upgrade
pip install selenium
```
## 1. Sign Up on Browserstack
> Once you do that,  go here: https://automate.browserstack.com/ and keep this page open
#### A dashboard should open up, make sure you select python


`https://www.browserstack.com/docs/automate/selenium/getting-started/python#run-your-first-test`
[detailed documentation on running tests on browserstack using python and selenium ]

## 2. Get Access Keys
### Find a drop down named Access Keys on automate.browserstack.com/dashboard 
#### An access key dropdown will give details of your dashboard's  user name and access key
#### These are crucial  for running the python scripts and viewing the output on the browserstack automate dashboard

> If you cant get it right, visit this link: 
> https://www.browserstack.com/docs/automate/selenium/getting-started/python#run-your-first-test

In there search for `command_excutor`, since browserstack  is pretty cool , it will create a sample python test script using your access-keys

```py
command_executor='https://<username>:<accesskey>@hub-cloud.browserstack.com/wd/hub
```
## 3. Run your Tests

> Okay so we have reached the main part of this tutorial now
 - `test_login.py` : Test login functionality of the website 
 - `test_cart.py`  : Test putting an item into a cart[iphone 12 and iphone XR]
#### Find the `command_executor` value into these script
> Warning: The scripts are made w.r.t. the website being tested: if you change the website, change the script as well.
#### In your linux console write:
```
python test_script.py
or
python3 test_script.py
```
> To run these tests simultaneously, first make the shell script executable and then run it:
```sh
chmod +x Test.sh
./Test.sh
```
### Now once you execute any of these commands in step3 , go and check automate.browserstack.com/dashboard


