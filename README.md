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
- [ ] Strings with unicode escape sequences, such as `"\u0068\u0065\u006c\u006c\u006f"`

# Run EVM Tests

```
python3 -m unittest discover -s evmtests -t .
```

## Manual evmtests run

1.  copy `lity/json.lity` to the same directory of `test.lity` so it can be imported
2.  run `python3 run.py path/to/test.lity path/to/input.json`
