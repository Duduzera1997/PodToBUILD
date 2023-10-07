## Requirements 🛠️

- [React Native - Environment Setup](https://reactnative.dev/docs/environment-setup)
- Patience 🤣

### Step 1: Bootstrap your Project

```bash
make bootstrap
```

### Step 2: Use the Bazel to update_pods

```bash
 bazel run @rules_pods//:update_pods -- --src_root $PWD
```

### Comments and Tips

- We Need the node dependencies and _node_modules_ folder to use react_native_pods.rb script on Podfile without a patch to access the @react-native-community/cli;

- The BUILD name of the Bazel file doesn’t work with React-Codegen because the Pod uses the ./build folder and we need to rename BUILD to BUILD.bazel;

- React-debug.podspecs / React-runtimescheduler.podspec / React-utils.podspec is necessary add min_ios_version_supported = "12.4" line on top of files because we don't using the react_native_pods.rb on bazel pods installation;
