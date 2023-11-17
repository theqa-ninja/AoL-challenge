from faker import Faker
from playwright.sync_api import Page, expect
import json

fake = Faker()

with open('test_data.json') as data_file:
    file_contents = data_file.read()

data = json.loads(file_contents)

import pdb; pdb.set_trace()

def test_SignUp(page: Page):
    # Go to https://www.abcmouse.com
    page.goto(data["starting_url"])

    # If we get "Please verify you are a human" check on h1 tag, fail
    expect(page.get_by_role("heading", level=1, name="Please verify you are a human")).not_to_be_visible(timeout=5000)

    # Click “Sign Up” button (Located it by the aria-label)
    page.get_by_label("Sign Up for ABCmouse.com").click(timeout=5000)

    # Verify that  https://www.abcmouse.com/abt/register page is returned
    # changed this to https://www.abcmouse.com/abc/prospect-register/ per the manual test of this page
    expect(page).to_have_url(data["signup_url"])

    # Enter Email address (any email address)
    # generate fake e-mail
    email = fake.email()

    # if we really want to load then uncomment next line
    # email = data["email"]

    # locate & fill out by aria-label
    page.get_by_label("Edit box, Email Address, Enter your email address. This is a required field.").fill(email, timeout=5000)

    # Click “Submit” button
    page.get_by_role("button", name="Submit your email address to begin.").click(timeout=5000)

    # Verify that https://www.abcmouse.com/abt/subscription page is returned.
    expect(page).to_have_url(data["submitted_url"])

    # Verify that on subscription page, “Become a Member!” text is rendered.
    # verify the e-mail entered on the last page matches the one displayed here
    expect(page.locator("#email-input")).to_have_value(email, timeout=5000)
    # verify we're offered to Try it FREE for 30 days!
    expect(page.get_by_role("heading", level=2, name="Try it FREE for 30 days!")).to_be_visible(timeout=5000)
