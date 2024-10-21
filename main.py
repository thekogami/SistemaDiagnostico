from unidecode import unidecode

class SistemaDiagnostico:
    def __init__(self):
        self.perguntas = {
            1: "Quais matérias você mais gosta? (Exatas, Humanas, Biológicas)",
            2: "Você tem mais interesse em trabalhos teóricos ou práticos? (Teóricos, Práticos)",
            3: "Você prefere trabalhar com pessoas ou mais individualmente? (Pessoas, Sozinho)",
            4: "Qual tipo de profissão você acha interessante? (Engenharia, Medicina, Direito, etc.)",
            5: "Você tem interesse em tecnologia? (Sim, Não)",
            6: "Você prefere ambientes dinâmicos ou estáveis? (Dinâmicos, Estáveis)"
        }
        self.respostas = {}

    def fazer_pergunta(self, num_pergunta):
        resposta = input(self.perguntas[num_pergunta] + ": ").strip().lower()
        resposta = unidecode(resposta)
        self.respostas[num_pergunta] = resposta

    def diagnostico(self):
        print("Bem-vindo ao sistema de diagnóstico de cursos!")

        for i in range(1, len(self.perguntas) + 1):
            self.fazer_pergunta(i)

        print(f"Respostas: {self.respostas}")

        if self.respostas[1] == "exatas":
            self.diagnostico_exatas()
        elif self.respostas[1] == "biologicas":
            self.diagnostico_biologicas()
        elif self.respostas[1] == "humanas":
            self.diagnostico_humanas()
        else:
            print("Resposta inválida, tente novamente.")

    def diagnostico_exatas(self):
        if self.respostas[2] == "praticos" and self.respostas[3] == "sozinho":
            print("Sugestão de cursos: Engenharia da Computação, Ciência da Computação.")
        elif self.respostas[2] == "praticos" and self.respostas[3] == "pessoas":
            print("Sugestão de cursos: Engenharia Civil, Engenharia Elétrica.")
        elif self.respostas[2] == "teoricos" and self.respostas[3] == "sozinho":
            print("Sugestão de cursos: Física, Matemática.")
        elif self.respostas[2] == "teoricos" and self.respostas[3] == "pessoas":
            print("Sugestão de cursos: Ensino de Matemática, Física Aplicada.")
        if self.respostas[5] == "sim":
            print("Sugestão adicional: Ciência da Computação, Sistemas de Informação.")
        if self.respostas[6] == "dinamicos":
            print("Sugestão adicional: Engenharia de Software, Desenvolvimento Web.")
        else:
            print("Sugestão adicional: Análise de Sistemas, Engenharia de Controle e Automação.")

    def diagnostico_biologicas(self):
        if self.respostas[2] == "praticos" and self.respostas[3] == "pessoas":
            print("Sugestão de cursos: Medicina, Enfermagem, Fisioterapia.")
        elif self.respostas[2] == "praticos" and self.respostas[3] == "sozinho":
            print("Sugestão de cursos: Biotecnologia, Bioquímica.")
        elif self.respostas[2] == "teoricos" and self.respostas[3] == "pessoas":
            print("Sugestão de cursos: Psicologia, Medicina Veterinária.")
        elif self.respostas[2] == "teoricos" and self.respostas[3] == "sozinho":
            print("Sugestão de cursos: Biologia, Ciências Biológicas.")
        if self.respostas[5] == "sim":
            print("Sugestão adicional: Biomedicina, Ciências Farmacêuticas.")
        if self.respostas[6] == "dinamicos":
            print("Sugestão adicional: Farmácia, Gestão Ambiental.")
        else:
            print("Sugestão adicional: Tecnologia em Análise e Desenvolvimento de Sistemas.")

    def diagnostico_humanas(self):
        if self.respostas[2] == "praticos" and self.respostas[3] == "pessoas":
            print("Sugestão de cursos: Direito, Administração, Ciências Sociais.")
        elif self.respostas[2] == "praticos" and self.respostas[3] == "sozinho":
            print("Sugestão de cursos: História, Filosofia.")
        elif self.respostas[2] == "teoricos" and self.respostas[3] == "pessoas":
            print("Sugestão de cursos: Pedagogia, Serviço Social.")
        elif self.respostas[2] == "teoricos" and self.respostas[3] == "sozinho":
            print("Sugestão de cursos: Letras, Linguística.")
        if self.respostas[5] == "nao":
            print("Sugestão adicional: Administração Pública, Relações Internacionais.")
        if self.respostas[6] == "estaveis":
            print("Sugestão adicional: História, Biblioteconomia.")
        else:
            print("Sugestão adicional: Psicologia, Sociologia.")


if __name__ == "__main__":
    sistema = SistemaDiagnostico()
    sistema.diagnostico()