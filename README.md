# EXE

Can be downloaded [here](https://nextcloud.osug.fr/index.php/s/P4bk4YWxdwGJrAj)

# About

This code is a programme to calculate **spectrum convolution**. 

That is, it serves to reduce the resolution of the original high-resolution spectrum so that it corresponds to an instrument with lower resolution, while preserving the energy as much as possible. 

# How it works

The programme is written in **Python** using **PyQt**. 

It consists of two parts: **the core** and **the interface**. 

The core itself completely solves the problem of convolution. For convenience of working with it, a layer working with the interface is created on top of it: the interface.

Conv_core.py is responsible for the core. The interface is nested in main.py.

A [separate repository](https://github.com/FlexStudia/Convolution_core.git) has been created for the core. If you are more interested in using the core, we invite you to visit this repository. Here is the repository for the core-interface tandem.

There are several possibilities for working with this code:

- use exe (see EXE section at the beginning of this README)
- modify this code and compile your own EXE (to do this you need to install Python, install a virtual environment, install the packages from requirements.txt and then work with the code).
- use this code as a module in your project

# License

As we use the PyQt package for free, it obliges us to use **the GNU General Public License v3.0**. This licence imposes two obligations. First: the resulting **code must be made freely available** to the public (we fulfil this obligation through this repository). Second: any code based on this code must also be **distributed under the GNU General Public License** v3.0.

You should keep this in mind when using this code.

If this is not possible, there are two ways out. One: rewrite the interface code through **PySide**, where there is no obligation to use the GNU licence. Second: create your own interface based on the **core**, since the core itself we distribute under the MIT licence.

# Questions

Any questions and suggestions please send to [flex.studia.dev@gmail.com](mailto:flex.studia.dev@gmail.com).
