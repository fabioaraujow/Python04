#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        imputed_data = None
        text = None
        to_replace = ""
        replaced = None
        try:
            imputed_data = open(sys.argv[1])
            print("---\n")
            text = imputed_data.read()
            print(text)
            print("---")
            print(f"File '{sys.argv[1]}' closed.")
        except OSError as err:
            print(f"Error opening file '{sys.argv[1]}': {err}")
        finally:
            if imputed_data is not None:
                imputed_data.close()
        print()
        if text is not None:
            lines = text.splitlines()
            n_lines = [line + "#" for line in lines]
            rebuild = "\n".join(n_lines)
            rebuild += "\n"
            print("Transform data:")
            print("---\n")
            print(f"{rebuild}")
            print("---")
            to_replace = input("Enter new file name (or empty): ")
            if to_replace:
                try:
                    replaced = open(to_replace, "w")
                    print(f"Saving data to '{to_replace}'")
                    replaced.write(rebuild)
                    print(f"Data saved in file '{to_replace}'.")
                except OSError as err:
                    print(f"Error opening file '{to_replace}': {err}")
                finally:
                    if replaced is not None:
                        replaced.close()
            else:
                print("Not saving data.")
    else:
        print("Usage: ft_archive_creation.py <file>")
