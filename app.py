import argparse
from passman import cli, ui_qt

def main():
    parser = argparse.ArgumentParser(description="Password Manager Application")
    parser.add_argument(
        "-g", "--gui",
        action="store_true",
        help="Launch the application with the graphical interface (Qt)"
    )

    args = parser.parse_args()

    if args.gui:
        ui_qt.run_qt_app()
    else:
        cli.run_cli()

if __name__ == "__main__":
    main()
