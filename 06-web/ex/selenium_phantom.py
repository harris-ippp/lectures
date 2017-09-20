#!/usr/bin/env python 

from selenium import webdriver
from datetime import datetime

driver = webdriver.PhantomJS() # the normal SE phantomjs binding
driver.set_window_size(1024, 768)
driver.get('https://shop.nordstrom.com/') # any URL

date = '{0:%Y}{0:%m}{0:%d}_{0:%H}{0:%M}'.format(datetime.now())
driver.save_screenshot(date + '.png')

