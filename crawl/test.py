import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://search.douban.com/book/subject_search?search_text=mysql&cat=1001&start=15')
    print(page)
    await page.screenshot({'path': 'example.png'})

    await browser.close()
asyncio.get_event_loop().run_until_complete(main())