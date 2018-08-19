# Hypnotic Spiral 2.0
Copyright (C) 2006, 2007 by Yonah Arakoslav

## New in this version

Recording with an iSight (Mac only)
Much better speech synthesis (Mac only)

Several new scripts

## Introduction

A few years ago, the hypno-fetish artiste known as William Lee wrote a
program called SlaveMaker.  It was a flexible hypnosis toolkit---and
quite a blast.  I've been using it on and off over the years since
with great effect.  I've enjoyed using it with and on partners.
Unfortunately, SlaveMaker has a few flaws:

 * It's expired.  WLee built in a timing device to discourage use of
   old copies and eventually help him sell the program to Jane Caine
   as the "Erotic Inducer"

 * It's Shockwave Flash.  That and the way its loops are written mean
   it takes a *lot* of processor.  My fan spins up every time I run
   it.

   This also means that it's somewhat less flexible than I'd like.

And since it's not free software, I can't really fix any of this.  So
thank you, William Lee, for inspiring me to write something entirely
new.  You did fantastic work.  I do hope that you yourself find some
use from this program.

A decade before that, an anonymous author posted a story to
alt.sex.stories.  It opened my eyes to what erotica could be like.  I
believe it established the hypnofetish genre.  Though my tastes since
have run more to Tabico and trilby else, this story first got me
looking in this direction.  I'm grateful to that original author, and
to Tabico and trilby, for their work.

## Using the program

The program is made to be very easy to use.  It should be able to get
out of your way and get its job done.

### Installation

This program is written in a language called Python, and heavily uses
a library for Python called PyGame.  To use this program, you'll have
to install both of them.  You can get Python from
<http://www.python.org/download/> and PyGame from
<http://www.pygame.org/download.shtml>.  If you're on a reasonable
Linux system, you can probably just install both through your package
manager.  On a Mac, there are nice pre-packaged installers.  On
Windows, you're on your own.

If you're on a Mac *AND* you want the video-recording feature, you'll have to install Quicktime Broadcaster.  It's free from Apple at 
<http://www.apple.com/quicktime/broadcaster/>.
If not, don't worry about it.

You will also need media.  Put pictures in the "images" directory.  I
haven't included any pictures partly because they're huge, and partly
because they're not mine to give away.  I've got a 40 MB bundle with
image manipulations by Haywaine, Tabico, WLee, nightcrawler... but
don't feel right sending around copies without their permission.

You can replace the included MP3 files if you like.  In fact, you'll
have to!  To cut down on size, I don't ship any MP3s.

After that, you can just run spiral.py:

> python spiral.py

If you make it executable, Windows or Mac machines should be able to
just double-click it:

> chmod a+x spiral.py

If you are on a Mac, you can use speaker.py instead.  It has much better speech
synthesis than the spiral.py code.  It uses a different configuration file,
configSpeaker.py.

### Usage

The program may prompt you with information you must acknowledge to
proceed.  Read it and just hit return.

It may ask you questions, requiring either yes/no or short text
answers.  You can press "y" or "n" to answer the simple questions, or
just type an answer to later questions.  It *should* handle non-ASCII
characters properly, but I don't use that often and so haven't tested
it as much.

While it's running, you can press single keys to change some
behavior.  "<" or ">" will adjust the speed, as will their unshifted
equivalents "," or ".".  "f" will toggle fullscreen mode, and "i" will
toggle the background images.  "q" will quit the program.

The program can do those things on its own, too---sometimes a script
will cause it to go full-screen on its own, or to start showing you
pictures.

## Extending the program: writing scripts

I've included a number of example scripts in "config.py".  This should
make it easy to see what you can do.  There are a couple of points
worth mentioning:

You don't have to subclass Standard; it just catches you if you screw
up.  The top of config.py has utility functions.  You don't have to
use those either, though they can make things easier.  You should see
most of them used in the body of the work.

Running text is separated by any white space; the "words" helper
function turns words("foo bar baz") into ["foo", "bar", "baz"].
Nothing stops you from including spaces in words to display---I just
find whitespace works well as a separator.

Variables always start with "$" when used, and don't have the "$" when
you're assigning to them.  I don't guarantee you can pull off
double-substitution tricks like replacing $$role with Alice, where
$role=slave and $slave=Alice.  That particular version will work, but
only by accident.

Any string starting with ! will be interpreted as a command; see
Spiral.act_on for the evaluator.  It's pretty cruddy, but it does work
for this purpose.  Sometimes you'll want to make sure evaluation is
delayed until run-time.  For example, you don't care about whether the
music is playing when you *start* the program, but you'd like to check
whether it's on at this particular moment in the course of the run.
Put this material in quotes; it'll be evaluated at run-time.
You can see this in Standard:

        cond("self.draw_image",
             words("Turn on the pictures.  Hit the 'i' key.")) + \
             words("""You lust for the pictures. $name will be like the
             pictures. This turns you both on. You need the changes. You
             lust for the changes. $name will be changed. This is sexy. It
             would feel so good just to surrender to it.""") + \
        cond("not self.config.fullscreen",
             words("Feel so good to go fullscreen.  Hit 'f'."),
             words("So good to be fullscreen.  So good to be immersed.")) + \

If there were no quotes around self.draw_image, it would be checked
when the program started---no good at all.

The "alpha" values are for transparency.  "scale" adjusts the size of
the spiral, and "time_scale" the number of ticks that pass per frame.
"frequencies" controls how many ticks must pass before the spiral,
text, or images advance.  At the default setting, the spiral advances
every tick, the images every 10 ticks (5 frames because time_scale is
2), and the words every 20 ticks (10 frames).

Each config script will start with its "text()" method.  That's the
one thing you must override; the other names like "body()" are just
my convention.

Experiment!  Try new things and let me hear about them!


## Extending the program: new modules

Right now, it's hard to add new things like subliminal text or a
"click me if you're not my mindfucked little hypnoslave" button that
goes away on its own.  I'd like to make it easier, but so far you're
pretty much on your own.

## My to-do list

I know there's more to do.  My progress with this program is driven by
my own desires.  I'm willing to entertain requests, but rather
unlikely to implement them---think of them as attempts at
inspiration.  If I'm inspired, I'll implement a requested feature.  If
not, I suggest *you* implement it and send a patch my way.  I'm very
likely to accept patches, integrate them, and redistribute them to the
community.

My own notes on what to do are at the top of the spiral.py file.

## About the Author

Yonah Arakoslav is a none-too-clever pseudonym.  I'm sure that with a
little work, you can figure out who I really am.  That's OK.  I just
don't want search engines fingering me.
