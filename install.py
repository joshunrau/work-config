import os
import subprocess
import sys

BASE_DIR = os.path.dirname(__file__)
HOME_DIR = os.path.expanduser("~")
SCRATCH_DIR = "/scratch/unrjos"

GIT_REPOS = {
    f"{SCRATCH_DIR}/zsh/plugins/zsh-autosuggestions": "https://github.com/zsh-users/zsh-autosuggestions",
    f"{SCRATCH_DIR}/zsh/plugins/zsh-syntax-highlighting": 'https://github.com/zsh-users/zsh-syntax-highlighting.git',
    f"{SCRATCH_DIR}/zsh/plugins/zsh-history-substring-search":'https://github.com/zsh-users/zsh-history-substring-search.git',
    f"{SCRATCH_DIR}/zsh/plugins/zsh-completions": 'https://github.com/zsh-users/zsh-completions.git',
    f"{SCRATCH_DIR}/zsh/themes/powerlevel10k": "https://github.com/romkatv/powerlevel10k.git"
}


def run_command(command: str) -> None:
    result = subprocess.run(
        command, shell=True, capture_output=True, text=True, check=True
    )
    result.check_returncode()


def warn(message: str) -> None:
    print(f"\033[31mWARNING: {message}\033[0m", file=sys.stderr)


def install_symlinks(source_dir: str, target_dir: str) -> None:
    for source_path, _, source_files in os.walk(source_dir):
        target_path = target_dir + source_path.removeprefix(source_dir)
        if not os.path.exists(target_path):
            os.mkdir(target_path)
        elif os.path.isfile(target_path):
            raise NotADirectoryError(f"File is not a directory: {target_path}")
        for filename in source_files:
            source_file = f"{source_path}/{filename}"
            target_file = f"{target_path}/{filename}"
            if os.path.islink(target_file):
                resolved_path = os.readlink(target_file)
                if resolved_path == source_file:
                    print(f'Already Installed: {target_file}')
                else:
                    warn(
                        f"Unexpected Target for Symlink '{target_file}': {resolved_path}"
                    )
                continue
            elif os.path.exists(target_file):
                warn(f"Not a Symlink: {target_file}")
                continue
            os.symlink(source_file, target_file)
            print(f"Created Symlink: {target_file}")


def install_git_repos() -> None:
    for filepath, url in GIT_REPOS.items():
        if os.path.exists(filepath):
            print(f'Already Installed: {filepath}')
            continue
        run_command(f"git clone --depth 1 {url} {filepath}")
        assert os.path.isdir(filepath)
        print(f"Cloned Repository: {filepath}")
        


def main() -> None:
    install_symlinks(f"{BASE_DIR}/scratch", SCRATCH_DIR)
    install_symlinks(f"{BASE_DIR}/home", HOME_DIR)
    install_git_repos()


if __name__ == "__main__":
    main()
