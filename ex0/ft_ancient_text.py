#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        imputed_data = None
        try:
            imputed_data = open(sys.argv[1])
            print("---\n")
            print(imputed_data.read())
            print("---")
            print(f"File '{sys.argv[1]}' closed.")
        except OSError as err:
            print(f"Error opening file '{sys.argv[1]}': {err}")
        finally:
            if imputed_data is not None:
                imputed_data.close()
    else:
        print("Usage: ft_ancient_text.py <file>")
