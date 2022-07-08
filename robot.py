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
#import lxml.html as html
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def robot(url, incremento, lim_inf, lim_sup):
        
    #Lee usuario un contraseña:
    credenciales_excel = r"C:\ROBOT GRIKY\credenciales.xlsx"
    df = pandas.read_excel(credenciales_excel)
    user = df["username"][0]
    psw = df["password"][0]

    # Url de instancia a descargar data:
    #url = 'https://autonomadigital.learning-tribes.com/analytics/customized/'
    #url = 'https://campus.clase.edu.co/analytics/customized/'
    #url = 'https://campus.class-run.com/analytics/customized/'
    #url='https://go.coronaaprende.com/analytics/customized/'
    #url= 'https://campus.eanx.io/analytics/customized/'
    #url = 'https://campus.griky.co/analytics/customized/'
    #url = 'https://fundacion.holastaffeducacion.com/analytics/customized/'
    #url = 'https://isttezeta.learning-tribes.com/analytics/customized/'
    #url = 'https://academiakonfio.learning-tribes.com/analytics/customized/'
    #url = 'https://onconnection.learning-tribes.com/analytics/customized/'
    #url= 'https://global-i.triboolearning.com/analytics/customized/'
    #url = "https://umaplus.uma.edu.pe/analytics/customized/"
    #url = 'https://robinfooduniversity.learning-tribes.com/analytics/customized/'
    #url = 'https://educatubolsillo.learning-tribes.com/analytics/customized/'
    #url = 'https://sura.learning-tribes.com/analytics/customized/'
    #url = 'https://click-umecit.learning-tribes.com//analytics/customized/'
    #url = 'https://usap.learning-tribes.com/analytics/customized/'
    #url = 'https://plus.ugb.edu.sv/analytics/customized/'
    #url = 'https://edpplus.triboolearning.com/analytics/customized/'
    #url = 'https://cursos.amashop.com.co/analytics/customized/' #cablemas
    #url = 'https://campus.uisep.one/analytics/customized/' #ISEP

    # Aplicar filtros y descargar
    aplicar = '//*[@id="submit-button"]'
    nube = '//*[@id="main"]/div/nav/ul/li/a/i'
    archivo = '//*[@id="report-file-list"]/div[1]/a'

    driver = webdriver.Chrome()

    # Maximizar pantalla
    driver.maximize_window()
    driver.get(url)
    time.sleep(10)

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

    # Acciones:
    #driver.find_element(By.CSS_SELECTOR, "#login-form > article > div > div.email-login-link > a").click()
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

    #driver.get(url)

    # información inicial:
    total_cursos = len(driver.find_elements(By.XPATH, '//*[@id="course_section_contents"]/div/div/div[2]/ul/li'))
    #print(total_cursos)

    # Parametros:
    #incremento = 25
    #lim_inf = 10
    #lim_sup =50

    #Variables de inicio:
    contador = 1
    cant_contador = int(lim_sup/5)
    ciclos_descarga = incremento
    contador2 = contador
    ciclos_descarga2 = ciclos_descarga
    cant_descargas = int(total_cursos / ciclos_descarga)
    residuo = total_cursos % ciclos_descarga
    print("total cursos: " + str(total_cursos))
    print("cantidad archivos: " + str(cant_descargas + 1))

    # Seleccionar filtros:
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "#user_properties_section").click()
    # driver.find_element_by_css_selector(selector_correo).click()

    cuenta_filtros = len(driver.find_elements(By.NAME, "selected_properties"))
    for i in range(1, cuenta_filtros + 1):
        driver.find_element(
            By.XPATH, '//*[@id="id_selected_properties"]/li[' + str(i) + "]/label"
        ).click()


    time.sleep(2)
    # Filtros para elegir formato de descarga (xls):
    driver.find_element(By.CSS_SELECTOR, "#format_section").click()
    driver.find_element(
        By.CSS_SELECTOR, "#table-export-selection > li:nth-child(2)"
    ).click()

    time.sleep(2)

    #driver.find_element(By.CSS_SELECTOR, "#course_section").click()
    #print("ciclos de descarga: " + str(ciclos_descarga))
    #print("cantidad descargas: " + str(cant_descargas))
    # ------------------------------------------------------------------------
    # Buscar nombre de ultimo archivo descargado:
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 0)")
    driver.find_element(By.XPATH, nube).click()
    last_file = driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]').text

    #print("-----------------------------")
    #print(type(last_file))
    #print(last_file)

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

    #------------------------------------------------
    #print("-----------------------------")
    # ------------------------------------------------------------------------


    driver.execute_script("window.scrollTo(0, 0)")
    driver.find_element(By.CSS_SELECTOR, "#course_section").click()
    driver.find_element(By.CSS_SELECTOR, "#course_section_contents > div > div > div.select").click()

    time.sleep(2)
    #----------------------------
    #pendiente ajuste de widget de bienvenida 

    # INICIO CICLO 1------------------------------------------------------------------------------------------------------------------
    while contador <= cant_descargas * incremento:
        #print("entré en el ciclo 1")

        while contador <= ciclos_descarga:
            digitar_cursos = ("#course_section_contents > div > div > div.panel > ul > li:nth-child("
                + str(contador)+ ") > label"   )
            driver.find_element(By.CSS_SELECTOR, digitar_cursos).click()
            contador += 1
        ciclos_descarga += incremento
        #time.sleep(1)

        driver.find_element(By.XPATH, aplicar).click()
        time.sleep(5)
        
        #driver.find_element(By.ID, 'dialog-container')
        driver.find_element(By.XPATH, '//*[@id="dialog-container"]')
        driver.find_element(By.XPATH, '//*[@id="dialog-container"]/div[1]')
        #driver.find_element(By.XPATH, '//*[@id="dialog-container"]/div[1]/i').click()

        try:
            element = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="dialog-container"]/div[1]/i'))
            )
        except TimeoutException as ex:
                print(ex.message)

        try: 
            driver.find_element(By.XPATH, '//*[@id="dialog-container"]/div[1]/i').click()
        except Exception:
            time.sleep(5)
            driver.find_element(By.XPATH, '//*[@id="dialog-container"]/div[1]/i').click()


        #--------------------------------------------------------------------------
        time.sleep(lim_inf)
        driver.execute_script("window.scrollTo(0, 0)")
        driver.find_element(By.XPATH, nube).click()
        
        try:
            new_file = driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]').text
        except Exception:
            time.sleep(2)
            new_file = driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]').text
            
        #driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div').click()
        ActionChains(driver).move_to_element(element_to_hover_over).perform()
        #print(new_file)
        n_contador = 0

        if new_file != last_file:
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

                #driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div').click()
                n_contador += 1
                if n_contador >= cant_contador:
                    break
            driver.execute_script("window.scrollTo(0, 0)")
            driver.find_element(By.XPATH, nube).click()
            driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]/a').click()

            
        ActionChains(driver).move_to_element(element_to_hover_over).perform()
        last_file=new_file

    # Borrar cursos seleccionados
        driver.execute_script("window.scrollTo(0, 0)")
        # time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="course_section"]')
        #time.sleep(1)

        try:
            driver.find_element(By.XPATH, '//*[@id="course_section_contents"]/div/div').click()
        except Exception:
            driver.find_element(By.CSS_SELECTOR, '#course_section').click()
            driver.find_element(By.XPATH, '//*[@id="course_section_contents"]/div/div').click()


        while contador2 <= ciclos_descarga2:
            digitar_cursos2 = (
                "#course_section_contents > div > div > div.panel > ul > li:nth-child("
                + str(contador2)
                + ") > label"
            )
            driver.find_element(By.CSS_SELECTOR, digitar_cursos2).click()
            contador2 += 1
        
        ciclos_descarga2 += incremento

    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
        #print('ultima descarga: '+last_file)
        print("ciclos de descargda: " + str(ciclos_descarga))
        print("contador" + str(contador))
        #time.sleep(0)
    # FIN CICLO -------------------------------------------------------------------------------------------------------------------

    contador3 = contador
    limite = residuo + contador - 1
    ciclo_final = 1
    # INICIO CICLO ------------------------------------------------------------------------------------------------------------------

    print(contador)

    if residuo >0:
        print("entreé en el if2")
        # Filtros de cursos a elegir:
        #driver.find_element(By.CSS_SELECTOR, "#course_section_contents > div > div").click()

        while contador <= limite:
            digitar_cursos = (
                "#course_section_contents > div > div > div.panel > ul > li:nth-child("
                + str(contador)
                + ") > label"
            )
            driver.find_element(By.CSS_SELECTOR, digitar_cursos).click()
            contador += 1

        driver.find_element(By.XPATH, aplicar).click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="dialog-container"]')
        driver.find_element(By.XPATH, '//*[@id="dialog-container"]/div[1]')
        driver.find_element(By.XPATH, '//*[@id="dialog-container"]/div[1]/i').click()

        driver.execute_script("window.scrollTo(0, 0)")
        time.sleep(lim_sup)
        driver.find_element(By.XPATH, nube).click()
        driver.find_element(By.XPATH, '//*[@id="report-file-list"]/div[1]/a').click()


    # FIN CICLO -------------------------------------------------------------------------------------------------------------------

    time.sleep(5)
    # Cerrar las acciones:
    # driver.quit()

#robot(url='https://campus.eanx.io/login?next=/analytics/customized/', incremento=1, lim_inf=10, lim_sup=40)
#robot(url='https://go.coronaaprende.com/analytics/customized/', incremento=15, lim_inf=10, lim_sup=450)
#robot(url='https://campus.griky.co/analytics/customized/', incremento=20 ,lim_inf=10, lim_sup=45)