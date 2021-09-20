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

import unittest

from redacted.config import load_config_from_string
from redacted.filter import FilterAction, Filter

CONFIG = """
[name]
FOO: bar
"""


class TestSmudgeFilter(unittest.TestCase):
    def setUp(self):
        self.config = load_config_from_string(CONFIG)
        self.filters = []
        self.filters.append(
            Filter.from_config("name", FilterAction.SMUDGE, self.config)
        )

    def test_nosecret_sub(self):
        line = '"baz": "bat"'
        self.assertEqual(self.filters[0].sub(line), line)

    def test_single_sub(self):
        self.assertEqual(self.filters[0].sub('"baz": "bar"'), '"baz": "FOO"')


if __name__ == "__main__":
    unittest.main()
