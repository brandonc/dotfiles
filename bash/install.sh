#!/usr/bin/env bash

if grep -q "$HOMEBREW_PREFIX/bin/bash" "/etc/shells"; then
  echo 'Brew bash already installed'
else
  # Add the new shell to the list of allowed shells
  sudo bash -c "echo $HOMEBREW_PREFIX/bin/bash >> /etc/shells"
  # Change to the new shell
  chsh -s $HOMEBREW_PREFIX/bin/bash
fi
