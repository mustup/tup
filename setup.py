import setuptools


packages = setuptools.find_namespace_packages(
    include=[
        'mustup.*',
    ],
)

setuptools.setup(
    name='mustup_tup',
    packages=packages,
    python_requires='>= 3.8',
    version='0.1',
    zip_safe=False, # due to namespace package
)
