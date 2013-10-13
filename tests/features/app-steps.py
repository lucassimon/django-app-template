from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals

@before.all
def set_browser():
    world.browser = Client()

@step(r'I access the url "(.*)"')
def access_url(step, url):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'I see the header "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect('h1')[0]
    assert header.text == text


from lettuce import step
from lettuce.django import mail
from nose.tools import assert_equals


@step(u'an email is sent to "([^"]*?)" with subject "([^"]*)"')
def email_sent(step, to, subject):
    message = mail.queue.get(True, timeout=5)
    assert_equals(message.subject, subject)
    assert_equals(message.recipients(), [to])
