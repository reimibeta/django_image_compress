from setuptools import setup, find_packages

setup(
    name='django_image_compress',
    version='0.4',
    description='A sample image compress',
    long_description='Test Long',
    author='ReimiBeta',
    author_email='reimi846@gmail.com',
    url='https://github.com/reimibeta',
    license='MIT',
    packages=find_packages(),
    # py_modules=['image_compress',],
    install_requires=[
        # other dependencies
        'Pillow'
    ],
    # other optional arguments
)
