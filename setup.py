import setuptools

setuptools.setup(
    name="common",
    version="0.0.19",
    author="Indoc Research",
    author_email="etaylor@indocresearch.org",
    description="Generates entity ID and connects with Vault (secret engine) to retrieve credentials",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'flask-executor==0.9.3',
        'gunicorn==20.0.4',
        'flask-restx==0.2.0',
        'Flask==1.1.4',
        'Flask-Cors==3.0.8',
        'python-json-logger==0.1.11',
        'requests>=2.23.0,<=2.27.0',
        'python-dotenv==0.19.1',
        'pydantic==1.8.2',
        'itsdangerous==1.1.0',
        'markupsafe==1.1.1',
    ],
    include_package_data=True,
    package_data={
        "": ["*.crt"],
    }
)
