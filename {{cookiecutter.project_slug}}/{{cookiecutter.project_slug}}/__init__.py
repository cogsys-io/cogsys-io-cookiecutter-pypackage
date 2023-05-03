#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""

# fmt: off
from . import _version
__version__ = _version.get_versions()['version']
__version_dict__ = _version.get_versions()
# fmt: on

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"


def get_module_version():
    return __version__


# end
