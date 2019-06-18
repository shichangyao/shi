import time
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
import requests

url="https://music.163.com/weapi/v1/resource/comments/R_50_4_547973474?csrf_token=123"
headers={}
body="params="
def fetch(url):




start =time.time()
#for i in range(100):
fetch(url)
pprint(f"耗时{time.time()-start:.2f}秒")