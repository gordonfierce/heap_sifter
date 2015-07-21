from setuptools import setup

setup(
    name='heap_sifter',
    version='0.1',
    py_modules=['heap_sifter'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        heap_sifter=insert:add_todo
    ''',
)
