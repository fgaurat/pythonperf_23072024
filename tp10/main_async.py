#!/usr/bin/env python
import asyncio
import time
import threading

async def add(a,b):
    print("add",threading.current_thread().name)
    # await asyncio.sleep(1)
    return a+b


async def main():
    print("main",threading.current_thread().name)
    start = time.perf_counter()

    # print('Hello ...')
    # await asyncio.sleep(1)
    # print('... World!')

    # r =  await add(1,2)
    # print(r)
    # r = await add(1,2)
    # print(r)
    # r = await add(1,2)
    # print(r)
    
    all =[add(1,2),add(1,2),add(1,2)]

    # results = await asyncio.gather(*all)
    # print(results)
    
    # end = time.perf_counter()
    # print(f"{end-start:.3}s")




if __name__ == '__main__':
    asyncio.run(main())
