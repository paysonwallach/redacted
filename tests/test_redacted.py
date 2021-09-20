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

import pytest

from click.testing import CliRunner

from redacted.cli import main
from redacted.config import REDACTED_CONFIG_FILE

REDACTED_CONF_CONTENTS = """
[test.txt]
FOO: bar
baz: bat
"""


@pytest.fixture
def repo(tmp_path):
    marker = tmp_path.joinpath(".git")
    marker.mkdir()

    config_file = tmp_path.joinpath(REDACTED_CONFIG_FILE)
    config_file.write_text(REDACTED_CONF_CONTENTS)


def test_no_match(repo):
    with open(REDACTED_CONFIG_FILE, "r") as f:
        print(f.readline())
    runner = CliRunner()
    result = runner.invoke(main, ["smudge", "test.txt"], input='"foo": "bar"')
    assert result.output == '"foo": "FOO"'
