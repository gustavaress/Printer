import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
 
# Defina a URL e as credenciais de login (não são necessárias, já que você usa o cache)
url = "https://youtube.com"
caminho_cache = r"C:\Users\Administrador\AppData\Local\Google\Chrome\User Data"
diretorioPrints = r"C:\Users\Administrador\Documents\Workspace\Trabalho\PrintadorFoda\Printscreens"
os.makedirs(diretorioPrints, exist_ok=True)
 
# Configurações do Chrome
configs = Options()
configs.add_argument(f"--user-data-dir={caminho_cache}")  # Usar o cache do usuário
configs.add_argument("profile-directory=Default")  # Usar o perfil 'Default' (ou o que você usa)
configs.add_argument("--window-size=1920x1080")  # Tamanho da janela do navegador
# configs.add_argument("--headless")  # Se não quiser que a janela do navegador apareça
 
# Iniciar o navegador com as configurações
navegador = webdriver.Chrome(options=configs)
 
# Abrir a URL especificada
navegador.get(url)
time.sleep(5)  # Aguardar o carregamento da página
 
# Salvar captura de tela
dataArquivo = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
caminhoPrint = f"{diretorioPrints}/Print_{dataArquivo}.png"
navegador.save_screenshot(caminhoPrint)
 
# Fechar o navegador
navegador.quit()