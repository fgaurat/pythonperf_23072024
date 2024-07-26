from celery import Celery
import requests
app = Celery('tasks', broker='pyamqp://guest@localhost//',backend="rpc://")

@app.task
def add(x, y):
    return x + y

@app.task
def hello():
    return 'hello world'


@app.task
def download(url):
    log_file = url.split("/")[-1]
    response = requests.get(url)
    data = {
            "log_file":log_file,
            "text":response.text
        }    
    
    return data

@app.task
def save(data):
    log_file = data['log_file']
    text = data['text']
    print("write",log_file)
    with open(log_file,'w') as f:
        f.write(text)
