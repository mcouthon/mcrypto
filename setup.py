from setuptools import setup


setup(
    name='mcrypto',
    version='0.1',
    author='Pavel Brodsky',
    author_email='mcouthon@gmail.com',
    packages=[
        'mcrypto',
        'mcrypto.mcrypto_project',
        'mcrypto.mcrypto_project.mcrypto_project',
        'mcrypto.mcrypto_project.portfolio',
        'mcrypto.mcrypto_project.portfolio.migrations',
    ],
    description='A cryptocurrency portfolio manager',
    install_requires=[
        'Django>=1.11.1',
    ],
)
