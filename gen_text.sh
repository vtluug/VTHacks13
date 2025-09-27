#!/usr/bin/env bash

text=$(tr '\n' ' ' < <(cat ./inputs/*))

echo "$text"
