from setuptools import setup
import re

version = ''
with open('epicbot_images/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("Version is not set.")

setup(
    name="epicbot-images",
    url="https://github.com/Nirlep5252/epicbot-images",
    version=version,
    packages=['epicbot-images'],
    license='MIT',
    description="An image manipulation module for EpicBot.",
    install_requires=['pillow>=8.1.2'],
    python_requires='>=3.5.3'
)