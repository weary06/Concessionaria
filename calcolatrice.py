
import tkinter as tk
from tkinter import messagebox
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calcolatrice")
        self.geometry("510x685")

        self.expression = ""
        self.memory = 0

        # Variabile temporanea per memorizzare l'ultimo valore inserito nel display
        self.last_value = ""

        # Flag per lo stato corrente del frame scientifico
        self.scientific_visible = False

        # Frame principale
        main_frame = tk.Frame(self)
        main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Frame per il display e i tasti numerici
        display_frame = tk.Frame(main_frame)
        display_frame.grid(row=0, column=0, columnspan=4, sticky='nsew')

        self.display = tk.Entry(display_frame, font=("Arial", 20))
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew')

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for btn_text, row, col in buttons:
            self.create_button(display_frame, btn_text, row, col)

        # Frame per i tasti C e scientifici
        controls_frame = tk.Frame(main_frame)
        controls_frame.grid(row=1, column=0, columnspan=4, sticky='nsew', pady=5)

        # Tasto C
        self.create_button(controls_frame, 'C', 0, 0)

        # Frame per i tasti scientifici
        self.scientific_frame = tk.Frame(controls_frame)
        self.scientific_frame.grid(row=0, column=1, sticky='nsew', padx=5)

        scientific_buttons = [
            ('sin', 0, 0), ('cos', 0, 1), ('tan', 0, 2),
            ('√', 1, 0), ('^', 1, 1), ('^n', 1, 2),
            ('MEM', 2, 0), ('STO', 2, 1), ('M+', 2, 2),
            ('Reciproco', 3, 0), ('Fattoriale', 3, 1), ('(', 3, 2), (')', 3, 3),
            ('radice n-esima', 4, 0)
        ]
        for btn_text, row, col in scientific_buttons:
            self.create_button(self.scientific_frame, btn_text, row, col)

        # Pulsante per mostrare/nascondere i tasti scientifici
        self.scientific_button = tk.Button(controls_frame, text="Sci", font=("Arial", 16), command=self.toggle_scientific)
        self.scientific_button.grid(row=0, column=2, sticky='nsew')

        # Nasconde il frame scientifico all'avvio del programma
        self.scientific_frame.grid_remove()

    def create_button(self, frame, text, row, col):
        btn = tk.Button(frame, text=text, font=("Arial", 16), command=lambda t=text: self.on_button_click(t))
        btn.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
        if len(text) == 1:  # Imposta altezza doppia per i tasti numerici e operazioni
            btn.config(height=2)

    def on_button_click(self, text):
        if self.expression == "Errore":
            if text != 'C':
                messagebox.showerror("Errore", "La calcolatrice è in errore. Premere il tasto C per continuare.")
                return
            else:
                self.display.delete(0, tk.END)
                self.expression = ""
                if self.scientific_visible:
                    self.toggle_scientific()
                return

        if text == '=':
            try:
                result = eval(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Errore")
                self.expression = "Errore"
        elif text == 'C':
            self.display.delete(0, tk.END)
            self.expression = ""  # Reset the current expression
            if self.scientific_visible:  # Hide the scientific frame if it's visible
                self.toggle_scientific()
        elif text in ('sin', 'cos', 'tan'):
            self.calculate_trig_function(text)
        elif text == '^':
            self.expression += '**2'
            self.display.insert(tk.END, '^2')
        elif text == '^n':
            self.expression += '**'
            self.display.insert(tk.END, '^n')
        elif text == 'radice n-esima':
            self.expression += '**(1/'
            self.display.insert(tk.END, '^(1/')
        elif text == 'MEM':
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(self.memory))
        elif text == 'STO':
            # Memorizziamo solo la parte numerica dell'espressione attuale nella memoria
            self.memory = float(''.join(filter(str.isdigit, self.expression)))
        elif text == 'M+':
            try:
                current_value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(current_value + self.memory))
            except ValueError:
                messagebox.showerror("Errore", "Impossibile eseguire l'operazione. Assicurarsi che il valore visualizzato sia un numero.")
        elif text == 'Reciproco':
            try:
                current_value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(1 / current_value))
            except ValueError:
                messagebox.showerror("Errore", "Impossibile eseguire l'operazione. Assicurarsi che il valore visualizzato sia un numero diverso da zero.")
            except ZeroDivisionError:
                messagebox.showerror("Errore", "Impossibile dividere per zero.")
        elif text == 'Fattoriale':
            try:
                current_value = int(self.display.get())
                if current_value < 0:
                    messagebox.showerror("Errore", "Il fattoriale è definito solo per numeri interi non negativi.")
                else:
                    result = math.factorial(current_value)
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, str(result))
            except ValueError:
                messagebox.showerror("Errore", "Il fattoriale è definito solo per numeri interi non negativi.")
        else:
            self.expression += text
            self.display.insert(tk.END, text)

    def toggle_scientific(self):
        if self.scientific_visible:
            self.scientific_frame.grid_remove()
            self.scientific_button.config(text="Sci")
            self.scientific_visible = False
        else:
            self.scientific_frame.grid(row=0, column=1, sticky='nsew', padx=5)
            self.scientific_button.config(text="Hide")
            self.scientific_visible = True

    def calculate_trig_function(self, function_name):
        try:
            angle = float(self.display.get())
            if function_name == 'sin':
                result = math.sin(math.radians(angle))
            elif function_name == 'cos':
                result = math.cos(math.radians(angle))
            elif function_name == 'tan':
                result = math.tan(math.radians(angle))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except ValueError:
            messagebox.showerror("Errore", "Impossibile eseguire l'operazione. Assicurarsi che il valore visualizzato sia un numero.")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
