from lib2to3.pgen2 import driver
from tabnanny import check
import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

credenciales_excel = r'D:\PROYECTOS\ROBOT GRIKY\credenciales.xlsx'

df = pandas.read_excel(credenciales_excel)

user= df['username'][0]
psw= df['password'][0]
url= 'https://umaplus.uma.edu.pe/analytics/customized/'

#Selectores inicio:
inicio = '#login-form > article > div > div.email-login-link > a'
selector_user = '#login-email'
selector_pass = '#login-password'
selector_login = '#login > button'

#Selectores de filtros:
selector_correo = '#user_properties_section'
check_correo ='#id_selected_properties_2'
formato= '#format_section'
check_formato = '#table-export-selection > li:nth-child(2)'


driver = webdriver.Chrome()

#Maximizar pantalla
driver.maximize_window()
driver.get(url)

#Acciones:
driver.find_element_by_css_selector(inicio).click()
#driver.find_element(by=By.CSS_SELECTOR, value= user)
#Login:
driver.find_element_by_css_selector(selector_user).send_keys(user)
driver.find_element_by_css_selector(selector_pass).send_keys(psw)
driver.find_element_by_css_selector(selector_login).click()

#Filtros:
driver.get(url)
#Filtros de correo
driver.find_element_by_css_selector(selector_correo).click()
driver.find_element_by_css_selector(check_correo).click()
#Filtros de formato xls
driver.find_element_by_css_selector(formato).click()
driver.find_element_by_css_selector(check_formato).click()

#Filtros de cursos a elegir:


time.sleep(20)

# Cerrar las acciones:
driver.quit()

