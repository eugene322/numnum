from common.apps import CommonConfig


def test_apps():
    assert 'common' == CommonConfig.name
