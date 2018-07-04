# Powrbot API
Python module to interact with Powrbot API

## How Tos
1. Login powrbot.com.
2. Click on your name (top right corner). A drop down menu appears.
3. Click on DEVELOPER.

## Secret Key
Use Secret Key to make API Requests. You find secret key in developer section. See below **Examples**.

## Powrbotclient
We have developoed lightweight wrapper to interact with Powrbot API. Install Powrbotclient

    pip install git+https://github.com/daviddigital/powrbotclient.git

## Callback URL
This is useful for bulk search. Bulk search process runs in background and notify you by email after search is finished. It also callback given URL. It makes POST request and send following data:

     {
        'id': ,
        'count': , 
        'is_completed': , 
        'download_url': 
    }

You can simply make API call to download_url and get your CSV. See **Download CSV** below.

## Examples

### 1. Search a Company

Search can be simple as:

    curl https://powrbot.com/api/v1/search/single/?company=Apple -H 'Authorization: secret-key <secret-key>'

Returns

    [
        {
            "wiki:Total assets": "US$375.319 billion[1] (2017)",
            "wiki:Type": "Public",
            "wiki:Number of employees": "123,000[1] (2017)",
            "name": "Apple",
            "wiki:Services": [
                "Apple Pay",
                "Apple Store",
                "iTunes Store",
                "App Store",
                "Mac App Store",
                "iBooks Store",
                "iCloud",
                "Apple Music"
            ],
            "wiki:ISIN": "US0378331005",
            "wiki:Founded": "1976",
            "wiki:Formerly called": [
                "Apple Computer Company(1976–1977)",
                "Apple Computer, Inc.(1977–2007)"
            ],
            "wiki:Revenue": "US$229.234 billion[1] (2017)",
            "wiki:Founders": [
                "Steve Jobs",
                "Steve Wozniak",
                "Ronald Wayne"
            ],
            "wiki:Net income": "US$48.351 billion[1] (2017)",
            "wiki:Website": "apple.com",
            "search:display_url": "apple.com",
            "wiki:Industry": [
                "Computer hardware",
                "Computer software",
                "Consumer electronics",
                "Digital distribution",
                "Semiconductors",
                "Fabless silicon design",
                "Corporate venture capital"
            ],
            "wiki:Number of locations": "499 retail stores (2017)",
            "wiki:Divisions": "",
            "wiki:Products": [
                "Macintosh",
                "iPod",
                "iPhone",
                "iPad",
                "Apple Watch",
                "Apple TV",
                "HomePod",
                "macOS",
                "iOS",
                "watchOS",
                "tvOS",
                "iLife",
                "iWork"
            ],
            "search:snippet": "Apple leads the world in innovation with iPhone, iPad, Mac, Apple Watch, iOS, OS X, watchOS and more. Visit the site to learn, buy, and get support.",
            "wiki:Area served": "Worldwide",
            "wiki:Subsidiaries": [
                "Shazam",
                "FileMaker Inc.",
                "Anobit",
                "Braeburn Capital",
                "Beats Electronics",
                "Apple Energy, LLC",
                "Apple Sales International[2]"
            ],
            "wiki:Total equity": "US$134.047 billion[1] (2017)",
            "wiki:Traded as": [
                "NASDAQ: AAPL",
                "NASDAQ-100 component",
                "DJIA component",
                "S&P 100 component",
                "S&P 500 component"
            ],
            "wiki:Headquarters": "Apple Park, 1 Apple Park Way, Cupertino, California, U.S.",
            "wiki:Key people": [
                "Arthur D. Levinson (Chairman)",
                "Tim Cook (CEO)",
                "Jonathan Ive (CDO)",
                "Luca Maestri (CFO)",
                "Jeff Williams (COO)"
            ],
            "wiki:Operating income": "US$61.344 billion[1] (2017)"
        }
    ]


You also can use post method, with Powrbotclient:

    from powrbot import Powrbot
    powrbot = Powrbot('secret_key')
    data = {
        'company': 'Apple'
    }

    result = powrbot.send(resource="/search/single/", data=data, method='post')

Returns:

    [
        {
            "wiki:Total assets": "US$375.319 billion[1] (2017)",
            "wiki:Type": "Public",
            "wiki:Number of employees": "123,000[1] (2017)",
            "name": "Apple",
            "wiki:Services": [
                "Apple Pay",
                "Apple Store",
                "iTunes Store",
                "App Store",
                "Mac App Store",
                "iBooks Store",
                "iCloud",
                "Apple Music"
            ],
            "wiki:ISIN": "US0378331005",
            "wiki:Founded": "1976",
            "wiki:Formerly called": [
                "Apple Computer Company(1976–1977)",
                "Apple Computer, Inc.(1977–2007)"
            ],
            "wiki:Revenue": "US$229.234 billion[1] (2017)",
            "wiki:Founders": [
                "Steve Jobs",
                "Steve Wozniak",
                "Ronald Wayne"
            ],
            "wiki:Net income": "US$48.351 billion[1] (2017)",
            "wiki:Website": "apple.com",
            "search:display_url": "apple.com",
            "wiki:Industry": [
                "Computer hardware",
                "Computer software",
                "Consumer electronics",
                "Digital distribution",
                "Semiconductors",
                "Fabless silicon design",
                "Corporate venture capital"
            ],
            "wiki:Number of locations": "499 retail stores (2017)",
            "wiki:Divisions": "",
            "wiki:Products": [
                "Macintosh",
                "iPod",
                "iPhone",
                "iPad",
                "Apple Watch",
                "Apple TV",
                "HomePod",
                "macOS",
                "iOS",
                "watchOS",
                "tvOS",
                "iLife",
                "iWork"
            ],
            "search:snippet": "Apple leads the world in innovation with iPhone, iPad, Mac, Apple Watch, iOS, OS X, watchOS and more. Visit the site to learn, buy, and get support.",
            "wiki:Area served": "Worldwide",
            "wiki:Subsidiaries": [
                "Shazam",
                "FileMaker Inc.",
                "Anobit",
                "Braeburn Capital",
                "Beats Electronics",
                "Apple Energy, LLC",
                "Apple Sales International[2]"
            ],
            "wiki:Total equity": "US$134.047 billion[1] (2017)",
            "wiki:Traded as": [
                "NASDAQ: AAPL",
                "NASDAQ-100 component",
                "DJIA component",
                "S&P 100 component",
                "S&P 500 component"
            ],
            "wiki:Headquarters": "Apple Park, 1 Apple Park Way, Cupertino, California, U.S.",
            "wiki:Key people": [
                "Arthur D. Levinson (Chairman)",
                "Tim Cook (CEO)",
                "Jonathan Ive (CDO)",
                "Luca Maestri (CFO)",
                "Jeff Williams (COO)"
            ],
            "wiki:Operating income": "US$61.344 billion[1] (2017)"
        }
    ]



### 2. Bulk Search

Download sample from [powrbot.com](https://powrbot.com/assets/sample.csv)

    from powrbot import Powrbot
    powrbot = Powrbot('secret_key')

    result = powrbot.send(file=path_to_csv_file, method='POST')
    # or can be this way too
    # result = powrbot.send(resource='search/', file=path_to_csv_file, method='POST')

### 3. Get Searches

    from powrbot import Powrbot
    powrbot = Powrbot('secret_key')

    result = powrbot.send()
    # or can be this way too
    # result = powrbot.send(resource='search', method='GET')


### 4. Get Result

    from powrbot import Powrbot
    powrbot = Powrbot('secret_key')

    result = powrbot.send( resource='search/<id>')
    # or 
    # result = powrbot.send( resource='search/<id>', method='GET')

### 5. Download CSV

    from powrbot import Powrbot
    powrbot = Powrbot('secret_key')

    result = powrbot.send(resource='search/<id>/download', method='GET')
