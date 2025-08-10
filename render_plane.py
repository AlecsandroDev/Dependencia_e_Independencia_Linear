import matplotlib.pyplot as plt

def model_geometric(vetores: list):
       list_args = vetores
       max_size = int()

       # Criando a figura e eixos
       fig, ax = plt.subplots()
       
       # Origem
       origem = [0, 0]

       # Adicionar ponto na origem
       ax.plot(0, 0, 'ko')

       for i, vetor in enumerate(list_args):
              if vetor[0] > max_size: 
                     max_size = vetor[0]
              if vetor[1] > max_size: 
                     max_size = vetor[1]
              

              ax.quiver(*origem , vetor[0], vetor[1], angles='xy', scale_units='xy', scale=1, color=vetor[2])
              ax.plot(*vetor, marker='o', color=vetor[2])
              
              ax.text(vetor[0] + 0.5, vetor[1], (vetor[0], vetor[1]), fontsize=10, color='black')
              

        # Definir limites e grid
       max_size+=2

       ax.set_xlim(-max_size, max_size)
       ax.set_ylim(-max_size, max_size)
       ax.set_xticks(range(-max_size, max_size+1, 1))  # ticks de 1 em 1 no eixo x
       ax.set_yticks(range(-max_size, max_size+1, 1))
       ax.grid(True)
       ax.set_aspect('equal')

       plt.get_current_fig_manager().set_window_title("Espaço Vetorial")


       plt.show()