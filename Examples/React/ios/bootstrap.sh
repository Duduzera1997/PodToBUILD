set -x
prepare_setup() {
    if [ ! -d ../node_modules ]; then
        yarn install
    fi

    if [ ! -d ./Vendor/React ]; then
        ln -s ../../node_modules/react-native ./Vendor/React
    fi

    # prepare_command is unsupported these are right out of the podspecs
    sed -i '' \
        's,spec.prepare_command,#spec.prepare_command,g' \
        Vendor/React/third-party-podspecs/glog.podspec
}

prepare_setup
# make update_xcodeproj gen_podfile_deps
