#!/bin/bash

./read_input.sh input.txt | python solution.py | diff --strip-trailing-cr output.txt -