from django.shortcuts import render

import pandas as pd
import time
from selenium.webdriver import Chrome
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
import urllib.request

# Create your views here.

def OpenImage(request, num, site):
    browser = Chrome()
    browser.maximize_window()
    site = "https://www.instagram.com/p/" + site + '/'
    browser.get(site)
    image = browser.find_elements_by_tag_name('img')
    browser.get(image[num].get_attribute('src'))
    return render(request, 'home.html', {})

def HomePage(request):
    return render(request, 'home.html', {})
    
