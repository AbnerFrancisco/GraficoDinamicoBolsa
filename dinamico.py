import pyautogui
import time

# Site usado no experimento (https://www.infomoney.com.br/ferramentas/altas-e-baixas/)

#baixa o arquivo
#----------------------------------#
pyautogui.hotkey('alt','tab')
pyautogui.sleep (1)
pyautogui.moveTo(x=1318,y=584)


pyautogui.click()
#-----------------------------#




#da alt tab até o excel
#-------------------------------------#
pyautogui.hotkey('alt','tab')
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.keyUp('alt')
#-------------------------------------------#






#Cria uma tabela dinamica
#---------------------------------#
pyautogui.moveTo(x=21,y=211)
pyautogui.sleep (1)
pyautogui.click()
pyautogui.sleep (1)

pyautogui.keyDown('alt')
pyautogui.sleep (3)

pyautogui.sleep (1)
pyautogui.press('t')
pyautogui.sleep (1)
pyautogui.press('v')
pyautogui.sleep (1)
pyautogui.press('t')
pyautogui.sleep (1)
pyautogui.keyUp('alt')
pyautogui.press('enter')
#------------------------------------#

#Cria um gráfico dinamico
#--------------------------------#
pyautogui.sleep (1)
pyautogui.doubleClick(x=1041, y=346) #ativo
pyautogui.click(x=1041, y=346)

pyautogui.sleep (1)

pyautogui.moveTo(x=1045,y=384) #ultimo
pyautogui.click()
pyautogui.sleep (1)

pyautogui.moveTo(x=1042,y=411) #dia
pyautogui.click()
pyautogui.sleep (1)

pyautogui.moveTo(x=1040,y=429) #sem
pyautogui.click()
pyautogui.sleep (1)

pyautogui.moveTo(x=1085,y=92) #gráfico
pyautogui.click
pyautogui.sleep (1)

pyautogui.moveTo(x=1085,y=92) #gráfico
pyautogui.click()

pyautogui.moveTo(x=876, y=660) #botao
pyautogui.click()
