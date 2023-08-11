import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyscreenshot
from time import sleep


def Download(driver):
    try:
        sleep(10)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.NAME,"customerName")))
        driver.execute_script('document.querySelector(`[href="https://s3-us-west-2.amazonaws.com/aai-devportal-media/wp-content/uploads/2021/07/08203317/MissingCustomers.csv"]`).click()')

    except Exception as error:
        raise Exception(f"Error: {str(error)} \n Line:{error.__traceback__.tb_lineno}")
    

def ReadFile():
    return pd.read_csv("MissingCustomers.csv",dtype="str")


def InsertFormValue(driver,name,value):
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.NAME,name)))
        driver.find_element(By.NAME,name).send_keys(value)

    except Exception as error:
        raise Exception(f"Error: {str(error)} \n Line:{error.__traceback__.tb_lineno}")
    

def SelectState(driver,State):
    driver.execute_script(f'document.querySelector(`[value="{State}"]`).selected = true')


def DiscountOffered(driver,Option):
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"activeDiscountNo")))
        
        if Option == "YES":
            driver.find_element(By.ID,"activeDiscountYes").click()

        else:
            driver.find_element(By.ID,"activeDiscountNo").click()


    except Exception as error:
        raise Exception(f"Error: {str(error)} \n Line:{error.__traceback__.tb_lineno}")
    

def DisclosureAgreement(driver):    
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"NDA")))
        driver.find_element(By.ID,"NDA").click()

    except Exception as error:
        raise Exception(f"Error: {str(error)} \n Line:{error.__traceback__.tb_lineno}")
    

def Register(driver):
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"submit_button")))
        driver.find_element(By.ID,"submit_button").click()

    except Exception as error:
        raise Exception(f"Error: {str(error)} \n Line:{error.__traceback__.tb_lineno}")
    
    