from time import sleep
from behave import given, when, then


@when('Click on first off plan product')
def open_first_off_plan_product(context):
    context.app.off_plan_page.open_first_off_plan_product()
    sleep(10)


@then('Verify one of the three options is available')
def visualization_option_is_available(context):
    context.app.off_plan_page.visualization_option_is_available()