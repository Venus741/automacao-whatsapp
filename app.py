import PySimpleGUI as sg
import pywhatkit as pwk

# Layout
sg.theme('Reddit')

layout = [
    [sg.Text('Destinatário'), sg.Input(key='destinatario')],
    [sg.Text('* ex: +5582999999999')],
    [sg.Text('Mensagem'), sg.Input(key='mensagem')],
    [sg.Text('Hora'), sg.Input(key='hora')],
    [sg.Text('Minuto'), sg.Input(key='minuto')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('Mensagem automática', layout)

# Lógica dos eventos
while True:
    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == 'Entrar':
        # atribuindo valores dos inputs à váriáveis
        destinatario = valores['destinatario']
        mensagem = valores['mensagem']
        hora = int(valores['hora'])
        minuto = int(valores['minuto'])

        pwk.sendwhatmsg(destinatario, mensagem, hora, minuto)