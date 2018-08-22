## brandonc's dotfiles
Modifies an OSX/Linux system in the way that I like. Use at your own risk.

---

#### New Machine

```
./bootstrap
```

- installs homebrew
- bundles Brewfile
- sets OSX defaults
- finds and runs topic `bootstrap.sh` files
- runs install

#### Update $HOME

```
./install
```

- symlinks files/folders named `.symlink` into `$HOME`
- finds and runs topic `install.sh` files
