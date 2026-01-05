import time
from playwright.sync_api import Page


def test_playwright_basics_locator(page : Page):
    page.goto("https://practicetestautomation.com/practice-test-table/")

    #DropDown handle
    page.get_by_role("combobox").select_option("col_lang")

    #radio button handle
    page.get_by_role("radio", name = "Java").check()

    #CheckBox handle
    page.get_by_role("checkbox", name = "Intermediate").uncheck()

    page.get_by_role("checkbox", name="Intermediate").check()


    #Heading
    HeadingTexth1 = page.get_by_role("heading").first.text_content()
    print(HeadingTexth1)

    #otherHeading
    #HeadingTexth2 = page.get_by_role("heading", name="Automation Courses").text_content()
    #print(HeadingTexth2)

    #HeadingText1h2 = page.locator("h2").first.text_content()
    #HeadingText1h2 = page.locator("h2").last.text_content()
    #HeadingText1h2 = page.locator("h2").nth(0).text_content()

    h2HeadingLocator  = page.locator("h2").nth(0)
    h2HeadingLocator.wait_for(state="visible")
    text = h2HeadingLocator.text_content()
    print(text)

    page.get_by_role("link", name="XPath Locators for Selenium").click()
    time.sleep(5)