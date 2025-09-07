import aiomoex
import pandas as pd
import asyncio
import aiohttp


class MOEXapi(object):
    """MOEXapi."""
    
    def __init__(self):
        self.api_url = r'https://iss.moex.com/'

    
    async def get(self, api_method, params, field, all=False):
        async with aiohttp.ClientSession() as session:
            iss = aiomoex.ISSClient(
                session,
                self.api_url + api_method,
                params
            )

            if all:
                data = await iss.get_all()
            
            else:
                data = await iss.get()
            
            data = pd.DataFrame(data[field])
            return data

                

if __name__ == '__main__':
    api = MOEXapi()
    url = r'/iss/statistics/engines/futures/markets/forts/series.json'
    params = {}
    field = 'series'

    df = asyncio.run(
        api.get(url, params, field)
    )

    pass
