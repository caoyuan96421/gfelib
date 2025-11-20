# gfelib
A collection of reusable components for [gdsfactory](https://github.com/gdsfactory).

## Use This Library
```sh
# navigate to your project's root directory
$ cd your/project/directory

# add this repository as a git submodule
$ git submodule add https://github.com/DanielHeEGG/gfelib libs/gfelib

# install the library
$ pip install -e lib/gfelib
```

## Contributing
```sh
# fork this repo on GitHub

# clone this repo
$ git clone https://github.com/your_github_username/gfelib
$ cd gfelib

# initialize local venv
$ python -m venv venv
$ source venv/bin/activate

# install dependencies
$ pip install gdsfactory numpy

# install pre-commit hooks
$ pre-commit install

# create a new branch for your component
$ git checkout -b your_new_component

# add commits and push
$ git commit -m "your commit message"
$ git push origin your_new_component

# create a PR on GitHub
```
- Each component shall have it's own file, and be imported by the submodule's `__init__.py` file
- Each new component shall be added in it's own pull request
- Use the provided `.pre-commit-config.yaml` file for commit checks
- Follow the general style guide in `STYLEGUIDE.md`
