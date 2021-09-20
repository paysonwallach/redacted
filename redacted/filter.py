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

import enum
import configparser

from redacted.secret import Secret


class FilterAction(enum.Enum):
    CLEAN = 0
    SMUDGE = 1


class Filter(object):
    @classmethod
    def from_config(
        cls, name: str, action: FilterAction, config: configparser.ConfigParser
    ):
        try:
            config = dict(config.items(name))
        except configparser.NoSectionError:
            config = {}
        return cls(name, action, config)

    def __init__(self, name: str, action: FilterAction, secrets: dict = {}):
        self.name = name
        self.action = action
        self.secrets = secrets

        self.parse_secrets()

    def parse_secrets(self):
        for key, secret in self.secrets.items():
            self.secrets[key] = Secret(key, secret)

    def sub(self, line: str):
        if self.action is FilterAction.CLEAN:
            for key in self.secrets:
                line = line.replace(key, self.secrets[key].secret)
        elif self.action is FilterAction.SMUDGE:
            for secret in self.secrets.values():
                line = line.replace(secret.secret, secret.key)
        else:
            assert False

        return line
