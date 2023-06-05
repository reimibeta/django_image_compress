from setuptools import setup, find_packages

setup(
    name='image_compress',
    version='0.2',
    description='A sample image compress',
    long_description='Test Long',
    author='ReimiBeta',
    author_email='reimi846@gmail.com',
    url='http://pcrpallet.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        # other dependencies
        'Pillow'
    ],
    # other optional arguments
)
