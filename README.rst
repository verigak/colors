ANSI colors for Python
======================

A simple module to add ANSI colors and decorations to your strings.

Example Usage
-------------

You can choose one of the 8 basic ANSI colors: black, red, green, yellow, blue,
magenta, cyan, white.

::

    from colors import red, green, blue
    print red('This is red')
    print green('This is green')
    print blue('This is blue')

Optionally you can specify a background color.

::

    print red('red on blue', bg='blue')
    print green('green on black', bg='black')

You can additionally specify one of the supported styles: bold, faint, italic,
underline, blink, blink2, negative, concealed, crossed. Not all styles are
supported by all terminals.

::

    from colors import bold, underline
    print bold('This is bold')
    print underline('underline red on blue', fg='red', bg='blue')
    print green('bold green on black', bg='black', style='bold')

You can also use more than one styles at once.

::

    print red('This is very important', style='bold+underline')

xterm-256 colors are supported as well, to use them give an integer instead of
a color name.

::

    from colors import color
    for i in range(256):
        print color('Color #%d' % i, fg=i)


License
-------

colors is licensed under the ISC license.
