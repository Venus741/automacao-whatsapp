import customtkinter
import pywhatkit as pwk

janela = customtkinter.CTk()
janela.geometry('500x500')

def enviar_mensagem():
    destinatario_value = destinatario.get()
    mensagem_value = mensagem.get()
    hora_value = int(hora.get())
    minuto_value = int(minuto.get())

    pwk.sendwhatmsg(destinatario_value, mensagem_value, hora_value, minuto_value)

titulo = customtkinter.CTkLabel(janela, text='Mensagem automatizada')
titulo.pack(padx=10, pady=10)

destinatario = customtkinter.CTkEntry(janela, placeholder_text="Nº de destino")
destinatario.pack(padx=5, pady=5)
dica = customtkinter.CTkLabel(janela, text='Ex: +5582988887777')
dica.pack()

mensagem = customtkinter.CTkEntry(janela, placeholder_text='Sua mensagem...')
mensagem.pack()

hora = customtkinter.CTkEntry(janela, placeholder_text='Hora do envio')
hora.pack(padx=5, pady=5)

minuto = customtkinter.CTkEntry(janela, placeholder_text='Minuto do envio')
minuto.pack(padx=3, pady=3)

botao = customtkinter.CTkButton(janela, text='Enviar', command=enviar_mensagem)
botao.pack(padx=7, pady=7)

janela.mainloop()