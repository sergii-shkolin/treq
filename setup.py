from setuptools import setup

setup(
    name='treq',
    version='0.1.0',
    author='Marius Stanca',
    author_email=['me@marius.xyz'],
    url='http://marius.xyz',
    license='MIT',
    description='Create backend resources for Terraform states',
    packages=['treq'],
    long_description=open('README.md').read(),
    include_package_data=True,
    package_data={'': ['README.md']},
    install_requires=['click>=7.0',
                      'cerberus==1.2',
                      'pyyaml',
                      'boto3==1.9.122',
                      'termcolor==1.1.0'],
    extras_require={
        'click': ['click>=7.0']},
    classifiers=[
        'Environment :: Tools',
        'Intended Audience :: Operations',
        'License :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.x',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points='''
        [console_scripts]
        treq=treq.cli:cli
    '''
)