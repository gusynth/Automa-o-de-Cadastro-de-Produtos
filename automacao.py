# Libs
import pyautogui
import time
import pandas

# Variável
link_sistema = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # Utlize um link para o sistema.
email_bot = "seuemailaqui@gmail.com" # Substitua para email que será utilizado.
senha_bot = "sua_senha_aqui" # Substitua para senha que será utilizada.
tabela = pandas.read_csv("produtos.csv") # Importa a base de dados com a lib pandas. Mude para o nome exato para a base de dados utilizada.

# CONFIGURAÇÃO GLOBAL
# A cada comando dado, irá esperar 1 segundo automaticamente. Aumente caso necessário pro seu sistema.
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# ABRIR O NAVEGADOR

pyautogui.press("win")
pyautogui.write("microsoft edge")
pyautogui.press("enter")
time.sleep(2) # Para o navegador carregar.

# NAVEGAR PARA O SITE DO SISTEMA
# Na maioria dos casos, o navegador abre automaticamente na parte de digitar. 
# Se não for o caso, abrir "posicao_mouse", capturar onde deve ser clicado, e adicionar o comando .click.

pyautogui.write(link_sistema)
pyautogui.press("enter")
time.sleep(1.5) # Para dar tempo do site carregar.
pyautogui.click(x=672, y=363)

# EFETUAR LOGIN NO SISTEMA

pyautogui.write(email_bot)
pyautogui.press("tab")
pyautogui.write(senha_bot)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3) # Para o sistema carregar.

# CADASTRO DOS PRODUTOS (ATENTE-SE A BASE DE DADOS)

for linha in tabela.index:
    pyautogui.click(x=675, y=250) # Clica no primeiro campo para início da automação
    codigo = tabela.loc[linha, "codigo"] # Pega da base de dados o campo que irá ser preenchido
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter") # Cadastro do produto
    pyautogui.scroll(5000) # Volta para o começo da página

# Repete o processo até o fim da base de dados.
# Para parar a automação, mova o cursor do mouse para o canto superior esquerdo da tela.