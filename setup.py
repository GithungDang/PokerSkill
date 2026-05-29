from setuptools import setup, find_packages

setup(
    name="pokerskill-agent",
    version="2.0.0",
    description="PokerSkill: Expert-Level Poker Play from Pure Language Models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Boning Li, Baoxiang Wang, Longbo Huang",
    author_email="li-bn22@mails.tsinghua.edu.cn",
    url="https://github.com/lbn187/PokerSkill",
    python_requires=">=3.9",
    packages=find_packages(),
    package_data={
        "pokerskill_agent._core": ["*.so", "*.pyd"],
        "pokerskill_agent._range": ["*.so", "*.pyd"],
        "pokerskill_agent._battle": ["*.so", "*.pyd"],
        "pokerskill_agent.examples": ["*.json"],
    },
    install_requires=[
        "httpx>=0.24,<1.0",
        "anthropic>=0.30,<1.0",
        "openai>=1.0,<2.0",
    ],
    entry_points={
        "console_scripts": [
            "pokerskill-agent=pokerskill_agent.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: POSIX :: Linux",
    ],
    zip_safe=False,
)
