# """
# 异步处理：
# 多任务协作处理
# 回调式编程/feature对象获取任务执行的结果
# python3 使用asyncio模块和await、async关键字支持异步处理
# """
#
# import time
# import asyncio
# from aiohttp import ClientSession
#
# tasks = []
# url = "https://www.baidu.com/{}"
# async def hello(url):
#     async with ClientSession() as session:
#         async with session.get(url) as response:
#             response = await response.read()
# #           print(response)
#             print('Hello World:%s' % time.time())
#
# def run():
#     for i in range(5):
#         task = asyncio.ensure_future(hello(url.format(i)))
#         tasks.append(task)
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     run()
#     loop.run_until_complete(asyncio.wait(tasks))

import asyncio

from aiohttp import web


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')


async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
