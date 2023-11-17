# Age of Learning Coding challenge

## Objective:
Implement the test case below

## Instructions:
1.  Use programming language (C#, Java or Python) and testing library of your choice (i.e. Python & Pytest, Java & TestNG)
2.	Use UI automation library like Selenium (preferably).
3.	Implementation should be clear and preferably show the skills of page object model, set up of “BaseTestCase” class, test method is set up in separate class, url, and email address is read from config file.
4.	Run the test
5.	Test case results could be returned on IDE console.

## Task Prompt:
You may encounter some changes on the homepage, so please adjust your test accordingly.
* Go to https://www.abcmouse.com
* Click “Sign Up” button
* Verify that  https://www.abcmouse.com/abt/register page is returned
* Enter Email address (any email address)
* Click “Submit” button
* Verify that https://www.abcmouse.com/abt/subscription page is returned.
* Verify that on subscription page, “Become a Member!” text is rendered.

## Run steps
* poetry install
* poetry shell
* run the tests with `pytest --headed`
