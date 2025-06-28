import pytest
from open_interest_fetcher import get_open_interest

def test_get_open_interest_usdt_futures_live():
    """
    Tests get_open_interest with "USDT-FUTURES" using live data.
    Checks that the function returns a non-empty dictionary with string keys and values.
    """
    product_type = "USDT-FUTURES"
    print(f"Testing get_open_interest with product type: {product_type} (Live Data) - expecting dict")

    result = get_open_interest(product_type)

    assert isinstance(result, dict), "Result should be a dictionary."
    assert len(result) > 0, "Result dictionary should not be empty for USDT-FUTURES."

    # Check a few items to ensure structure
    for symbol, holding_amount in result.items():
        assert isinstance(symbol, str), "Symbol should be a string."
        assert len(symbol) > 0, "Symbol string should not be empty."
        assert isinstance(holding_amount, str), f"Holding amount for {symbol} should be a string."
        # Try to convert holding_amount to float to ensure it's a numerical string
        try:
            float(holding_amount)
        except ValueError:
            pytest.fail(f"Holding amount '{holding_amount}' for symbol '{symbol}' is not a valid number string.")
        break # Only need to check one item's structure for this test

    print(f"Received {len(result)} symbols for {product_type}.")

def test_get_open_interest_coin_futures_live():
    """
    Tests get_open_interest with "COIN-FUTURES" using live data.
    Checks that the function returns a non-empty dictionary with string keys and values.
    """
    product_type = "COIN-FUTURES"
    print(f"Testing get_open_interest with product type: {product_type} (Live Data) - expecting dict")

    result = get_open_interest(product_type)

    assert isinstance(result, dict), "Result should be a dictionary."
    assert len(result) > 0, "Result dictionary should not be empty for COIN-FUTURES."

    for symbol, holding_amount in result.items():
        assert isinstance(symbol, str), "Symbol should be a string."
        assert isinstance(holding_amount, str), f"Holding amount for {symbol} should be a string."
        try:
            float(holding_amount)
        except ValueError:
            pytest.fail(f"Holding amount '{holding_amount}' for symbol '{symbol}' is not a valid number string.")
        break
    print(f"Received {len(result)} symbols for {product_type}.")

def test_get_open_interest_invalid_product_type_live(capsys):
    """
    Tests get_open_interest with an invalid product type.
    Checks that it returns an empty dictionary and prints an HTTP error to console.
    """
    product_type = "INVALID-PRODUCT-TYPE"
    print(f"Testing get_open_interest with product type: {product_type} (Live Data) - expecting empty dict and error print")

    result = get_open_interest(product_type)

    assert isinstance(result, dict), "Result should be a dictionary."
    assert len(result) == 0, "Result dictionary should be empty for an invalid product type."

    captured = capsys.readouterr()
    assert f"HTTP error fetching open interest for {product_type}" in captured.out
    assert "400 Client Error: Bad Request" in captured.out
    print(f"Correctly received empty dict for {product_type}. Error printed: {captured.out.strip()}")

def test_get_open_interest_empty_product_type_live(capsys):
    """
    Tests get_open_interest with an empty product type string.
    Checks that it returns an empty dictionary and prints an HTTP error to console.
    """
    product_type = ""
    print(f"Testing get_open_interest with product type: '{product_type}' (Live Data) - expecting empty dict and error print")

    result = get_open_interest(product_type)

    assert isinstance(result, dict), "Result should be a dictionary."
    assert len(result) == 0, "Result dictionary should be empty for an empty product type."

    captured = capsys.readouterr()
    assert f"HTTP error fetching open interest for {product_type}" in captured.out
    assert "400 Client Error: Bad Request" in captured.out
    print(f"Correctly received empty dict for empty product type. Error printed: {captured.out.strip()}")

# Note: As per AGENTS.MD: "when doing test use live data for better results do not mock data"
# Therefore, no mocking is used here.
# The `capsys` fixture is still used for error cases to check console output,
# as the function is designed to print errors while returning an empty dict.
