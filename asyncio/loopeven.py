import asyncio  
  
async def speech_async():  
    print('This is a asynchronicity!')  
  
loop = asyncio.get_event_loop()  
loop.run_until_complete(speech_async())  
loop.close()  