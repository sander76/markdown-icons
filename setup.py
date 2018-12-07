from setuptools import setup

setup(
    name='markdown-iconfonts',
    description='Easily display icon fonts in markdown.',
    version="2.1.1",
    py_modules=['iconfonts'],
    install_requires=['markdown', 'six'],
    author='Eric Eastwoord',
    url='https://github.com/MadLittleMods/markdown-icons',
    keywords='markdown, icons, fontawesome, bootstrap',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
