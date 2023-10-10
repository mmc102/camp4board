import multiprocessing

bind = "http://127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gthread"
threads = 2

errorlog = "error.txt"
accesslog = "access.txt"
