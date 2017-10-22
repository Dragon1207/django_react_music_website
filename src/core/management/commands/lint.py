#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from glob import glob
from subprocess import call

from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Lint and check code style with flake8 and isort'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--fix-imports', action='store_true',
                            help='Fix imports using isort, before linting')

    def handle(self, *args, **options):
        skip = ['requirements', 'env', 'static']
        root_files = glob('*.py')
        root_directories = [name for name in next(os.walk('.'))[1] if not name.startswith('.')]
        files_and_directories = [arg for arg in root_files + root_directories if arg not in skip]

        def execute_tool(description, *args2):
            """Execute a checking tool with its arguments."""
            command_line = list(args2) + files_and_directories
            print('{}: {}'.format(description, ' '.join(command_line)))
            rv = call(command_line)
            if rv is not 0:
                exit(rv)

        scripts_path = os.path.dirname(sys.executable)
        if os.name == 'nt':
            scripts_path = os.path.join(scripts_path, 'Scripts')

        if options['fix_imports']:
            execute_tool('Fixing import order', os.path.join(scripts_path, 'isort'), '-rc')
        execute_tool('Checking code style', os.path.join(scripts_path, 'flake8'))
