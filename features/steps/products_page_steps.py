from behave import given, when, then


@then('Verify the visualization options are clickable')
def verify_visualization_options_clickable(context):
    context.app.products_page.verify_visualization_options_clickable()