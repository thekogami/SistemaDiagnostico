import tkinter as tk
from tkinter import messagebox, ttk
from unidecode import unidecode
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class SistemaDiagnosticoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Diagnóstico de Cursos")
        self.root.geometry("1500x900")
        self.root.configure(bg="#F5F5F7")

        self.perguntas = {
            1: "Quais matérias você mais gosta? (Exatas, Humanas, Biológicas)",
            2: "Você tem mais interesse em trabalhos teóricos ou práticos? (Teóricos, Práticos)",
            3: "Você prefere trabalhar com pessoas ou mais individualmente? (Pessoas, Sozinho)",
            4: "Qual tipo de profissão você acha interessante? (Engenharia, Medicina, Direito, etc.)",
            5: "Você tem interesse em tecnologia? (Sim, Não)",
            6: "Você prefere ambientes dinâmicos ou estáveis? (Dinâmicos, Estáveis)"
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
        }

        # Dados para múltiplos perfis
        self.dados_perfis = []

        self.current_question = 1
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
            5: ['sim', 'nao'],
            6: ['dinamicos', 'estaveis']
        }

        if self.current_question in respostas_validas and resposta not in respostas_validas[self.current_question]:
            messagebox.showerror("Erro", "Por favor, insira uma resposta válida.")
        else:
            self.respostas[self.current_question] = resposta
            self.current_question += 1

            if self.current_question > len(self.perguntas):
                self.calcular_pontuacao()
                self.salvar_perfil()
                self.exibir_resultado_na_tela()
            else:
                self.label_pergunta.config(text=self.perguntas[self.current_question])
                self.entry_resposta.delete(0, tk.END)

    def salvar_perfil(self):
        perfil_atual = self.cursos.copy()
        self.dados_perfis.append(perfil_atual)

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

    def exibir_resultado_na_tela(self):
        for widget in self.frame_perguntas.winfo_children():
            widget.destroy()

        self.label_resultado = tk.Label(self.frame_perguntas, text="Comparação de Perfis Acadêmicos:",
                                        font=("Helvetica", 14), bg="#F5F5F7", fg="#000000")
        self.label_resultado.pack(pady=20)

        if len(self.dados_perfis) > 1:
            self.mostrar_grafico_multilinhado()
            self.mostrar_planilha_comparativa()
        else:
            self.exibir_mensagem("Apenas um perfil registrado, execute o diagnóstico mais vezes para comparar perfis.")
        
        self.btn_novo_diagnostico = tk.Button(self.frame_perguntas, text="Novo Diagnóstico", 
                                              command=self.iniciar_novo_diagnostico, 
                                              font=("Helvetica", 12), bg="#28A745", fg="#FFFFFF",
                                              relief="flat", borderwidth=2, cursor="hand2")
        self.btn_novo_diagnostico.pack(pady=20)

    def iniciar_novo_diagnostico(self):
        self.current_question = 1
        self.respostas = {}
        self.cursos = {key: 0 for key in self.cursos}
        self.create_widgets()

    def mostrar_grafico_multilinhado(self):
        fig, ax = plt.subplots(figsize=(10, 7))

        cursos = list(self.cursos.keys())
        for i, perfil in enumerate(self.dados_perfis):
            pontuacoes = [perfil[curso] for curso in cursos]
            ax.plot(cursos, pontuacoes, marker='o', label=f'Perfil {i+1}')

        ax.set_title('Comparação de Perfis Acadêmicos')
        ax.set_xlabel('Cursos')
        ax.set_ylabel('Pontuação')
        ax.legend()
        ax.grid(True)

        plt.xticks(rotation=45, ha='right', fontsize=8)
        ax.set_xticks(np.arange(len(cursos)))
        ax.set_xticklabels(cursos, fontsize=8, ha='right')

        canvas = FigureCanvasTkAgg(fig, master=self.frame_perguntas)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)


    def mostrar_planilha_comparativa(self):
        cursos = list(self.cursos.keys())
        planilha_frame = tk.Frame(self.frame_perguntas)
        planilha_frame.pack(fill='both', expand=True)

        colunas = ('Curso', *[f'Perfil {i+1}' for i in range(len(self.dados_perfis))])
        tree = ttk.Treeview(planilha_frame, columns=colunas, show='headings')
        tree.pack(fill='both', expand=True)

        tree.column('Curso', width=200)
        for i in range(len(self.dados_perfis)):
            tree.column(f'Perfil {i+1}', width=100)

        tree.heading('Curso', text='Curso')
        for i in range(len(self.dados_perfis)):
            tree.heading(f'Perfil {i+1}', text=f'Perfil {i+1}')

        for curso in cursos:
            valores = [perfil[curso] for perfil in self.dados_perfis]
            tree.insert('', 'end', values=(curso, *valores))


    def exibir_mensagem(self, mensagem):
        self.label_mensagem = tk.Label(self.frame_perguntas, text=mensagem, font=("Helvetica", 12), bg="#F5F5F7", fg="#333333")
        self.label_mensagem.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaDiagnosticoGUI(root)
    root.mainloop()
