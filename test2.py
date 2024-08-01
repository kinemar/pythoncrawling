import test
import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

title = test.blog_title
link = test.blog_href

async def main(url):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)

    html = await page.content()
    await page.close()
    return html

i = 0
url = link[i]
html_response = asyncio.get_event_loop().run_until_complete(main(url))
soup = BeautifulSoup(html_response, 'html.parser')
blog = soup.find('iframe', {'id': 'mainFrame'})
print(blog)

