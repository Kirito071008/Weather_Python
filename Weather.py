import pyfiglet,python_weather,platform
import asyncio,os
if platform.system() == "Windows":
    def clear(): os.system("cls")
else:
    def clear(): os.system("clear")
async def getweather():
    clear()
    ascii_banner = pyfiglet.figlet_format("Weather")
    print(ascii_banner)
    print("By Kirito071008")
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
      x = input("Enter the city name: ")
      weather = await client.get(f'{x}')
      z = (weather.current.temperature-32)*(5/9)
      print(f"Temperature: {round(z)}")
asyncio.run(getweather())
