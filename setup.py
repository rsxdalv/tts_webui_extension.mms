import setuptools

setuptools.setup(
    name="extension_mms",
    packages=setuptools.find_namespace_packages(),
    version="0.0.1",
    author="rsxdalv",
    description="MMS (Massively Multilingual Speech) is a text-to-speech model supporting over 1000 languages",
    url="https://github.com/rsxdalv/extension_mms",
    project_urls={},
    scripts=[],
    install_requires=[
        "transformers>=4.30.0",
        "iso639-lang==2.2.3",
    ],
    package_data={
        "extension_mms.resources": ["*.txt"],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
