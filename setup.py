from setuptools import setup

install_requires = []

setup(
    name='storysniffer',
    version='0.0.1',
    description='Inspect a URL and estimate if it links to news story',
    author='Ben Welsh',
    author_email='ben.welsh@gmail.com',
    url='https://github.com/pastpages/storysniffer',
    license='MIT',
    packages=('storysniffer',),
    install_requires=install_requires,
)
