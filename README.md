<div align="center">
  <h1>Redacted</h1>
  <p>Keep your config secrets in place and out of Git.</p>
  <a href="https://github.com/paysonwallach/redacted/releases/latest">
    <img alt="Version 0.1.0" src="https://img.shields.io/badge/version-0.1.0-red.svg?cacheSeconds=2592000&style=flat-square" />
  </a>
  <a href="https://github.com/paysonwallach/redacted/blob/master/LICENSE" target="\_blank">
    <img alt="Licensed under the GNU General Public License v3.0" src="https://img.shields.io/github/license/paysonwallach/redacted?style=flat-square" />
  <a href=https://buymeacoffee.com/paysonwallach>
    <img src=https://img.shields.io/badge/donate-Buy%20me%20a%20coffe-yellow?style=flat-square>
  </a>
  <br>
  <br>
</div>

## Installation

Clone this repository or download the [latest release](https://github.com/paysonwallach/redacted/releases/latest).

```shell
git clone https://github.com/paysonwallach/redacted
```

Install the dependencies. Poetry will automatically create and activate a virtual environment if it does not detect an active one:

```shell
poetry install
```

Build the package:

```shell
poetry build
```

Finally, install the resulting wheel, located under `dist/`, using `pip`:

```shell
pip install --user dist/redacted-0.1.0-py3-none-any.whl
```

## Usage

Create a `.redacted.conf` file at the root of your repository. For each file to redact, create a section with the relative path to the file as the name, and add a key-value pair to the section for each string to be redacted.

```toml
[path/to/file.txt]
KEY: secret
```

Configure the filter in `git`:

```shell
git config filter.redacted.clean "git-redact clean %f"
git config filter.redacted.smudge "git-redact smudge %f"
git config filter.redacted.required true
```

Enable the filter in `.gitattributes`:

```
* filter=redacted
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change. By participating in this project, you agree to abide by the terms of the [Code of Conduct](https://github.com/paysonwallach/redacted/blob/master/CODE_OF_CONDUCT.md).

## License

[Redacted](https://github.com/paysonwallach/redacted) is licensed under the [GNU General Public License v3.0](https://github.com/paysonwallach/redacted/blob/master/LICENSE).
