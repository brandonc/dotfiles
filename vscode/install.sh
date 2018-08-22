set -e
DIR="$(dirname "$0")"

install_settings () {
  if test "$(uname)" = "Darwin"
  then
    mkdir -p "$HOME/Library/Application Support/Code/User"
    cp $DIR/settings.json "$HOME/Library/Application Support/Code/User/"
  else
    mkdir -p "$HOME/.config/Code/User"
    cp $DIR/settings.json "$HOME/.config/Code/User/settings.json"
  fi
}

install_settings