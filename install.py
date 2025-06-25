import os
import sys


def warn(message: str) -> None:
    print(f"\033[31mWARNING: {message}\033[0m", file=sys.stderr)


def install(source_dir: str, target_dir: str) -> None:
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
                if resolved_path != source_file:
                    warn(
                        f"Unexpected Target for Symlink '{target_file}': {resolved_path}"
                    )
                continue
            elif os.path.exists(target_file):
                warn(f"Not a Symlink: {target_file}")
            else:
                os.symlink(source_file, target_file)
                print(f"Created Symlink: {target_file}")


def main() -> None:
    base_dir = os.path.dirname(__file__)
    home_dir = os.path.expanduser("~")
    install(f"{base_dir}/scratch", "/scratch/unrjos")
    install(f"{base_dir}/home", home_dir)


if __name__ == "__main__":
    main()
