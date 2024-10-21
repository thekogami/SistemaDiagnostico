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
        self.cursos = {
            'engenharia_computacao': 0,
            'engenharia_civil': 0,
            'ciencia_computacao': 0,
            'medicina': 0,
            'direito': 0,
            'psicologia': 0,
            'biotecnologia': 0,
            'fisica': 0,
            'matematica': 0,
            'historia': 0,
            'administracao': 0,
            'quimica': 0,
            'engenharia_quimica': 0,
            'biologia': 0,
        }

    def fazer_pergunta(self, num_pergunta):
        while True:
            resposta = input(self.perguntas[num_pergunta] + ": ").strip().lower()
            resposta = unidecode(resposta)
            if num_pergunta == 1 and resposta in ['exatas', 'humanas', 'biologicas']:
                break
            elif num_pergunta == 2 and resposta in ['teoricos', 'praticos']:
                break
            elif num_pergunta == 3 and resposta in ['pessoas', 'sozinho']:
                break
            elif num_pergunta == 4:
                break
            elif num_pergunta == 5 and resposta in ['sim', 'nao']:
                break
            elif num_pergunta == 6 and resposta in ['dinamicos', 'estaveis']:
                break
            else:
                print("Por favor, insira uma resposta válida.")
        self.respostas[num_pergunta] = resposta

    def diagnostico(self):
        print("Bem-vindo ao sistema de diagnóstico de cursos!")

        for i in range(1, len(self.perguntas) + 1):
            self.fazer_pergunta(i)

        print(f"Respostas: {self.respostas}")
        self.calcular_pontuacao()

        # Retornar cursos com maiores pontuações
        cursos_recomendados = sorted(self.cursos.items(), key=lambda x: x[1], reverse=True)
        print("Sugestões de cursos mais indicados para você:")
        for curso, pontos in cursos_recomendados[:3]:
            print(f"{curso.replace('_', ' ').title()} (Pontuação: {pontos})")

    def calcular_pontuacao(self):
        # Peso para Exatas, Humanas ou Biológicas
        if self.respostas[1] == "exatas":
            self.cursos['engenharia_computacao'] += 10
            self.cursos['ciencia_computacao'] += 10
            self.cursos['fisica'] += 7
            self.cursos['matematica'] += 7
            self.cursos['quimica'] += 7
            self.cursos['engenharia_quimica'] += 8
        elif self.respostas[1] == "biologicas":
            self.cursos['medicina'] += 10
            self.cursos['biotecnologia'] += 8
            self.cursos['psicologia'] += 6
            self.cursos['biologia'] += 8
        elif self.respostas[1] == "humanas":
            self.cursos['direito'] += 10
            self.cursos['psicologia'] += 7
            self.cursos['historia'] += 8
            self.cursos['administracao'] += 6

        # Peso para Trabalhos Teóricos ou Práticos
        if self.respostas[2] == "teoricos":
            self.cursos['fisica'] += 5
            self.cursos['matematica'] += 5
            self.cursos['quimica'] += 5
            self.cursos['historia'] += 4
        elif self.respostas[2] == "praticos":
            self.cursos['engenharia_civil'] += 7
            self.cursos['engenharia_computacao'] += 7
            self.cursos['medicina'] += 6
            self.cursos['biotecnologia'] += 5
            self.cursos['engenharia_quimica'] += 6

        # Peso para trabalhar com Pessoas ou Sozinho
        if self.respostas[3] == "pessoas":
            self.cursos['psicologia'] += 8
            self.cursos['direito'] += 7
            self.cursos['medicina'] += 5
        elif self.respostas[3] == "sozinho":
            self.cursos['engenharia_computacao'] += 6
            self.cursos['ciencia_computacao'] += 6
            self.cursos['fisica'] += 5

        # Interesse em tecnologia
        if self.respostas[5] == "sim":
            self.cursos['engenharia_computacao'] += 8
            self.cursos['ciencia_computacao'] += 8
        elif self.respostas[5] == "nao":
            self.cursos['historia'] += 5
            self.cursos['psicologia'] += 5

        # Preferência por ambientes dinâmicos ou estáveis
        if self.respostas[6] == "dinamicos":
            self.cursos['engenharia_civil'] += 6
            self.cursos['medicina'] += 6
            self.cursos['administracao'] += 5
        elif self.respostas[6] == "estaveis":
            self.cursos['fisica'] += 5
            self.cursos['historia'] += 5


if __name__ == "__main__":
    sistema = SistemaDiagnostico()
    sistema.diagnostico()
