if grep -q "/usr/local/bin/bash" "/etc/shells"; then
  echo 'Brew bash already installed'
else
  # Add the new shell to the list of allowed shells
  sudo bash -c 'echo /usr/local/bin/bash >> /etc/shells'
  # Change to the new shell
  chsh -s /usr/local/bin/bash
fi
