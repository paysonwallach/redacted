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

import os
import configparser

from pathlib import Path
from typing import Optional

REDACTED_CONFIG_FILE = ".redacted.conf"


def get_repository_root() -> Optional[str]:
    cwd_path = Path.cwd()
    parent_paths = [
        cwd_path,
    ]
    parent_paths.extend(cwd_path.parents)
    for parent_path in parent_paths:
        if parent_path.joinpath(".git").exists():
            return parent_path

    return None


def get_config_file_path() -> str:
    config_file_path = None
    config_file_path_override = os.getenv("REDACTED_CONFIG_PATH")
    if config_file_path_override is not None:
        config_file_path = Path(config_file_path_override)
    else:
        repository_root_path = get_repository_root()
        if repository_root_path is None:
            config_file_path = Path(REDACTED_CONFIG_FILE)
        else:
            config_file_path = repository_root_path.joinpath(
                REDACTED_CONFIG_FILE
            )

    if not config_file_path.is_absolute():
        config_file_path = Path.home().joinpath(config_file_path)

    return config_file_path


def load_config_from_string(contents: str) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read_string(contents)

    return config


def get_config():
    with open(get_config_file_path(), "r") as config_file:
        return load_config_from_string(config_file.read())
