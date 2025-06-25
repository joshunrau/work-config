import os
import sys

def warn(message: str) -> None:
    print(f"\033[31mWARNING: {message}\033[0m", file=sys.stderr)
    
def main() -> None:
    source_dir = os.path.dirname(__file__)
    target_dir = "/scratch/unrjos"

    base_dirs = ["etc"]

    for base_dir in base_dirs:
        for source_path, _, source_files in os.walk(f"{source_dir}/{base_dir}"):
            target_path = target_dir + source_path.removeprefix(source_dir)
            if not os.path.exists(target_path):
                os.mkdir(target_path)
            elif os.path.isfile(target_path):
                raise NotADirectoryError(f"File is not a directory: {target_path}")
            for filename in source_files:
                source_file = f"{source_path}/{filename}"
                target_file = f"{target_path}/{filename}"
                if not os.path.exists(target_file):
                    os.symlink(source_file, target_file)
                    print(f"Created Symlink: {target_file}")
                elif not os.path.islink(target_file):
                    warn(f"Not a Symlink: {target_file}")
                else:
                    resolved_path = os.readlink(target_file)
                    warn(f"Unexpected Target for Symlink '{target_file}': {resolved_path}")


if __name__ == '__main__':
    main()
