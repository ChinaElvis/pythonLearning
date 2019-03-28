# 使用Beautiful Soup的屏幕抓取程序
from urllib import request
from bs4 import BeautifulSoup
response = request.urlopen("http://python.org/community/jobs").read()
soup = BeautifulSoup(response)

jobs = set()
for header in soup('h3'):
    links = header('a', 'reference')
    if not links: continue
    link = links[0]
    jobs.add('%s (%s)' % (link.string, link['href']))

print('\n'.join(sorted(jobs, key=lambda s:s.lower())))
