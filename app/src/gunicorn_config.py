pidfile = 'app01.pid'
worker_tmp_dir = '/dev/shm'
worker_class = 'gevent'
# worker_class = 'gthread'
# worker_class = 'sync'
workers = 1
#Threads under the same workers will use the same memory
#For us, we need to have one worker
worker_connections = 300
timeout = 1200
keepalive = 7200
threads = 2
proc_name = 'app01'
bind = '0.0.0.0:5001'
backlog = 2048
accesslog = '-'
errorlog = '-'
user = 'ubuntu'
group = 'ubuntu'
# Testing for blue green dev
# graceful_timeout = 7200
# loglevel = 'debug'