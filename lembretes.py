import asyncio
from datetime import datetime
from asyncio import tasks
import requests
import discord
from discord.ext  import commands, tasks

TOKEN="INSERT_YOUR_BOT_TOKEN_HERE"

bot= commands.Bot("!")
leader_list = ['H. Wilson#6897']

def log_command(ctx):
    print(f'{ctx.author} used "{ctx.message.content}" in the channel #{ctx.channel} at {get_hms()}')
def get_hms():
    dt = datetime.datetime.now()
    return f'{dt.hour}:{dt.minute}:{dt.second}'

@bot.event
async def on_command_error(ctx, error):
    await ctx.channel.send(error)
    return print(
        f'{ctx.author} caused an error using "{ctx.message.content}" in the channel #{ctx.channel} at {get_hms()}'
    )
@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user}")
    current_time.start()
@bot.event
async def on_message(message):
    if  message.author == bot.user:
        return
    if "palavrão" in message.content:
        await message.channel.send(
            f"Por favor, {message.author.name}, não ofenda os demais usuários!"
        )
        await message.delet()
    await bot.process_commands(message)


#commands
@bot.command(name="oi")
async def send_hello(ctx):
    autor= ctx.author.name
    response = "Olá, " + autor
    await ctx.send(response)

@bot.command(name="calcular")
async def  calculate_expression(ctx, *expression):
    expression = "".join(expression)
    print(expression)
    response= eval(expression)
    await ctx.send("A resposta é: " + str (response))


@bot.command(name="add")
async def add(ctx):
        with open(f"{ctx.author.name}#{ctx.author.discriminator}.txt", "a") as texto:
            content= (ctx.message.content.split("add")[1])
            texto.write(f"{content}\n")

@bot.command(name="agenda")
async def agenda(ctx):
    try:
        with open(f"{ctx.author.name}#{ctx.author.discriminator}.txt", "r") as texto:
            await ctx.author.send(f"Suas anotações:\n{texto.read()}")
    except FileNotFoundError:
        with open(f"{ctx.author.name}#{ctx.author.discriminator}.txt", "x") as texto:
            await ctx.author.send("Arquivo vazio, criando um")

@bot.command(name='clear')
async def clear_command(ctx, count):
    if str(ctx.author) in leader_list:
        if int(count) <= 50:
            await ctx.channel.purge(limit=int(count)+1)
        elif int(count) > 50:
            await ctx.channel.send('Eu posso limpar até 50 mensagens só!')

#tasks
@tasks.loop(hours=2)
async def current_time():
    now = datetime.now()
    now = now.strftime("%d/%m/%Y às %H:%M:%S")
    channel = bot.get_channel(995894787330809876)
    await channel.send("Data atual: " + now)


if __name__ == "__main__":
    bot.run(TOKEN)