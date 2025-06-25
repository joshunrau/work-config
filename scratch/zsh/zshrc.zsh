#!/usr/bin/env zsh

fpath=($ZSH_ROOT/functions $ZSH_ROOT/plugins $fpath)
autoload -Uz $fpath[1]/*(-.:t)
zmodload zsh/complist
zmodload zsh/zutil

# NAVIGATION
setopt AUTO_PUSHD           # Push the old directory onto the stack on cd.
setopt PUSHD_IGNORE_DUPS    # Do not store duplicates in the stack.
setopt PUSHD_SILENT         # Do not print the directory stack after pushd or popd.
setopt EXTENDED_GLOB        # Use extended globbing syntax.

# HISTORY
setopt EXTENDED_HISTORY          # Write the history file in the ':start:elapsed;command' format.
setopt SHARE_HISTORY             # Share history between all sessions.
setopt HIST_EXPIRE_DUPS_FIRST    # Expire a duplicate event first when trimming history.
setopt HIST_IGNORE_DUPS          # Do not record an event that was just recorded again.
setopt HIST_IGNORE_ALL_DUPS      # Delete an old recorded event if a new event is a duplicate.
setopt HIST_FIND_NO_DUPS         # Do not display a previously found event.
setopt HIST_IGNORE_SPACE         # Do not record an event starting with a space.
setopt HIST_SAVE_NO_DUPS         # Do not write a duplicate event to the history file.
setopt HIST_VERIFY               # Do not execute immediately upon history expansion.

# COMPLETION
bindkey '^[[A' history-search-backward
bindkey '^[[B' history-search-forward

# SOURCE THEME
if [[ $ZSH_VERSION > 5.1 ]]; then
  if [[ -r "${XDG_CACHE_HOME}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
    source "${XDG_CACHE_HOME}/p10k-instant-prompt-${(%):-%n}.zsh"
  fi
  source $ZSH_ROOT/themes/powerlevel10k/powerlevel10k.zsh-theme
  source $ZSH_ROOT/p10k.zsh
fi

# ALIASES
source $ZSH_ROOT/aliases.zsh

# # SOURCE 3RD PARTY PLUGINS
source $ZSH_ROOT/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source $ZSH_ROOT/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source $ZSH_ROOT/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh
source $ZSH_ROOT/plugins/zsh-completions/zsh-completions.plugin.zsh

# LOAD COMPLETIONS
autoload -U compinit
compinit


export PATH="$SCRATCH_BIN:$PATH"

if [[ -d $PYENV_ROOT/bin ]]; then
  export PATH="$PYENV_ROOT/bin:$PATH"
  eval "$(pyenv init - zsh)"
fi

if [ -d "$FNM_PATH" ]; then
  eval "`fnm env`"
fi

if [[ -d "$CARGO_HOME" ]]; then
  source "$CARGO_HOME/env"
fi
