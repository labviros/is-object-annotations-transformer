from setuptools import setup, find_packages

setup(
    name='is_object_annotations_transformer',
    version='0.0.1',
    description='',
    url='http://github.com/labviros/is-object-annotations-transformer',
    author='labviros',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'is-object-annotations-transformer=is_object_annotations_transformer.service:main',
        ],
    },
    zip_safe=False,
    install_requires=[
        'is-wire==1.1.3',
        'is-msgs==1.1.8',
        'numpy==1.14.3',
    ],
)
