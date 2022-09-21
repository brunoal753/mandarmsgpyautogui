import pyautogui
import pyperclip

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

# Arrastar pra onde está a conversa
pyautogui.moveTo(798,222,duration=2)
# Clicar na conversa
pyautogui.click()
# Arrastar pra onde vai escrever
pyautogui.moveTo(1138,694,duration=1.2)
# Clicar onde vai escrever
pyautogui.click()
# Escrever a frase
escrever_frase('Oi, LINDEUSA!')
pyautogui.click(duration=1.2)
# Arrastar pra onde está o botão enviar
pyautogui.moveTo(1347,684,duration=1.2)
# Clicar em enviar
pyautogui.click()
# Arrastar pra área de escrever novamente
pyautogui.moveTo(1237,688,duration=1.2)
escrever_frase('Você vem sempre aqui?')
pyautogui.click(duration=1.2)
# Arrastar pra onde está o botão enviar
pyautogui.moveTo(1347,684,duration=1.2)
# Clicar em enviar
pyautogui.click()
# Arrastar pra área de escrever novamente
pyautogui.moveTo(1237,688,duration=1.2)
escrever_frase('Cê sabe que nem o céu tem a quantidade de estrelas')
pyautogui.click(duration=1.2)
# Arrastar pra onde está o botão enviar
pyautogui.moveTo(1347,684,duration=1.2)
# Clicar em enviar
pyautogui.click()
# Arrastar pra área de escrever novamente
pyautogui.moveTo(1237,688,duration=1.2)
escrever_frase('Nem o mar tem a quantidade de gotas suficientes')
pyautogui.click(duration=2)# Arrastar pra onde está o botão enviar
pyautogui.moveTo(1347,684,duration=1.2)
# Clicar em enviar
pyautogui.click()
# Arrastar pra área de escrever novamente
pyautogui.moveTo(1237,688,duration=1.2)
escrever_frase('Pra expressar o quanto te admiro e amo te conhecer todo dia mais.')
pyautogui.click(duration=1.2)
# Arrastar pra onde está o botão enviar
pyautogui.moveTo(1347,684,duration=1.2)
# Clicar em enviar
pyautogui.click()
escrever_frase('Esse é um teste que tô fazendo que vou te enviar o vídeo, mas as frases são reais hihi')
pyautogui.click(duration=1.2)
# Arrastar pra onde está o botão enviar
pyautogui.moveTo(1347,684,duration=1.2)