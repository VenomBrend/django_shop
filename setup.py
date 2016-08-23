from setuptools import setup, find_packages

setup(
    name='Cats Shop',
    version='0.1',
    packages=find_packages(),
    install_requires=['Django==1.8',
                      'six=1.10.0',
                      'enum34=1.1.6',
                      'django-enumfields==0.8.2',
                      'Pillow==3.3.1'
                      ],
    description='Cats Shop on Django',
)
