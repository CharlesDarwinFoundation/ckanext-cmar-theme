[![Tests](https://github.com/CharlesDarwinFoundation/ckanext-cmar-theme/workflows/Tests/badge.svg?branch=main)](https://github.com/CharlesDarwinFoundation/ckanext-cmar-theme/actions)

# ckanext-cmar-theme
Theme for the CMAR instance of CKAN.


## Requirements
A working CKAN installation.

## Installation
To install ckanext-cmar-theme:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    git clone https://github.com/CharlesDarwinFoundation/ckanext-cmar-theme.git
    cd ckanext-cmar-theme
    pip install -e .
	pip install -r requirements.txt

3. Add `cmar-theme` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload



## Developer installation

To install ckanext-cmar-theme for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/CharlesDarwinFoundation/ckanext-cmar-theme.git
    cd ckanext-cmar-theme
    python setup.py develop
    pip install -r dev-requirements.txt


## Tests
To run the tests, do:

    pytest --ckan-ini=test.ini


## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
