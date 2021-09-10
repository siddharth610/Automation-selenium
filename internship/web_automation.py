from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.get("https://www.thesparksfoundationsingapore.org/")

print("\nTest 1:")
if driver.title:
    print("\nTitle Verification Passed!: ", driver.title)
else:
    print("\nTitle Verification Failed!\n")

print("\nTest 2:")
try:
    driver.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a/*').click()
    print('The logo is present\n')
    time.sleep(3)
except NoSuchElementException:
    print('No logo is present!\n')

print("Test 3:")
try:
    driver.find_element_by_class_name("navbar")
    print("Navbar Verification Passed!\n")
except NoSuchElementException:
    print("Navbar Verification Failed!\n")

print("Test 4:")
try:
    driver.find_element_by_partial_link_text("The Sparks Foundation").click()
    print("Home link is working!\n")
except NoSuchElementException:
    print("Home Link Doesn't Work!\n")

print("Test 5:")
try:
    driver.find_element_by_link_text('About Us').click()
    time.sleep(3)
    driver.find_element_by_link_text('Corporate Partners').click()
    time.sleep(3)
    print('Page visited Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)

print('Test 6:')
try:
    driver.find_element_by_link_text('Policies and Code').click()
    time.sleep(3)
    driver.find_element_by_link_text("Policies").click()
    time.sleep(3)
    driver.find_element_by_link_text('Code of Ethics and Conduct').click()
    time.sleep(3)
    print('Policy Page Verification Passed!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

print('Test 7:')
try:
    driver.find_element_by_link_text('Student Scholarship Program').click()
    time.sleep(3)
    driver.find_element_by_link_text("Student Mentorship Program").click()
    time.sleep(3)
    driver.find_element_by_link_text('Student SOS Program').click()
    time.sleep(3)
    print('Programs Page Verification Passed!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

print("Test 8:")
try:
    driver.find_element_by_link_text("Contact Us").click()
    time.sleep(3)
    info = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(3)

    # print(info.text)
    if info.text == "+65-8402-8590, info@thesparksfoundation.sg":
        print('Contact Information is Correct!')
    else:
        print('Contact Information is Incorrect!')
    print("Contact Page Verification Passed!\n")
except NoSuchElementException:
    print("Contact Page Verification Unsuccessful!")

print("Test 9:")
try:
    driver.find_element_by_link_text('LINKS').click()
    time.sleep(3)
    driver.find_element_by_link_text('Software & App').click()
    time.sleep(3)
    driver.find_element_by_link_text('AI in Education').click()
    time.sleep(3)
    print('LINKS Verfication Passed!\n')
except NoSuchElementException:
    print("LINKS Verification Failed!\n")

print("Test 10:")
try:
    driver.find_element_by_link_text('Join Us').click()
    time.sleep(3)
    driver.find_element_by_link_text('Why Join Us').click()
    time.sleep(3)
    driver.find_element_by_name('Name').send_keys('Siddharth Kumar')
    time.sleep(3)
    driver.find_element_by_name('Email').send_keys('kumarsiddharth0610@gmail.com')
    time.sleep(3)
    select = Select(driver.find_element_by_class_name('form-control'))
    time.sleep(3)
    select.select_by_visible_text('Intern')
    time.sleep(3)
    driver.find_element_by_class_name('button-w3layouts').click()
    time.sleep(3)
    print("Form Verification Passed!\n")
except NoSuchElementException:
    print("Form Verification Failed!\n")
    time.sleep(3)
cls=driver.close()