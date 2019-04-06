from bs4 import BeautifulSoup
import urllib.request as url
url_domain = 'http://likms.assembly.go.kr'
url_sub = '/bill/billDetail.do?'
url_qstr = 'billId=PRC_R1N9J0N1X0Y9A1O8S3R5Z3J3K9O8N7'
url_str = url_domain+url_sub+url_qstr
html = url.urlopen(url_str).read()
soup = BeautifulSoup(html, 'html.parser')
txt = soup.find(attrs={'class' : 'subti01'} ).text
print(txt)