# content of test_pycheck.py
from Pycheck import is_current,get_release_age, get_releases
class TestClass:
    def test_is_current(self): 
        assert is_current('v22.03.2','openwrt/openwrt') == True
    def test_get_release_age(self):
        assert isinstance(get_release_age('v21.02.3','openwrt/openwrt'), int)
    def test_get_releases(self):
        assert isinstance(get_releases('openwrt/openwrt'), list)

