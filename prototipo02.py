import PySimpleGUI as sg
import time, pyautogui
import script as sc
#Resolução do client desse script: 1024x576.

#Criando a primeira janela:
def pagina_inicial():
    sg.theme('SandyBeach')

    layout = [
        [sg.Text('Deseja executar o script?')],
        [sg.Checkbox('Sim',key=1), sg.Checkbox('Não', key=2)],
        [sg.Button('Próximo', key='prox'), sg.Button('Sair', key='sair')]
    ]

    window = sg.Window('Unfriend', layout)
#configurando o esquema de entrada e saida da janela 1:
    while True:
        event, values = window.read()

        if event in (None, 'sair'):
            break
        
        if event == 'prox' and values[2]:
            break

        if event == 'prox' and values[1] and values[2]:
            break
        
        if event == "prox" and values[1]:
            window.close()
            executar()

    window.close()

#Segunda janela:
def executar():
    layout = [
        [sg.Text('Quantos amigos você quer excluir?', size=(25,1)), sg.Input('', key='p')],
        [sg.Button('Excluir', key='exc'), sg.Button('Sair', key='sair')]
    ]

    window = sg.Window('Unfriend', layout)
    
    while True:
        event, values = window.read()

        #Sair da segundda janela atraves do botão 'Sair':
        if event == 'sair':
            break

        valor = int(values['p'])

        if event == "exc":
                #definindo o loop:
                for loop in range(valor):
                    sc.icone()
                    time.sleep(0.8)

                    sc.excluindo()
                    time.sleep(0.8)

                    sc.excluir()
                    time.sleep(1)

        sg.popup('Amigos excluídos.')            
                                    
        window.close()
#iniciando a janela 1:
pagina_inicial()
