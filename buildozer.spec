[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion/exclusion patterns
source.include_pattern = images/*,sounds/*

# (list) Source files to exclude (let it empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions in source files
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (list) Custom source folders for requirements
# Sets custom source for any requirements with "locally"-hosted source.
#requirements.source.src = ../kivy

# (list) PERMISSIONS
#android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.min_api = 21

# (str) Android NDK version to use
#android.ndk = 25b

# (int) Android SDK version to use
#android.sdk = 33

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.renpy.android.PythonActivity

# (list) List of Java .jar files to add to the libs/ toplevel folder
#android.add_jars = foo.bar.jar,bar.baz.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

name: Build APK

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y git zip unzip openjdk-17-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libstdc++6 patchelf libffi-dev libssl-dev
        pip install --upgrade pip buildozer cython==0.29.36 virtualenv

    - name: Build with Buildozer and Auto-accept Licenses
      run: |
        yes | buildozer android debug || buildozer android debug

    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: package
        path: bin/*.apk