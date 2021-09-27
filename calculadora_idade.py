import tkinter as tk
from datetime import datetime as dt

BG_FRAME_IMPUT = '#D9ED92'
BG_FRAME_NOW = '#b5e48c'
BG_FRAME_OUTPUT = '#99d98c'

TEXT_LABEL_INSERT_DATA = 'dd/mm/yyyy:'
TEXT_EXPLICACAO = 'Data atual:'
TEXT_BUTTON_CREATE = 'Calcular idade'


class CalculadoraIdade:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("600x160")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.data_input = tk.StringVar()
        self.now = dt.now()
        self.data_now = f"{self.now.day}/{self.now.month}/{self.now.year}"

        self.text_years, self.text_months, self.text_days = [""]*3
        self.list_texts = [self.text_years, self.text_months, self.text_days]

        self.frame_input, self.entry_data = self.create_frame_input()
        self.frame_output = self.create_frame_output()

    def create_frame_input(self):
        frame_input = tk.Frame(self.window, bg=BG_FRAME_IMPUT)
        frame_input.pack(expand=True, fill='both')
        for i in range(4):
            frame_input.rowconfigure(i, weight=1)
        frame_input.columnconfigure(0, weight=1)
        frame_input.columnconfigure(1, weight=3)

        label_insert_data = tk.Label(frame_input, text=TEXT_LABEL_INSERT_DATA, bg=BG_FRAME_NOW)
        label_insert_data.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

        entry_data = tk.Entry(frame_input, textvariable=self.data_input,
                              width=30, justify='center')
        entry_data.grid(row=1, column=1, padx=5, pady=5)

        label_explicacao = tk.Label(frame_input, text=TEXT_EXPLICACAO, bg=BG_FRAME_NOW)
        label_explicacao.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)

        label_atual_data = tk.Label(frame_input, text=self.data_now, bg='White',
                                    width=30)
        label_atual_data.grid(row=2, column=1, padx=5, pady=5)

        return frame_input, entry_data

    def create_frame_output(self):
        frame_output = tk.Frame(self.window, bg=BG_FRAME_OUTPUT)
        frame_output.pack(expand=True, fill='both')

        [frame_output.rowconfigure(i, weight=1) for i in range(3)]
        [frame_output.columnconfigure(i, weight=1) for i in range(3)]

        button_calc = tk.Button(frame_output, text=TEXT_BUTTON_CREATE,
                                bg=BG_FRAME_NOW)
        button_calc.grid(row=1, column=0, padx=5, pady=5)

        list_names = ['Anos:', 'Meses:', 'Dias:']
        for indice, value in enumerate(list_names):
            label_name = tk.Label(frame_output, text=value, bg=BG_FRAME_NOW)
            label_name.grid(row=indice, column=1, padx=5, pady=2)

        labels_output = []
        for i in range(3):
            label = tk.Label(frame_output, text=self.list_texts[i],
                             bg=BG_FRAME_NOW, width=15)
            label.grid(row=i, column=2)

        return frame_output

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    calc_idade = CalculadoraIdade()
    calc_idade.run()
