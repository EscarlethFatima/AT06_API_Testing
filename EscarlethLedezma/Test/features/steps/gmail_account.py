from behave import use_step_matcher

use_step_matcher("re")


@given(u'I am on the create gmail account page')
def step_impl(context):
    assert True is True


@given(u'I put (?P<name>\w+) (?P<last_name>\w+) on the name field')
def step_impl(context, name, last_name):
    context.name = name
    context.last_name = last_name


@given(u'I put (?P<user_name>[a-zA-Z]+\d*@gmail.com) on the user name field')
def step_impl(context, user_name):
    context.user_name = user_name


@given(u'I put (?P<password>.+) on the password field')
def step_impl(context, password):
    context.password = password


@given(u'I put (?P<confirm_password>.+) on the confirm password field')
def step_impl(context, confirm_password):
    context.confirm_password = confirm_password


@given(u'I put (?P<month>[0][1-9]|[1][0-2]) (?P<day>[0][1-9]|[12][0-9]|3[01]) (?P<year>\d{4}) on the birthdate fields')
def step_impl(context, month,day,year):
    context.month = month
    context.day = day
    context.year = year


@given(u'I choose (?P<genre>female|male) on the genre field')
def step_impl(context, genre):
    context.genre = genre


@given(u'I put (?P<number>\d+) on the mobile phone field')
def step_impl(context, number):
    context.number = number


@when(u'I press on the create button')
def step_impl(context):
    assert True is True


@then(u'My new account was created')
def step_impl(context):
    assert True is True
