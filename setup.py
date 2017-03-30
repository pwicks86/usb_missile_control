import setuptools

setuptools.setup(
    name="usb_missile_control",
    version="0.1.0",
    url="https://github.com/pwicks86/usb_missile_control",

    author="Paul Wicks",
    author_email="pwicks86@gmail.com",

    description="Control module for the Dream Cheeky USB Missile launcher",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[
        "pyusb",
        "pynput",
        "python3_xlib"],
    entry_points={
        'console_scripts': ['missile-control-cli=usb_missile_control.missile_control:basic_missile_test'],
    },

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
