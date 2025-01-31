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

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate

3. **Crie um ambiente virtual**
   ```bash
   pip install gradio==5.13.0 openai-whisper torch==2.5.1 numpy==1.22.0 googletrans==4.0.2 gtts==2.5.4 moviepy==1.0.3
4. **Instale o FFmpeg**
Certifique-se de que o FFmpeg está instalado. Verifique executando:
   ```bash
   ffmpeg -version
   ```
Caso não esteja instalado, siga as instruções em https://ffmpeg.org/download.html.

### Idiomas Suportados
O aplicativo suporta tradução para os seguintes idiomas:
 - `Inglês (en)`
 - `Espanhol (es)`
 - `Francês (fr)`
 - `Italiano (it)`
 - `Alemão (de)`
 - `Português (pt)`
 - `Japonês (ja)`
 - `Coreano (ko)`
 - `Chinês Simplificado (zh-cn)`

### Expansões Futuras
 - `Melhorias na precisão da tradução`
 - `Criação de uma página web`
 - `Criação de uma interface de usuário`
   
### Contribuições
Contribuições para melhorar o projeto são bem-vindas! Para contribuir:
1. Faça um fork do repositório.
2. Crie uma branch para suas alterações.
3. Submeta um pull request com uma descrição detalhada das alterações.

