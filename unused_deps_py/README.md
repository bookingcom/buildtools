# Unused Deps Py

unused_deps_py is a command line tool to determine any unused dependencies
in [java_library](https://docs.bazel.build/versions/master/be/java.html#java_library)
rules. targets.  It outputs `buildozer` commands to apply the suggested
prunings. It's based on unused_deps but it also adds support for rules_jvm_external
maven repositories.

## Installation

Build a binary and put it into your $PATH:

```bash
bazel build //unused_deps_py
mkdir -p ~/bin
ln -s $(pwd)/bazel-bin/unused_deps_py/unused_deps_py ~/bin/unused_deps_py
```

## Usage

```shell
unused_deps_py TARGET...
```

Here, `TARGET` is a space-separated list of Bazel labels, with support for `:all` and `...`

## Releasing

In order to release a new version you need to run this commands:

```shell
bazel build --build_python_zip //unused_deps_py
```

And then upload `bazel-bin/unused_deps_py/unused_deps_py.zip` to GitHub
