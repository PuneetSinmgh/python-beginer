from pyodide.http import pyfetch # type: ignore
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())


import asyncio

async def main():
    await download(filename, "Product-sales.csv")
    df = pd.read_csv("Product-sales.csv")
    print(df)

asyncio.run(main())