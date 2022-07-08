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
![Screenshot (41)](https://user-images.githubusercontent.com/44931750/177943152-d254466e-85a7-433f-9ec8-e0968d0a7ab9.png)


> Find detailed documentation on running tests on browserstack using python and selenium 
> https://www.browserstack.com/docs/automate/selenium/getting-started/python#run-your-first-test

![Screenshot (42)](https://user-images.githubusercontent.com/44931750/177943239-c8d6ca26-4f3f-496b-91c8-ece40fea6a80.png)

## 2. Get Access Keys
### Find a drop down named Access Keys on automate.browserstack.com/dashboard 
#### An access key dropdown will give details of your dashboard's  user name and access key
#### These are crucial  for running the python scripts and viewing the output on the browserstack automate dashboard
![Screenshot (43)](https://user-images.githubusercontent.com/44931750/177944056-db470f36-c075-40db-b05e-b8aace1747d7.png)

> If you cant get it right, visit this link: 
> https://www.browserstack.com/docs/automate/selenium/getting-started/python#run-your-first-test

In there search for `command_excutor`, since browserstack  is pretty cool , it will create a sample python test script using your access-keys
![Screenshot (44)](https://user-images.githubusercontent.com/44931750/177945390-2a37ad77-8ee6-4566-88bd-929daebcb987.png)

```py
command_executor='https://<username>:<accesskey>@hub-cloud.browserstack.com/wd/hub
```
## 3. Run your Tests

> Okay so we have reached the main part of this tutorial now
 - `test_login.py` : Test login functionality of the website 
 - `test_cart.py`  : Test putting an item into a cart[iphone 12 and iphone XR]
#### Feed the `command_executor` value into these script
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


