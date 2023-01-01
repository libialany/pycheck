from Pycheck import is_current,get_release_age,get_current_release,get_releases
print('is_current>\n',is_current('v22.03.2','openwrt/openwrt'))
print('get_release_age>\n',get_release_age('v21.02.3','openwrt/openwrt'))
print('get_current_release>\n',get_current_release('openwrt/openwrt'))
print('get_releases>\n',get_releases('openwrt/openwrt'))