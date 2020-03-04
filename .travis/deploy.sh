echo "testing..."
python setup.py sdist bdist_wheel
pip install twine wheel
PROD_REPOSITORY="https://upload.pypi.org/legacy/"
twine upload \
    --username "ellentao" \
    --password ${PASSWORD} \
    --repository-url "$PROD_REPOSITORY" \
    dist/*
