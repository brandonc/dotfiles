#!/bin/bash

if [ ! -f "$HOME/.secrets" ]; then
  echo "# place any environment secrets here" > "$HOME/.secrets"
fi
