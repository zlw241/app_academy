
import requests

def fibonacci(n):
    pre = 0
    post = 1
    fibs = [post]
    while len(str(post)) < 1000:
        pre, post = post, pre+post
        fibs.append(post)

    return len(fibs)


#print(fibonacci(100))


ip = requests.get('http://httpbin.org/ip')

print(ip.text)


