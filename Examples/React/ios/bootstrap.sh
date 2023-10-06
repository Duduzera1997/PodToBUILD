set -x
# This is not trival and generally installed with npm
# Alternatively, add an entry in Pods.WORKSPACE with the latest URL for RN
# Note: on this release, there's an issue with this commit.
# this should be patched on somehow
# https://github.com/facebook/react-native/pull/28946
VERSION="0.72.5"

cleanup() {
    rm -rf react-native-${VERSION}*
}

download_react_if_necessary() {
    if [[ "$(cat PodsHost/RN_VERSION)" == "$VERSION" ]]; then
        echo "Already updated to $VERSION"
        return
    fi

    # PODIR=Vendor
    # mkdir -p PodsHost
    # echo $VERSION > PodsHost/RN_VERSION
    # [[ -f react-native-${VERSION}.zip ]] || \
    #     curl -L https://github.com/facebook/react-native/archive/v${VERSION}.zip \
    #     -o react-native-${VERSION}.zip
    # unzip -qu react-native-${VERSION}.zip

    # mkdir -p $PODIR
    # [[ ! -d $PODIR/react-native ]] \
    #     || rm -rf $PODIR/react-native
    # mv react-native-${VERSION}/packages/react-native $PODIR/react-native

    if [ ! -d ./Vendor/react-native ]; then
        ln -s ../../node_modules/react-native ./Vendor/React
    fi

    # prepare_command is unsupported these are right out of the podspecs
    sed -i '' \
        's,spec.prepare_command,#spec.prepare_command,g' \
        Vendor/react-native/third-party-podspecs/glog.podspec
}

trap cleanup EXIT
download_react_if_necessary
# make update_xcodeproj gen_podfile_deps
