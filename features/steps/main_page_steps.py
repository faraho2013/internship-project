from time import sleep
from behave import given, when, then


@given('Open reely main page')
def open_main(context):
    context.app.main_page.open_main()


@when('Login to the page with {email} and {password}')
def login(context, email, password):
    context.app.main_page.login(email, password)
    sleep(6)


@when('Click on “off plan" at the left side menu')
def open_off_plan(context):
    context.app.main_page.open_off_plan()
    sleep(6)