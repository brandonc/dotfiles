#!/usr/bin/env bash

set -e
DIR="$(dirname "$0")"

install_fonts () {
  if test "$(uname)" = 'Darwin'
  then
    find "$DIR/fonts" -name "*.otf" -exec cp -n {} "$HOME/Library/Fonts/" \;
    find "$DIR/fonts" -name "*.ttf" -exec cp -n {} "$HOME/Library/Fonts/" \;
  fi

  if test "$(uname)" = 'Linux'
  then
    sudo cp -r "$DIR/fonts/*" "/usr/local/share/fonts"
  fi
}

install_fonts
