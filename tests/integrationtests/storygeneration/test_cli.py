from nanogenmo2022.storygeneration.cli import cli


def test_cli(capsys):
    args = []
    cli(args)
    captured = capsys.readouterr()
    result = captured.out
    assert "Start genering a new story!" in result
