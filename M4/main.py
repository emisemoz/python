import discord 
import random
intents = discord.Intents.default()
intents.message_content=True
client = discord.Client(intents=intents)
sad_words=["sad", "depressed", "angry", "hurting", "stressed"]
encouragements = [
    "Cheer up! 🤗",
    "Hang in there",
    "You are a great person! 👍",
    "Come on! You can do it! 💪",
    "Stay strong"
]
happy_words=["happy", "glad", "joyful", "satisfied", "blessed"]
encouragement = [
    "There you go! 👏",
    "Keep up the good work 👍",
    "Keep it up 🙌",
    "Good job 👍",
    "I'm so proud of you! 🥰"
]
songs=[
    "https://youtu.be/9t57C7NcjWo?si=gscD7bYbI_xFvi2M",
    "https://youtu.be/-GQg25oP0S4?si=l6b-TcwRc8CFAGAw",
    "https://youtu.be/0P0aQreFs8w?si=VH9QMEjzSqf9JBMG",
    "https://youtu.be/wXFLzODIdUI?si=0CWgvbyKNmle0vLn"
]

@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send(f'Hello 👋😃')
    if message.content.startswith('w!hello'):
        await message.channel.send('https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjJ3aHVjZnZkZDUwbjJ5cTgybWx4dXUzcjc5cWVvcnMyNHZnNHozcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/sGAun8ArlRC0KcisbC/giphy.gif')
        
    if any(word in message.content for word in sad_words):
        response = random.choice(encouragements)
        await message.channel.send(response)
    if any(word in message.content for word in happy_words):
        response = random.choice(encouragement)
        await message.channel.send(response)
    if message.content.startswith('!random song'):
        random_song = random.choice(songs)
        await message.channel.send(random_song)
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
