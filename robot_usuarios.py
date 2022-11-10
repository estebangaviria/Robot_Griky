from lib2to3.pgen2 import driver
from tabnanny import check
from typing import final
from unicodedata import name
from urllib import response
import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def robot(url, lim_sup):
        
    #Lee usuario un contraseña:
    credenciales_excel = r"D:\PROYECTOS\ROBOT GRIKY\credenciales.xlsx"
    df = pandas.read_excel(credenciales_excel)
    user = df["username"][0]
    psw = df["password"][0]

    # Aplicar filtros y descargar
    aplicar = '//*[@id="submit-button"]'
    nube = '//*[@id="main"]/div/nav/ul/li/a/i'
    archivo = '//*[@id="report-file-list"]/div[1]/a'

    driver = webdriver.Chrome()

    # Maximizar pantalla
    driver.maximize_window()
    driver.get(url)
    time.sleep(10)

    cant_contador = int(lim_sup/5)
    #Quitar widget eanx
    try:
        driver.switch_to.frame(1)
        driver.find_element(By.CLASS_NAME, "widget")
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/button").click()
        driver.switch_to.default_content()
    except:
        driver.switch_to.default_content()
        pass

    #Quitar widget griky
    try:
        driver.switch_to.frame(2)
        driver.find_element(By.CLASS_NAME, "widget")
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/button").click()
        driver.switch_to.default_content()
    except:
        driver.switch_to.default_content()
        pass

    # Opcion de login
    try:
        driver.find_element(By.CSS_SELECTOR, "#login-form > article > div > div.email-login-link > a").click()
    except Exception:
        pass

    # Login:
    driver.find_element(By.CSS_SELECTOR, "#login-email").send_keys(user)
    # time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#login-password").send_keys(psw)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#login > button").click()
    time.sleep(2)


    # Seleccionar filtros:
    time.sleep(2)              

    #Seleccionar propiedades:  
    driver.find_element(By.XPATH, '//*[@id="learner-report"]/section/div/div[1]/ul/li[2]').click()

    #contar filtros de propiedades:
    total_propiedades = len(driver.find_elements(By.XPATH, '//*[@id="learner-report"]/section/div/div[1]/div/div[2]/div/ul/li'))

    #Seleccionar todas las propiedades:
    for i in range(1, total_propiedades + 1):
        driver.find_element(
            By.XPATH, '//*[@id="learner-report"]/section/div/div[1]/div/div[2]/div/ul/li['+str(i)+']'
        ).click()

    time.sleep(2)
    
    #Selecionar boton export:
    driver.find_element(By.XPATH, '//*[@id="learner-report"]/section/div/div[1]/ul/li[4]').click()
    #Seleccionar formato xls:
    driver.find_element(By.XPATH, '//*[@id="learner-report"]/section/div/div[1]/div/div[4]/div/ul/li[2]').click()
    time.sleep(5)

    # Buscar nombre de ultimo archivo descargado:

    driver.execute_script("window.scrollTo(0, 0)")
    driver.find_element(By.XPATH, nube).click()
    last_file = driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]').text
    print(last_file)

    without_files = "No hay informes disponibles"

    time.sleep(2)
    while without_files == last_file or last_file =='':
        driver.execute_script("window.scrollTo(0, 0)")
        driver.find_element(By.XPATH, nube).click()
        time.sleep(2)
        try:
            element = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="report-file-list"]/div[1]'))
            )
            last_file = driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]').text
        except TimeoutException as ex:
                print(ex.message)


    element_to_hover_over = driver.find_element(By.CSS_SELECTOR, "#main > div > nav > ol > li:nth-child(5)")
    ActionChains(driver).move_to_element(element_to_hover_over).perform()

    #Seleccionar boton Aplicar
    driver.find_element(By.XPATH, '//*[@id="learner-report"]/section/div/div[1]/div/div[4]/div/input').click()
    
    time.sleep(5)
    
    #Cerrar aviso de descarga:
    driver.find_element(By.XPATH, '//*[@id="dialog-container"]')
    driver.find_element(By.XPATH, '//*[@id="dialog-container"]/div[1]')

    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="dialog-container"]/div[1]/i'))
        )
    except TimeoutException as ex:
            print(ex.message)

    try: 
        driver.find_element(By.XPATH, '//*[@id="dialog-container"]/div[1]/i').click()
    except Exception:
        pass

    #--------------------------------------------------------------------------

    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 0)")
    driver.find_element(By.XPATH, nube).click()
    try:
        new_file = driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]').text
    except Exception:
        time.sleep(2)
        new_file = driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]').text
            
    ActionChains(driver).move_to_element(element_to_hover_over).perform()
    n_contador = 0

    if new_file != last_file and last_file != without_files:
                driver.execute_script("window.scrollTo(0, 0)")
                driver.find_element(By.XPATH, nube).click()
                driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]/a').click()
    else:
        while new_file == last_file:
            time.sleep(5)
            driver.execute_script("window.scrollTo(0, 0)")
            driver.find_element(By.XPATH, nube).click()
            try: 
                new_file = driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]').text
            except Exception:
                time.sleep(2)
                new_file = driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]').text
            time.sleep(lim_sup)
            n_contador += 1
            if n_contador >= cant_contador:
                break
        driver.execute_script("window.scrollTo(0, 0)")
        driver.find_element(By.XPATH, nube).click()
        driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]/a').click()

    time.sleep(lim_sup/2)


    #--------------------------------

robot(url='https://campus.griky.co/analytics/learner/', lim_sup = 10)