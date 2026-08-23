[app]

title = AI Assistant
package.name = aiassistant
package.domain = org.assistant
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*,images/*.png
source.exclude_exts = spec
source.exclude_dirs = tests, bin, venv
source.exclude_patterns = license,images/*.jpg
version = 0.1
requirements = python3,kivy
android.permissions = INTERNET
orientation = portrait
android.archs = arm64-v8a, armeabi-v7a

android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.0

p4a.bootstrap = sdl2
android.format = apk

[buildozer]
log_level = 2
warn_root = 1
bin_dir = ./bin
