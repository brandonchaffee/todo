USER='brandonchaffee'
API_TOKEN=''
GIT_API_URL='https://api.github.com'

def get_api(url):
    try:
        request = urllib2.Request(GIT_API_URL + url)
        base64string = base64.encodestring('%s/token:%s' % (USER, API_TOKEN)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
        result = urllib2.urlopen(request)
        print(result)
        result.close()
    except:
        print('Failed to get api request from %s' % url)
