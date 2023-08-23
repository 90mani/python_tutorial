import asyncio
  
async def sample_programe():
    await asyncio.sleep(2)
    print('hello world')
    await asyncio.sleep(5)
    print('Is basic programming')
    await asyncio.sleep(6)
    print('in python')
  
asyncio.run(sample_programe())