import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

async def main(url):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)

    html = await page.content()
    await page.close()
    return html

keywords = input("Enter keywords: ")
htmlurl = 'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query='
htmlurl = htmlurl + keywords
print(htmlurl)

html_response = asyncio.get_event_loop().run_until_complete(main(htmlurl))

soup = BeautifulSoup(html_response, 'html.parser')
blog = soup.findAll('a',{'class':'title_link'})
blog_title = [value.text for value in blog]
print('title', blog_title)
blog_href = [value.attrs['href'] for value in blog]
print('href', blog_href)