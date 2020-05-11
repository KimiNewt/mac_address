import mac_address
import pytest


@pytest.mark.parametrize(["input_string"], [
    ("aa:bb:cc:dd:ee:ff",),
    ("aa-bb-cc-dd-ee-ff",),
])
def test_mac_address_parses_different_strings(input_string):
    assert mac_address.MACAddress(input_string).binary == b"\xaa\xbb\xcc\xdd\xee\xff"
