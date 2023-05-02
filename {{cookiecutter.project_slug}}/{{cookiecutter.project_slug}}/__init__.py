#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""


__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"


from . import _version
__version__ = _version.get_versions()['version']
__version_dict__ = _version.get_versions()


def get_module_version():
    return __version__
