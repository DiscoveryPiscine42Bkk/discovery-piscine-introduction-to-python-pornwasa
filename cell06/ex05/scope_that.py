#!/usr/bin/env python3

def add_one(x):
    x = x + 1
    print(f"[inside function] x = {x}")

if __name__ == "__main__":
    a = 5
    print(f"[before function] a = {a}")
    add_one(a)
    print(f"[after function] a = {a}")
