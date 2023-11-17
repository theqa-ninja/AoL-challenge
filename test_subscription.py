from faker import Faker
from playwright.sync_api import Page, expect

fake = Faker()

def test_SignUp(page: Page):
    # Go to https://www.abcmouse.com
    page.goto("https://www.abcmouse.com")

    # If we get "Please verify you are a human" check on h1 tag, fail
    expect(page.get_by_role("heading", level=1, name="Please verify you are a human")).not_to_be_visible(timeout=5000)

    # Click “Sign Up” button (Located it by the aria-label)
    page.get_by_label("Sign Up for ABCmouse.com").click(timeout=5000)

    # Verify that  https://www.abcmouse.com/abt/register page is returned
    # changed this to https://www.abcmouse.com/abc/prospect-register/ per the manual test of this page
    expect(page).to_have_url("https://www.abcmouse.com/abc/prospect-register/")

    # Enter Email address (any email address)
    # generate fake e-mail
    email = fake.email()
    # locate & fill out by aria-label
    page.get_by_label("Edit box, Email Address, Enter your email address. This is a required field.").fill(email, timeout=5000)

    # Click “Submit” button
    page.get_by_role("button", name="Submit your email address to begin.").click(timeout=5000)

    # Verify that https://www.abcmouse.com/abt/subscription page is returned.
    expect(page).to_have_url("https://www.abcmouse.com/abc/subscription/")

    # Verify that on subscription page, “Become a Member!” text is rendered.
    # verify the e-mail entered on the last page matches the one displayed here
    expect(page.locator("#email-input")).to_have_value(email, timeout=5000)
    # verify we're offered to Try it FREE for 30 days!
    expect(page.get_by_role("heading", level=2, name="Try it FREE for 30 days!")).to_be_visible(timeout=5000)
