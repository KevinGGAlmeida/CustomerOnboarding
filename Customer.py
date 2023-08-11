from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from Functions import DisclosureAgreement,DiscountOffered,Download,InsertFormValue,ReadFile,SelectState,Register


class Customer:

    def __init__(self,site):
        self.site = site
        self.chrome_options = Options()
        #self.chrome_options.add_argument('--no-sandbox')
        #self.chrome_options.add_argument('--headless')
        #self.chrome_options.add_argument('--disable-dev-shm-usage')

    def Launch(self):
        self.driver = webdriver.Chrome(service=Service("/home/kevinadm/Development/RpaChallenge2/chromedriver"),options=self.chrome_options)
        self.driver.get(self.site)

    def DownloadFile(self):
        Download(self.driver)

    def ReadData(self):
        self.Data = ReadFile()

    def FillingOutForm(self):
        for lines in self.Data.index:
            InsertFormValue(self.driver,"customerName",str(self.Data["Company Name"][lines]))
            InsertFormValue(self.driver,"customerID ",str(self.Data["Customer ID"][lines]))
            InsertFormValue(self.driver,"contact ",str(self.Data["Primary Contact"][lines]))
            InsertFormValue(self.driver,"street ",str(self.Data["Street Address"][lines]))
            InsertFormValue(self.driver,"city ",str(self.Data["City"][lines]))
            SelectState(self.driver,str(self.Data["State"][lines]))
            InsertFormValue(self.driver,"zip ",str(self.Data["Zip"][lines]))
            InsertFormValue(self.driver,"email",str(self.Data["Email Address"][lines]))
            DiscountOffered(self.driver,str(self.Data["Offers Discounts"][lines]))
            
            if str(self.Data["Non-Disclosure On File"][lines]) == "YES":
                DisclosureAgreement(self.driver)

            Register(self.driver)
            print(f"Line: {lines} Done")
            
        sleep(2)
        self.driver.save_screenshot("finished.png")



Run = Customer("https://developer.automationanywhere.com/challenges/automationanywherelabs-customeronboarding.html?")
Run.Launch()
Run.DownloadFile()
Run.ReadData()
Run.FillingOutForm()
print("Processo Finalizado")

