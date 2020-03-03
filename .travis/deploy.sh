echo 'test deploy...'
python setup.py sdist bdist_wheel
pip install twine wheel
twine upload dist/*
