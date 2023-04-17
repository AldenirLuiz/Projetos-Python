from tkinter import *
from collections import defaultdict

class Chatbot:

    def __init__(self):
        self.data = defaultdict(list)
        self.window = Tk()
        self.window.title("Chatbot")
        self.window.geometry("400x500")
        
        # Criando o Frame
        self.frame = Frame(self.window)
        self.frame.pack(expand=True, fill=BOTH)

        # Criando a caixa de diálogo
        self.dialogue_box = Text(self.frame, state=DISABLED)
        self.dialogue_box.pack(expand=True, fill=BOTH)
        
        # Criando a caixa de entrada
        self.entry_box = Entry(self.frame, bd=3)
        self.entry_box.pack(side=BOTTOM, padx=5, pady=5, fill=X)
        self.entry_box.bind("<Return>", self.send_message)

        # Inicializando o chatbot
        self.initialize()

    def initialize(self):
        self.data['oi'] = ['Olá, como posso ajudar?', 'Oi, tudo bem?', 'Oi, como vai?', 'Olá, o que deseja?']
        self.data['tchau'] = ['Até logo!', 'Até mais!', 'Tchau!']
        self.data['como voce esta'] = ['Estou bem, obrigado por perguntar!', 'Estou ótimo, obrigado!']
        
        # Iniciando o diálogo
        self.dialogue_box.config(state=NORMAL)
        self.dialogue_box.insert(END, "Chatbot: Olá, como posso ajudar? \n\n")
        self.dialogue_box.config(state=DISABLED)

    def send_message(self, event):
        user_message = self.entry_box.get()
        self.entry_box.delete(0, END)

        # Exibindo a mensagem do usuário
        self.dialogue_box.config(state=NORMAL)
        self.dialogue_box.insert(END, "Você: " + user_message + "\n\n")
        self.dialogue_box.config(state=DISABLED)

        # Verificando se há uma resposta para a mensagem do usuário
        for key in self.data:
            if user_message.lower() == key:
                bot_message = self.data[key][0]
                self.dialogue_box.config(state=NORMAL)
                self.dialogue_box.insert(END, "Chatbot: " + bot_message + "\n\n")
                self.dialogue_box.config(state=DISABLED)
                break
        else:
            bot_message = "Desculpe, não entendi o que você disse!"
            self.dialogue_box.config(state=NORMAL)
            self.dialogue_box.insert(END, "Chatbot: " + bot_message + "\n\n")
            self.dialogue_box.config(state=DISABLED)

            # Adicionando a nova mensagem ao conjunto de dados do chatbot
            self.data[user_message.lower()].append(bot_message)

chatbot = Chatbot()
chatbot.window.mainloop()
