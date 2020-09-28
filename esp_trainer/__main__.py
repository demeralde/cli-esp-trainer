import sys

from colorama import init as init_colorama

from esp_trainer.cli import CLI


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    init_colorama()
    cli = CLI()
    cli.run_trainer()


if __name__ == "__main__":
    sys.exit(main())
