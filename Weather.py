import pyfiglet,python_weather,platform
# import the module

import python_weather

import asyncio

import os

if platform.system() == "Windows":

    def clear(): os.system("cls")

else:

    def clear(): os.system("clear")

async def getweather():

  # Settiamo la libreria e le unità di misura come client

    clear()

    ascii_banner = pyfiglet.figlet_format("Weather")

    print(ascii_banner)

    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:

    # Prendiamo la temperatura della città

      x = input("Inserisci il nome della ciità (inglese): ")

      weather = await client.get(f'{x}')

    # Scriviamo nel terminale la temperatura

      z = (weather.current.temperature-32)*(5/9)
      print(f"Temperatura attuale: {round(z)}")
asyncio.run(getweather())