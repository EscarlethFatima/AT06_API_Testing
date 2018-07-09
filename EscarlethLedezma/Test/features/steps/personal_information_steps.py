@given(u'I am from {country:w}')
def step_impl(context, country):
    context.country = country

@given(u'The zipcode is {zipcode:d}')
def step_impl(context, zipcode):
    context.zipcode = zipcode

@given(u'The number of habitants is:{habitants:n}')
def step_impl(context, habitants):
    context.habitants = habitants
