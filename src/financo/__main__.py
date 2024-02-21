"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Financo."""


if __name__ == "__main__":
    main(prog_name="financo")  # pragma: no cover
