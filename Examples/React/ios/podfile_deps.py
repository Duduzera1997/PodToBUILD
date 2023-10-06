new_pod_repository(
  name = "DoubleConversion",
  url = 'https://github.com/google/double-conversion/archive/v1.1.6.zip',
  podspec_url = 'Vendor/React/third-party-podspecs/DoubleConversion.podspec',
  install_script = """
    # prepare_command
    mv src double-conversion
    __INIT_REPO__
  """
)
new_pod_repository(
  name = "RCT-Folly",
  podspec_url = "Vendor/React/third-party-podspecs/RCT-Folly.podspec",
  generate_header_map = 1
)
new_pod_repository(
  name = "boost",
  url = "https://github.com/react-native-community/boost-for-react-native/archive/v1.63.0-0.zip",
  podspec_url = "Vendor/React/third-party-podspecs/boost.podspec",
  generate_header_map = 1
)
new_pod_repository(
  name = "CocoaAsyncSocket",
  url = "https://github.com/robbiehanson/CocoaAsyncSocket/archive/7.6.5.zip",
  podspec_url = "Vendor/Podspecs/CocoaAsyncSocket.podspec.json",
  generate_header_map = 1
)

new_pod_repository(
  name = "FBLazyVector",
  url = "Vendor/React/Libraries/FBLazyVector",
  generate_header_map = 1
)
new_pod_repository(
  name = "FBReactNativeSpec",
  # url = "Vendor/React/React/FBReactNativeSpec",
  podspec_url = "Vendor/Podspecs/FBReactNativeSpec.podspec.json",
  generate_header_map = 1
)
new_pod_repository(
  name = "Flipper",
  url = "https://github.com/facebook/flipper/archive/v0.221.0.zip",
  podspec_url = "Vendor/Flipper/iOS/Podspecs/Flipper.podspec.json",
  generate_header_map = 1
)
new_pod_repository(
  name = "Flipper-Boost-iOSX",
  url = "https://github.com/priteshrnandgaonkar/Flipper-Boost-iOSX/archive/1.76.0.1.11.zip",
  podspec_url = "Vendor/Flipper/iOS/Podspecs/Flipper-Boost-iOSX.podspec",
  generate_header_map = 1
)
new_pod_repository(
  name = "Flipper-DoubleConversion",
  url = "https://github.com/lblasa/double-conversion/archive/flipper-double-conversion-v3.2.0.1.zip",
  podspec_url = "Vendor/Flipper/iOS/Podspecs/Flipper-DoubleConversion.podspec",
  generate_header_map = 1
)
new_pod_repository(
  name = "Flipper-Fmt",
  url = "https://github.com/priteshrnandgaonkar/fmt/archive/7.1.7.zip",
  podspec_url = "Vendor/Flipper/iOS/Podspecs/Flipper-Fmt.podspec",
  generate_header_map = 1
)
new_pod_repository(
  name = "Flipper-Folly",
  url = "https://github.com/facebook/folly/archive/v2021.06.14.00.zip",
  podspec_url = "Vendor/Flipper/iOS/Podspecs/Flipper-Folly.podspec",
  generate_header_map = 1
)
new_pod_repository(
  name = "Flipper-Glog",
  url = "https://github.com/lblasa/glog/archive/flipper-glog-v0.5.0.5.zip",
  podspec_url = "Vendor/Flipper/iOS/Podspecs/Flipper-Glog.podspec",
  generate_header_map = 1
)
new_pod_repository(
  name = "Flipper-PeerTalk",
  url = "https://github.com/priteshrnandgaonkar/peertalk/archive/v0.0.3.zip",
  podspec_url = "Vendor/Flipper/iOS/Podspecs/Flipper-PeerTalk.podspec",
  generate_header_map = 1
)
new_pod_repository(
  name = "FlipperKit",
  url = "https://github.com/facebook/flipper/archive/v0.221.0.zip",
  podspec_url = "Vendor/Flipper/iOS/Podspecs/FlipperKit.podspec",
  generate_header_map = 1
)
new_pod_repository(
  name = "fmt",
  url = "https://github.com/fmtlib/fmt/archive/7.1.3.zip",
  podspec_url = "Vendor/Podspecs/fmt.podspec.json",
  generate_header_map = 1
)
new_pod_repository(
  name = "glog",
  url = "https://github.com/google/glog/archive/v0.3.4.zip",
  podspec_url = "Vendor/React/third-party-podspecs/glog.podspec",
  generate_header_map = 1
)
new_pod_repository(
  name = "hermes-engine",
  url = "https://github.com/facebook/hermes/archive/refs/tags/hermes-2023-03-20-RNv0.72.0-49794cfc7c81fb8f69fd60c3bbf85a7480cc5a77.tar.gz",
  podspec_url = "Vendor/Podspecs/hermes-engine.podspec.json",
  generate_header_map = 1
)
new_pod_repository(
  name = "libevent",
  url = "https://github.com/libevent/libevent/archive/release-2.1.12-stable.zip",
  podspec_url = "Vendor/Flipper/iOS/Podspecs/libevent.podspec",
  generate_header_map = 1
)
new_pod_repository(
  name = "OpenSSL-Universal",
  url = "https://github.com/krzyzanowskim/OpenSSL/archive/1.1.1100.zip",
  # podspec_url = "Vendor/OpenSSL-Universal/OpenSSL-Universal.podspec",
  generate_header_map = 1
)

new_pod_repository(
  name = "RCTRequired",
  url = "Vendor/React/Libraries/RCTRequired",
  generate_header_map = 1
)
new_pod_repository(
  name = "RCTTypeSafety",
  url = "Vendor/React/Libraries/TypeSafety",
  generate_header_map = 1
)
new_pod_repository(
  name = "React",
  url = "Vendor/React",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-callinvoker",
  url = "Vendor/React/ReactCommon/callinvoker",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-Codegen",
  # url = "build/generated/ios",
  podspec_url = "Vendor/Podspecs/React-Codegen.podspec.json",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-Core",
  url = "Vendor/React",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-CoreModules",
  url = "Vendor/React/React/CoreModules",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-cxxreact",
  url = "Vendor/React/ReactCommon/cxxreact",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-debug",
  url = "Vendor/React/ReactCommon/react/debug",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-hermes",
  url = "Vendor/React/ReactCommon/hermes",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-jsi",
  url = "Vendor/React/ReactCommon/jsi",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-jsiexecutor",
  url = "Vendor/React/ReactCommon/jsiexecutor",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-jsinspector",
  url = "Vendor/React/ReactCommon/jsinspector",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-logger",
  url = "Vendor/React/ReactCommon/logger",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-NativeModulesApple",
  url = "Vendor/React/ReactCommon/react/nativemodule/core/platform/ios",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-perflogger",
  url = "Vendor/React/ReactCommon/reactperflogger",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-RCTActionSheet",
  url = "Vendor/React/Libraries/ActionSheetIOS",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-RCTAnimation",
  url = "Vendor/React/Libraries/NativeAnimation",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-RCTAppDelegate",
  url = "Vendor/React/Libraries/AppDelegate",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-RCTBlob",
  url = "Vendor/React/Libraries/Blob",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-RCTImage",
  url = "Vendor/React/Libraries/Image",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-RCTLinking",
  url = "Vendor/React/Libraries/LinkingIOS",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-RCTNetwork",
  url = "Vendor/React/Libraries/Network",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-RCTSettings",
  url = "Vendor/React/Libraries/Settings",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-RCTText",
  url = "Vendor/React/Libraries/Text",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-RCTVibration",
  url = "Vendor/React/Libraries/Vibration",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-rncore",
  # url = "Vendor/React/ReactCommon",
  podspec_url = "Vendor/Podspecs/React-rncore.podspec.json",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-runtimeexecutor",
  url = "Vendor/React/ReactCommon/runtimeexecutor",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-runtimescheduler",
  url = "Vendor/React/ReactCommon/react/renderer/runtimescheduler",
  generate_header_map = 1
)
new_pod_repository(
  name = "React-utils",
  url = "Vendor/React/ReactCommon/react/utils",
  generate_header_map = 1
)
new_pod_repository(
  name = "ReactCommon",
  url = "Vendor/React/ReactCommon",
  generate_header_map = 1
)
new_pod_repository(
  name = "SocketRocket",
  url = "https://github.com/facebookincubator/SocketRocket/archive/0.7.0.zip",
  podspec_url = "Vendor/Podspecs/SocketRocket.podspec.json",
  generate_header_map = 1
)
new_pod_repository(
  name = "Yoga",
  url = "Vendor/React/ReactCommon/yoga",
  generate_header_map = 1
)
new_pod_repository(
  name = "YogaKit",
  url = "https://github.com/facebook/yoga/archive/v2.0.0.zip",
  podspec_url = "Vendor/Podspecs/YogaKit.podspec",
  generate_header_map = 1
)
