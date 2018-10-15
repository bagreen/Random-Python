import bs4, os, requests

url = 'http://xkcd.com'

os.makedirs('xkcd', exist_ok=True) # makes a directory to store data

while not url.endswith('#'):
    # downloading the page
    print('Downloading page %s...' %url)
    webRequest = requests.get(url)
    webRequest.raise_for_status()

    webSoup = bs4.BeautifulSoup(webRequest.text)

    # find url of comic
    comicElement = webSoup.select('#comic img')
    if comicElement == []:
        print('Could not find comic image')
    else:
        comicUrl = 'http:' + comicElement[0].get('src')

        # download image
        print('Downloading image %s...' %(comicUrl))
        webRequest = requests.get(comicUrl) # new webRequest is image, then checks it for errors
        webRequest.raise_for_status()

        # save image
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

        for chunk in webRequest.iter_content(100000):
            imageFile.write(chunk)

        imageFile.close()

    # get previous buttons url to go to next one
    previousLink = webSoup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + previousLink.get('href')

print('Done.')
