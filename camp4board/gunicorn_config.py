import multiprocessing

bind = "localhost:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gthread"
threads = 2

# gunicorn_config.py
import logging

logconfig_dict = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',  # Set the desired log level, e.g., 'DEBUG' for maximum logging.
    },
}
logconfig_dict['loggers'] = {
    'gunicorn.error': {
        'level': 'DEBUG',  # Adjust the log level as needed.
        'handlers': ['console'],
        'propagate': False,
        'qualname': 'gunicorn.error',
    },
}
