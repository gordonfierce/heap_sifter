from setuptools import setup

setup(
    name='heapsifter',
    version='0.1',
    py_modules=['heapsifter'],
    install_requires=[
        'Click',
        'future',
        'pbr',
        'hypothesis',
    ],
    entry_points='''
        [console_scripts]
        heapsifter=heapsifter:cli
    ''',
    pbr=True
)
