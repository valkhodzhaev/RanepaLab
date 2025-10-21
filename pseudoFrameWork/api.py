import aiomoex
import pandas as pd
import asyncio
import aiohttp


MOEX_API_URL = r'https://iss.moex.com'


async def getAnyMOEX(api_method: str, arguments: dict, field: str, all: bool = False) -> pd.DataFrame:
    """getAnyMOEX"""
    async with aiohttp.ClientSession(trust_env=True) as session:
        iss = aiomoex.ISSClient(session, MOEX_API_URL + api_method, arguments)

        data = await iss.get_all() if all else await iss.get()
    
        return pd.DataFrame(data[field])
