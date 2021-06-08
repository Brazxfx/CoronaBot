from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import discord
from discord.ext import commands


url = 'https://www.coronatracker.com/pt-br/'

option = Options()
option.headless = True 
driver = webdriver.Chrome() 
driver.get(url)
sleep(3)

casos1 = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span').text
curados1 = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span').text
mortes1 = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/span').text
driver.quit()

print(f'Infectados: {casos1:>10}\nCurados: {curados1:>13}\nMortes: {mortes1:>14}')

#CoronaBot
client = commands.Bot(command_prefix= "!", case_insensitive = True)

@client.event
async def on_ready():
    print('Entramos como {0.user}' .format(client))

@client.command()
async def casos(ctx):
    await ctx.send(casos1)

@client.command()
async def curados(ctx):
    await ctx.send(curados1)
    
@client.command()
async def mortes(ctx):
    await ctx.send(mortes1)

client.run("TOKEN")