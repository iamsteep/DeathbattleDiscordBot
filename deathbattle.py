import json
import asyncio
import aiohttp
from aiohttp import ClientSession
from imageLayer import *
from os import system, name
import requests
import random

if name == "nt":
	system("cls")
else:
	system("clear")

# token
token = "Bot " + os.environ["TOKEN"]
headers = {
  "authorization": token,
}

fileheaders = {
  "authorization": token,
  "multipart/form-data": "file",
}

# gateway url
URL = "wss://gateway.discord.gg/"

wsauth = {
  "op": 2,  
  "d": {
    "token": token,
    "properties": {},
    "compress": False,
    "large_threshold": 250
    }
}

heart = {
  "op": 1,
  "d": ""
}

embed = {
  "embed": {
    "title": "cao",
    "description": "bruh",
    "color": "3066993",
  },
}

pfp1 = None
pfp2 = None

async def api(method, path, params=None):
  try:
    async with aiohttp.ClientSession() as session:
      if method == "DELETE":
        async with session.delete(f"https://discord.com/api/v6{path}", headers=headers) as resp:
          #return await resp.json()
          pass
      elif method == "GET":
        async with session.get(f"https://discord.com/api/v6{path}", headers=headers) as resp:
          return await resp.json()
      elif method == "POST":
        async with session.post(f"https://discord.com/api/v6{path}", headers=headers, json=params) as resp:
          return await resp.json()
          #pass
      elif method == "PUT":
        async with session.put(f"https://discord.com/api/v6{path}", headers=headers, json=params) as resp:
          return await resp.json()
          #pass
      elif method == "PATCH":
        async with session.patch(f"https://discord.com/api/v6{path}", headers=headers, json=params) as resp:
          return await resp.json()
          #pass
  except Exception as e:
    pass

async def heartbeat(ws, interval):
  #await asyncio.sleep(interval / 1000)
  await ws.send_str(json.dumps(heart))

async def start(url):
  try:
    async with aiohttp.ClientSession() as session:
      async with session.ws_connect(f"{url}?v=6&encoding=json") as ws:
        async for msg in ws:
          data = json.loads(msg.data)

          hb = data["d"]["heartbeat_interval"]
          heart["d"] = data["d"]

          if data["op"] == 10:
            await ws.send_str(json.dumps(wsauth))
            await heartbeat(ws, hb)

            while True:
              recv = await ws.receive()
              if recv.data != 1000:
                if "MESSAGE_CREATE" in recv.data:
                  datamsg = json.loads(str(recv.data))
                  if datamsg["t"] == "MESSAGE_CREATE":
                    if str("!deathbattle") in datamsg["d"]["content"]:
                      await Download(f'https://cdn.discordapp.com/avatars/{datamsg["d"]["mentions"][0]["id"]}/{datamsg["d"]["mentions"][0]["avatar"]}.png', f'https://cdn.discordapp.com/avatars/{datamsg["d"]["author"]["id"]}/{datamsg["d"]["author"]["avatar"]}.png')
                      makeimg(datamsg["d"]["author"]["username"], datamsg["d"]["mentions"][0]["username"])

                      authorname = datamsg["d"]["author"]["username"]
                      mentionname = datamsg["d"]["mentions"][0]["username"]

                      if name == "nt":
                        system("del *.png")
                      else:
                        system("rm *.png")

                      files = {
                        "final.jpg": ('final.jpg', open('final.jpg', 'rb'))
                      }

                      bruhmomenat = {"content": "Борба!"}
                      await api("POST", "/channels/{chid}/messages".format(chid=datamsg["d"]["channel_id"]), bruhmomenat)

                      requests.post("https://discord.com/api/v6/channels/{chid}/messages".format(chid=datamsg["d"]["channel_id"]), headers=fileheaders, files=files)

                      embed["embed"]["title"] = datamsg["d"]["author"]["username"] + " против " + datamsg["d"]["mentions"][0]["username"]
                      embed["embed"]["description"] = "Борба почиње!"

                      fightmsg = await api("POST", "/channels/{chid}/messages".format(chid=datamsg["d"]["channel_id"]), embed)
                      fightjson = json.dumps(fightmsg)
                      json2 = json.loads(fightjson)
                      msgid = json2['id']

                      p1 = 100
                      p2 = 100

                      while True:

                        p1win = authorname + " = " + str(p1) + "\n" + mentionname + " = " + str(0) +  "\n\n" + authorname + ' је краљ игре'
                        p2win = mentionname + " = " + str(p2) + "\n" + authorname + " = " + str(0) +  "\n\n" + mentionname + ' је краљ игре'
                          
                        xpxd = random.randint(5, 50)

                        wordsp1 = list()
                        wordsp2 = list()

                        wordsp1.append(authorname + ' је запалио ' + mentionname + ' бацачем пламена, добар посао Ханс ' + str(xpxd) + ' ХП')
                        wordsp1.append(authorname + ' је претукао ' + mentionname + ' на мртво ' + str(xpxd) + ' ХП')
                        wordsp1.append(authorname + ' је набио курцем ' + mentionname + ' ' + str(xpxd) + ' ХП')
                        wordsp1.append(authorname + ' је јебао кеву ' + mentionname + ' ' + str(xpxd) + ' ХП')
                        wordsp1.append(authorname + ' је извршио геноцид над градом у којем живи ' + mentionname + ' ' + str(xpxd) + ' ХП')
                        wordsp1.append(authorname + ' је натукао ' + mentionname + ' на волеј ' + str(xpxd) + ' ХП')
                        wordsp1.append(authorname + ' се попишао по гробу од ' + mentionname + ' ' + str(xpxd) + ' ХП')
                      
                        wordsp2.append(mentionname + ' је запалио ' + authorname + ' бацачем пламена, добар посао Ханс ' + str(xpxd) + ' ХП')
                        wordsp2.append(mentionname + ' је претукао' + authorname + ' на мртво ' + str(xpxd) + ' ХП')
                        wordsp2.append(mentionname + ' је набио курцем ' + authorname + ' ' + str(xpxd) + ' ХП')
                        wordsp2.append(mentionname + ' је јебао кеву ' + authorname + ' ' + str(xpxd) + ' ХП')
                        wordsp2.append(mentionname + ' је извршио геноцид над градом у којем живи ' + authorname + str(xpxd) + ' ХП')
                        wordsp2.append(mentionname + ' је натукао ' + authorname + ' на волеј ' + str(xpxd) + ' ХП')
                        wordsp2.append(mentionname + ' се попишао по гробу од ' + authorname + str(xpxd) + ' ХП')

                        p2 -= xpxd
                        if p2 < 0:
                          p1 = 0
                          embed["embed"]["description"] = p1win
                          await api("PATCH", "/channels/{chid}/messages/{msgid}".format(chid=datamsg["d"]["channel_id"], msgid=msgid), embed)
                          break
                        await api("PATCH", "/channels/{chid}/messages/{msgid}".format(chid=datamsg["d"]["channel_id"], msgid=msgid), embed)
                        embed["embed"]["description"] = random.choice(wordsp2) + "\n\n" + mentionname + " = " + str(p2) + "\n" + authorname + " = " + str(p1)

                        await asyncio.sleep(2)

                        wordsp1.clear()
                        wordsp2.clear()

                        xpxd = random.randint(5, 50)

                        wordsp1.append(authorname + ' је запалио ' + mentionname + ' бацачем пламена, добар посао Ханс ' + str(xpxd) + ' ХП')
                        wordsp1.append(authorname + ' је претукао ' + mentionname + ' на мртво ' + str(xpxd) + ' ХП')
                        wordsp1.append(authorname + ' је набио курцем ' + mentionname + ' ' + str(xpxd) + ' ХП')
                        wordsp1.append(authorname + ' је јебао кеву ' + mentionname + ' ' + str(xpxd) + ' ХП')
                        wordsp1.append(authorname + ' је извршио геноцид над градом у којем живи ' + mentionname + ' ' + str(xpxd) + ' ХП')
                        wordsp1.append(authorname + ' је натукао ' + mentionname + ' на волеј ' + str(xpxd) + ' ХП')
                        wordsp1.append(authorname + ' се попишао по гробу од ' + mentionname + ' ' + str(xpxd) + ' ХП')
                      
                        wordsp2.append(mentionname + ' је запалио ' + authorname + ' бацачем пламена, добар посао Ханс ' + str(xpxd) + ' ХП')
                        wordsp2.append(mentionname + ' је претукао' + authorname + ' на мртво ' + str(xpxd) + ' ХП')
                        wordsp2.append(mentionname + ' је набио курцем ' + authorname + ' ' + str(xpxd) + ' ХП')
                        wordsp2.append(mentionname + ' је јебао кеву ' + authorname + ' ' + str(xpxd) + ' ХП')
                        wordsp2.append(mentionname + ' је извршио геноцид над градом у којем живи ' + authorname + str(xpxd) + ' ХП')
                        wordsp2.append(mentionname + ' је натукао ' + authorname + ' на волеј ' + str(xpxd) + ' ХП')
                        wordsp2.append(mentionname + ' се попишао по гробу од ' + authorname + str(xpxd) + ' ХП')

                        p1 -= xpxd
                        if p1 < 0:
                          p2 = 0
                          embed["embed"]["description"] = p2win
                          await api("PATCH", "/channels/{chid}/messages/{msgid}".format(chid=datamsg["d"]["channel_id"], msgid=msgid), embed)
                          break
                        await api("PATCH", "/channels/{chid}/messages/{msgid}".format(chid=datamsg["d"]["channel_id"], msgid=msgid), embed)
                        embed["embed"]["description"] = random.choice(wordsp1) + "\n\n" + authorname + " = " + str(p1) + "\n" + mentionname + " = " + str(p2)

                        await asyncio.sleep(2)

                        wordsp1.clear()
                        wordsp2.clear()

          elif data["op"] == 0:
            print(data['t'], data['d'])
          else:
            print(data)

  except Exception as e:
    await start(URL)

async def main():
  response = await api("GET", "/gateway")
  URL = response["url"]
  await start(URL)   

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.run_forever()