import asyncio
  
async def fn():
      
    print('welcome')
    await asyncio.sleep(2)
    await fn2()
    print('good morning')
    await asyncio.sleep(4)
    print('guys')
    await asyncio.sleep(5)
  
async def fn2():
    await asyncio.sleep(8)
    print('Hi')
    await asyncio.sleep(9)
    print("world")
asyncio.run(fn())
