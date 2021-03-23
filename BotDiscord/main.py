import discord 
import os
import random 
from discord.ext import commands

client = commands.Bot(command_prefix = '%')
sadwords = ['morrer', 'depressão', 'saltar da ponte', 'depressivo',]
badwords = ['nigger', 'NIGGA', 'Nigga', 'nigga', 'niggers', 'Niggers', 'Nigger', 'NIGGERS', 'NIGGER',]
absacc = ['https://tenor.com/6uo6.gif', 'https://tenor.com/ynI8.gif','https://tenor.com/br7vB.gif','https://tenor.com/bqMaa.gif','https://tenor.com/X6Bo.gif','https://tenor.com/KGB6.gif','https://tenor.com/NaI5.gif','https://tenor.com/bfSMW.gif','https://media.giphy.com/media/110bpWUJADwimQ/giphy.gif','https://media.giphy.com/media/NHQcgEaQtZCqQ/giphy.gif','https://media.giphy.com/media/3hcrZnsyPkgc8/giphy.gif','https://media.giphy.com/media/7ySkq8ot1x7z2/giphy.gif','https://media.giphy.com/media/RzAONHu711636/giphy.gif','https://tenor.com/W4b2.gif','https://media.giphy.com/media/aF3KcOxCMTss0/giphy.gif','https://tenor.com/bpGgz.gif','https://tenor.com/6u5l.gif','https://tenor.com/6xob.gif','https://tenor.com/8L6U.gif','https://tenor.com/bgnFm.gif','https://tenor.com/bcWnC.gif','https://tenor.com/bavXR.gif','https://tenor.com/J5YW.gif','https://tenor.com/bvMVT.gif','https://media.giphy.com/media/gxd2234VretZC/giphy.gif','https://tenor.com/bfRvh.gif','https://tenor.com/QysC.gif','https://tenor.com/bm4wH.gif','https://media.giphy.com/media/3ohuAcEIQXmhPYNcju/giphy.gif','https://tenor.com/W4bZ.gif','https://tenor.com/bbmOo.gif','https://tenor.com/bwNaa.gif','https://tenor.com/byB0Q.gif','https://tenor.com/buBv3.gif','https://tenor.com/wsr9.gif','https://tenor.com/vT6z.gif','https://tenor.com/bcU2E.gif',]
rafaela = [':thumbsup:', 'És muita fixe Girafa', 'Cala-te sua abécula', 'Poderias ser menos achavascada', 'Por favor, para de ser biltre', 'OK tabitite', 'Imagina ser xexé']

@client.event
async def on_ready():
  print('Ola, bom dia a todos! {0.user}'.format(client))


@client.command(aliases = ['KPOP', 'ABS', 'kpop', 'Kpop','Abs'])
async def abs(ctx):
  Krand = random.randint(0,39)
  await ctx.send(absacc[Krand])

@client.command()
async def horas(ctx, *, ano): 
  #em desenvolvimento
  return

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, *, delete=0):
    delete = delete + 1
    await ctx.channel.purge(limit=delete)
    return
  

@client.command()
async def ola(ctx, member: discord.Member):
  delete = 1
  await ctx.channel.purge(limit=delete)
  await ctx.send(f'Olá {member.mention}! Está tudo bem? Estou extremamente interessado na sua situação atual. O que tem feito nos últimos dias? Tem se alimentado como deve de ser?')
  return

@client.event
async def on_message(message):

  if any (word in message.content for word in badwords):
    delete = 1
    await message.channel.purge(limit=delete)
    await message.channel.send('NÃO!')


  if any (word in message.content for word in sadwords):
    await message.channel.send('Não sejas assim! Todos temos dias mais negros porém ||um dia vai tudo piorar e ficarás para sempre em desespero!||\n**JKJK!** Queres falar?')

  a = 761608631535403018
  b = 436940721212096514
  c = 761608631535403018
  if message.author == client.user:
    return
  
  if 'Zoom Meeting Information' in message.content:
    await message.channel.send('Obrigado Rita!')
  
  if 'Bom bot' in message.content:
    await message.channel.send('Ora eça')
    await message.channel.send('https://cdn.discordapp.com/attachments/682398136676646965/823563563187568660/GetResource.png')

  if 'Olá bot' in message.content:
    await message.channel.send('Olá')
  if 'tudo?' in message.content:
    await message.channel.send('tudo.\ntudo?')
  if 'VIVA' in message.content:
    await message.channel.send('VIVA')
    
  #if message.author.id == a and message.content.startswith (''):
    #IA = random.randint(1, 3)
    #if IA == 1:
     # botrafa = random.randint(0,7)
      #await message.channel.send(rafaela[botrafa])
      #return 

  #if message.author.id == b and message.content.startswith (''):
    #delete = 1
    #await message.channel.purge(limit = delete)
    #return

  #if message.author.id == c and message.content.startswith (''):
    #delete = 1
    #await message.channel.purge(limit = delete)
    #return  

  await client.process_commands(message)  


@client.command(aliases = ['LIDL', 'Lidl'])
async def lidl(ctx):
  await ctx.send('Quem é LIDL?\nPara o cego, é a luz.\nPara o faminto, é o pão.\nPara o sedento, é a fonte de água viva.\nPara o morto, é a vida.\nPara o enfermo, é a cura.\nPara o prisioneiro, é a liberdade.\nPara o solitário, é o companheiro.\nPara o viajante, é o caminho.\nPara o sábio, é a sabedoria.\nPara a medicina, é o médico dos médicos.\nPara o réu, é o advogado.\nPara o advogado, é o Juiz.\nPara o Juiz, é a justiça.\nPara o cansado, é o alívio.\nPara o pedreiro, é a pedra principal.\nPara o jardineiro, é a rosa de Sharon.\nPara o triste, é a alegria.\nPara o leitor, é a palavra.\nPara o pobre, é o tesouro.\nPara o devedor, é o perdão.')

@client.command()
async def rng(ctx,*, numero=2):
  rng1 = random.randint(1, numero)
  await ctx.send(f'O teu número é: {rng1}')
  
@client.command()
async def gdl(ctx):
  IA = random.randint(1,6)

  if IA == 1:
      await ctx.send('https://cdn.discordapp.com/attachments/797630475039539221/816710195195150366/unknown.png')
      return
  if IA == 2:
      await ctx.send('https://cdn.discordapp.com/attachments/797630475039539221/818838003119816756/Captura_de_ecra_2021-03-09_133000.png')
      return
  if IA == 3:
      await ctx.send('https://cdn.discordapp.com/attachments/797630475039539221/819957614531969054/unknown.png')
      return
  if IA == 4:
      await ctx.send('https://cdn.discordapp.com/attachments/797630475039539221/820674670147403787/rita.png')
      return
  if IA==5:
      await ctx.send('https://cdn.discordapp.com/attachments/797630475039539221/820675195160625152/unknown.png')
      return
  

@client.command(aliases=['pocinho', 'rita'])
async def notion(ctx):
  embed = discord.Embed(title = 'Melhor Notion(?)', url = 'https://www.notion.so/IST-MEEC-0c22d514a81645eca3c2a58739e323e1')
  embed.set_image(url='https://upload.wikimedia.org/wikipedia/pt/thumb/e/ed/IST_Logo.png/200px-IST_Logo.png')
  await ctx.send(embed = embed)


client.run(os.getenv('T0KEN'))