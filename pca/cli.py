"""Console script for datapca."""

import click


@click.command()
def main():
    """Run the main entrypoint."""
    click.echo("datapca")
    click.echo("=" * len("datapca"))
    click.echo("Data platform utility with Python Clean Architcture")


if __name__ == "__main__":
    main()  # pragma: no cover
