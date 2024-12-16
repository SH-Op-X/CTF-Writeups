from setuptools import setup, Extension
from Cython.Build import cythonize

ext_module = [
    Extension(
        name="restore_symbol",
        sources=["restore_symbol.py"],
        extra_compile_args=["/Zi"],
        extra_link_args=["/DEBUG"]
    )
]

setup(
    name="restore_symbol",
    ext_modules=cythonize(ext_module, annotate=True),
)

