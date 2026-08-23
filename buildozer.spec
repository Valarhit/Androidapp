[app]

# (str) Title of your application
title = AI Assistant

# (str) Package name
package.name = aiassistant

# (str) Package domain (needed for android packaging)
package.domain = org.assistant

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
# Add your required python libraries here (e.g. requests, google-generativeai)
requirements = python3,kivy

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../../kivy

# (list) Permissions
android.permissions = INTERNET

# (list) Features
#android.features = android.hardware.usb.host

# (str) Supported orientations (landscape, portrait, all)
orientation = portrait

# (list) List of service to declare
#services = NAME:gsd.py,NAME2:other.py

#
# OSX Specific
#

#
# PDF icon (not yet supported)
#

#
# Android specific
#

# (list) Warn about extra permissions
#android.add_permissions = 

# (list) Target architectures, supported: arm64-v8a, armeabi-v7a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (int) The Android API to target
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use (fixed to a stable version to prevent build crashes)
android.ndk = 25b

# (bool) Use --private data storage (True) or --public storage (False)
#android.private_storage = True

# (str) Android SDK version to use
#android.sdk = 20

# (str) ANT version to use
#android.ant_version = 1.9.4

# (str) Fulling package name for python-for-android
#android.p4a_package_name = org.kivy.pythonforandroid

# (bool) If True, then skip trying to update the Android SDK
#android.skip_sdk_update = False

# (str) Bootstrap to use for android builds
android.bootstrap = sdl2

# (str) XML files to add to AndroidManifest.xml
#android.manifest.xml = 

# (str) Manifest metadata to add
#android.manifest.metadata = 

# (str) Extra xml to add to build.gradle
#android.gradle_dependencies = 

# (bool) Use multidexed applications
#android.multidex = False

# (str) The format used to package the app for release/debug (aab or apk)
android.format = apk


[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1

# (str) Path to build artifact, local or absolute
bin_dir = ./bin

# (int) Number of processes to use for parallel compilation
# build_threads = 4

# (bool) Skip pre-build checks (useful for specific environments like CI)
# skip_prebuild_checks = False
