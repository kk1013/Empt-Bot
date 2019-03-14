import discord
import asyncio
import datetime
import random
import os
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

            if "바보" in message.content or "멍청이" in message.content:
        file = openpyxl.load.workbook("경고.xlsx")
        sheet = file.active
        member = discord.utils.get(client.get_all_members(), id="553935362716729356")
        for i in range(1, 31):
            if str(sheet["A" + str(i)].value) == str(message.author.id):
                sheet["B" + str(i)].value == int(sheet["B" + str(i)].value) + 1
                if int(sheet["B" + str(i)].value) == 3:
                    await client.ban(member, 1)
                break

            if str(sheet["A" + str(i)].value) == "-":
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 1
                break
        file.save("경고.xlsx")
        await client.send_message(message.channel, "경고를 받았습니다. 단어선택에 주의해주세요.")

    if message.content.startswith("!학습"):
        file = openpyxl.load_workbook("기억.xlsx")
        sheet = file.active
        learn = message.content.split(" ")
        for i in range (1, 51):
            if sheet["A" + str(i)].value == "-" or sheet["A" + str(i)].value ==learn[1]:
                sheet["A" + str(i)].value = learn[1]
                sheet["B" + str(i)].value = learn[2]
                await client.send_message(message.channel, "단어가 학습되었습니다.")
                break
        file.save("기억.xlsx")

    if message.content.startswith("!기억"):
        file = openpyxl.load_workbook("기억.xlsx")
        sheet = file.active
        memory = message.content.split(" ")
        for i in range ( 1, 51):
            if sheet["A" + str(i)].value == memory[1]:
                await client.send_message(message.channel, sheet["B" + str(i)].value)
                break

    if message.content.startswith("!기억삭제"):
        file = openpyxl.load_workbook("기억.xlsx")
        sheet = file.active
        memory = message.content.split(" ")
        for i in range(1, 51):
            if sheet["A" + str(i)].value == str(memory[1]):
                sheet["A" + str(i)].value = "-"
                sheet["B" + str(i)].value = "-"
                await client.send_message(message.channel, "기억이 삭제 되었습니다.")
                file.save("기억.xlsx")
                break

            
    if message.content.startswith("봇"):
        await client.send_message(message.channel, "뭐, 병X아")
    if message.content.startswith("씨발"):
        await client.send_message(message.channel, "욕하지마잉...미워! ㅠ_ㅠ")
    if message.content.startswith("병신"):
        await client.send_message(message.channel, "욕하지마잉...미워! ㅠ_ㅠ")
    if message.content.startswith("미친"):
        await client.send_message(message.channel, "욕하지마잉...미워! ㅠ_ㅠ")
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
