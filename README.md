# Environment setup

1. Git clone this repo with --recursive
2. run `build.sh` to build ENI and SkyPat
3. Download `lityc` and put it in this directory
4. Build evm with `--inputfile` support from https://git-cybermiles.skymizer.com/afg/go-ethereum, and place the evm executable it in this directory


# Testing command examples

```
run.sh [lity source] [input file]
```

```
$ sh run.sh lity/Reverse.lity data/test.txt
$ sh showresult.sh
dlroW ,olleH
```

# Expected result

```
$ sh run.sh lity/Example.lity data/ethereum.json
$ sh showresult.sh
Wyoming energy company to tokenize Oil assets on the Ethereum blockchain
```
