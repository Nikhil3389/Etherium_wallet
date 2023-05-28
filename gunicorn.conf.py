import multiprocessing

bind = "0.0.0.0:8080"
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
timeout = 120
max_requests = 1000
max_requests_jitter = 50
preload_app = True
daemon = True
module_name = "eth_balance.wsgi"

# Log configuration
accesslog = "-"
errorlog = "-"
loglevel = "info"
