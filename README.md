# python-snippets
Short Python scripts I created.


# Table of Contents

- [Overview](#overview)
- [Scripts](#scripts)
  - [1. `highlight.py`](#1-highlightpy)
    - [Description](#description)
    - [Usage](#usage)
  - [2. `unicode_chart.py`](#2-unicode_chartpy)
    - [Description](#description-1)
    - [Usage](#usage-1)
- [Installation](#installation)
- [License](#license)

---

## Overview

This repository contains several Python scripts, each with its own specific utility. Below is a brief description of each script along with examples and instructions for how to use them.

## Scripts

### 1. `highlight.py`

#### Description

The `highlight.py` script searches through an input text file for words beginning with the letters provided in the arguments. Matched words are "highlighted" by printing out a new version of the original file with the matches in uppercase.

#### Usage

```bash
python3 highlight.py <filename> [<a> <b> <c> ...]

```bash
python3 highlight.py sample1.txt p 
python3 highlight.py sample2.txt h m e

### 2. `unicode_chart.py`

The `unicode_chart.py` script prints out a chart of unicode characters, showing the character and its numerical value. One argument: prints everything

#### Usage

0 arguments mode: Displays the first 100 characters.
1 argument mode: Displays characters from 0 up to the given number.
2 arguments: Displays characters from the first number up to the second number.

```bash
python3 unicode_chart.py [<number> <number>]

```bash
python3 unicode_chart.py
python3 unicode_chart.py 9000 9400
