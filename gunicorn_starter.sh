#!/bin/sh

gunicorn --preload -c gunicorn_config.py --chdir ./common "app:create_app()"
