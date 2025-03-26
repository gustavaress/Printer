from selenium import webdriver
from selenium.webdriver import ChromeOptions as Options
from selenium.webdriver.common import by as By, keys as Keys
from selenium.webdriver.support import ui as WebDriverWait, expected_conditions as EC
import time, os
from datetime import datetime

# Configura o Chrome
configs = Options()
configs.add_argument("--headless")  # Abre o Chrome no modo invisível
configs.add_argument("--window-size=1920x1080")  # Define a resolução

# Define o caminho da pasta para salvar os prints
diretorioPrint = r"C:\Users\Administrador\Documents\Workspace\Trabalho\PrintadorFoda\Printscreens"
os.makedirs(diretorioPrint, exist_ok=True)

# URL da página e credenciais
url = "https://www.instagram.com/"
usuario = "k"
senha = ""

# Inicializa o navegador
navegador = webdriver.Chrome(options=configs)
navegador.get(url)

# Aguarda a página carregar completamente antes de continuar
WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Verifica se a tela de login está presente
try:
    campo_usuario = WebDriverWait(navegador, 5).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    print("Tela de login encontrada! Realizando autenticação...")

    # Preenche os campos de login
    campo_usuario.send_keys(usuario)
    navegador.find_element(By.NAME, "password").send_keys(senha)
    navegador.find_element(By.NAME, "password").send_keys(Keys.RETURN)

    # Aguarda a autenticação antes de continuar
    WebDriverWait(navegador, 10).until_not(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    print("Login realizado com sucesso!")

except Exception:
    print("Usuário já autenticado. Seguindo para a próxima etapa.")

# Gera um nome com data/hora para o arquivo
dataArquivo = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
caminhoPrint = f"{diretorioPrint}/splunk_{dataArquivo}.png"

# Tira o print e salva
navegador.save_screenshot(caminhoPrint)
print(f"Print salvo com sucesso em: {caminhoPrint}")

# Fecha o navegador
navegador.quit()
