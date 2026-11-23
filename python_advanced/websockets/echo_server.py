#!/usr/bin/env python3

import asyncio
import websockets


async def connection_handler(websocket):
    async for message in websocket:
        if isinstance(message, str):
            await websocket.send(message)


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()  # Run forever


if __name__ == "__main__":
    asyncio.run(main())
