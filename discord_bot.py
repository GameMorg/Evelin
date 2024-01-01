import discord
import bot_2

# Создание экземпляра клиента Discord с указанием параметра intents
intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)

# Событие запуска бота
@client.event
async def on_ready():
    print('Бот успешно запущен!')

# Событие при получении нового сообщения
@client.event
async def on_message(message):
    # Проверка, чтобы бот не реагировал на свои собственные сообщения
    if message.author == client.user:
        return

    # Получение текста сообщения от пользователя
    user_message = message.content

    print(user_message)
    

    # Создание ответного сообщения с добавленным текстом от пользователя
    response = bot_2.neural_network_response(user_message)

    # Отправка ответного сообщения
    await message.channel.send(response)

# Запуск бота с помощью токена вашего приложения Discord
client.run('#')
