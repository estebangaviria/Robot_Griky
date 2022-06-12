from urllib import response
import requests
import lxml.html as html


XPATH_FILE_NAME = '//*[@id="report-file-list"]/div[1]/a/text()'


home = response.content.decode('utf-8')
parsed=  html.fromstring(home)
names= parsed.xpath(XPATH_FILE_NAME)
prin