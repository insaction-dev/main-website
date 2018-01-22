"""Gunicorn server production settings."""

bind = "unix:/opt/insaction/insaction.sock"
workers = 5
worker_class = "eventlet"
max_requests = 1000
max_requests_jitter = 50
preload = True
