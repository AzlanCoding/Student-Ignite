#!/bin/env python
import asyncio
import sys
from mitmproxy import options
from mitmproxy.tools import dump

blocklist = ('discord.com')

class RequestLogger:
    def request(self, flow):
        print(flow.request.pretty_host)
        for hosts in blocklist:
            if flow.request.pretty_host == host:
                print('Blocked')
                #flow.request.host = "mitmproxy.org"
                flow.response.content = body.replace(OLD, NEW).encode("utf-8")
                flow.response.headers["XXX"] = "PATCHED"

async def start_proxy(host, port):
    opts = options.Options(listen_host=host, listen_port=port)

    master = dump.DumpMaster(
        opts,
        with_termlog=False,
        with_dumper=False,
    )
    master.addons.add(RequestLogger())
    
    await master.run()
    return master

if __name__ == '__main__':
    host='0.0.0.0'
    port=8080
    asyncio.run(start_proxy(host, port))
