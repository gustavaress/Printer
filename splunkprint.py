from selenium import webdriver
from selenium.webdriver import ChromeOptions as Options
from selenium.webdriver.common import by as By, keys as Keys
from selenium.webdriver.support import ui as WebDriverWait, expected_conditions as EC
import time, os
from datetime import datetime

# Configura o Chrome pra abrir de forma "Invisivel" e no tamanho de 1080p
configs = Options()
configs.add_argument("--headless")
configs.add_argument("--window-size=1920x1080")

# Define o caminho da pasta para salvar os prints no PC
diretorioPrint = r"C:\Users\Administrador\Documents\Workspace\Trabalho\PrintadorFoda\Printscreens"
os.makedirs(diretorioPrint, exist_ok=True)

# URL da página e credenciais
url = "https://www.instagram.com/"
usuario = "k"
senha = "2"

# Inicializa o navegador com as configs setadas anteriormente no inicio do código, pega o codigo e aguarda o carregamento da página (5 segundo)
navegador = webdriver.Chrome(options=configs)
navegador.get(url)
time.sleep(5)

# Esperar a tela de carregar com um driverwait
esperarCarregamento = WebDriverWait(navegador, 10)

# Determina o que é a tela de login sendo existente
login_existe = len(navegador.find_elements(By.NAME, "username")) > 0

if login_existe:
    print("Tela de login encontrada! Realizando autenticação...")
    # Preencher campos de login
    navegador.find_element(By.NAME, "username").send_keys(usuario)  # Campo de usuário
    navegador.find_element(By.NAME, "password").send_keys(senha)  # Campo de senha
    navegador.find_element(By.NAME, "password").send_keys(Keys.RETURN)  # Pressiona Enter para logar

    time.sleep(10)  # Aguarda a autenticação
else:
    print("Usuário ja autenticado. Seguindo para próxima etapa.")

# Gera um nome com data/hora para o arquivo
dataArquivo = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
caminhoPrint = f"{diretorioPrint}\Splunk_{dataArquivo}.png"

# Tira o print e salva na pasta configurada usando o parametro save_screenshot
navegador.save_screenshot(caminhoPrint)
print(f"Print salva com sucesso em: {caminhoPrint}")

# Fechar o navegador invisivel que foi aberto
navegador.quit()