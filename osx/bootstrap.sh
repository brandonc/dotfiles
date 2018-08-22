#!/usr/bin/env bash

set -e
DIR="$(dirname "$0")"

set_defaults () {
  # Ask for password up front
  sudo -v

  # Save to disk (not to iCloud) by default
  defaults write NSGlobalDomain NSDocumentSaveNewDocumentsToCloud -bool false

  # Automatically quit printer app once the print jobs complete
  defaults write com.apple.print.PrintingPrefs "Quit When Finished" -bool true

  # Disable press-and-hold for keys in favor of key repeat
  defaults write NSGlobalDomain ApplePressAndHoldEnabled -bool false

  # Set a blazingly fast keyboard repeat rate
  defaults write NSGlobalDomain KeyRepeat -int 1
  defaults write NSGlobalDomain InitialKeyRepeat -int 10

  # Finder: Always open everything in list view
  defaults write com.apple.Finder FXPreferredViewStyle Nlsv

  # Finder: show hidden files by default
  defaults write com.apple.finder AppleShowAllFiles -bool true

  # Finder: show all filename extensions
  defaults write NSGlobalDomain AppleShowAllExtensions -bool true

  # Disable the warning when changing a file extension
  defaults write com.apple.finder FXEnableExtensionChangeWarning -bool false

  # Avoid creating .DS_Store files on network or USB volumes
  defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true
  defaults write com.apple.desktopservices DSDontWriteUSBStores -bool true

  # Disable the warning before emptying the Trash
  defaults write com.apple.finder WarnOnEmptyTrash -bool false

  # Show the ~/Library folder
  chflags nohidden ~/Library

  # Show the /Volumes folder
  sudo chflags nohidden /Volumes

  # Hot corners
  # Possible values:
  #  0: no-op
  #  2: Mission Control
  #  3: Show application windows
  #  4: Desktop
  #  5: Start screen saver
  #  6: Disable screen saver
  #  7: Dashboard
  # 10: Put display to sleep
  # 11: Launchpad
  # 12: Notification Center
  # Top left screen corner → Mission Control
  defaults write com.apple.dock wvous-tl-corner -int 2
  defaults write com.apple.dock wvous-tl-modifier -int 0
  # Top right screen corner → Desktop
  defaults write com.apple.dock wvous-tr-corner -int 4
  defaults write com.apple.dock wvous-tr-modifier -int 0
  # Bottom right screen corner → Display Sleep
  defaults write com.apple.dock wvous-br-corner -int 10
  defaults write com.apple.dock wvous-br-modifier -int 0

  # Only use UTF-8 in Terminal.app
  defaults write com.apple.terminal StringEncodings -array 4

  hostname=$(scutil --get ComputerName)
  read -r -p "Name the computer [$hostname]: " newhostname </dev/tty

  if [ -z "$newhostname"]
  then
    newhostname=$hostname
  fi

  sudo scutil --set ComputerName "$newhostname"
  sudo scutil --set HostName "$newhostname"
  sudo scutil --set LocalHostName "$newhostname"
  sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string "$newhostname"
}

if test "$(uname)" = "Darwin"
then
  set_defaults

  # setup terminal
  # Use a modified version of the Pro theme by default in Terminal.app
  osascript <<EOD
  tell application "Terminal"
    local allOpenedWindows
    local initialOpenedWindows
    local windowID
    set themeName to "dotfiles"
    (* Store the IDs of all the open terminal windows. *)
    set initialOpenedWindows to id of every window
    (* Open the custom theme so that it gets added to the list
      of available terminal themes (note: this will open two
      additional terminal windows). *)
    do shell script "open '${DIR}/" & themeName & ".terminal'"
    (* Wait a little bit to ensure that the custom theme is added. *)
    delay 1
    (* Set the custom theme as the default terminal theme. *)
    set default settings to settings set themeName
    (* Get the IDs of all the currently opened terminal windows. *)
    set allOpenedWindows to id of every window
    repeat with windowID in allOpenedWindows
      (* Close the additional windows that were opened in order
        to add the custom theme to the list of terminal themes. *)
      if initialOpenedWindows does not contain windowID then
        close (every window whose id is windowID)
      (* Change the theme for the initial opened terminal windows
        to remove the need to close them in order for the custom
        theme to be applied. *)
      end if
    end repeat
  end tell
EOD
fi
