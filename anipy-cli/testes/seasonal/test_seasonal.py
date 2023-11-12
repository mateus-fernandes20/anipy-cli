import pytest
from hashlib import md5
from ..util import config_clearer
from anipy_cli import Seasonal, config


@pytest.fixture
def test_del_hyouka(show_details):
    MD5 = "99914b932bd37a50b983c5e7c90ae93b"

    Seasonal().add_show(*show_details)
    Seasonal().del_show(show_details[0])

    assert _check_md5(MD5), "MD5 mismatch"
