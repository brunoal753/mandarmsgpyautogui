import pyautogui
import pyperclip

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

# Arrastar pra procurar a conversa
pyautogui.moveTo(853,165,duration=8)
# Clicar onde é a caixa de procura do nome
pyautogui.click()
escrever_frase('Lena')
# Arrastar pra clicar na conversa
pyautogui.moveTo(851,231,duration=2)
pyautogui.click()
# Arrastar pra onde vai escrever
pyautogui.moveTo(1287,692,duration=2)
# Clicar onde vai escrever
pyautogui.click()
# Escrever a frase
escrever_frase('Oi Dona Gil!')
pyautogui.click(duration=2)
# Arrastar pra onde está o botão enviar
pyautogui.moveTo(1345,687,duration=2)
# Clicar em enviar
pyautogui.click()
# Arrastar pra área de escrever novamente
pyautogui.moveTo(1287,692,duration=2)
escrever_frase('Iniciando o teste de mensagem automática')
pyautogui.click(duration=2)
# Arrastar pra onde está o botão enviar
pyautogui.moveTo(1345,687,duration=2)
# Clicar em enviar
pyautogui.click()
# Arrastar pra área de escrever novamente
pyautogui.moveTo(1287,692,duration=2)
escrever_frase('Teste 1')
pyautogui.click(duration=2)
# Arrastar pra onde está o botão enviar
pyautogui.moveTo(1345,687,duration=2)
# Clicar em enviar
pyautogui.click()
# Arrastar pra área de escrever novamente
pyautogui.moveTo(1287,692,duration=2)
escrever_frase('Teste 2')
pyautogui.click(duration=2)
# Arrastar pra onde está o botão enviar
pyautogui.moveTo(1345,687,duration=2)
# Clicar em enviar
pyautogui.click()
# Arrastar pra área de escrever novamente
pyautogui.moveTo(1287,692,duration=2)
escrever_frase('Teste 3')
pyautogui.click(duration=2)
# Arrastar pra onde está o botão enviar
pyautogui.moveTo(1345,687,duration=2)
# Clicar em enviar
pyautogui.click()
escrever_frase('Teste de envio finalizado')
pyautogui.click(duration=2)
# Arrastar pra onde está o botão enviar
pyautogui.moveTo(1345,687,duration=2)