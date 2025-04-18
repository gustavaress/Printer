import os, time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Limpa o terminal
os.system('cls')

# Define o diretorio aonde as prints serão salvas
url = "https://github.com/gustavaress"
diretorioArquivos = r"C:\Users\killy\Desktop\Printer\Printscreens"
caminhoCache = r"C:\Users\killy\AppData\Local\Google\Chrome\User Data"
os.makedirs(diretorioArquivos, exist_ok=True)

# Define os presets do navegador
preset = Options()  # Usar o cache do usuário 
preset.add_argument(f'user-data-dir={caminhoCache}') #Diz o que é o caminho do cache do user
preset.add_argument("--profile-directory=Default") # Usar o perfil 'Default' (ou o que você usa)
preset.add_argument('--window-size=1920,1080')
# preset.add_argument('--headless')

# Abre o navegador com os presets setados anteriormente
navegador = webdriver.Chrome(options=preset)
navegador.get(url)

time.sleep(5)

# Puxa a data em que o print foi tirado e adiciona esse valor no nome do diretorio do arquivo (Ou então, no nome do arquivo)
dataPrint = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
diretorioPrint = f"{diretorioArquivos}\Print_{dataPrint}.png"

# Tira o screenshot e o caminho do arquivo.png criado
navegador.save_screenshot(diretorioPrint)

# Fecha navegador
navegador.quit()

# Limpa o terminal
os.system('cls')

print('Arquivo Printado com sucesso!')