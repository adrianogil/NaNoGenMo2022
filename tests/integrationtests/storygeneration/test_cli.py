from nanogenmo2022.storygeneration.cli import cli

import subprocess


def test_cli_output(capsys):
    args = []
    cli(args)
    captured = capsys.readouterr()
    result = captured.out
    assert "Start genering a new story!" in result


def test_cli_output_subprocess():
    result = subprocess.run(["generate"], capture_output=True)
    assert b"Start genering a new story!" in result.stdout
