import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def send_get_request(url):
    with urllib.request.urlopen(url) as response:
        print("Headers Information:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
        return response.read().decode('utf-8')

def send_post_request(url, data):
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')  
    req = urllib.request.Request(url, data, method='POST')
    with urllib.request.urlopen(req) as response:
        print("Headers Information:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
        return response.read().decode('utf-8')

def send_put_request(url, data):
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')  
    req = urllib.request.Request(url, data, method='PUT')
    with urllib.request.urlopen(req) as response:
        print("Headers Information:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
        return response.read().decode('utf-8')

def send_delete_request(url):
    req = urllib.request.Request(url, method='DELETE')
    with urllib.request.urlopen(req) as response:
        print("Headers Information:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
        return response.read().decode('utf-8')


# 예제 API 엔드포인트
api_url = 'https://api.bgogooma.com/'

# GET 요청 보내기
print("GET 요청 결과:")
print(send_get_request(api_url+'kakaomap'))

# BeautifulSoup을 사용하여 HTML을 파싱합니다.
soup = BeautifulSoup(send_get_request(api_url+'kakaomap'), 'html.parser')

# 웹 페이지에서 원하는 정보를 찾습니다.
# 예를 들어, <title> 태그 안에 있는 제목을 추출합니다.
title = soup.title.string

# 추출한 정보를 출력합니다.
print("웹 페이지 제목:", title)

# POST 요청 보내기
post_data = {'username': 'wee45387@gmail.com', 'password': 'wee45387'}
print("\nPOST 요청 결과:")
print(send_post_request(api_url+'v1/users/signin/', post_data))


# PUT 요청 보내기
put_data = {'id': 1, 'title': 'foo', 'body': 'bar', 'userId': 1}
print("\nPUT 요청 결과:")
print(send_put_request(api_url, put_data))

# DELETE 요청 보내기
print("\nDELETE 요청 결과:")
print(send_delete_request(api_url))

# 네이버 홈페이지 URL
naver_url = "https://www.naver.com"

# send_get_request 함수를 사용하여 네이버 홈페이지에 GET 요청을 보냅니다.
naver_page_content = send_get_request(naver_url)

# BeautifulSoup을 사용하여 HTML을 파싱합니다.
soup = BeautifulSoup(naver_page_content, 'html.parser')

# 네이버 홈페이지의 제목을 가져옵니다.
# 네이버 홈페이지의 제목은 <title> 태그 내에 있습니다.
title = soup.title.string

# 추출한 제목을 출력합니다.
print("네이버 홈페이지 제목:", title)