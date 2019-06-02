import sys
from setuptools import find_packages, setup
from setuptools_rust import RustExtension


PYTHON_MAJOR_VERSION = sys.version_info[0]

setup_requires = ['setuptools-rust>=0.6.0']
install_requires = ['numpy']
test_requires = install_requires + ['pytest']

setup(
    name='rs_estimator',
    version='0.1.0',
    description='Example of python-extension using rust-numpy',
    rust_extensions=[RustExtension(
        'rs_estimator.rs_estimator',
        './Cargo.toml',
    )],
    install_requires=install_requires,
    setup_requires=setup_requires,
    test_requires=test_requires,
    packages=find_packages(),
    zip_safe=False,
)
