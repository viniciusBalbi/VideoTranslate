# Video Translation App

Uma aplicação minimalista para tradução de vídeos em português para inglês (ou outros idiomas) com síntese de voz e sincronização labial. O aplicativo utiliza inteligência artificial para transcrever o áudio do vídeo, traduzir o texto para o idioma-alvo e gerar um vídeo com áudio traduzido sincronizado.

## Funcionalidades

- **Transcrição de Áudio:** Extrai automaticamente o áudio do vídeo e o transcreve usando o modelo Whisper da OpenAI.
- **Tradução de Texto:** Traduz o texto transcrito para um idioma escolhido utilizando a biblioteca Google Translate.
- **Síntese de Voz:** Gera áudio do texto traduzido usando Google Text-to-Speech (gTTS).
- **Processamento de Vídeo:** Sincroniza o novo áudio traduzido ao vídeo original, gerando um vídeo final com áudio e texto traduzidos.
- **Interface Intuitiva:** Interface amigável baseada em Gradio para upload de vídeos e escolha do idioma de destino.

## Tecnologias e Bibliotecas Utilizadas

- **[Gradio (v5.13.0)](https://www.gradio.app/):** Interface gráfica para interação com o usuário.
- **[OpenAI Whisper](https://github.com/openai/whisper):** Modelo de IA para transcrição de áudio.
- **[gTTS (v2.5.4)](https://github.com/pndurette/gTTS):** Biblioteca para conversão de texto em áudio.
- **[Googletrans (v4.0.2)](https://py-googletrans.readthedocs.io/en/latest/):** API de tradução de idiomas.
- **[MoviePy (v1.0.3)](https://zulko.github.io/moviepy/):** Processamento e edição de vídeos.
- **[NumPy (v1.22.0)](https://numpy.org/):** Manipulação de arrays e cálculos numéricos.

## Requisitos do Sistema

- Python 3.8 ou superior
- `pip` instalado para gerenciar dependências
- FFmpeg instalado (necessário para MoviePy)

## Instalação e Configuração

1. **Clone o repositório**
   ```bash
   git clone <URL-do-repositório>
   cd <nome-do-repositório>
