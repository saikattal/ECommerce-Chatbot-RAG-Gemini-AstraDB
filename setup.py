from setuptools import find_packages,setup

setup(
    name='ECommerceChatbot',
    version='0.0.1',
    author='Saikat',
    author_email='saikat07taluk@gmail.com',
    description='A chatbot for an e-commerce platform',
    packages= find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain-openai','datasets','pypdf','python-dotenv','flask']
)
