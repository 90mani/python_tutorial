import asyncio
  
async def fn():
      
    print("good night")
    await asyncio.sleep(2)
    await fn2()
    print('good morning')
    await asyncio.sleep(3)
    print('how are you')
    await asyncio.sleep(4)
  
async def fn2():
    await asyncio.sleep(5)
    print("hi")
    await asyncio.sleep(6)
    print("iam")
asyncio.run(fn())