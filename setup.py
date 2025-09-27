import setuptools
from pathlib import Path

HERE = Path(__file__).parent
README = (HERE / "README.md").read_text(encoding="utf-8") if (HERE / "README.md").exists() else ""

setuptools.setup(
    name="tts_webui_extension.mms",
    packages=setuptools.find_namespace_packages(),
    version="0.0.3",
    author="rsxdalv",
    description="MMS (Massively Multilingual Speech) is a text-to-speech model supporting over 1000 languages",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rsxdalv/tts_webui_extension.mms",
    project_urls={},
    scripts=[],
    install_requires=[
        "transformers>=4.30.0",
        "iso639-lang==2.2.3",
    ],
    package_data={
        "tts_webui_extension.mms.resources": ["*.txt"],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

