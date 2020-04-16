from multiprocessing import cpu_count

bind = '0.0.0.0:8000'
worker_class = 'gevent'
workers = cpu_count() * 2 + 1
max_requests = 1024
capture_output = True
