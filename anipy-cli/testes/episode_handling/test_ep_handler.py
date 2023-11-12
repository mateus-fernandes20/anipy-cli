from anipy_cli import epHandler, Entry
from urllib.parse import urlparse


def test_gen_link_regular():
    show_entry = epHandler(
        Entry(category_url="https://gogoanime.tel/category/hyouka", ep=1)
    ).gen_eplink()

    assert (
        urlparse(show_entry.ep_url).path == "//hyouka-episode-1"
    ), "Link errado"


def test_gen_latest():
    last_ep = epHandler(
        Entry(category_url="https://gogoanime.tel/category/hyouka")
    ).get_latest()

    assert last_ep == 22, "Nao eh o ultimo ep"


def test_gen_first_ep():
    first_ep = epHandler(
        Entry(category_url="https://gogoanime.tel/category/hyouka")
    ).get_first()

    assert int(first_ep) == 1, "Nao eh o primeiro ep"


def test_next_ep():
    show_entry = epHandler(
        Entry(category_url="https://gogoanime.tel/category/hyouka", ep=1)
    ).next_ep()

    assert show_entry.ep == 2, "Episodio errado"
    assert "2" in show_entry.ep_url, "Url errada"


def test_prev_ep():
    show_entry = epHandler(
        Entry(category_url="https://gogoanime.tel/category/hyouka", ep=3)
    ).prev_ep()

    assert show_entry.ep == 2, "Episodio errado"
    assert "2" in show_entry.ep_url, "Url errada"
