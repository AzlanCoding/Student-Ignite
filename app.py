#!/usr/bin/env python

import asyncio
import signal
import os

import websockets


###

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

# scope of the application
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "/home/AzlanCoding/Student-Ignite/Cred.json", scope)

client = gspread.authorize(credentials)


# Open the spreadhseet
sheet = client.open("Zalando Data").worksheet("zalando_data")

# Get a list of all records
data = sheet.get_all_records()
pprint(data)

###

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)


async def main():
    # Set the stop condition when receiving SIGTERM.
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    async with websockets.serve(
        echo,
        host="",
        port=int(os.environ["8917"]),
    ):
        await stop


if __name__ == "__main__":
    asyncio.run(main())
