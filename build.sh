set -eux

mkdir -p prefix
CFLAGS=-I$PWD/SkyPat/prefix/include
LDFLAGS=-L$PWD/SkyPat/prefix/lib

skypat() {
pushd SkyPat
	./autogen.sh
	mkdir -p build
	pushd build
		../configure --prefix=$(realpath ../prefix)
		make -j$(nproc) install
	popd
popd
}

libeni() {
pushd libeni
	ln -sf ../SkyPat/prefix/include PRIVATE
	mkdir -p build
	pushd build
		cmake .. -GNinja -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS" -DCMAKE_STATIC_LINKER_FLAGS="$LDFLAGS" -DCMAKE_MODULE_LINKER_FLAGS="$LDFLAGS" -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS" -DCMAKE_EXPORT_COMPILE_COMMANDS=1
		ninja
	popd
popd
}

skypat
libeni
