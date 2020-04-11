import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(options={'args': ['--no-sandbox']})
    page = await browser.newPage()
    await page.goto('http://jianwi.cn')
    
    await page.screenshot({'path': 'example.png'})

    await browser.close()
asyncio.get_event_loop().run_until_complete(main())