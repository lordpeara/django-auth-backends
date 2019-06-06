from setuptools import setup, find_packages


setup(
    name='django-auth-backends',
    version='0.0.0',
    packages=find_packages(exclude=['*.tests']),
    scripts=[],

    install_requires=[
        'Django<2.2,>=1.11.21',
    ],

    author='lordpeara',
    author_email='lordpeara@gmail.com',
    description='django auth backends you might need to use',
    license='MIT',
    keywords='django auth authentication backend social-auth ouath2',
    url='http://github.com/lordpeara/django-auth-backends',

    zip_safe=False,
    include_package_data=True,

    classifiers=[
        # 'Framework :: Django',
        # 'Intended Audience :: Developers',
        # 'Intended Audience :: System Administrators',
        # 'Operating System :: OS Independent',
        # 'Topic :: Software Development'
    ],
)
