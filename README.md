# `tap-jaffle-shop`

A Singer tap that generates Jaffle Shop sample data.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## About the Jaffle Shop Generator

The [Jaffle Shop Generator](https://github.com/dbt-labs/jaffle-shop-generator), aka "`jafgen`" is a python-based data generated created by [dbt Labs](https://www.getdbt.com).

This Singer Tap wraps the `jafgen` tool so that it generate data streams compliant with the [Singer Spec](https://hub.meltano.com/singer/spec/) for data replication.

## Known limitations

At the current time, there is no ability to use this tap in incremental replication modes - and nor is it possible to rerun the data sync and still ensure the target will have maintained referential integrity. Rather, each new sync invocation will generate an entirely new database based on a new (randomly generated) Jaffle Shop company.

Targets that support the `ACTIVATE_VERSION` message type will automatically delete the old records. If your target does not support `ACTIVATE_VERSION` and do want to regenerate the data, please first drop or truncate your tables before reloading. Alternatively, you can use the `stream_name_prefix` config option to change your target table names.

> **Info**
>
> Please see [this link](https://github.com/meltanolabs/tap-jaffle-shop/issues/1) for more information, and let us know if you would like to help contribute further improvements in this area.

## Installation

Install from GitHub `main` branch:

```bash
pipx install git+https://github.com/MeltanoLabs/tap-jaffle-shop.git@main
```

Install from a recent GitHub release:

- Important: check [here](https://github.com/MeltanoLabs/tap-jaffle-shop/releases) for the latest version number.

```bash
pipx install git+https://github.com/MeltanoLabs/tap-jaffle-shop.git@v0.1.0
```

Install from PyPi:

[Coming soon]

<!--
```bash
pipx install tap-jaffle-shop
```
-->

## Configuration

### Accepted Config Options

<!--
Developer TODO: Provide a list of config options accepted by the tap.

This section can be created by copy-pasting the CLI output from:

```
tap-jaffle-shop --about --format=markdown
```
-->

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-jaffle-shop --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

<!--
Developer TODO: If your tap requires special access on the source system, or any special authentication requirements, provide those here.
-->

## Usage

You can easily run `tap-jaffle-shop` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-jaffle-shop --version
tap-jaffle-shop --help
tap-jaffle-shop --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Manual Testing

```console
# Install everything if working from a fresh clone
poetry install

# Stream output to a file
poetry run tap-jaffle-shop > outfile-01.singer.jsonl

# Generate a catalog.json file
poetry run tap-jaffle-shop --discover > catalog.json

# Stream to JSONL files
pipx install target-jsonl
echo '{"destination_path": "./output/"}' > target-jsonl.config.json
poetry run tap-jaffle-shop | target-jsonl --config=target-jsonl.config.json

# Stream to DuckDB
pipx install target-duckdb
echo '{"filepath": "output/out.duckdb", "default_target_schema": "raw"}' > target-duckdb.config.json
poetry run tap-jaffle-shop | target-duckdb --config=target-duckdb.config.json
```

### Create and Run Tests

Create tests within the `tap_jaffle_shop/tests` subfolder and
then run:

```bash
poetry run pytest
```

You can also test the `tap-jaffle-shop` CLI interface directly using `poetry run`:

```bash
poetry run tap-jaffle-shop --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

<!--
Developer TODO:
Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any "TODO" items listed in
the file.
-->

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-jaffle-shop
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-jaffle-shop --version
# OR run a test `elt` pipeline:
meltano elt tap-jaffle-shop target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
