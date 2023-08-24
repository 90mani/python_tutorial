import asyncio  
import time  
  
async def execute(delay, value):  
    await asyncio.sleep(delay)  
    print(value)  
  
async def main():  
    print(f"started at {time.strftime('%X')}")  
  
    await execute(1, 'hello')  
    await execute(2, 'world')  
  
    print(f"finished at {time.strftime('%X')}")  
  
asyncio.run(main())  