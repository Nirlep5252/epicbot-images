from setuptools import setup
import re
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with open('epicbot_images/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

if not version:
    raise RuntimeError("Version is not set.")

setup(
    name="epicbot-images",
    author="Nirlep_5252_",
    url="https://github.com/Nirlep5252/epicbot-images",
    version=version,
    packages=['epicbot_images'],
    license='MIT',
    description="An image manipulation module for EpicBot.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=['pillow>=8.1.2'],
    python_requires='>=3.5.3',
    include_package_data=True,
    keywords=['discord.py', 'meme', 'discord', 'image-gen']
)
