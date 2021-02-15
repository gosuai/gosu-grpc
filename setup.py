import setuptools

packages = [
    package
    for package in setuptools.PEP420PackageFinder.find()
    if package.startswith('google') or package.startswith('gosu')
]

namespaces = ['google']
if 'google.cloud' in packages:
    namespaces.append('google.cloud')

setuptools.setup(
    name='google-gosu',
    packages=packages,
    namespace_packages=namespaces,
    version='0.3.1',
    license='MIT',
    description='Library to work with google libs',
    author='Gosu developers',
    author_email='support@gosu.ai',
    url='https://github.com/gosuai/gosu-grpc',
    keywords=['grpc', 'gosu'],
    install_requires=[
        'aiohttp>=3.6.2',
        'google-api-core>=1.25.0',
        'google-auth>=1.25.0',
        'google-auth-httplib2>=0.0.4',
        'google-auth-oauthlib>=0.4.2',
        'grpclib>=0.4.1',
        'protobuf>=3.12.2',
    ],
    classifiers=[
        'Development Status :: Production',
        'Intended Audience :: Gosu Fellows',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
