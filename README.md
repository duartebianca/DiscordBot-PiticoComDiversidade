# Bot de Discord do Comitê de Diversidade & Inclusão - CITi-UFPE

Este é um bot de Discord criado para o servidor de Diversidade do CITi-UFPE. Seu objetivo é promover o reconhecimento, engajamento e facilitar o acesso às informações sobre o Comitê de Diversidade & Inclusão.

## Funcionalidades

O bot possui as seguintes funcionalidades:

1. Reconhecimento:
   - **!gigabig @pessoa/cargo**: Reconhece atitudes de diversidade e inclusão de pessoas do CITi.
   - **!hino @pessoa/cargo**: Reconhece atitudes extraordinárias de diversidade e inclusão de pessoas do CITi.
   - **!majestade @pessoa/cargo**: Levanta a moral de outra pessoa.

2. Comemoração:
   - **!comemorar @pessoa/cargo**: Entra no canal de voz do autor do comando e toca uma música de comemoração da playlist do Comitê.

3. Informações:
   - **!proximo_evento**: Mostra informações sobre o próximo evento do Comitê.
   - **!agenda**: Mostra a agenda do mês do Comitê.
   - **!nucleos**: Exibe descrições dos núcleos do Comitê de Diversidade e Inclusão.
   - **!comandos**: Mostra a lista de comandos disponíveis.

4. Controle de Voz:
   - **!sair**: Faz o bot sair do canal de voz.

## Tecnologias Utilizadas

- **Discord.py**: Biblioteca para interagir com a API do Discord.
- **gspread**: Biblioteca para acessar planilhas do Google Sheets.
- **oauth2client**: Biblioteca para autenticação OAuth2 para acesso ao Google Sheets.
- **asyncio**: Biblioteca para programação assíncrona.
- **random**: Módulo para geração de números aleatórios.
- **pytube**: Biblioteca para interagir com vídeos do YouTube.
- **moviepy**: Biblioteca para edição de vídeos.

## Uso

1. Clone este repositório.
2. Instale as dependências listadas no arquivo `requirements.txt`.
3. Obtenha o token do seu bot e insira no código.
4. Insira o ID da planilha em `SPREADSHEET_ID`.
5. Obtenha as credenciais na Google Cloud Plataform.
6. Execute o bot através do comando `python nome_do_arquivo.py`.
7. Para conseguir usar os comandos de eventos/agenda, você precisa utilizar uma planilha neste [modelo](https://docs.google.com/spreadsheets/d/1K0Do_NzQXoZIA1LflTqi-ZQoWmdqlMf38uIo-CV185M/edit?usp=sharing).
   
Para obter os itens 4, 5, 6, verifique as instruções disponíveis neste [pdf](https://github.com/duartebianca/DiscordBot-PiticoComDiversidade/blob/main/como_criar_bot_discord.pdf).

## Documentação

Para obter mais detalhes sobre o funcionamento dos comandos e configurações, consulte a documentação completa do bot.

## Objetivo

Este bot foi desenvolvido para atender às necessidades específicas do servidor de Diversidade do CITi-UFPE. Se você deseja contribuir ou adaptar o bot para outro contexto, fique à vontade para fazer um fork deste repositório e adaptar o código conforme necessário. 

## Agradecimentos

Agradecimentos à equipe do Comitê de Diversidade e Inclusão, à equipe de Inteligência de Dados & Finanças e  a Arthur Brito pelo auxílio no Deploy, na época em que o Bot foi ao ar.
