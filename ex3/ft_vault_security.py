#!/usr/bin/env python3

def secure_archive(source_data: str) -> tuple[bool, str]:
    boolean = False
    result = ""
    try:
        with open(source_data) as o_data:
            result = o_data.read()
        boolean = True
    except OSError as err:
        result = str(err)
    return boolean, result