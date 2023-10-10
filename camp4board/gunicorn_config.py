import multiprocessing

bind = "0.0.0.0:80"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gthread"
threads = 2

errorlog = "error.txt"
accesslog = "access.txt"
