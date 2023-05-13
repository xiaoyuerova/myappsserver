#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management.commands.runserver import Command as Runserver
from myappsserver.conf import PORT


def main():
    # Runserver.default_addr = '0.0.0.0'  # 修改默认地址
    Runserver.default_port = PORT  # 修改默认端口

    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myappsserver.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
