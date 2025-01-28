# Aplicativo de Tradução de Vídeos

Este programa é uma aplicação minimalista que utiliza inteligência artificial para processar e traduzir vídeos. Ele transcreve o áudio do vídeo, traduz o texto para um idioma escolhido e gera um novo vídeo com áudio traduzido e sincronizado.

## Como Funciona

O aplicativo segue um fluxo simples e intuitivo:

1. **Upload do Vídeo**  
   O usuário faz o upload de um vídeo diretamente na interface da aplicação.

2. **Transcrição de Áudio**  
   O áudio do vídeo é transcrito automaticamente utilizando o modelo Whisper da OpenAI.

3. **Tradução de Texto**  
   O texto transcrito é traduzido para o idioma escolhido pelo usuário usando a biblioteca Google Translate.

4. **Geração de Áudio Traduzido**  
   O texto traduzido é convertido em áudio utilizando a biblioteca Google Text-to-Speech (gTTS).

5. **Criação do Vídeo Final**  
   O áudio traduzido é sincronizado com o vídeo original, criando um novo vídeo com o áudio na língua desejada.

6. **Exibição dos Resultados**  
   O vídeo traduzido, a transcrição original e o texto traduzido são exibidos para o usuário.

## Requisitos e Configuração

Antes de executar o programa, certifique-se de que os seguintes requisitos estão atendidos:

- **Python 3.8 ou superior**
- **FFmpeg instalado** (necessário para processamento de vídeos com MoviePy)
- As seguintes bibliotecas Python:
  - `gradio==5.13.0`
  - `openai-whisper`
  - `torch==2.5.1`
  - `numpy==1.22.0`
  - `googletrans==4.0.2`
  - `gTTS==2.5.4`
  - `moviepy==1.0.3`

### Instalação

1. **Clone o repositório**  
   ```bash
   git clone https://github.com/viniciusBalbi/VideoTranslate.git
   cd https://github.com/viniciusBalbi/VideoTranslate.git
