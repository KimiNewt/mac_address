import binascii
import re

import typing

_MAC_ADDRESS_REGEX_HYPHEN = re.compile("^([0-9A-Fa-f]{2}[-]){5}([0-9A-Fa-f]{2})$")
_MAC_ADDRESS_REGEX_COLON = re.compile("^([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})$")

_COLON_SEPARATOR = ":"
_HYPHEN_SEPARATOR = "-"


class MACAddress:
    """An object which represents a MAC Address and can display it several ways

    It can be initiated with a hex string (e.g. aa:bb:cc:dd:ee:ff or AA-BB-CC-DD-EE-FF), a bytes object
    (e.g. b'\xaa\xbb\xcc\xdd\xee\xff') or another MACAddress object.

    The address can then be displayed as a binary or string, and the conversion will be cached for future use)
    """

    def __init__(self, string_or_bytes_or_mac: typing.Union[bytes, str, "MACAddress"],
                 default_mac_separator=_COLON_SEPARATOR):
        self._default_mac_separator = default_mac_separator
        if isinstance(string_or_bytes_or_mac, (bytes, bytearray)):
            self._mac_bytes = string_or_bytes_or_mac
            self._mac_string = None
        elif isinstance(string_or_bytes_or_mac, MACAddress):
            self._mac_bytes = string_or_bytes_or_mac._mac_bytes
            self._mac_string = string_or_bytes_or_mac._mac_string
        else:
            self._mac_bytes = None
            self._mac_string = self._make_mac_string(string_or_bytes_or_mac.lower())

    @property
    def binary(self) -> bytes:
        if self._mac_bytes is None:
            self._mac_bytes = binascii.unhexlify(self._mac_string.replace(self._default_mac_separator, ""))
        return self._mac_bytes

    @property
    def string(self) -> str:
        if self._mac_string is None:
            no_separator_mac = binascii.hexlify(self._mac_bytes).decode("ascii")
            self._mac_string = self._default_mac_separator.join(
                a + b for a, b in zip(no_separator_mac[::2], no_separator_mac[1::2]))
        return self._mac_string
    hex = string

    def as_string(self, custom_separator=None) -> str:
        if custom_separator:
            return self.string.replace(self._default_mac_separator, custom_separator)
        return self.string

    def __bytes__(self):
        return self.binary

    def __str__(self):
        return self.string

    def __repr__(self):
        return "<MACAddress %s>" % self.string

    def _make_mac_string(self, mac_string):
        if _MAC_ADDRESS_REGEX_COLON.match(mac_string):
            if self._default_mac_separator == _HYPHEN_SEPARATOR:
                return mac_string.replace(_COLON_SEPARATOR, _HYPHEN_SEPARATOR)
        elif _MAC_ADDRESS_REGEX_HYPHEN.match(mac_string):
            if self._default_mac_separator == _COLON_SEPARATOR:
                return mac_string.replace(_HYPHEN_SEPARATOR, _COLON_SEPARATOR)
        else:
            raise ValueError("Badly formatted MAC string %s" % mac_string)

        # Is a valid MAC and no replacements were necessary
        return mac_string
