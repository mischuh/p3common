# python3-common
Common utility classes

## To use it simply install it via pip

    pip install git+git://github.com/mischuh/p3common.git#egg=p3common
    
## To run it locally
    
    python3 -m venv venv
    source venv/bin/activate

    pip install -Ur requirements-test.txt
    pip install -Ur requirements.txt

## Import
    from common import validators as validate
    validate.is_str('Hallo')

## Build it
    
    python3 setup.py sdist