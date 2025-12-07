from setuptools import setup, find_packages

setup(
    name="sahr",
    version="1.0.0",
    description="Telegram bot wrapper for auto file scanning and command execution",
    author="sahr",
    packages=find_packages(),
    install_requires=[
        "pyTelegramBotAPI",
        "requests",
    ],
    python_requires=">=3.7",
)