import pytest
from bgb import get_bgb_price
import io
import sys

def test_get_bgb_price_output(capsys):
    """Tests that get_bgb_price prints output containing the expected string."""
    get_bgb_price()
    captured = capsys.readouterr()
    assert "The current price of BGB/USDT is:" in captured.out
