# Read and Write Challenge (Improved Version)

from pathlib import Path


def modify_file(input_file: str, output_file: str = "output.txt", mode: str = "upper") -> None:
    """
    Reads a file, transforms content, and writes to output file.
    Modes: upper | lower
    """

    try:
        input_path = Path(input_file).resolve()

        if not input_path.exists():
            raise FileNotFoundError(f"File '{input_file}' not found.")

        # Read file
        content = input_path.read_text(encoding="utf-8")

        # Modify content based on mode
        if mode == "lower":
            modified_content = content.lower()
        else:
            modified_content = content.upper()

        # Write output
        output_path = Path(output_file).resolve()
        output_path.write_text(modified_content, encoding="utf-8")

        print(f"✔ Success! Output written to: {output_path} (mode: {mode})")

    except FileNotFoundError as e:
        print(f"Error: {e}")

    except PermissionError:
        print("Error: Permission denied when accessing file.")

    except Exception as e:
        print(f"Unexpected error: {e}")


def get_input_file() -> str:
    """
    Prompts user until a valid file path is provided.
    """

    while True:
        path = input("Enter input file path (e.g. output.txt): ").strip()

        p = Path(path)

        if p.exists() and p.is_file():
            return str(p)

        print(f"Error: File '{path}' not found in current directory or path is invalid.")


# Main execution
if __name__ == "__main__":
    input_file_path = get_input_file()

    output_name = input("Enter output file name (default: output.txt): ").strip()
    if not output_name:
        output_name = "output.txt"

    mode = input("Choose mode (upper/lower) [default: upper]: ").strip().lower()
    if mode not in ["upper", "lower"]:
        mode = "upper"

    modify_file(input_file_path, output_name, mode)