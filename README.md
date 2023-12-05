# Reconhecimento Facial em Python

Este projeto implementa um sistema de reconhecimento facial utilizando Python, oferecendo uma solução eficiente e prática para identificação de indivíduos em imagens e vídeos.

## Funcionalidades

- **Captura de Imagens**: Utiliza a webcam para capturar imagens faciais, armazenando-as para treinamento e reconhecimento.
- **Treinamento de Reconhecimento Facial**: Implementa algoritmos de treinamento para reconhecer faces específicas.
- **Reconhecimento em Tempo Real**: Identifica e reconhece faces em tempo real através da webcam.
- **Suporte a Diferentes Algoritmos**: Inclui suporte para múltiplos algoritmos de reconhecimento facial, como Eigenfaces, Fisherfaces e LBPH (Local Binary Patterns Histograms).
- **Teste com Base de Dados Yale**: Realiza testes de reconhecimento utilizando a base de dados Yale, demonstrando a eficácia do sistema.

## Tecnologias e Bibliotecas Utilizadas

- **Linguagem de Programação**: Python.
- **OpenCV**: Biblioteca principal para processamento de imagens e visão computacional.
- **Haar Cascades**: Utilizados para detecção de faces e olhos nas imagens.
- **Pillow**: Para manipulação de imagens no contexto do teste com a base de dados Yale.

## Estrutura do Projeto

- `Captura.py`: Script para captura de imagens faciais através da webcam.
- `Reconhecedor_eigenfaces.py`, `Reconhecedor_fisherfaces.py`, `Reconhecedor_lbph.py`: Scripts para reconhecimento facial utilizando diferentes algoritmos.
- `Teste_Yale.py`: Script para testar o reconhecimento com a base de dados Yale.
- `Treinamento.py`, `Treinamento_yale.py`: Scripts para treinar o reconhecedor facial com as imagens capturadas.
- `haarcascade-eye.xml`, `haarcascade-frontalface-default.xml`: Arquivos XML para detecção de faces e olhos.

## Como Usar

### Pré-requisitos

Antes de começar, certifique-se de que você tem o Python instalado em sua máquina. Este projeto foi desenvolvido utilizando Python 3. Além disso, você precisará instalar a biblioteca OpenCV para processamento de imagens e visão computacional.

### Instalação

1. **Clone o Repositório**: Faça o clone deste repositório para sua máquina local usando: `git clone https://github.com/leandropsampaio/ReconhecimentoFacial.git`.

2. **Instale as Dependências**: Navegue até o diretório do projeto clonado e instale as dependências necessárias executando o seguinte comando no terminal: `pip install opencv-python`.

3. Se necessário, instale também a biblioteca Pillow para manipulação de imagens: `pip install Pillow`.


### Execução

1. **Captura de Imagens**: Execute o script `Captura.py` para começar a captura de imagens faciais. Essas imagens serão usadas para o treinamento do modelo. Para cada pessoa, um identificador único deve ser fornecido.
`python Captura.py`
Siga as instruções na tela para capturar as imagens.

2. **Treinamento do Modelo**: Após a captura das imagens, execute o script `Treinamento.py` para treinar o modelo de reconhecimento facial.
`python Treinamento.py`
Este script processará as imagens capturadas e criará um modelo treinado.

3. **Reconhecimento Facial**: Com o modelo treinado, você pode executar um dos scripts de reconhecimento (`Reconhecedor_eigenfaces.py`, `Reconhecedor_fisherfaces.py`, `Reconhecedor_lbph.py`) para identificar as faces em tempo real.   
`python Reconhecedor_eigenfaces.py`
Substitua `Reconhecedor_eigenfaces.py` pelo script de reconhecimento desejado.

4. **Teste com Base de Dados Yale**: Para testar o sistema com a base de dados Yale, execute o script `Teste_Yale.py`.
`python Teste_Yale.py`
Este script avaliará a eficácia do modelo utilizando um conjunto de dados externo.

### Notas Adicionais

- Certifique-se de que sua webcam está funcionando corretamente para a captura de imagens e reconhecimento em tempo real.
- Os scripts podem ser modificados para atender a requisitos específicos ou para melhorar a funcionalidade.

