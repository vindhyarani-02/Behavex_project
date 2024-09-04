import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the Demo Login Page')
def step_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")

@when('I fill the account information for account {account_type} into the Username field and the Password field')
def step_when_i_fill_account_information(context, account_type):
    username_field = context.driver.find_element(By.ID, "user-name")
    password_field = context.driver.find_element(By.ID, "password")

    if account_type == "StandardUser":
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
    elif account_type == "LockedOutUser":
        username_field.send_keys("locked_out_user")
        password_field.send_keys("secret_sauce")
@when('I click the Login Button')
def step_login_button(context):
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()

@then('I am redirected to demo main page')
def step_redirected_to_main_page(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/inventory.html")
    )

@then('I verify the App Logo exists')
def step_verify_app_logo_exists(context):
    app_logo = context.driver.find_element(By.CLASS_NAME, "app_logo")
    assert app_logo.is_displayed()

@then('I verify the Error Message contains the text "{expected_text}"')
def step_verify_error_message(context, expected_text):
    error_message_element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )
    actual_text = error_message_element.text
    assert expected_text in actual_text, f"Expected '{expected_text}' but got '{actual_text}'"

@given('I am logged in')
def step_i_am_logged_in(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com")

    # Log in with valid credentials
    username_field = context.driver.find_element(By.ID, "user-name")
    password_field = context.driver.find_element(By.ID, "password")
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()

    # Wait until redirected to the main page
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/inventory.html")
    )

@when('I am on the inventory page')
def step_on_the_inventory_page(context):
    context.driver.get("https://www.saucedemo.com/inventory.html")

@then('I extract content from the web page')
def step_extract_content_from_web_page(context):
    # Locate the inventory items
    inventory_items = context.driver.find_elements(By.CLASS_NAME, "inventory_item")
    extracted_content = []
    for item in inventory_items:
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        item_desc = item.find_element(By.CLASS_NAME, "inventory_item_desc").text
        item_price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
        extracted_content.append(f"Name: {item_name}\nDescription: {item_desc}\nPrice: {item_price}\n")

    context.extracted_content = "\n\n".join(extracted_content)

@then('Save it to a text file')
def step_save_to_text_file(context):
    with open("extracted_content.txt", "w") as file:
        file.write(context.extracted_content)

@then('I log out')
def step_log_out(context):
    context.driver.find_element(By.ID,"react-burger-menu-btn").click()
    time.sleep(5)
    logout_button = context.driver.find_element(By.ID, "logout_sidebar_link")
    logout_button.click()

@then('I verify I am on the Login page again')
def step_verify_on_login_page_again(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("saucedemo.com")
    )
    assert "saucedemo.com" in context.driver.current_url, "Not on the login page after logout"


def after_scenario(context, scenario):
    context.driver.quit()