# sprint5
Sprint 5, Ana Carolina C. Alves

# Análise de Dados de Veículos

## Descrição do Projeto

Este projeto consiste em uma aplicação web interativa, criada para explorar e visualizar dados de anúncios de venda de veículos, analisando a relação entre quilometragem e preço por meio de gráficos interativos.

## Funcionalidades

A aplicação oferece:
* **Gráfico de histograma** para visualizar a distribuição da quilometragem dos veículos.
* **Gráfico de dispersão** para analisar a relação entre quilometragem e preço.
* Botões interativos para gerar cada visualização.
* Gráficos interativos.
* Layout clean, moderno e profissional, com uma paleta em azul-marinho.

## Tecnologias Utilizadas

* **GitHub**
* **Python**
* **Pandas** — leitura e manipulação dos dados.
* **Plotly Express** — criação dos gráficos interativos.
* **Render**
* **Streamlit** — desenvolvimento da aplicação web.
* **Visual Studio Code**

## Conjunto de Dados

O projeto utiliza o arquivo `vehicles_us.csv`, que contém informações sobre anúncios de veículos.

As principais variáveis utilizadas na aplicação são:

* `odometer` — quilometragem do veículo em milhas.
* `price` — preço do veículo em dólares americanos (USD).

## Estrutura do Projeto

```text
vehicle-project/
│
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
│
├── notebooks/
│   └── EDA.ipynb
│
└── .streamlit/
    └── config.toml
```

## Como Executar o Projeto Localmente

### 1. Instalar as bibliotecas

No terminal do VS Code, execute:

```bash
pip install -r requirements.txt
```

### 2. Executar a aplicação

Depois da instalação, execute:

```bash
streamlit run app.py
```

A aplicação será aberta automaticamente no navegador.

## Visualizações

### Distribuição da Quilometragem

O histograma apresenta a distribuição da quilometragem dos veículos presentes no conjunto de dados. Fazendo uso de um design clean, com fundo branco, azul-marinho intenso e sem linhas de grade para facilitar a leitura.

### Preço do Veículo x Quilometragem

O gráfico de dispersão apresenta a relação entre o preço dos veículos e sua quilometragem. Cada ponto representa um anúncio de veículo, permitindo observar possíveis padrões entre essas duas variáveis.

## Aplicação Online

A aplicação foi publicada utilizando o **Render**.

### Aplicação no Render

**https://lecture-m3d8.onrender.com/**
Por se tratar de um serviço free charge, o site pode levar um tempo de quase meio minuto para ser carregado, ele não está quebrado. Portanto tenha um pouco de paciência para carregar o mesmo.

### Repositório no GitHub

**https://github.com/carolacezalves/sprint5**

## Design da Aplicação

A aplicação foi desenvolvida com uma identidade visual clean, moderna e profissional.

Os gráficos utilizam:

* Azul-marinho intenso;
* Fundo branco;
* Ausência de linhas de grade;
* Espaçamento suave entre as barras do histograma;
* Títulos centralizados;
* Elementos visuais discretos;
* Gráficos interativos do Plotly.

## Objetivo do Projeto

O objetivo deste projeto é demonstrar a utilização de **Python, Pandas, Plotly Express e Streamlit** para transformar um conjunto de dados em uma aplicação web interativa.

O projeto também permite praticar conceitos de:

* Análise exploratória de dados;
* Manipulação de dados com Pandas;
* Visualização de dados;
* Criação de gráficos interativos;
* Desenvolvimento de aplicações web com Streamlit;
* Organização de projetos em Python;
* Publicação de aplicações utilizando Render.
