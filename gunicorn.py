"""Gunicorn server production settings."""

bind = "127.0.0.1:80"
workers = 5
worker_class = "eventlet"
max_requests = 1000
max_requests_jitter = 50
preload = True
