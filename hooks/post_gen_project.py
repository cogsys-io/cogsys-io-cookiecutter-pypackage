#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        print("="*77)
        print("Removing AUTHORS.rst file.")
        remove_file('AUTHORS.rst')
        print("Removing docs/source/authors.rst file.")
        remove_file('docs/source/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        print("="*77)
        print("Removing cli.py file.")
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        print("="*77)
        print("Removing LICENSE file.")
        remove_file('LICENSE')
