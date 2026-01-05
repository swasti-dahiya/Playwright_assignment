import time

from playwright.sync_api import Page

def test_yahookeyboardaction(page:Page):
    page.goto("https://login.yahoo.com/account/create")

    page.get_by_label("First Name").type("Swasti", delay=300)
    page.keyboard.press("Tab")
    page.get_by_label("Surname").type("Dahiya", delay=300)
    page.keyboard.press("Tab")
    page.get_by_label("New Yahoo email address").type("testthisemail", delay=150)
    time.sleep(5)