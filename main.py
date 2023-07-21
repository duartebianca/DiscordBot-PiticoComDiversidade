import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from typing import Union
import datetime
import asyncio
import random
from discord import FFmpegPCMAudio
from pytube import YouTube, Playlist
from moviepy.editor import AudioFileClip

#Credenciais
TOKEN = ''
SPREADSHEET_ID = ''
CREDENTIALS_FILE = 'credencial.json'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
intents.members = True
intents.voice_states = True

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send(":diamond_shape_with_a_dot_inside: Hmmm, esse comando é diferente, hein?! Você pode sugerir em [link para Notion com documentação]. Para saber os comandos válidos, utilize o !comandos.")

@bot.command(name='comandos')
async def comandos(ctx):
    embed = discord.Embed(title="O que eu posso fazer?", description="Lista de comandos disponíveis:")
    embed.add_field(name="!gigabig @pessoa/cargo", value="Use quando quiser reconhecer uma atitude de diversidade e/ou inclusão de alguma pessoa do CITi. Equivalente a !pedrinha do servidor do CITi.", inline=False)
    embed.add_field(name="!hino @pessoa/cargo", value="Use quando quiser reconhecer uma atitude FE-NO-ME-NAL de diversidade e/ou inclusão de alguma pessoa do CITi. Equivalente ao !bacon do servidor do CITi.", inline=False)
    embed.add_field(name="!majestade @pessoa/cargo", value="Levante a moral de outra pessoa :heart:.", inline=False)
    embed.add_field(name="!comemorar @pessoa/cargo", value="Use quando quiser comemorar mesmo! Eu vou entrar no canal de voz em que a pessoa que chamou o comando estiver e tocar uma música de comemoração da playlist do Comitê.", inline=False)
    embed.add_field(name="!sair", value="Ao utilizar este comando, eu saio do canal de voz em que estiver conectado.", inline=False)
    embed.add_field(name="!proximo_evento", value="Use para saber o próximo evento do Comitê de Diversidade e Inclusão.", inline=False)
    embed.add_field(name="!agenda", value="Use para saber a agenda do mês do Comitê de Diversidade e Inclusão.", inline=False)
    embed.add_field(name="!nucleos", value="Retorna a descrição de cada núcleo do comitê, também disponível na #introdução.", inline=False)
    await ctx.send(embed=embed)


@bot.command(name='hino')
async def hino_command(ctx, *args):
    mentions = []
    text = ''
    for arg in args:
        if arg.startswith('<@') and arg.endswith('>'):
            # Verifica se o argumento é uma menção a um membro ou cargo
            if arg != ctx.author.mention:
                mentions.append(arg)
            else:
                await ctx.send(f':diamond_shape_with_a_dot_inside: Hey, porquinh@! Os comandos **!hino** e **!gigabig** são formas de reconhecimento coletivas, e podemos usá-los para reconhecer as outras pessoas. Caso esteja precisando se reconhecer um pouco, por que não usar o **!majestade** ou o **!comemorar**?\n')
                return
        else:
            # Se não for uma menção, assume que é texto
            text += arg + ' '
    if len(mentions) > 1:
        last_mention = mentions.pop()
        mention_string = ", ".join(mentions)
        mention_string += f" e {last_mention}"
        frase_restante = 'deixaram seus legados'
    elif len(mentions) == 1:
        mention_string = mentions[0]
        frase_restante = 'deixou seu legado'
    else:
        mention_string = "CITi"
        frase_restante = 'deixou seu legado'
    await ctx.send(f':diamond_shape_with_a_dot_inside: {mention_string} {frase_restante}! :sparkles:\n')


@bot.command(name='gigabig')
async def gigabig_command(ctx, *args):
  mentions = []
  text = ''
  for arg in args:
    if arg.startswith('<@') and arg.endswith('>'):
        if arg != ctx.author.mention:
            mentions.append(arg)
        else:
            await ctx.send(f':diamond_shape_with_a_dot_inside: Hey, porquinh@! Os comandos **!hino** e **!gigabig** são formas de reconhecimento coletivas e podemos usá-los para reconhecer as outras pessoas. Caso esteja precisando se reconhecer um pouco, por que não usar o **!majestade** ou o **!comemorar**?\n')
            return
    else:
        # Se não for uma menção, assume que é texto
        text += arg + ' '
  if len(mentions) > 1:
        last_mention = mentions.pop()
        mention_string = ", ".join(mentions)
        mention_string += f" e {last_mention}"
        frase_restante = "vocês arrasaram, tão"
  elif len(mentions) == 1:
      mention_string = mentions[0]
      frase_restante = 'você arrasou, tá'
  else:
      mention_string = "CITi"
      frase_restante = 'você arrasou, tá'
  await ctx.send(f':diamond_shape_with_a_dot_inside: {mention_string}, {ctx.author.mention} mandou dizer que {frase_restante} de **PA-RA-BÉNS!** :speaking_head: :tada:\n')

@bot.command(name='majestade')
async def majestade_command(ctx, *args):
  mentions = []
  text = ''
  for arg in args:
    if arg.startswith('<@') and arg.endswith('>'):
        mentions.append(arg)

    else:
        # Se não for uma menção, assume que é texto
        text += arg + ' '
  if len(mentions) > 1:
        last_mention = mentions.pop()
        mention_string = ", ".join(mentions)
        mention_string += f" e {last_mention}"
  elif len(mentions) == 1:
      mention_string = mentions[0]
  else:
      mention_string = 'CITi'

  await ctx.send(f':diamond_shape_with_a_dot_inside: **{mention_string}, levanta a cabeça!** Se não, a coroa cai :crown:\n')
  

@bot.command(name='nucleos')
async def nucleos_command(ctx):
    guild = ctx.guild
    núcleos = {
        'Núcleo A': 'descrição',
        'Núcleo B': 'descrição',
        'Núcleo C': 'descrição',
        'Núcleo D': 'descrição',
        'Núcleo E': 'descrição'
    }

    response = "Aqui estão os núcleos do Comitê de Diversidade e Inclusão:\n"

    for núcleo, descrição in núcleos.items():
        cargo = discord.utils.get(guild.roles, name=núcleo)
        if cargo is not None:
            response += f"- {cargo.mention}: {descrição}\n"
        else:
            response += f"- {núcleo}: {descrição}\n"

    await ctx.send(response)

@bot.command(name='proximo_evento')
async def proximo_evento_command(ctx): 
  # Envia a mensagem no canal onde o comando foi utilizado
  await ctx.send(proximo_evento_funcao()) 

def proximo_evento_funcao ():
  # Autenticação no Google Sheets
  scope = ['https://www.googleapis.com/auth/spreadsheets']
  credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scopes=scope)
  client = gspread.authorize(credentials)
     # Acesso à planilha
  planilha = client.open_by_key(SPREADSHEET_ID)
  guia = planilha.get_worksheet(0)
    # Extrai as informações relevantes
  data = guia.acell('A2').value
  nome_evento = guia.acell('B2').value
  hora = guia.acell('C2').value
  local = guia.acell('D2').value
  formato = guia.acell('E2').value
  descricao = guia.acell('F2').value

  # Cria a mensagem de resposta
  mensagem = "Eita, como engaja! Porquinh@, aqui estão as informações do próximo evento do comitê:\n"
  mensagem += f"- **{nome_evento}**\n"
  mensagem += f"**Quando**: {data}, às {hora}.\n"
  mensagem += f"**Formato**: {formato}.\n"
  mensagem += f"**Onde**: {local}.\n"
  mensagem += f"**Mais detalhes**: {descricao}."
  return mensagem
    

@bot.command(name='agenda')
async def agenda_command(ctx):
    # Obtém o mês atual
    mes_atual = datetime.datetime.now().month

    # Envia a mensagem no canal onde o comando foi utilizado
    await ctx.send(agenda_funcao(mes_atual))

@bot.command(name='comemorar')
async def comemorar_command(ctx, *args):
    mentions = []
    text = ''
    for arg in args:
        if arg.startswith('<@') and arg.endswith('>'):
            # Verifica se o argumento é uma menção a um membro ou cargo
            mentions.append(arg)
        else:
            # Se não for uma menção, assume que é texto
            text += arg + ' '
    if len(mentions) > 1:
        last_mention = mentions.pop()
        mention_string = ", ".join(mentions)
        mention_string += f" e {last_mention}"
        brilhar = 'BRILHARAM'
        querer = 'quiserem'
        conexao = 'conecte-se'
        comemoracao = 'Comemorem'
    elif len(mentions) == 1:
        mention_string = mentions[0]
        brilhar = 'BRILHOU'
        querer = 'quiser'
        conexao = 'conecte-se'
        comemoracao = 'Comemore'
    else:
        mention_string = 'CITi'
        brilhar = 'BRILHOU'
        querer = 'quiser'
        conexao = 'conecte-se'
        comemoracao = 'Comemore'
    if not ctx.author.voice:
        await ctx.send(f':diamond_shape_with_a_dot_inside: {brilhar} MUITO, {mention_string}! Se {querer} comemorar em grande estilo, {conexao} com {ctx.author.mention} a um canal de voz.\n')   
        return
    if ctx.author.voice:
        voice_channel = ctx.author.voice.channel   
        try:
            voice_client = await voice_channel.connect()
            await ctx.send(f':diamond_shape_with_a_dot_inside: **Ei, {mention_string} {brilhar} DEMAISSSS!** :star_struck::green_heart::rocket: {comemoracao} muito no canal de voz {voice_channel.name}.\n')
            await ctx.send(":arrow_forward: Preparando-se para tocar a música! Aguarde um pouquinho que já vai começar :rocket:")
            # Carregar a playlist do YouTube
            playlist_url = '[link]'
            playlist = Playlist(playlist_url)
            video_urls = playlist.video_urls
            # Selecionar um vídeo aleatório da playlist
            video_url = random.choice(video_urls)
            # Baixar o áudio do YouTube
            youtube = YouTube(video_url)
            audio_stream = youtube.streams.get_audio_only()
            audio_stream.download(output_path='.', filename='music.mp4')
            #Obter a duração da música em segundos
            audio_path = 'music.mp4'
            audio_clip = AudioFileClip(audio_path)
            duration = audio_clip.duration
            audio_clip.close()
            audio_source = FFmpegPCMAudio('music.mp4')
            voice_client.play(audio_source)
            await ctx.send(":stop_button: **Tocando a música! :notes:** Se quiser parar, utilize o comando !sair.")
            await asyncio.sleep(duration)
            await voice_client.disconnect()
        except Exception as e:
            await ctx.send(f':diamond_shape_with_a_dot_inside: Erro ao conectar ao canal de voz: {str(e)}')
        finally:
            if voice_client.is_connected():
                await voice_client.disconnect()

@bot.command(name='sair')
async def sair(ctx):
  if ctx.voice_client is None:
    await ctx.send(':diamond_shape_with_a_dot_inside: Opa, eu não estou conectado a um canal de voz. :grimacing:')
    return
  await ctx.voice_client.disconnect()
  await ctx.send(':diamond_shape_with_a_dot_inside: Tudo bem, saí do canal de voz. :man_running:')


#Funções

def agenda_funcao(mes_atual):
    # Autenticação no Google Sheets
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scopes=scope)
    client = gspread.authorize(credentials)

    # Acesso à planilha
    planilha = client.open_by_key(SPREADSHEET_ID)
    guia = planilha.get_worksheet(0)

    # Extrai as informações relevantes
    data = guia.col_values(1)[1:]  # Coluna de datas (ignora o cabeçalho)
    eventos_mes = []

    # Filtra os eventos que estão no mês atual
    for i, data_evento in enumerate(data):
        data_evento_obj = datetime.datetime.strptime(data_evento, "%d/%m/%Y")
        if data_evento_obj.month == mes_atual:
            evento = {
                'data': data_evento,  # Coluna A
                'nome': guia.cell(i + 2, 2).value,  # Coluna B
                'hora': guia.cell(i + 2, 3).value,  # Coluna C
                'local': guia.cell(i + 2, 4).value,  # Coluna D
                'formato': guia.cell(i + 2, 5).value,  # Coluna E
                'descricao': guia.cell(i + 2, 6).value  # Coluna F
            }
            eventos_mes.append(evento)

    if len(eventos_mes) == 0:
        return "Não há eventos programados para o mês atual."

    # Cria a mensagem de resposta
    mensagem = f"EITAAA! Tá merecendo até um !hino. Esta é a agenda do comitê para o mês de {mes_nome(mes_atual)}:\n\n"
    for evento in eventos_mes:
        mensagem += f"- **{evento['nome']}**, dia **{evento['data']}**, às {evento['hora']}. Vai ser no formato {evento['formato']}, em {evento['local']}.\n"
    return mensagem


def mes_nome(numero_mes):
    nomes_meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    return nomes_meses[numero_mes - 1]

bot.run(TOKEN)
