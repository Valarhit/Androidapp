[app]

# (str) Title of your application
title = AI Assistant

# (str) Package name
package.name = aiassistant

# (str) Package domain (needed for android packaging)
package.domain = org.assistant

# (str) Source directory where the main.py file is located
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion patterns relative to the source dir
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let it empty to exclude none)
source.exclude_exts = spec

# (list) List of directory to exclude (let it empty to exclude none)
source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
source.exclude_patterns = license,images/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (list) Permissions
android.permissions = INTERNET

# (str) Supported orientations (landscape, portrait, all)
orientation = portrait

# (list) Target architectures, supported: arm64-v8a, armeabi-v7a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (int) The Android API to target
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK version to use
android.sdk = 33

# (str) Android build tools version to use
android.build_tools_version = 33.0.0

# (str) Bootstrap to use for android builds
p4a.bootstrap = sdl2

# (str) The format used to package the app for release/debug (aab or apk)
android.format = apk


[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1

# (str) Path to build artifact, local or absolute
bin_dir = ./bin
