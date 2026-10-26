[app]
title = Weather App
package.name = weatherapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,kivymd,requests,urllib3,chardet,idna,certifi

orientation = portrait
osx.kivy_version = 2.3.0
fullscreen = 0

android.api = 34
android.minapi = 26
android.ndk_api = 26
android.private_storage = True
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
