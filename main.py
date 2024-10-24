import tkinter as tk
from tkinter import messagebox
from unidecode import unidecode
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class SistemaDiagnosticoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Diagnóstico de Cursos")
        self.root.geometry("1400x800")
        self.root.configure(bg="#F5F5F7")

        self.perguntas = {
            1: "Quais matérias você mais gosta? (Exatas, Humanas, Biológicas)",
            2: "Você tem mais interesse em trabalhos teóricos ou práticos? (Teóricos, Práticos)",
            3: "Você prefere trabalhar com pessoas ou mais individualmente? (Pessoas, Sozinho)",
            4: "Qual tipo de profissão você acha interessante? (Engenharia, Medicina, Direito)",
            5: "Você tem interesse em tecnologia? (Sim, Não)",
            6: "Você prefere ambientes dinâmicos ou estáveis? (Dinâmicos, Estáveis)",
            7: "Você gosta de resolver problemas complexos? (Sim, Não)",
            8: "Prefere tarefas criativas ou estruturadas? (Criativas, Estruturadas)"
        }

        self.respostas = {}
        self.cursos = {
            'Engenharia de Computação': 0,
            'Engenharia Civil': 0,
            'Ciência da Computação': 0,
            'Medicina': 0,
            'Direito': 0,
            'Psicologia': 0,
            'Biotecnologia': 0,
            'Física': 0,
            'Matemática': 0,
            'História': 0,
            'Administração': 0,
            'Química': 0,
            'Engenharia Química': 0,
            'Biologia': 0,
            'Design': 0,
            'Publicidade': 0
        }

        self.current_question = 1
        self.criar_tela_inicial()

    def criar_tela_inicial(self):
        self.frame_inicial = tk.Frame(self.root, bg="#F5F5F7")
        self.frame_inicial.pack(expand=True, fill="both")

        label_titulo = tk.Label(self.frame_inicial, text="Bem-vindo ao Sistema de Diagnóstico de Cursos!",
                                font=("Helvetica", 24, "bold"), bg="#F5F5F7", fg="#000000")
        label_titulo.pack(pady=50)

        label_instrucao = tk.Label(self.frame_inicial, text="Responda algumas perguntas e descubra sugestões de cursos universitários!",
                                   font=("Helvetica", 14), bg="#F5F5F7", fg="#333333", wraplength=800)
        label_instrucao.pack(pady=20)

        btn_iniciar = tk.Button(self.frame_inicial, text="Iniciar Diagnóstico", command=self.iniciar_diagnostico,
                                font=("Helvetica", 16), bg="#007AFF", fg="#FFFFFF", relief="flat",
                                borderwidth=2, cursor="hand2")
        btn_iniciar.pack(pady=40)

    def iniciar_diagnostico(self):
        self.frame_inicial.destroy()
        self.create_widgets()

    def create_widgets(self):
        self.frame_perguntas = tk.Frame(self.root, bg="#F5F5F7")
        self.frame_perguntas.pack(expand=True)

        self.label_pergunta = tk.Label(self.frame_perguntas, text=self.perguntas[self.current_question],
                                       font=("Helvetica", 14), bg="#F5F5F7", fg="#000000")
        self.label_pergunta.pack(pady=20)

        self.entry_resposta = tk.Entry(self.frame_perguntas, font=("Helvetica", 12), bg="#FFFFFF", fg="#000000", relief="flat",
                                       borderwidth=3)
        self.entry_resposta.pack(ipady=5, padx=20)

        self.btn_proxima = tk.Button(self.frame_perguntas, text="Próxima", command=self.proxima_pergunta, font=("Helvetica", 12),
                                     bg="#007AFF", fg="#FFFFFF", activebackground="#005BB5", relief="flat",
                                     borderwidth=2, cursor="hand2")
        self.btn_proxima.pack(pady=20)

    def proxima_pergunta(self):
        resposta = self.entry_resposta.get().strip().lower()
        resposta = unidecode(resposta)

        respostas_validas = {
            1: ['exatas', 'humanas', 'biologicas'],
            2: ['teoricos', 'praticos'],
            3: ['pessoas', 'sozinho'],
            4: ['engenharia', 'medicina', 'direito'],
            5: ['sim', 'nao'],
            6: ['dinamicos', 'estaveis'],
            7: ['sim', 'nao'],
            8: ['criativas', 'estruturadas']
        }

        if self.current_question in respostas_validas and resposta not in respostas_validas[self.current_question]:
            messagebox.showerror("Erro", "Por favor, insira uma resposta válida.")
            self.entry_resposta.delete(0, tk.END)
        else:
            self.respostas[self.current_question] = resposta
            self.current_question += 1

            if self.current_question > len(self.perguntas):
                self.calcular_pontuacao()
                self.exibir_resultado_na_tela()
            else:
                self.label_pergunta.config(text=self.perguntas[self.current_question])
                self.entry_resposta.delete(0, tk.END)

    def calcular_pontuacao(self):
        if self.respostas[1] == "exatas":
            self.cursos['Engenharia de Computação'] += 10
            self.cursos['Ciência da Computação'] += 10
            self.cursos['Física'] += 7
            self.cursos['Matemática'] += 7
            self.cursos['Química'] += 7
            self.cursos['Engenharia Química'] += 8
        elif self.respostas[1] == "biologicas":
            self.cursos['Medicina'] += 10
            self.cursos['Biotecnologia'] += 8
            self.cursos['Psicologia'] += 6
            self.cursos['Biologia'] += 8
        elif self.respostas[1] == "humanas":
            self.cursos['Direito'] += 10
            self.cursos['Psicologia'] += 7
            self.cursos['História'] += 8
            self.cursos['Administração'] += 6

        if self.respostas[2] == "teoricos":
            self.cursos['Física'] += 5
            self.cursos['Matemática'] += 5
            self.cursos['Química'] += 5
            self.cursos['História'] += 4
        elif self.respostas[2] == "praticos":
            self.cursos['Engenharia Civil'] += 7
            self.cursos['Engenharia de Computação'] += 7
            self.cursos['Medicina'] += 6
            self.cursos['Biotecnologia'] += 5
            self.cursos['Engenharia Química'] += 6

        if self.respostas[3] == "pessoas":
            self.cursos['Psicologia'] += 8
            self.cursos['Direito'] += 7
            self.cursos['Medicina'] += 5
        elif self.respostas[3] == "sozinho":
            self.cursos['Engenharia de Computação'] += 6
            self.cursos['Ciência da Computação'] += 6
            self.cursos['Física'] += 5

        if self.respostas[4] == "engenharia":
            self.cursos['Engenharia de Computação'] += 8
            self.cursos['Engenharia Civil'] += 8
            self.cursos['Engenharia Química'] += 7
        elif self.respostas[4] == "medicina":
            self.cursos['Medicina'] += 10
            self.cursos['Biologia'] += 7
            self.cursos['Biotecnologia'] += 6
        elif self.respostas[4] == "direito":
            self.cursos['Direito'] += 10
            self.cursos['Administração'] += 6

        if self.respostas[5] == "sim":
            self.cursos['Engenharia de Computação'] += 8
            self.cursos['Ciência da Computação'] += 8
        elif self.respostas[5] == "nao":
            self.cursos['História'] += 5
            self.cursos['Psicologia'] += 5

        if self.respostas[6] == "dinamicos":
            self.cursos['Engenharia Civil'] += 6
            self.cursos['Medicina'] += 6
            self.cursos['Administração'] += 5
        elif self.respostas[6] == "estaveis":
            self.cursos['Física'] += 5
            self.cursos['História'] += 5

        if self.respostas.get(7) == "sim":
            self.cursos['Ciência da Computação'] += 6
            self.cursos['Engenharia de Computação'] += 5
            self.cursos['Matemática'] += 4
        elif self.respostas.get(7) == "nao":
            self.cursos['Psicologia'] += 5
            self.cursos['Direito'] += 4

        if self.respostas.get(8) == "criativas":
            self.cursos['Design'] += 7
            self.cursos['Publicidade'] += 6
        elif self.respostas.get(8) == "estruturadas":
            self.cursos['Engenharia Civil'] += 5
            self.cursos['Administração'] += 5

    def exibir_resultado_na_tela(self):
        for widget in self.frame_perguntas.winfo_children():
            widget.destroy()

        self.label_resultado = tk.Label(self.frame_perguntas, text="Perfil Acadêmico: Sugestões de Cursos e suas Pontuações:",
                                        font=("Helvetica", 14), bg="#F5F5F7", fg="#000000")
        self.label_resultado.pack(pady=20)

        cursos_recomendados = sorted(self.cursos.items(), key=lambda x: x[1], reverse=True)[:5]
        cursos_nomes = [curso[0] for curso in cursos_recomendados]
        cursos_pontos = [curso[1] for curso in cursos_recomendados]

        self.mostrar_grafico(cursos_nomes, cursos_pontos)

        metodologia = ("As sugestões de cursos foram geradas com base nas suas respostas às perguntas fornecidas. "
                       "Cada curso foi pontuado de acordo com características como interesse por matérias específicas, "
                       "preferência por atividades teóricas ou práticas, e outros critérios de afinidade.")
        self.label_metodologia = tk.Label(self.frame_perguntas, text=metodologia, font=("Helvetica", 12), bg="#F5F5F7", fg="#333333", wraplength=1000, justify="left")
        self.label_metodologia.pack(pady=20)


    def mostrar_grafico(self, nomes, pontos):
        fig, ax = plt.subplots(figsize=(10, 8))
        barras = ax.bar(nomes, [0]*len(pontos), color='blue')
        ax.set_title('Pontuação dos Cursos Recomendados')
        ax.set_xlabel('Cursos')
        ax.set_ylabel('Pontuação')

        ax.set_xticklabels(nomes, rotation=45, ha='right')

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.frame_perguntas)
        canvas.draw()
        canvas.get_tk_widget().pack()

        self.root.after(500, self.animar_barras, barras, pontos, ax, canvas)

    def animar_barras(self, barras, pontos_finais, ax, canvas, step=1):
        animado = False
        for i, (barra, ponto_final) in enumerate(zip(barras, pontos_finais)):
            altura_atual = barra.get_height()
            nova_altura = min(altura_atual + step, ponto_final)
            barra.set_height(nova_altura)
            if nova_altura < ponto_final:
                animado = True

        if animado:
            ax.relim()
            ax.autoscale_view()
            canvas.draw()
            self.root.after(50, self.animar_barras, barras, pontos_finais, ax, canvas, step + 1)


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaDiagnosticoGUI(root)
    root.mainloop()
