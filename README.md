# Environment setup

1. Git clone this repo with --recursive
2. run `build.sh` to build ENI and SkyPat
3. Download `lityc` and put it in this directory
4. Build evm with `--inputfile` support (`make -C lityvm evm`).

# Usage examples

See ``evmtests/``

# Status

APIs are likely to change.

- [x] Get string
- [x] Get array object by index
- [x] Get object attribute by key (string)
- [x] Nested arrays & objects

# Testing command examples

```
python3 run.py [lity source] [input file]
```

```
$ python3 run.py lity/Reverse.lity data/test.txt
$ sh showresult.sh
dlroW ,olleH
```
