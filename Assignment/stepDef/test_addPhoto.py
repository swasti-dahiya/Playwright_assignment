import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import expect

from Assignment.pageObject.login import LoginPage
from Assignment.pageObject.addPhoto import AddPhotograph

scenarios("../features/personalDetails.feature")

@given("user is already logged in")
@given("user is already logged in and My Info page")
def given_user_logged_in(page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    username = "Admin"
    password = "admin123"

    login_page = LoginPage(page)
    login_page.login(username, password)

    try:
        page.get_by_role("button", name="OK").click(timeout=5000)
    except:
        pass

    page.wait_for_url("**/dashboard/**")

    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    page.get_by_text("My Info").click()
    page.wait_for_url("**/viewPersonalDetails/**")
    expect(page.get_by_role("heading", name="Personal Details")).to_be_visible()

@when("user navigate to my profile")
def navigate_to_profile(page):

    page.get_by_text("My Info").click()
    page.wait_for_url("**/viewPersonalDetails/**")
    expect(page.get_by_role("heading", name="Personal Details")).to_be_visible()

@when("user update personal details")
def update_personal_details(page):
    expect(page.get_by_role("heading", name="Personal Details")).to_be_visible()
    edit_btn = page.locator("button:has-text('Edit')")

    if edit_btn.count() > 0:
        edit_btn.first.click()
    else:
        print("Edit button not found. Already in edit mode.")

    first_name = page.locator("input[name='firstName']")
    expect(first_name).to_be_enabled()

    first_name.fill("new")
    middle_name = page.locator("input[name='middleName']")
    middle_name.fill("test")

    last_name = page.locator("input[name='lastName']")
    last_name.fill("user")

    save_btn = page.locator("button:has-text('Save')")
    expect(save_btn).to_be_visible()
    save_btn.click()

@when("user upload image")
def upload_image(page):

    image = page.locator("img.employee-image")
    image.click()
    page.wait_for_url("**/viewPhotograph/**")
    expect(page.get_by_text("Change Profile Picture")).to_be_visible()
    add_photo = AddPhotograph(page)
    add_photo.addPhotograph()

@then("user should be able to view his profile")
def verify_profile(page):

    expect(page.get_by_role("heading", name="Personal Details")).to_be_visible()


@then("successfully updated pop up should come")
def verify_update_popup(page):

    expect(page.locator(".oxd-toast")).to_be_visible()


@then("image should be successfully updated")
def verify_image_uploaded(page):

    success_toast = page.get_by_text("Successfully Updated")
    expect(success_toast).to_be_visible()
