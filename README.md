# How to work

```shell
git clone git@github.com:kenzo-tanaka/dependency_sort.git
python3 lib/dependencies.py https://github.com/github/view_component 100
# python3 lib/dependencies.py [repository_url] [min_star]
```

クリップボードにコピー

```shell
python3 lib/dependencies.py https://github.com/github/view_component 500 | pbcopy
```

# Test

```shell
python3 test/test_dep_star_sort.py
```
