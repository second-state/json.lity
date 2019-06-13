set -eux
litysource="$1"
input="$2"
set +u
export ENI_LIBRARY_PATH=$PWD/libeni/build/examples/eni
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PWD/libeni/build
rm -rf tempdir
mkdir tempdir
./lityc --bin-runtime "$litysource" --abi -o tempdir
python3 scripts/generate_string_input.py "$input" > tempdir/inputfile
exec ./evm --codefile tempdir/*.bin-runtime --inputfile tempdir/inputfile --statdump run > tempdir/outputfile
