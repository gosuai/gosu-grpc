import os
from contextlib import asynccontextmanager
from contextvars import ContextVar
from functools import lru_cache
from types import MappingProxyType

import aiohttp
from google.auth.transport._aiohttp_requests import Request
from google.oauth2._service_account_async import Credentials
from grpclib.client import Channel


@lru_cache
def get_credentials():
    return Credentials.from_service_account_file(
        os.getenv('GOOGLE_APPLICATION_CREDENTIALS'),
        scopes=[
            'https://www.googleapis.com/auth/cloud-platform',
            'https://www.googleapis.com/auth/cloud-translation',
        ],
    )


channels_var = ContextVar('channels', default=MappingProxyType({}))


@asynccontextmanager
async def get_or_create_channel(host):
    channels = channels_var.get()
    if host in channels:
        yield channels[host]
    else:
        channel = Channel(host, 443, ssl=True)
        credentials = get_credentials()
        channel.project_id = credentials.project_id
        async with aiohttp.ClientSession() as sess:
            await credentials.refresh(Request(sess))
            channel.metadata = dict(authorization=f'Bearer {credentials.token}')
        new_channels = {host: channel}
        new_channels.update(channels)
        token = channels_var.set(MappingProxyType(new_channels))
        try:
            yield channel
        finally:
            channels_var.reset(token)
            channel.close()
