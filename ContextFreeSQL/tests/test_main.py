import pytest
from myproject.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from MyProject!" in captured.out