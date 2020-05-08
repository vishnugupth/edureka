from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=chrome_options)
driver.get("http://34.87.174.47:9097/content")
driver.find_element_by_partial_link_text(("about-us.php")).click();
print driver.page_source
print(driver.title)
pgsource=driver.page_source

x_string = "Lorem Ipsum Dipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standar"

if x_string in pgsource :
   print "Expected result"
else:
   print "Not expected"
