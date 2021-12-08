# Unused Deps Py

unused_deps_py is a command line tool to determine any unused dependencies
in [java_library](https://docs.bazel.build/versions/master/be/java.html#java_library)
targets. It outputs `buildozer` commands to apply the suggested
prunings. It's based on [unused_deps](https://github.com/bazelbuild/buildtools/blob/master/unused_deps/README.md)
but it also adds support for [rules_jvm_external](https://github.com/bazelbuild/rules_jvm_external)
maven repositories.

## Installation

### Preferred way
```shell
$ pip install unused-deps-py
$ unused_deps_py --help
```

### Building from sources
```shell
$ bazel run //unused_deps_py -- --help
```

## Usage

```shell
unused_deps_py --workspace-path WORKSPACE_PATH TARGET...
```

Here, `TARGET` is a space-separated list of Bazel labels, with support for `:all` and `...`

## Releasing to PyPI

In order to release a new version you first need to edit BUILD.bazel to bump the
version number, then you need to run:

```shell
$ bazel build //unused_deps_py:unused_deps_py_wheel
$ twine upload bazel-bin/unused_deps_py/unused_deps_py-<version>-py3-none-any.whl
```
