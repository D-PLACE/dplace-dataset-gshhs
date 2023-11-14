from setuptools import setup


setup(
    name='cldfbench_dplace-dataset-gshhs',
    py_modules=['cldfbench_dplace-dataset-gshhs'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'dplace-dataset-gshhs=cldfbench_dplace-dataset-gshhs:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
