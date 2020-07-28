import aiofiles
import aiohttp
import asyncio
from cv import Edit

pfp = None
pfp1 = None

async def Download(url, url1):
    global pfp
    global pfp1
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                pfp = url.split("/")[-1]
                f = await aiofiles.open(pfp, mode='wb')
                await f.write(await resp.read())
                await f.close()
	            
        async with session.get(url1) as resps:
            if resps.status == 200:
                pfp1 = url1.split("/")[-1]
                f1 = await aiofiles.open(pfp1, mode='wb')
                await f1.write(await resps.read())
                await f1.close()
	           
def makeimg(name, name1):
    Edit(pfp1, pfp, name1, name)