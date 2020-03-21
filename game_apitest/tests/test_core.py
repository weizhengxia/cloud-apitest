# -*- coding: utf-8 -*-

def test_version():
    from game_apitest import __version__
    assert isinstance(__version__,str)