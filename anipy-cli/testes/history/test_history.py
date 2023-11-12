import pytest
from ..util import config_clearer
from anipy_cli import Entry, history, config
from hashlib import md5


@pytest.fixture
def show_entry():
    config_clearer.clear_and_backup()

    config.Config().history_file_path.unlink(missing_ok=True)

    hyouka_entry = Entry(
        show_name="Hyouka",
        category_url="https://gogoanime.tel/category/hyouka",
        ep_url="https://gogoanime.tel/hyouka-episode-1",
        ep=1,
    )

    yield hyouka_entry

    config_clearer.revert()


def test_hyouka(show_entry):
    MD5 = "a789a8734272e5d3025696468822bd19"

    history(show_entry).write_hist()

    assert _check_md5(MD5)


def test_prepend(show_entry):
    MD5 = "fe772be16ced55a1618ecd16743b7f5b"

    history(show_entry).write_hist()

    another_entry = Entry(
        show_name="Shoujo Shuumatsu Ryokou",
        category_url="https://gogoanime.tel/category/shoujo-shuumatsu-ryokou",
        ep_url="https://gogoanime.tel/shoujo-shuumatsu-ryokou-episode-1",
        ep=1,
    )

    history(another_entry).write_hist()

    assert _check_md5(MD5)
