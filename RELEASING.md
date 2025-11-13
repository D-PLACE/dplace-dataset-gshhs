# Releasing the ea


```shell
cldfbench makecldf cldfbench_gshhs.py --with-zenodo --with-cldfreadme --glottolog-version v5.2
pytest
```

```shell
cldfbench readme cldfbench_gshhs.py
cldfbench zenodo --communities dplace cldfbench_gshhs.py
dplace check cldfbench_gshhs.py
```

```shell
git status
git tag
```

Adapt CHANGELOG.md.
Add, commit and push all changes.

```shell
dplace release cldfbench_gshhs.py vX.Y
```