#!/unr/bin/env zsh

# BASE
export SCRATCH_ROOT="/scratch/unrjos"
export SCRATCH_BIN="$SCRATCH_ROOT/bin"
export ZSH_ROOT="$SCRATCH_ROOT/zsh"
export EDITOR=nvim

# XDG
export XDG_CONFIG_HOME="$SCRATCH_ROOT/etc"
export XDG_CACHE_HOME="$SCRATCH_ROOT/cache"
export XDG_DATA_HOME="$SCRATCH_ROOT/share"
export XDG_STATE_HOME="$SCRATCH_ROOT/state"

# PYENV
export PYENV_ROOT="$SCRATCH_ROOT/opt/pyenv"

# FNM
export FNM_PATH=$SCRATCH_BIN

# RUST
export CARGO_HOME="$SCRATCH_ROOT/opt/cargo"
export RUSTUP_HOME="$SCRATCH_ROOT/opt/rustup"

# ZSH
export HISTFILE="$ZSH_ROOT/.zhistory"
export HISTSIZE=20000
export SAVEHIST=10000
