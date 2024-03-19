import multiprocessing

max_requests = 1000
max_requests_jitter = 50
log_file = "-"
bind = "0.0.0.0"
# bind = "0.0.0.0:50505"

timeout = 230
# https://learn.microsoft.com/en-us/troubleshoot/azure/app-service/web-apps-performance-faqs#why-does-my-request-time-out-after-230-seconds

num_cpus = multiprocessing.cpu_count()
workers = (num_cpus * 2) + 1

worker_class = "uvicorn.workers.UvicornWorker"

# az webapp up --runtime PYTHON:3.9 --sku B1 --name python-backend-api-webapp --resource-group appsvc_linux_centralus_basic
# az webapp config set --startup-file "python3 -m gunicorn app:app" --name python-backend-api-webapp