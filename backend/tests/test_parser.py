import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from parser import audit_page


def test_invalid_url():
    with pytest.raises(ValueError):
        audit_page("abc")


def test_non_html():
    with pytest.raises(ValueError):
        audit_page("https://httpbin.org/image/png")


def test_example_com():
    result = audit_page("https://example.com")

    assert result["status"] == 200
    assert result["title"] == "Example Domain"
    assert result["h1_count"] >= 1
    assert result["word_count"] > 0