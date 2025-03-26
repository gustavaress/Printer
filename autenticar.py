import os, time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import ChromeOptions as Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
 
os.system("cls")
 
caminho_cache = r"C:\Users\Administrador\AppData\Local\Google\Chrome\User Data"
 
configs = Options()
configs.add_argument("--window-size=1920x1080")
# configs.add_argument("--headless")
 
diretorioPrints = r"C:\Users\Administrador\Documents\Workspace\Trabalho\PrintadorFoda\Printscreens"
os.makedirs(diretorioPrints, exist_ok=True)
 
url = "https://portal.office.com"
login = "gustavo.tavares"
senha = "C6@"
 
navegador = webdriver.Chrome(options=configs)
navegador.get(url)
time.sleep(3)
 
email_input = navegador.find_element(By.ID, "i0116")
email_input.send_keys(login)
email_input.send_keys(Keys.RETURN)
 
time.sleep(3)
 
senha_input = navegador.find_element(By.ID, "i0118")
senha_input.send_keys(senha)
senha_input.send_keys(Keys.RETURN)
 
time.sleep(10)
 
# elemento_authenticator = navegador.find_element(By.ID, "idRichContext_DisplaySign")
# numero_authenticator = elemento_authenticator.text
# print(f"Realize sua autenticação via Microsoft Authenticator no celular: Insira o número: {numero_authenticator}")
 
print("Aguardando autenticação...")
time.sleep(15)  
 
while True:
    try:
        navegador.find_element(By.ID, "ohp-menur3")
        print("Autenticação concluída! Continuando com o processo...")
 
        dataArquivo = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        diretorioArquivo = f"{diretorioTestes}/YoutubePrintTeste_{dataArquivo}.png"
        navegador.save_screenshot(diretorioArquivo)
        print("Print realizado com sucesso!")
       
        break
 
    except Exception as e:
        print("Autenticação ainda não concluída. Tentando novamente...")
        time.sleep(5)
 
navegador.quit()