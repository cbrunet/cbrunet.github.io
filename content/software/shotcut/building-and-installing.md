title: Installing and Building Shotcut on Arch Linux
status: draft
lang: en


# Choosing the right software

I recently needed a video editing software, for a little project. 
Therefore, I looked at what was currently available on the Linux world.
I quickly eliminated *DaVinci Resolve* and *Lightworks*, because they are
proprietary softwares, limited in their free version. I don't want to
be limited in features, and I don't like installing a closed source software on
Linux. I saw many comments telling that *Blender* was the best open source
option on Linux. But using a 3D modeler for video editing sounds odd to me,
and my experience with Blender is that it has a steep learning curve. I
wanted something more conventional.

*OpenShot* was appealing, because it is written in Python.
But it seemed a little slow on my old computer.
And the interface seems a little too simplist for me.
For instance, when you insert text, you need to choose a predefined text layouts,
where you can adjuste the text itself and the color.
In fact, you can customize it further, but you need to use a svg editor like InkScape.
The software seems a very simple facade, but includes some very technical details,
in the properties window for instance. What I definitively like is
the possibility to add transitions between two different video tracks.
I still keep an eye on this software, but it is devinitively not my first choice for now.

I also gave a quick try to *Kdenlive*, but I definitively found the interface too bloated.
I doesn't allow in-track transitions: you always need to perform transitions between
two different tracks.

I successfully created some videos using *Shotcut*. 
It seemed more stable and faster than other video editors, and it has all the basic
features I needed. However, it is still in active development, and some features are missing
(like the ability to change the track order).


# Installation on Arch Linux

An up-to-date package is available: [shotcut](https://www.archlinux.org/packages/community/x86_64/shotcut/).
It is based on Qt, and on the MLT framework (in fact, the Shotcut developer is one of the MLT developers).

The software is translated in many languages. I was surprised to see that some translations were missing for very
basic commands (like Undo / Redo), until I realised I needed the
[qt5-translations](https://www.archlinux.org/packages/extra/any/qt5-translations/) package.

I also realized many filters were missing. Digging further, I found that the missing filters
were all the filters based on the *webvfx* library. Unfortunately, this lib was not available on Arch Linux.
Therefore, I packaged it on AUR: [webvfx](https://aur.archlinux.org/packages/webvfx/).
I also [filled a bug](https://bugs.archlinux.org/task/66654)
to the shotcut package maintainer on Arch, to see if he would include it in the future.



# Building from source

Buiding from sources is not complicated, since all needed dependencies were already installed
by the shotcut package. The Arch package has one patch, to replace the *qmelt* executable by
the *melt* executable. *melt* is a command line tool to interface the *MLT* library. It is
included in the *mlt* package. *qmelt* is a simple Qt wrapper for *melt*. As I understand,
it is needed on Mac OS and on Windows, but not on Linux. *qmelt* is provided by *webvfx*.
This is why it is not there with the original shotcut package.

    :::bash
    $ git clone https://github.com/mltframework/shotcut.git
    $ cd shotcut
    $ mkdir build
    $ cd build
    $ qmake ..
    $ make

The README file says the simplest way to run the compiled version is to directly
call `./src/shotcut`. However, I realised I first needed to symlink the qml files:

    :::bash
    $ cd share/shotcut
    $ ln -s ../../../src/qml
    $ cd -
    $ ./src/shotcut



