from setuptools import setup


setup(
    name='batchio',
    version='0.1',
    packages=['batchio', 'batchio.server'],
    package_dir={'': 'src'},
    url='https://github.com/rganjoo/batchio',
    license='ASL 2.0',
    author='Raymond Tham',
    author_email='raytham@gmail.com',
    description='',
    entry_points={
        'console_scripts': [
            'batchio = batchio.server.cli:main'
        ]
    }, requires=['aiohttp', 'apscheduler']
)
