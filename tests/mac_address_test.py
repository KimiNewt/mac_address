import mac_address
import pytest


@pytest.mark.parametrize(["input_string"], [
    ("aa:bb:cc:dd:ee:ff",),
    ("aa-bb-cc-dd-ee-ff",),
    ("AA-BB-CC-DD-EE-FF",),
    ("AA:BB:CC:DD:EE:FF",),
])
def test_mac_address_parses_different_strings(input_string):
    assert mac_address.MACAddress(input_string).binary == b"\xaa\xbb\xcc\xdd\xee\xff"


def test_mac_address_creation_fails_on_bad_string():
    with pytest.raises(ValueError):
        mac_address.MACAddress("foo")


def test_string_created_from_binary():
    assert mac_address.MACAddress(b"\xaa\xbb\xcc\xdd\xee\xff").string == "aa:bb:cc:dd:ee:ff"


def test_string_with_hyphen_created_from_binary():
    assert mac_address.MACAddress(b"\xaa\xbb\xcc\xdd\xee\xff",
                                  default_mac_separator="-").string == "aa-bb-cc-dd-ee-ff"
