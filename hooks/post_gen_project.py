#!/usr/bin/env python
import os
import git
import versioneer
from blessed import Terminal

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    term = Terminal()

    if "{{ cookiecutter.create_author_file }}" != "y":
        print("=" * 77)
        print("Removing AUTHORS.rst file.")
        remove_file("AUTHORS.rst")
        print("Removing docs/source/authors.rst file.")
        remove_file("docs/source/authors.rst")

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        print("=" * 77)
        print("Removing LICENSE file.")
        remove_file("LICENSE")

    print("=" * 77)
    print("Initializing GIT repository.")
    repo0 = git.Repo.init(PROJECT_DIRECTORY)

    print("=" * 77)
    print("Installing versioneer.")
    versioneer.vendor()
    versioneer.do_setup()

    print("=" * 77)
    print("Staging files.")
    repo0.index.add(
        [
            "**",
            ".editorconfig",
            ".github/",
            ".gitignore",
        ]
    )
    repo0.index.commit("Initial commit")

    print("=" * 77)
    VERSION_TAG = "{{ cookiecutter.project_slug }}-v{{ cookiecutter.version }}"
    print("Adding version tag ({term.bright_blue}{VERSION_TAG}{term.normal}).")
    repo0.create_tag(VERSION_TAG)

    print("=" * 77)
    print(f"PROJECT_DIRECTORY: {term.bright_blue}{PROJECT_DIRECTORY}{term.normal}")
    print("=" * 77)
    print(
        " ".join(
            [
                f"The {term.bold}{{ cookiecutter.project_name }}{term.normal}",
                "project setup complete.",
                f"{term.bold_bright_green}Happy hacking!{term.normal}",
            ]
        )
    )
    print("=" * 77)
