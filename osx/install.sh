#!/usr/bin/env bash

set -e
DIR="$(dirname "$0")"

install_fonts () {
  find $DIR/fonts -name *.otf -exec cp -n {} $HOME/Library/Fonts/ \;
}

if test $(uname) = 'Darwin'
then
  install_fonts
fi
