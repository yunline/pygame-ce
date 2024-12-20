Pygame-ce Front Page
====================

.. toctree::
   :maxdepth: 2
   :glob:
   :hidden:

   ref/*
   tutorials/en/*
   tutorials/en/**/*
   tutorials/ko/**/*
   tutorials/es/*
   c_api
   filepaths
   logos

Quick start
-----------

Welcome to pygame-ce! Once you've got pygame-ce installed
(:code:`pip install pygame-ce` or :code:`pip3 install pygame-ce` for most
people), the next question is how to get a game loop running. Pygame-ce,
unlike some other libraries, gives you full control of program
execution. That freedom means it is easy to mess up in your initial steps.

Here is a good example of a basic setup (opens the window, updates the screen, and handles events)--

.. literalinclude:: ref/code_examples/base_script.py

Here is a slightly more fleshed out example, which shows you how to move something
(a circle in this case) around on screen--

.. literalinclude:: ref/code_examples/base_script_example.py

For more in depth reference, check out the :ref:`tutorials-reference-label`
section below, check out a video tutorial (`I'm a fan of this one
<https://www.youtube.com/watch?v=AY9MnQ4x3zk>`_), or reference the API
documentation by module.

Experimental modules
--------------------

Experimental modules are work in progress, this is why you should refrain from relying on any features
provided by these modules, as they are subject to change or removal without prior notice.
If you want to test these experimental modules, you might want to understand how you import
them, this is how you can do it:

.. code-block:: python

  from pygame import experimental_module
  # Or for specific modules like _sdl2.controller
  from pygame._sdl2 import controller
  # Or
  import pygame.experimental_module

Don't forget to report us any problem with the experimental features on `github`_ so we can easily
turn them to stable API in the future ^^.

**Below is currently the list of experimental modules :**

:doc:`ref/geometry`
  Pygame module for the Circle, Line, and Polygon objects.

:doc:`ref/sdl2_controller`
  Pygame module to work with controllers.

:doc:`ref/sdl2_video`
  Pygame module for porting new SDL video systems.

.. _github: https://github.com/pygame-community/pygame-ce

Documents
---------

`Readme`_
  Basic information about pygame: what it is, who is involved, and where to find it.

:doc:`filepaths`
  How pygame handles file system paths.

:doc:`Pygame Logos <logos>`
   The logos of Pygame in different resolutions.


`LGPL License`_
  This is the license pygame is distributed under.
  It provides for pygame to be distributed with open source and commercial software.
  Generally, if pygame is not changed, it can be used with any type of program.

.. _tutorials-reference-label:

Tutorials
---------

:doc:`Introduction to Pygame <tutorials/en/intro-to-pygame>`
  An introduction to the basics of pygame.
  This is written for users of Python and appeared in volume two of the Py magazine.

:doc:`Import and Initialize <tutorials/en/import-init>`
  The beginning steps on importing and initializing pygame.
  The pygame package is made of several modules.
  Some modules are not included on all platforms.

:doc:`How do I move an Image? <tutorials/en/move-it>`
  A basic tutorial that covers the concepts behind 2D computer animation.
  Information about drawing and clearing objects to make them appear animated.

:doc:`Chimp Tutorial, Line by Line <tutorials/en/chimp-explanation>`
  The pygame examples include a simple program with an interactive fist and a chimpanzee.
  This was inspired by the annoying flash banner of the early 2000s.
  This tutorial examines every line of code used in the example.

:doc:`Sprite Module Introduction <tutorials/en/intro-to-sprites>`
  Pygame includes a higher level sprite module to help organize games.
  The sprite module includes several classes that help manage details found in almost all games types.
  The Sprite classes are a bit more advanced than the regular pygame modules,
  and need more understanding to be properly used.

:doc:`Surfarray Introduction <tutorials/en/intro-to-surfarray>`
  Pygame used the NumPy python module to allow efficient per pixel effects on images.
  Using the surface arrays is an advanced feature that allows custom effects and filters.
  This also examines some of the simple effects from the pygame example, arraydemo.py.

:doc:`Camera Module Introduction <tutorials/en/intro-to-camera>`
  Pygame, as of 1.9, has a camera module that allows you to capture images,
  watch live streams, and do some basic computer vision.
  This tutorial covers those use cases.

:doc:`Newbie Guide <tutorials/en/newbie-guide>`
  A list of thirteen helpful tips for people to get comfortable using pygame.

:doc:`Making Games Tutorial <tutorials/en/make-games>`
  A large tutorial that covers the bigger topics needed to create an entire game.

:doc:`Display Modes <tutorials/en/display-modes>`
  Getting a display surface for the screen.

:doc:`한국어 튜토리얼 (Korean Tutorial) <tutorials/ko/빨간블록 검은블록/개요>`
  빨간블록 검은블록

:doc:`Tutorial de Pygame - Ejemplo del Chimpancé, Línea Por Línea <tutorials/es/ChimpanceLineaporLinea>`
  Los ejemplos de pygame incluyen un sencillo programa con un puño interactivo y un chimpancé.
  Está inspirado en el molesto banner de flash de principios de la década de 2000.
  Este tutorial examina cada línea de código utilizada en el ejemplo.

:doc:`What is Premultiplied Alpha? <tutorials/en/premultiplied-alpha>`
  An explanation of alpha compositing and the advantages of using premultipled alpha.


Reference
---------

:ref:`genindex`
  A list of all functions, classes, and methods in the pygame package.

:doc:`ref/bufferproxy`
  An array protocol view of surface pixels

:doc:`ref/color`
  Color representation.

:doc:`ref/cursors`
  Loading and compiling cursor images.

:doc:`ref/display`
  Configure the display surface.

:doc:`ref/draw`
  Drawing simple shapes like lines and ellipses to surfaces.

:doc:`ref/event`
  Manage the incoming events from various input devices and the windowing platform.

:doc:`ref/examples`
  Various programs demonstrating the use of individual pygame modules.

:doc:`ref/font`
  Loading and rendering TrueType fonts.

:doc:`ref/freetype`
  Enhanced pygame module for loading and rendering font faces.

:doc:`ref/gfxdraw`
  Anti-aliasing draw functions.

:doc:`ref/image`
  Loading, saving, and transferring of surfaces.

:doc:`ref/joystick`
  Manage the joystick devices.

:doc:`ref/key`
  Manage the keyboard device.

:doc:`ref/locals`
  Pygame constants.

:doc:`ref/mixer`
  Load and play sounds

:doc:`ref/mouse`
  Manage the mouse device and display.

:doc:`ref/music`
  Play streaming music tracks.

:doc:`ref/pygame`
  Top level functions to manage pygame.

:doc:`ref/pixelarray`
  Manipulate image pixel data.

:doc:`ref/rect`
  Flexible container for a rectangle.

:doc:`ref/scrap`
  Native clipboard access.

:doc:`ref/sndarray`
  Manipulate sound sample data.

:doc:`ref/sprite`
  Higher level objects to represent game images.

:doc:`ref/surface`
  Objects for images and the screen.

:doc:`ref/surfarray`
  Manipulate image pixel data.

:doc:`ref/tests`
  Test pygame.

:doc:`ref/time`
  Manage timing and framerate.

:doc:`ref/transform`
  Resize and move images.

:doc:`ref/typing`
  Provide common typehints

:doc:`ref/window`
  Pygame object that handles a window.

:doc:`pygame C API <c_api>`
  The C api shared amongst pygame extension modules.

:ref:`search`
  Search pygame documents by keyword.

.. _Readme: https://github.com/pygame-community/pygame-ce#readme

.. _LGPL License: LGPL.txt
