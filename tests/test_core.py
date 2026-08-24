import pytest
from dredge.cli import main

def test_imports():
    import dredge
    assert dredge.__version__ == "1.0.2"

def test_cli_execution(capsys):
    import sys
    sys.argv = ["aquamarine-dredge", "--demo"]
    main()
    captured = capsys.readouterr()
    assert "Demo Mode Loaded" in captured.out
