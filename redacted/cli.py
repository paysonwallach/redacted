#
# Redacted
#
# Copyright © 2021 Payson Wallach
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import functools

from typing import Callable

import click

from redacted.filter import FilterAction, Filter
from redacted.config import get_config


def process(name: str, action: FilterAction):
    filter = Filter.from_config(name, action, get_config())
    while True:
        try:
            line = sys.stdin.readline()
        except KeyboardInterrupt:
            break

        if not line:
            break

        sys.stdout.write(filter.sub(line))


def common_arguments(func: Callable) -> Callable:
    @click.argument("name")
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@click.group()
def main():
    """redacted cli"""


@main.command()
@common_arguments
def clean(name: str):
    process(name, FilterAction.CLEAN)


@main.command()
@common_arguments
def smudge(name: str):
    process(name, FilterAction.SMUDGE)
