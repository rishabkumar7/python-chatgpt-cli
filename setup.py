from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'python-chatgpt-cli',
    version = '0.0.2',
    author = 'Rishab Kumar',
    author_email = 'rishabkumar7@gmail.com',
    license = 'MIT',
    description = 'A CLI wrapper for ChatGPT, used OPENAI API',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/rishabkumar7/python-chatgpt-cli',
    py_modules = ['python_chatgpt_cli', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        chatgpt_cli=python_chatgpt_cli:cli
    '''
)