import os, time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Limpa o terminal
os.system('cls')

# Define o diretorio aonde as prints serão salvas
url = "https://youtube.com"
diretorioArquivos = r"C:\Users\killy\Documents\Workspace\Projetos Pessoais\Printer\Printscreens"
caminhoCache = r"C:\Users\killy\AppData\Local\Google\Chrome\User Data"
os.makedirs(diretorioArquivos, exist_ok=True)

# Define os presets do navegador
preset = Options()
preset.add_argument(f"--user-data-dir={caminhoCache}")  # Usar o cache do usuário
preset.add_argument("profile-directory=Default")  # Usar o perfil 'Default' (ou o que você usa)
preset.add_argument('--start-maximized')

# Abre o navegador com os presets setados anteriormente
navegador = webdriver.Chrome(options=preset)
navegador.get('https://google.com')

# Abre uma nova guia sem nada. Famoso about blank. Muda o navegador para essa outra pagina e dps disso abre a url que setamos na variavel url.
navegador.execute_script("window.open('about-blank' , '_blank');")
navegador.switch_to.window(navegador.window_handles[1])
navegador.get(url)

# Volta pra janela antiga e fecha
navegador.switch_to.window(navegador.window_handles[0])
navegador.close()

# Volta pra nova guia
navegador.switch_to.window(navegador.window_handles[0])
time.sleep(5)

# Puxa a data em que o print foi tirado e adiciona esse valor no nome do diretorio do arquivo (Ou então, no nome do arquivo)
dataPrint = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
diretorioPrint = f"{diretorioArquivos}/Print_{dataPrint}.png"

# Tira o screenshot e o caminho do arquivo.png criado
navegador.save_screenshot(diretorioPrint)

# Fecha navegador
navegador.quit

# Limpa o terminal
os.system('cls')

print('Arquivo Printado com sucesso!')