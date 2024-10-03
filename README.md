# python-snippets
Short Python scripts I created.


# Table of Contents

- [Overview](#overview)
- [Scripts](#scripts)
  - [1. `highlight.py`](#1-highlightpy)
    - [Description](#description)
    - [Usage](#usage)
    - [Example](#example)
  - [2. `unicode_chart.py`](#2-unicode_chartpy)
    - [Description](#description-1)
    - [Usage](#usage-1)
    - [Example](#example-1)
- [Installation](#installation)
- [Contributing](#contributing)
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
