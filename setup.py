from setuptools import setup,find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='pcpartscraper',
    version='1.0.6',
    description="A powerful pcpartpicker.com WebScraper that extracts Data from Part URL's and search Queries.",
    long_description_content_type='text/markdown',
    long_description=open('README.md','r').read() + '\n\n' + open('changelog.txt','r').read(),
    url='https://github.com/Jeet-Chugh/pcpartscraper',
    author='Jeet Chugh',
    author_email='sunjeetchugh@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='pcpartpicker',
    package_dir={'pcpartscraper':'pcpartscraper'},
    packages=['pcpartscraper'],
    install_requires=['bs4','requests']
)
