# Verificador de Dependência Linear com Visualização Gráfica

## Descrição

Este projeto é uma ferramenta interativa desenvolvida em Python como um recurso de aprendizado para Álgebra Linear. A aplicação permite que os usuários insiram um conjunto de vetores bidimensionais para analisar se eles são Linearmente Dependentes (LD) ou Linearmente Independentes (LI).

Através de uma interface gráfica construída com Flet, o usuário pode adicionar quantos vetores desejar. Ao submeter os dados, a aplicação executa duas ações principais:

1.  **Análise de Dependência Linear**: O sistema de equações lineares correspondente é resolvido usando o método de eliminação de Gauss para classificar o conjunto de vetores. O resultado textual detalha o processo.
2.  **Visualização do Espaço Vetorial**: Um gráfico é gerado com Matplotlib, exibindo todos os vetores inseridos em um plano cartesiano para facilitar a interpretação geométrica.

## Funcionalidades

* Interface gráfica para adicionar e remover vetores dinamicamente.
* Análise matemática para determinar se um conjunto de vetores é LD ou LI.
* Apresentação do resultado com os passos da resolução via método de Gauss.
* Visualização gráfica dos vetores em um plano cartesiano.

## Como Executar o Projeto

### Pré-requisitos

* Python 3.x
* Pip

### Instalação

1.  Clone o repositório para a sua máquina local:
    ```bash
    git clone https://github.com/AlecsandroDev/Dependencia_e_Independencia_Linear.git
    ```

2.  Navegue até o diretório do projeto:
    ```bash
    cd Dependencia_e_Independencia_Linear
    ```

3.  Instale as dependências a partir do arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### Execução

Para iniciar a aplicação, execute o seguinte comando no seu terminal:

```bash
python app.py
```

A janela da aplicação será aberta, permitindo que você adicione os vetores que deseja analisar e, em seguida, envie-os para ver o resultado e a representação gráfica.

## Estrutura do Projeto

* **`app.py`**: Arquivo principal que gerencia a interface do usuário com Flet e orquestra as chamadas para os outros módulos.
* **`solve_depedencia.py`**: Contém toda a lógica para a análise de dependência linear através da resolução de sistemas de equações.
* **`render_plane.py`**: Responsável por gerar a visualização gráfica dos vetores com Matplotlib.
* **`requirements.txt`**: Lista as bibliotecas Python necessárias para o projeto.
