Pergunta = float(input("Largura da parade:"))
Pergunta2 = float(input("Altura da parede:"))
a = Pergunta * Pergunta2
b = a / 2
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m².".format(Pergunta, Pergunta2, a,))
print("Para pintar essa parede, você precisará de {}l de tinta.".format(b))
