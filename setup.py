from distutils.core import setup
setup(
    name='gosu_grpc',
    packages=['gosu_grpc'],
    version='0.1.4',
    license='MIT',
    description='Library to work with google libs',
    author='Gosu developers',
    author_email='support@gosu.ai',
    url='https://github.com/gosuai/gosu-grpc',
    keywords=['grpc', 'gosu'],
    install_requires=[
        'aiohttp==3.6.2',
        'google-auth@git+git://github.com/gosuai/google-auth-library-python@asyncio#egg=google-auth',
        'google-auth-httplib2==0.0.3',
        'google-auth-oauthlib==0.4.1',
        'grpclib==0.3.2',
        'protobuf==3.12.2',
        # -e git://github.com/gosuai/gosu-grpc@initial#egg=gosu_grpc
    ],
    classifiers=[
        'Development Status :: Production',
        'Intended Audience :: Gosu Fellows',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
