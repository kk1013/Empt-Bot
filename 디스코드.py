import discord
import asyncio
import datetime
import random
client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("--------------------")
    await client.change_presence(game=discord.Game(name='엠트가 시켜서 대화중...', type=1))

@client.event
async def on_message(message):
    if message.content.startswith('!프로필'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(coler=0x00ffbb)
        embed.add_field(name="사용자 이름", value=message.author.name, inline=True)
        embed.add_field(name="서버내 이름", value=message.author.display_name, inline=True)
        embed.add_field(name="계정생성일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith("!안녕"):
        await client.send_message(message.channel, "안녕하세요")

    if message.content.startswith("!롤하실분"):
        await client.send_message(message.channel, "@everyone 롤하실분들!! 구합니다!")

    if message.content.startswith("!바보"):
        await client.send_message(message.channel, "응 니달이\n애니\n미스포츈 좋더라")

    if message.content.startswith("엠트"):
        await client.send_message(message.channel, "지금 엠트님은 수면 중이니 급한거 있으시면 개인으로 보내주세요.")

    if message.content.startswith("!사랑해"):
        await client.send_message(message.channel, "나는 여자가 좋아 ")

    if message.content.startswith("!팀나누기"):
        team = message.content[6:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await client.send_message(message.channel, person[i] + "---->" + teamname[i])

    if message.content.startswith("!서버"):

        list = []
        for server in client.servers:
            list.append(server.name)
        await client.send_message(message.channel, "\n".join(list))


    if message.content.startswith("!투표"):
        vote = message.content[4:].split("/")
        await client.send_message(message.channel, "★투표 - " + vote[0])
        for i in range(1, len(vote)):
            choose = await client.send_message(message.channel, "```" + vote[i] + "```")
            await client.add_reaction(choose, '☺')

    if message.content.startswith("!명령어"):
        await client.send_message(message.channel, "``` 1. !안녕```")
        await client.send_message(message.channel, "``` 2. !롤하실분```")
        await client.send_message(message.channel, "``` 3. !바보```")
        await client.send_message(message.channel, "``` 4. 엠트```")
        await client.send_message(message.channel, "``` 5. !사랑해```")
        await client.send_message(message.channel, "``` 6. !프로필```")
        await client.send_message(message.channel, "``` 7. !서버```")

        if message.content.startswith('/신고'):
            text = ""

            learn = message.content.split(" ")

            vrsize = len(learn)

            vrsize = int(vrsize)

            for i in range(1, vrsize):
                text = text + learn[i]

            learn = message.content.split(" ")
            msg = '{0.author.mention}'.format(message) + '님이 신고하셨습니다.' + '\n 신고내용' + '' + text + ''
            user = await client.get_user_info(221590489835634699)
            await client.send_message(user, msg)
            
    if message.content.startswith("봇"):
        await client.send_message(message.channel, "뭐, 병X아")
    if message.content.startswith("씨발"):
        await client.send_message(message.channel, "욕하지마잉...미워! ㅠ_ㅠ")
    if message.content.startswith("병신"):
        await client.send_message(message.channel, "욕하지마잉...미워! ㅠ_ㅠ")
    if message.content.startswith("미친"):
        await client.send_message(message.channel, "욕하지마잉...미워! ㅠ_ㅠ")

client.run("NTUzOTM1MzYyNzE2NzI5MzU2.D2VbDw.WhTK7C6VMvaTV9rlVQUvUm1O2P4")
