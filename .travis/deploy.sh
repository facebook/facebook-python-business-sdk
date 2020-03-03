echo 'test deploy...'
python setup.py sdist bdist_wheel
twine upload dist/*
