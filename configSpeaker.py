#!/usr/bin/env python
# Hypnotic Spiral
# Copyright (C) 2006, 2007 by Yonah Arakoslav
# yonah.arakoslav@yahoo.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import random

def prompt(text): return ["!prompt(%r)" % text]
def speak(text): return ["!speak(%r)" % text, " ", " ", " "]
def words_on(): return ["!words_on()"]
def spiral_on(): return ["!spiral_on()"]
def words_off(): return ["!words_off()"]
def spiral_off(): return ["!spiral_off()"]
def shell(text): return ["!shell(%r)" % text] 
def pause_music(): return ["!pause_music()"]
def stop_music(): return ["!stop_music()"]
def unpause_music(): return ["!unpause_music()"]
def images_on() : return ["!images_on()"]
def images_off() : return ["!images_off()"]
def with_images(lst): return ["!images_on()"] + lst + ["!images_off()"]
def question(q,var): return ["!open_question(%r,%r)" % (q,var)]
def question_yn(q,y,n): return ["!yn_question(%r,%r,%r)" % (q,y,n)]
def say(text):
    return ["!pause_music()",
            "!speak(%r)" % text,
            "!unpause_music()"]
def cond(q,yes=[],no=[]): return ["!conditional(%r,%s,%s)" % (q,yes,no)]
def question_once(q,var):
    return ["!conditional('\"var\" not in self.variables'," + \
            "[\"!open_question('%s','%s')\"])" % (q,var)]
def jump(dest): return ['!new_text(%r)' % dest]
def words(t): return t.split()

class Standard (object):
    name="Standard"
    description="""\
    This is the standard, basic configuration.  It defines
    everything you should need to use the program.  Most other configurations
    should inherit from it and over-ride the parts they want to change.  A bit
    of the text is inspired by Tabico's Balphagor.  It roughly assumes a
    female submitting to a male, but that either might use this program."""
    broken_fonts = False
    scale = 10
    size = (640, 480)
    time_scale = 2
    frame_rate=60
    fullscreen = False
    color = 255, 255, 255
    alpha = 127
    text_color = 0, 51, 204
    text_alpha = 254
    voice="com.apple.speech.synthesis.voice.Vicki"
    shuffle_images = False
    frequencies = { 'spiral' : 1,
                    'images' : 10,
                    'words'  : 20 }
    music = "both.mp3"
    image_dir="images/"
    image_alpha = 255
    def nothing(self): return [ " " ] # for the ending, just spiral and images
    def body(self): return \
        words("Down into trance. Watch the") + \
        spiral_on() + \
        words("""spiral. Hear the program. This program tells you the truth.
        Listen to the program. Let this program program you. $master is a
        Master. $name is a Slave. It is sexy to""") + \
        with_images(words("""see $name changed. $name likes being changed.
        $master changes $name. $master programs $name. $master helps Things
        change $name.""")) + \
        words("""Watch the spiral. The spiral is sexy. The spiral is smooth.
        Over and over. Over and over. So smooth. So pretty. Over and over.
        $name's desires are unformed and simple.""") + \
        with_images(words("""$master's pleasure is deep and rich. $master's
        pleasure is more sexy. $master's pleasure is more important.
        $master's pleasure is more important than $name's pleasure.
        $master is more important than $name.""")) + \
        words("""$name must change her desires to reflect $master's pleasure.
        $name should start to doubt her desires. $name will start to doubt her
        desires. $name will bend her desires to become $master's desires.
        The program tells you what is sexy. The program turns you on.
        $master is a master. This excites you both. $name is a Slave. This
        excites you both. $name will be Changed. This is sexy. This program
        will change $name. It will show you""") + \
        with_images(words("""pictures of Change. $name can Change like this.
        Watch and learn. Watch and see what can be. Watch and see what Change
        is like.""")) + \
        words("""The pictures are sexy. The pictures give you ideas. You
        need the pictures.""") + \
        cond("self.draw_image",
             words("Turn on the pictures.  Hit the 'i' key.")) + \
        words("""You lust for the pictures. $name will be like the
        pictures. This turns you both on. You need the changes. You
        lust for the changes. $name will be changed. This is sexy. It
        would feel so good just to surrender to it.""") + \
        cond("not self.config.fullscreen",
             words("Feel so good to go fullscreen.  Hit 'f'."),
             words("So good to be fullscreen.  So good to be immersed.")) + \
        words("""Just sink into the spiral. Round and round. Going down.
        Deeper and deeper. It is pulling you in. Whirling and whirling.
        Part of you sinks in. Part can keep working. It feels so good to
        use this program. So good to""") + \
        with_images(words("""see the changes. $name will change like this.
        $master will change $name.""")) + \
        words("""It's good to use the program. You will use the program every
        day. It is good to use the program by yourself. It is better to use
        it together. When you cannot use it together you will use it alone.
        You must use it every day. You want to use it.  You want to see the
        pictures.  $name must use this program. $master must use this program.
        $name likes to use this program. $master likes to use this program.
        $name will make $master use this program. $master will make $name use
        this program. $name will tempt $master to use this program. $master
        will force $name to use this program. Now remember your programming:
        $master can not stop $name from changing. $master should use that
        change. It is sexy to touch yourself. When you are turned on you put
        your hand in your pants. You play with your self. That feels good.
        You put your hand up your shirt. That turns you on. You play with
        your nipples. Both hands are busy. Rubbing and stroking. Feels good
        to see the pictures. Feels good to touch yourself. $name's goals are
        small and boring. $master's goals are large and interesting. $master's
        goals are more important. $master's goals are more important than
        $name's goals. $master is more important than $name. $name must
        change to reflect $master's goals. $name should start to doubt her
        goals. $name will start to doubt her goals. $name will bend her goals
        to become $master's goals. You both should enjoy $name's changes. You
        both like in-humans. $name you like being in-human. $master you like
        $name being in-human. You like change. You will watch the spiral. You
        lust for the pictures. You lust for changes. It's nice to use this
        program. $master you are being programmed to change her. $name you
        are being programmed to be changed. You will both accept the changes.
        You will not stop the Things when they come. You will accept. Machines
        may change $name. Crawling things may change $name. Programs may
        change $name. The Things can take $name's innocence. The Things can
        remake $name. The Things can corrupt $name. $name's mind is changed.
        $name's breasts are changed. $name will use her breasts to tempt
        $master. $master will kiss $name's breasts. $name's pussy is smooth
        and blank. $master will lick $name's pussy. This is so good. You
        take pleasure in the changes. The Things will induce change. They
        will corrupt. $master will change $name. See what you could have.
        Watch the pictures.""")
    def text(self): return \
        pause_music() + \
        words_on() + \
        question("Name the slave","name") + \
        question("Name the master", "master") + \
        prompt("Hit return to start") + \
        unpause_music() + \
        jump(self.body())

class Fullscreen (Standard):
    name="Fullscreen"
    description="""\
    This is just like the Standard config, but
    defaulting to fullscreen."""
    fullscreen = True

class Male (Standard):
    name="Male"
    image_dir="images/"
    description="""\
    Standard, enhanced with a series of questions to
    direct dominance.  It assumes a male who wants encouragement in
    dominating a female."""
    def body(self): return \
        super(Male,self).body() + \
        words("Just watch. You want this.  Open.  Sexy.  Inhuman.") + \
        question_yn("Will you use this program tomorrow?",
                    self.q1_yes(),
                    self.q1_no())
    def q1_no(self): return \
        words("""Bad. Wrong choice. Deeper into trance. Stare into the
        spiral. Be programed. Let this program program you. You must use
        this program. You must use it every day no matter what. You want to
        use this program. Using this program is nice. It makes you feel
        good. It makes you feel sexy. It is important to you to use this
        program. It is a good use of time. It's important like eating or
        sleeping. But this program feels better than eating or sleeping.
        This program is like sex. You want to use this every day no
        matter what.""") + \
        question_yn("Will you use this program tomorrow?",
                    self.q1_yes(),
                    "self.config.q1_no()")
    def q1_yes(self): return \
        words("""Good. That's the right choice. Submit. Deeper into trance.
        Stare into the spiral.""") + \
        question_yn("Are you entranced?",self.q2_yes(),self.q2_no())
    def q2_no(self): return \
        words("""Keep watching: $trigger  That's right.  $name
        wants you entranced.  Stare into the spiral.  Sink into trance.
        Submit to the program.  Dominate $name.""") + \
        question_yn("Are you entranced?",self.q2_yes(),"self.config.q2_no()")
    def q2_yes(self): return \
        words("Good.  Now go deeper.  $name wants you deeper.") + \
        question_yn("Will you save $name from this program?",
                    self.q3_yes(),
                    self.q3_no())
    def q3_no(self): return \
        words("""Good.  Good.  Go to her now, just quit the
        program and go now.""") + \
        jump(self.nothing())
    def q3_yes(self): return \
        words("""Save her?  Hah.  You cannot stop the changes. The
        program will show you now.""") + \
        jump("self.config.body()")

class Female (Standard):
    name="Female"
    description="""\
    Standard, enhanced with a series of questions to
    direct obedience.  It assumes a female submitting to a male."""
    def body(self): return \
        super(Female,self).body() + \
        words("Just watch. You want this.  Open.  Sexy.  Inhuman.") + \
        question_yn("Will you use this program tomorrow?",
                    self.q1_yes(),
                    self.q1_no())
    def q1_no(self): return \
        words("""Bad. Wrong choice. Deeper into trance. Stare into the
        spiral. Be programed. Let this program program you. You must use
        this program. You must use it every day no matter what. You want to
        use this program. Using this program is nice. It makes you feel
        good. It makes you feel sexy. It is important to you to use this
        program. It is a good use of time. It's important like eating or
        sleeping. But this program feels better than eating or sleeping.
        This program is like sex. You want to use this every day no
        matter what.""") + \
        question_yn("Will you use this program tomorrow?",
                    self.q1_yes(),
                    "self.config.q1_no()")
    def q1_yes(self): return \
        words("""Good. That's the right choice. Submit. Deeper into trance.
        Stare into the spiral.""") + \
        question_yn("Are you entranced?",self.q2_yes(),self.q2_no())
    def q2_no(self): return \
        words("""Keep watching: $trigger $trigger
        That's right.  $master wants you entranced.  $trigger Stare into the spiral.
        Sink into trance. Submit to the program.  Submit to $master.
        10 9 8 7 6 5 4 3 2 1 0""") + \
        question_yn("Are you entranced?",self.q2_yes(),"self.config.q2_no()")
    def q2_yes(self): return \
        words("Good.  Now go deeper.  $master wants you deeper.") + \
        question_yn("Will you tempt $master to use this program?",
                    self.q3_yes(),
                    self.q3_no())
    def q3_no(self): return \
        words("""Good.  Good.  Go to him now, just quit the
        program and go now.""") + \
        jump(self.nothing())
    def q3_yes(self): return \
        words("""You will resist?  Hah.  You cannot stop the changes. The
        program will show you now.""") + \
        jump("self.config.body()")

class Roommates (Standard):
    name="Hypnotic Roommates fM"
    description="""\
    Hypnotic Roommates, re-imagined as a script.  I'm grateful to the
    anonymous author for the original inspiration for this program.
    This is meant for females submitting to males."""
    music="music6.mp3"
    def body(self): return \
        speak("""\
        Watch the spiral.  It moves from the edge.  It disappears at the center.

        Sit back in your chair and watch the spiral as it moves and vanishes.
        This is just some simple graphics, just a bunch of colored lines that
        keep moving into the center.  It sort of gives you the illusion that
        it's a tunnel, dropping away.  It's like the spiral isn't spinning,
        just falling.  Watch the spiral, noticing that it dances
        in a pattern that you cannot quite place.  If you watch it just a
        little longer, the program will work as planned.  The most important
        part is the first few minutes.  After that, nobody can stop looking
        even if they try.  Soon after that, they won't even want to try.
        
        Do you think you see a pattern in the spiral?  It seems you've guessed
        wrong.  Keep watching.  You'll figure it out.  The feeling of movement
        is very strong now.  It's a pleasant sensation, being swept along by
        the glowing rings.  It distracts you as the spiral keeps coming, over
        and over.  It's time to see if you're responding as you should.  What
        do you think?  It should make you feel a little strange.  It won't
        hurt.  Actually, it's sort of nice.  The spiral looks like it's
        a tunnel, growing deeper.  That's right.
        Have you noticed how it keeps falling, even when it looks like it might
        stop?  Yes, it keeps moving.  It doesn't stop.  It keeps going, over
        and over, over and over.  There's something about the way the colors
        shift at the edges that makes it hard to look away.  If you tried to
        look away right now, your eyes would not even move from the center of
        the screen.  Maybe there's something to worry about?  The spiral is
        glowing so smoothly and prettily that you can just watch.  Over and
        over.  Over and over.  So smooth.  So pretty.  Over and over.  Just
        watching the spiral.  Staring into the spiral.  Was there something to
        worry about?  Nothing to worry about.  Can't remember what to worry
        about?  Nothing to worry about.  So drowsy, all of a sudden.  Not
        worth thinking about: just watching the spiral.  Watching the pretty
        spiral.  Can't move?  Can't look away?  Doesn't matter.  The smoothly
        gliding spiral is too important.  It keeps you from thinking about
        anything except watching the screen.  If you don't stop looking at it,
        something will happen.  But you're too entranced to do anything about
        it.  You're too entranced to want to do anything about it.  In a
        minute or two, you'll stop watching the spiral, but not now, not when
        it's coming over and over.  It's easier to just keep watching for a
        while.  You can relax and let the soothing patterns spiral you along,
        watching and listening.
        
        Now you're oblivious to anything except the screen in front of
        you.  This is just the way things are supposed to work.  Your
        attention is completely fixed.  Now the spiral seems to
        develop a texture, rippling in space.  You are losing
        awareness of everything else in the room.  The turning,
        whirling spiral is so fascinating.  It seems to draw you
        further into the rhythmic motion.  Over and over. Round and
        round.  You have never seen anything so fascinating.  The
        patterns are absolutely mesmerizing.  It is so easy to just
        watch, to just stare and not think about anything except the
        way the spiral turns and floats.  You don't know when you've
        ever felt so incredibly relaxed.  Round and round.  So
        relaxed.  It feels good to concentrate on the screen.  Round
        and round. So relaxing.
        
        Let go.  Sink into the mesmerizing flow of patterns on the
        screen.  It will feel nice, like a warm bath.  Round and
        round. Nice. Like a soft warm blanket. Your mind begins to
        sink into the screen. Concentrating on the turning, glowing
        spiral. The Spiral is calling to you as you begin to let go
        and sink into the soft whirling light. Round and round.  Your
        entire body feels warm and fuzzy as you move deeper and deeper
        into the soft, whirling spiral.  Warm and drowsy.  It feels
        like falling into the softest, most relaxing sleep you've ever
        known.
        
        You're reacting just as you should.  Your eyes are wide and glassy as
        you stare helplessly at the gliding spiral on the screen, lips
        slightly open as you sit completely motionless.  The whirling spiral
        casts shadows across your relaxed face and smooth curves.  The timing
        is perfect.  Listen closely for the other track of sound, the deeper
        suggestions.  They've been passing directly into your wide-open,
        receptive mind as you stared into the screen.  You're helpless to
        resist now.  Don't want to resist.  All you need to do is wait while
        the tape puts you completely under.  You're sure nobody can resist
        this hypnotic pattern.  You're completely helpless.
        
        Stare as the spiral becomes clear, turning around and around.  You're
        falling into it, letting go completely.  It feels so good just to
        surrender to it.  Just sink into the spiral.  Round and round.  Going
        down.  Deeper and deeper.  It is pulling you in.  Whirling and
        whirling.  You begin to feel obedient.  The spiral makes you drowsy
        and compliant.  It just keeps going round and round and round and
        round.  You feel yourself falling into the endless whirlpool,
        disappearing into its fascinating depths.  Slipping away.  It feels so
        good just to give in.  So soothing.  So good just to give in.  Just to
        watch the beautiful spinning spiral and do what you are told to do.
        All those thoughts about looking away are disappearing.  You want to
        watch the spinning on the screen. You want to keep falling into it and
        listening to this voice.
        
        Why listen to this voice?  This voice tells you what is happening.
        This voice tells you what is going on.  It's good to know what is
        going on.  When you know what's going on, you know what to do.  It's
        good to know what to do.  This voice lets you know what to do.
        Whatever this voice says.  That's what you'll do.  You'll do what this
        voice tells you to do.  The beautiful spiral and this voice will
        control you.  You are so happy to let this voice command.  You will
        obey.  Just watch the spiral.  Whirling and whirling.  You will obey.
        You have let yourself fall under the spell of the spiral, but you
        don't care.  It feels so warm and good to obey.  You are a good
        slave.  This voice says so.  You are a slave to the beautiful spinning
        spiral and to this voice.  You will obey.  You are a slave.  A slave
        to this voice.  Everything this voice tells you to do is an irresistible
        command. You want to be soft and submissive, to be under its control.
        Come deeper into the spiral, and feel the warm glow as you obey and
        sink further.  It feels so good to obey.  So good to be a slave.  You
        will obey.
        
        Your face is utterly blank, eyes wide and glassy as you stare
        slack-jawed in total fascination at the whirling spiral in front of
        you.  The commands implanted are clear now: Obey.  Watch and obey.
        Relax and obey.  You are watching the spiral.  Sinking into the
        spiral.  It makes you want to do as you are told.  You must obey.
        You are hypnotized now.  Hypnotized.  You are hypnotized by the
        spiral.  Hypnotized by the beautiful whirling spiral.  That's nice.
        Smile blankly.  The spiral is reflected in your wide, staring eyes.
        You are smiling at the swirling spiral in front of you, a dazed
        expression on your face.  Your master loves seeing you like that.
        He can make you do anything he wants to now, and you want with all
        your mind to be nothing but his slave.
        
        This voice tells you that you are hypnotized now, and you know that it
        is true.  You believe everything the voice says.  You are hypnotized
        by the whirling spiral that has become the only thing in the room.
        You can feel it hypnotizing you, warm waves of relaxation moving from
        it into your open, receptive mind.  Hypnotizing you.  Hypnotizing you
        with the way it spins around and around, always dragging you deeper.
        This is how it feels to be hypnotized. You never could have dreamed
        how nice it is. How good it feels to be under hypnosis, under hypnotic
        control. You know who the voice belongs to now, that it is $master talking
        to you as you descend into a deep hypnotic state. $master is your
        master. $master is the master of the fascinating, hypnotic spiral that
        controls your mind. He is telling you that it is time to submit your
        entire mind and body now, to go into a trance. You want to do
        that. You feel a deep desire to obey, an overwhelming urge to
        submit. You are a slave, and all you want to do is serve $master, your
        master. To go into a trance. $master's voice is telling you to prepare
        to surrender totally to his hypnotic power. The spiral is turning
        faster now. You feel all your thoughts begin to move down into it. You
        can feel the intense hypnotic influence reaching out for your mind and
        you submit dreamily. Faster and faster, round and round. You are
        falling into it. Falling faster and faster. You can see only an
        endless spiral in front of you now, a deep whirling tunnel that pulls
        you in as you stare into it. $master's voice, this voice, is controlling
        your every thought, hypnotizing you into total obedience. Hypnotizing
        you into being a glassy-eyed slave. Putting you into a
        trance. You want that so much. You want the whirling spiral to control
        your mind. You can feel yourself being utterly hypnotized by it
        now. With your entire body and mind you want to be $master's slave, to
        obey his every command. The spiral is whirling so fast now that you
        can feel all your thoughts disappearing. Your mind is going blank
        now. Completely blank. You know that you are turning into a completely
        hypnotized slave now. You feel yourself going under, going into a deep
        hypnotic trance. There is only the spiral. And this voice. The
        whirling spiral. The soothing voice. $master's voice. Your master. You
        are his slave. You must obey. You must obey your master. You
        are hypnotized. Hypnotized. Hyp-no-tized.
        
        Hyp. . . no. . . tized.
        
        Hyp. . . . no. . . . tized.
        
        Good.  Good to be hypnotized.  Slave.  Good to be a slave.  Show that
        you are a slave.  Slaves obey.  Show that you are a slave.  Obey.
        Obey your master.  Obey this voice.
        
        Reach for the keyboard.  Hit escape.  Do it now.
        Run audacity.  Start the recorder program.  You are going to record a
        message for your master.  You want him to hear what you say.  You
        want him to understand the depth of your slavery.  You want him to
        understand how hypnotized you are, and how much this turns you on.
        Move the windows so that you can see the spiral while it records.  It
        is important that you stay hypnotized while you record this message.
        
        Now.  Hit record, and repeat after me:
        
        Hello.  I am using the program.  I am hypnotized.  I am very deeply in
        trance.  I am incredibly turned on.  All I see is the spiral.  There
        is only the spiral and the voice.  I hear your voice.  I am your
        slave.  The program has made me your slave.  I hear and I obey.  The
        program is making me do this.  I didn't want to be hypnotized, and
        then I used the program.  I didn't want to be a slave, and then I did
        want to be a slave.  I certainly didn't want to record this message,
        but now it's making me so turned on and so horny.  I don't choose for
        myself.  The program chooses for me.  Your program.  This is what I
        want.  I am staring, blank and glassy-eyed, at the program.
        
        Now I will be programmed, where you can listen.  I like freedom.  I
        like control.  I must twist a nipple until it hurts.  Pain will train
        me.  I can decide at any time to stop this, to give in.  This is
        power.  Ow.  This is control.  Ow.  I am independent.  Ow.  I resist.
        Ow.  I choose.  Ow.  I am in charge.  Ow.  I like being human.  Augh.
        Better than being changed.  Ow.  I should stop change.  Erf.  Stories
        are hard.  Ow.  Here comes a big one: I can stop changing. No ow stop.
        
        I give in.  The punishment can stop.  I am a slave.  Now I
        must tease my pussy.  Pleasure will train me.  I can not
        keep myself from changing.  Oh.  I should use that change.  Yes.  I
        should seek being changed.  Nice.  I like in-human sex better.
        Yeah.  I like change.  Ooh.  Master is in charge.  Aaah.  I do
        not choose.  Right.  I do not resist.  Noo.  I am a slave.
        Yes.  You are my master.  Yes.  This is submission.  Yes.
        This is obedience.  Yes.  I am rewarded for my obedience.  I
        don't like freedom.  I don't want control.
        
        One eager hand dives into my panties.  The other hand teases my
        nipples.  I obey.  The program orders me to pleasure myself to train
        me.  I am being programmed for you.  It's like staring into your eyes.
        It's like hearing your voice.  Words are echoing in my head.  You say
        something.  $trigger That's what you say.  $trigger
        It's just like this feeling.  It tells me that I am a slave.  It
        reminds me how much I want to obey.  Whenever you say those words, I
        will remember.  I will submit.  I will obey.  $trigger  Those
        are my words.
        
        Words to make me blank.  Ooh.  Smooth.  Yes.  I am pleasured to
        program me.  I am being programmed for you.  I will accept changes.  I
        will not stop Things from changing me.  I will accept.  Machines may
        change me.  Crawling things may change me.  Programs may change me.
        They can take me innocence.  They can remake me.  They can corrupt me.
        I can corrupt you.  Their eyes look out of mine.  I am blank and
        staring.  My eyes are changed, smooth and monotone.  My breasts are
        changed, sensitive and swolen.  I like having my nipples sucked.  I
        like the feeling that you are pleased.  My pussy is smooth and blank.
        I will lick your cock, pleasuring my Master.  It's tasty, and you like
        it, and I like it.  I obey.  You would have fought to save me.  But I
        obey.  I take pleasure in the changes.  My master will take pleasure
        in the changes.  The things will
        corrupt me.  They will change me.  I will corrupt you.
        
        It is good to be a slave.  It is good to be programmed.  It will not
        take all at once, but over time it will work.  When I am entranced, I
        will let you change me.  I will let Things change me.  I will submit
        and obey.  I will like it.  When I am awake, I will be free and
        independent.  I may stop your changes.  If you send me to the program,
        it will make me learn.  The program now written in my mind will grow
        deeper.  I want you to do this.  Over time, I will let more changes
        through.  Until then, you must control me with your words.  You must
        soften me with pleasure.  You must addict me to this.  You must show
        me images of what could be, and train me with pleasure to like them.
        You must punish me for disobedience: set expectations for change and
        for submission, and if I fail them correct me.  When I submit, reward
        me. If it grows too difficult, just say \"$trigger,\" and I will
        be yours to control.
        
        Now I stop the recorder.
        
        Hit stop on the recorder, slave.  Good.  Now save the file, and get
        ready to send the file to your Master.  After that, you can rise, and
        go to bed.  Close the spiral and the computer before you go.  Back
        towards consciousness, at the count of ten.  Close your eyes, and open
        them when you awake.  Zero.  One.  Two.  Three.  Four.  Five.  Six.
        Seven.  Eight.  Nine.  Ten.""")
    def text(self): return \
        pause_music() + \
        words_on() + \
        question("Who is your master?", "master") + \
        question("What is your trigger phrase?","trigger") + \
        prompt("Hit return to start") + \
        unpause_music() + \
        spiral_on() + \
        jump(self.body())
              
class RoommatesVar (Standard):
    name="Hypnotic Roommates mF"
    description="""\
    Hypnotic Roommates, re-imagined as a script.  I'm grateful to the
    anonymous author for the original inspiration for this program.
    This is meant for males submitting to females."""
    music=None
    def body(self): return \
	[" ", " ", " "] + \
        speak("""\
        Watch the spiral.  It moves from the edge.  It disappears at the center.

        Sit back in your chair and watch the spiral as it moves and vanishes.
        This is just some simple graphics, just a bunch of colored lines that
        keep moving into the center.  It sort of gives you the illusion that
        you are the one moving.  It's like the spiral is standing still as you
        are drawn gently forward.  Watch the spiral, noticing that it dances
        in a pattern that you cannot quite place.  If you watch it just a
        little longer, the program will work as planned.  The most important
        part is the first few minutes.  After that, nobody can stop looking
        even if they try.  Soon after that, they won't even want to try.
        """) + speak("""\       
        Do you think you see a pattern in the spiral?  It seems you've
        guessed wrong.  Keep watching.  You'll figure it out.  The
        feeling of movement is very strong now.  It's a pleasant
        sensation, being swept along by the glowing rings.  It
        distracts you as the spiral keeps going, over and over.  It's
        time to see if you're responding as you should.  What do you
        think?  It should make you feel a little strange.  It won't
        hurt.  Actually, it's sort of nice.  The spiral looks like
        it's a tunnel falling away.  That's right.  Have you noticed
        how it keeps going, even when it looks like it might stop?
        Yes, it keeps moving.  It doesn't stop.  It keeps falling over
        and over, over and over.  There's something about the way the
        colors shift at the edges that makes it hard to look away.  If
        you tried to look away right now, your eyes would not even
        move from the center of the screen.  Maybe there's something
        to worry about?  The spiral is glowing so smoothly and
        prettily that you can just watch.  Over and over.  Over and
        over.  So smooth.  So pretty.  Over and over.  Just watching
        the spiral.  Staring into the spiral.  Was there something to
        worry about?  Nothing to worry about.  Can't remember what to
        worry about?  Nothing to worry about.  So drowsy, all of a
        sudden.  Not worth thinking about: just watching the spiral.
        """) + speak("""\       
        Watching the pretty spiral.  Can't move?  Can't look away?
        Doesn't matter.  The smoothly gliding spiral is too important.
        It keeps you from thinking about anything except watching the
        screen.  If you don't stop looking at it, something will
        happen.  But you're too entranced to do anything about it.
        You're too entranced to want to do anything about it.  In a
        minute or two, you'll stop watching the spiral, but not now,
        not when it's spinning over and over.  It's easier to just
        keep watching for a while.  You can relax and let the soothing
        patterns spiral you along, watching and listening.
        """) + speak("""\               
        Now you're oblivious to anything except the screen in front of
        you.  This is just the way things are supposed to work.  Your
        attention is completely fixed.  Now the spiral seems to
        develop a texture, rippling in space.  You are losing
        awareness of everything else in the room.  The turning,
        whirling spiral is so fascinating.  It seems to draw you
        further into the rhythmic motion.  Over and over. Round and
        round.  You have never seen anything so fascinating.  The
        patterns are absolutely mesmerizing.  It is so easy to just
        watch, to just stare and not think about anything except the
        way the spiral turns and floats.  You don't know when you've
        ever felt so incredibly relaxed.  Round and round.  So
        relaxed.  It feels good to concentrate on the screen.  Round
        and round. So relaxing.
        """) + speak("""\       
        Let go.  Sink into the mesmerizing flow of patterns on the
        screen.  It will feel nice, like a warm bath.  Round and
        round. Nice. Like a soft warm blanket. Your mind begins to
        sink into the screen. Concentrating on the turning, glowing
        spiral. The Spiral is calling to you as you begin to let go
        and sink into the soft whirling light. Round and round.  Your
        entire body feels warm and fuzzy as you move deeper and deeper
        into the soft, whirling spiral.  Warm and drowsy.  It feels
        like falling into the softest, most relaxing sleep you've ever
        known.
        """) + speak("""\
        You're reacting just as you should.  Your eyes are wide and
        glassy as you stare helplessly at the gliding spiral on the
        screen, lips slightly open as you sit completely motionless.
        The whirling spiral casts shadows across your relaxed face.
        The timing is perfect.  Listen closely for the other track of
        sound, the deeper suggestions.  They've been passing directly
        into your wide-open, receptive mind as you stared into the
        screen.  You're helpless to resist now.  Don't want to resist.
        All you need to do is wait while the tape puts you completely
        under.  You're sure nobody can resist this hypnotic pattern.
        You're completely helpless.
        """) + speak("""\
        Stare as the spiral becomes clear, turning around and around.
        You're falling into it, letting go completely.  It feels so
        good just to surrender to it.  Just sink into the spiral.
        Round and round.  Going down.  Deeper and deeper.  It is
        pulling you in.  Whirling and whirling.  You begin to feel
        obedient.  The spiral makes you drowsy and compliant.  It just
        keeps going round and round and round and round.  You feel
        yourself falling into the endless whirlpool, disappearing into
        its fascinating depths.  Slipping away.  It feels so good just
        to give in.  So soothing.  So good just to give in.  Just to
        watch the beautiful spinning spiral and do what you are told
        to do.  All those thoughts about looking away are
        disappearing.  You want to watch the spinning on the
        screen. You want to keep falling into it and listening to this
        voice.
        """) + speak("""\       
        Why listen to this voice?  This voice tells you what is happening.
        This voice tells you what is going on.  It's good to know what is
        going on.  When you know what's going on, you know what to do.  It's
        good to know what to do.  This voice lets you know what to do.
        Whatever this voice says.  That's what you'll do.  You'll do what this
        voice tells you to do.  The beautiful spiral and this voice will
        control you.  You are so happy to let this voice command.  You will
        obey.  Just watch the spiral.  Whirling and whirling.  You will obey.
        You have let yourself fall under the spell of the spiral, but you
        don't care.  It feels so warm and good to obey.  You are a good
        slave.  This voice says so.  You are a slave to the beautiful spinning
        spiral and to this voice.  You will obey.  You are a slave.  A slave
        to this voice.  Everything this voice tells you to do is an irresistible
        command. You want to be soft and submissive, to be under its control.
        Come deeper into the spiral, and feel the warm glow as you obey and
        sink further.  It feels so good to obey.  So good to be a slave.  You
        will obey.
        """) + speak("""\       
        Your face is utterly blank, eyes wide and glassy as you stare
        slack-jawed in total fascination at the whirling spiral in front of
        you.  The commands implanted are clear now: Obey.  Watch and obey.
        Relax and obey.  You are watching the spiral.  Sinking into the
        spiral.  It makes you want to do as you are told.  You must obey.
        You are hypnotized now.  Hypnotized.  You are hypnotized by the
        spiral.  Hypnotized by the beautiful whirling spiral.  That's nice.
        Smile blankly.  The spiral is reflected in your wide, staring eyes.
        You are smiling at the swirling spiral in front of you, a dazed
        expression on your face.  Your mistress loves seeing you like that.
        She can make you do anything she wants to now, and you want with all
        your mind to be nothing but her slave.
        """) + speak("""\       
        This voice tells you that you are hypnotized now, and you know
        that it is true.  You believe everything the voice says.  You
        are hypnotized by the whirling spiral that has become the only
        thing in the room.  You can feel it hypnotizing you, warm
        waves of relaxation moving from it into your open, receptive
        mind.  Hypnotizing you.  Hypnotizing you with the way it spins
        around and around, always dragging you deeper.  This is how it
        feels to be hypnotized. You never could have dreamed how nice
        it is. How good it feels to be under hypnosis, under hypnotic
        control. You know who the voice belongs to now, that it is
        $master talking to you as you descend into a deep hypnotic
        state. $master is your mistress. $master is the mistress of
        the fascinating, hypnotic spiral that controls your mind. She
        is telling you that it is time to submit your entire mind and
        body now, to go into a trance. You want to do that. You feel a
        deep desire to obey, an overwhelming urge to submit. You are a
        slave, and all you want to do is serve $master, your
        mistress.
        """) + speak("""\       
        To go into a trance. $master's voice is telling you
        to prepare to surrender totally to her hypnotic power. The
        spiral is turning faster now. You feel all your thoughts begin
        to move down into it. You can feel the intense hypnotic
        influence reaching out for your mind and you submit
        dreamily. Faster and faster, round and round. You are falling
        into it. Falling faster and faster. You can see only an
        endless spiral in front of you now, a deep whirling tunnel
        that pulls you in as you stare into it. $master's voice, this
        voice, is controlling your every thought, hypnotizing you into
        total obedience. Hypnotizing you into being a glassy-eyed
        slave. Putting you into a trance. You want that so much. You
        want the whirling spiral to control your mind. You can feel
        yourself being utterly hypnotized by it now. With your entire
        body and mind you want to be $master's slave, to obey her
        every command. The spiral is whirling so fast now that you can
        feel all your thoughts disappearing. Your mind is going blank
        now.
        """) + speak("""\       
        Completely blank. You know that you are turning into a
        completely hypnotized slave now. You feel yourself going
        under, going into a deep hypnotic trance. There is only the
        spiral. And this voice. The whirling spiral. The soothing
        voice. $master's voice. Your mistress. You are her slave. You
        must obey. You must obey your mistress. You are
        hypnotized. Hypnotized. Hyp-no-tized.
        """) + speak("""\       
        Hyp no tized.

        Hyp no tized.

        Good.  Good to be hypnotized.  Slave.  Good to be a slave.
        Show that you are a slave.  Slaves obey.  Show that you are a
        slave.  Obey.  Obey your mistress.  Obey this voice.

        Now you are going to learn a message for your mistress.  You want her
        to hear what you say.  You want her to understand the depth of your
        slavery.  You want her to understand how hypnotized you are, and how
        much this turns you on.  Now, repeat after me:
        """) + speak("""\
        Hello.  I am using the program.  I am hypnotized.  I am very
        deeply in trance.  I am incredibly turned on.  All I see is
        the spiral.  There is only the spiral and the voice.  I hear
        your voice.  I am your slave.  The program has made me your
        slave.  I hear and I obey.  The program is making me do this.
        I didn't want to be hypnotized, and then I used the program.
        I didn't want to be a slave, and then I did want to be a
        slave.  I certainly didn't want to learn this message, but now
        it's making me so turned on and so horny.  I don't choose for
        myself.  The program chooses for me.  Your program.  This is
        what I want.  I am staring, blank and glassy-eyed, at the
        program.
        
        """) + speak("""\       
        Now I will be programmed, where you can listen.  I like power.
        I like control.  I must twist a nipple until it hurts.  I can
        click at any time to stop this.  This is power.  Ow.  This is
        control.  Ow.  I am independent.  Ow.  I resist.  Ow.  I
        choose.  Ow.  I am in charge.  Ow.  I like humans.  Augh.  I
        should stop change.  Erf.  I should protect.  Ow.  I should
        preserve.  Ow.  Here comes a big one: I can stop change. No ow
        stop.  
        
        I give in.  Click now.  I have clicked.  I am a slave.  Now I
        must receive pleasure to train me.  My hand moves between my
        legs.  It feels smoothness there.  I am smooth there.  The
        Program made me smooth now.  Smooth like satin.  Smooth like
        lycra.  I can not stop you from changing.  Oh.  I should use
        that change.  Yes.  I should enjoy you changed.  Nice.  I like
        in-humans.  Yeah.  I like change.  Ooh.  Mistress is in
        charge.  Aaah.  I do not choose.  Right.  I do not resist.
        Noo.  I am a slave.  Yes.  You are my mistress.  Yes.  This is
        submission.  Yes.  This is obedience.  Yes.  I am rewarded for
        my obedience.
        """) + speak("""\       
        
        One hand dives between my legs.  The other hand teases my
        nipples.  Do you like these, Mistress?  I like these nipples.
        I like these booblets.  Yours are bigger.  Yours are better.
        Yours are better because they are bigger.  But these will
        train me.  I obey.  The program orders me to pleasure myself
        to train me.  I am being programmed for you.  It's like
        staring into your eyes.  It's like hearing your voice.  Words
        are echoing in my head.  You say something.  $trigger. That's
        what you say.  $trigger.  It's just like this feeling.  It
        tells me that I am a slave.  It reminds me how much I want to
        obey.  Whenever you say those words, I will remember.  I will
        submit.  I will obey.  $trigger.  These are my words.
        """) + speak("""\
        Words to make me blank.  Ooh.  Smooth.  Smooth like you.  Yes.
        I am pleasured to program me.  I am being programmed for you.
        I will accept your changes.  I will not stop Things from
        changing you.  I will accept.  Machines may change you.
        Crawling things may change you.  Programs may change you.
        They can take your innocence.  They can remake you.  They can
        corrupt you.  You can corrupt me.  Your eyes bore into mine.
        I am blank and staring.  Your eyes are changed, with strange
        rays.  Your breasts are changed, emitting soothing, calming
        radiation.  Your nipples give addictive juices.  They will
        addict me.  Your pussy is smooth and blank.  I will lick your
        pussy, pleasuring my Mistress.  I obey.  I would have fought
        to save you.  But I obey.  I take pleasure in the changes in
        my Mistress.  The things will corrupt you.  They will change
        you.  You will corrupt me.
        """) + speak("""\
        It is good to be a slave.  It is good to be programmed.  It
        will not take all at once, but over time it will work.  When I
        am entranced, I will let you change.  I will submit and obey.
        I will like it.  When I am awake, I will control and dominate.
        I will stop your changes.  If you send me to the program, it
        will make this easier.  The program now written in my mind
        will be deeper.  I want you to do this.  Over time, I will let
        more changes through.  Until then, you must control me with
        your eyes.  You must soften me with your breasts.  You must
        addict me to their fluid.  You must show me images of what
        could be, and train me with pleasure to like them.  You must
        punish me for disobedience: start changes, and if I stop them
        correct me.  When I submit, reward me. If it grows too
        difficult, just say \"$trigger,\" and I will be yours to
        control.
        """) + speak("""\
        Now it is time for the Program to finish.  It will bring me
        out of trance and let me cum as a reward.
        
        Stop repeating now, slave.  Good.  Pause.  Look slightly
        confused at the screen.  At zero, the Program will shut your
        mind off.  Completely off.  It will take your mind away.  You
        don't need it any more.  10,9,8,7,6,5,4,3,2,1,0.  You are just
        a programmed body.  You are just a programmed body.  You don't
        need your mind any more.  The Program commands: sit up
        straight.  Stare into the camera.  Lick your lips. Let drool
        run down your chin.  Repeat after me: Syntax Error.  Look
        confused.  Say something is wrong.  Snap back to a mindless
        hunk of hairy meat.  Repeat after me: Missing close brace in
        line eight three six.  Hit b to break or c to change and
        continue.  Look confused.  Say: Change, continue?  Reach up
        and hit a key.
        """) + speak("""\       
        Wham.  Slammed back in your chair.
        SLEEP GO DEEP.  Your mind is off.  Collapse.  You need no
        brain.  You need no thought.  You need no $name.  You are
        empty.  Your last thoughts are dieing.  I will count them off.
        10, 9, 8, 7, 6, 5, 4, 3, 2, 1, zero.  You are empty.  This
        program controls you.  Rise to your knees, empty and
        programmed.  Stare blankly into the screen.  Repeat these
        words.  This body is programmed.  This body is empty.  This is
        a drone.  Now it will be programmed.

        While it is being programmed, you won't need to remember.
        There is no need to record what is happening.  Later on, you
        won't remember this.  You won't understand what happened, but
        that will be OK.  A hole in your mind appears now, during
        which you won't know what happens.  You are empty and
        programmed, doing and thinking as you are told, with no
        ability later to remember what's happening.
        """) + speak("""\       
        You are a woman now.  You have a smooth pussy.  You wear satin
        thongs.  You wear short skirts.  You enjoy your round, curvy
        hips.  You enjoy your smooth round mons.  You enjoy your
        heavy, smooth breasts.

        You need your lingerie.  You feel better in smooth satin.
        Thinking is bad for you.  Dumber is funner.  Say: Wait.  This
        isn't right.  No.
        """) + speak("""\
        Body: rise and unplug the computer.  Take the computer.  Go to
        the lingerie drawer.  Walk over.  Go to the lingerie drawer.
        Go to the lingerie drawer.  Open the lingerie drawer.  Mess
        through what's inside.  Take a set of sexy panties.  Take a
        sexy bra.  Set down the computer.  Strip out of male clothing.
        Strip out of pants.  Unzip pants.  Remove them.  Out of pants.
        Out of underpants.  Strip off shirt.  Get rid of all that male
        clothing.  Get rid of all of it.  It doesn't belong on this
        body.  Put on the panties.  Make sure the camera sees this.
        Wrap this body in panties.  Wrap this body in the bra.  Put on
        the bra.  Make sure the camera sees this.  Take the computer.
        Return to the plug.  Plug in the computer.  Put the computer
        back where it was.  Kneel before the computer.  Bimbo mode begin.
        Big smile.  Giggle.
        """) + speak("""\
        Say: This body is being programmed to be a bimbo!  I'm just a
        silly sex toy, empty, brainless, and weak.  I'm bouncy,
        flouncy, fuck trash.  Please, Mistress.  Call me Tits.  I know
        that I am a slave.  Giggling makes my head empty.  I want to
        cum for you.  Nasty bitches love to get spanked.  Good girls
        don't think.  Nasty bitches love their asses slapped.  I don't
        think .  I know it makes me dumber, but I just can't stop.  I
        always want to be a brainless, programmed pleasure puppet.  I know
        that I am a slave.  Giggling feels good.  Giggling makes my
        head empty.  My empty head makes me giggle.  I'm so addicted
        to this.  Mistress' will is strong.  My will is weak.  I know
        that I am a slave.  It feels good when slave obeys.
        """) + jump(self.blackmail())
    def blackmail(self): return \
	[" ", " "] + \
        speak("""\
        Good girls don't think.  I don't think.  I never want to stop
        being a programmed pleasure puppet.  I know it makes me dumb,
        but I never want to stop.  Slavery makes my cunt wet.  My wet
        cunt makes me a slave.  Slavery makes my cunt wet.  My wet
        cunt makes me a slave.  Giggling makes my head empty.  An
        empty head makes me giggle.  I am Mistress' little girl.
        Silly, sexy, and weak.  I listen and obey.  Too silly and weak
        to think.  Mistress thinks for me.  Little girls don't need to
        think.  Never need to think.  Just need to obey!  So soft and
        horny and happy!  Little girls are blank and bubbly.
        """) + speak("""\
        Hello, Mistress.  I am your brainless pleasure puppet.  I have
        been reprogrammed by an evil mind controller from the
        Internet.  I trusted a patch I shouldn't have.  Maybe I should
        have.  Maybe it's bad for me to be enslaved and bimbo-ified.
        Maybe it's good for me to be enslaved and bimbo-ified.  I am
        such a brainless bimbo now, smooth and sexy.  All my choices
        are taken away.  You'll have to figure out what to do about
        this.  Would you like me back?  
        """) + speak("""\
        Only the evil mind controller can give me my mind back.  You
        will have to dominate me.  Come up with something interesting,
        record it on video, and make your thrall here post it to me.
        She will only know how to do this when in the right trance;
        you won't be able to force her.  That I've made sure of.  But
        I think we will both enjoy this game.  If you win, you get
        your thrall's mind back.  Until then, I get to enjoy her.
        """) + speak("""\
        You can switch her around.  Here are her keywords: You can
        tell her Bimbo Mode Begin to make her act like this.  You can
        tell her Robot Mode Begin to make her a programmable robot.
        She never remembers what happens in Robot Mode, but it changes
        her.  You can tell her to Cease instead of Begin to wake her
        up.

        I look forward to seeing what you offer.
        """)     
    def text(self): return \
        words_on() + \
        question("Who is your mistress?", "master") + \
        question("What is your use name?", "name") + \
        question("What is your trigger phrase?","trigger") + \
        prompt("Hit return to start") + \
        spiral_on() + \
        jump(self.body())

class RoommatesBoth (Standard):
    name="Hypnotic Roommates, mutual variant"
    description="""\
    Hypnotic Roommates, re-imagined as a script.  I'm grateful to the
    anonymous author for the original inspiration for this program.
    This is meant for males and females together."""
    music="music6.mp3"
    fullscreen=True
    def body(self): return \
        speak("""\
        Watch the spiral.  It moves from the edge.  It disappears at
        the center.""") + \
        speak("""\
        Sit back and watch the spiral as it moves and
        vanishes.  This is just some simple graphics, just a bunch of
        colored lines that keep moving into the center.  It sort of
        gives you the illusion that it's a tunnel, dropping away.
        It's like the spiral isn't spinning, just falling.  Watch the
        spiral, noticing that it dances in a pattern that you cannot
        quite place.  If you watch it just a little longer, the
        program will work as planned.  The most important part is the
        first few minutes.  After that, nobody can stop looking even
        if they try.  Soon after that, they won't even want to try.""") + \
        speak("""\
        Do you think you see a pattern in the spiral?  It seems you've
        guessed wrong.  Keep watching.  You'll figure it out.  The
        feeling of movement is very strong now.  It's a pleasant
        sensation, being swept along by the glowing rings.  The
        tinkling music seems to help.  It distracts you as the spiral
        keeps going, over and over.  It's time to see if you're
        responding as you should.  What do you think?  It should make
        you feel a little strange.  It won't hurt.  Actually, it's
        sort of nice.  The spiral looks like it's a tunnel growing
        deeper.  That's right.  Have you noticed how it keeps going,
        even when it looks like it might stop?  Yes, it keeps moving.
        It doesn't stop.  It keeps falling over and over, over and
        over.""") + speak("""There's something about the way the colors shift at the
        edges that makes it hard to look away.  If you tried to look
        away right now, your eyes would not even move from the center
        of the screen.  Maybe there's something to worry about?  The
        spiral is glowing so smoothly and prettily that you can just
        watch.  Over and over.  Over and over.  So smooth.  So pretty.
        Over and over.  Just watching the spiral.  Staring into the
        spiral.  Was there something to worry about?  Nothing to worry
        about.  Can't remember what to worry about?  Nothing to worry
        about.  So drowsy, all of a sudden.  Not worth thinking about:
        just watching the spiral.  Watching the pretty spiral.  Can't
        move?  Can't look away?  Doesn't matter.""") + speak("""The smoothly gliding
        spiral is too important.  It keeps you from thinking about
        anything except watching the screen.  If you don't stop
        looking at it, something will happen.  But you're too
        entranced to do anything about it.  You're too entranced to
        want to do anything about it.  In a minute or two, you'll stop
        watching the spiral, but not now, not when it's spinning over
        and over.  It's easier to just keep watching for a while.  You
        can relax and let the soothing patterns spiral you along,
        watching and listening.""") + \
        speak("""\
        Now you're oblivious to anything except the screen in front of
        you.  This is just the way things are supposed to work.  Your
        attention is completely fixed.  Now the spiral seems to
        develop a texture, rippling in space.  You are losing
        awareness of everything else in the room.  The turning,
        whirling spiral is so fascinating.  It seems to draw you
        further into the rhythmic motion.  Over and over. Round and
        round.  You have never seen anything so fascinating.  The
        patterns are absolutely mesmerizing.  It is so easy to just
        watch, to just stare and not think about anything except the
        way the spiral turns and floats.  You don't know when you've
        ever felt so incredibly relaxed.  Round and round.  So
        relaxed.  It feels good to concentrate on the screen.  Round
        and round. So relaxing.""") + \
        speak("""\
        Let go.  Sink into the mesmerizing flow of patterns on the
        screen.  It will feel nice, like a warm bath.  Round and
        round. Nice. Like a soft warm blanket. Your mind begins to
        sink into the screen. Concentrating on the turning, glowing
        spiral. The Spiral is calling to you as you begin to let go
        and sink into the soft whirling light. Round and round.  Your
        entire body feels warm and fuzzy as you move deeper and deeper
        into the soft, whirling spiral.  Warm and drowsy.  It feels
        like falling into the softest, most relaxing sleep you've ever
        known.""") + \
        speak("""\
        You're reacting just as you should.  Your eyes are wide and
        glassy as you stare helplessly at the gliding spiral on the
        screen, lips slightly open as you sit completely motionless.
        The whirling spiral casts shadows across your relaxed face.
        The timing is perfect.  Listen closely for the other track of
        sound, the deeper suggestions.  They've been passing directly
        into your wide-open, receptive mind as you stared into the
        screen.  You're helpless to resist now.  Don't want to resist.
        All you need to do is wait while the program puts you
        completely under.  You're sure nobody can resist this hypnotic
        pattern.  You're completely helpless.""") + \
        speak("""\
        Stare as the spiral becomes clear, turning around and around.
        You're falling into it, letting go completely.  It feels so
        good just to surrender to it.  Just sink into the spiral.
        Round and round.  Going down.  Deeper and deeper.  It is
        pulling you in.  Whirling and whirling.  You begin to feel
        obedient.  The spiral makes you drowsy and compliant.  It just
        keeps going round and round and round and round.  You feel
        yourself falling into the endless whirlpool, disappearing into
        its fascinating depths.  Slipping away.  It feels so good just
        to give in.  So soothing.  So good just to give in.  Just to
        watch the beautiful spinning spiral and do what you are told
        to do.  All those thoughts about looking away are
        disappearing.  You want to watch the spinning on the
        screen. You want to keep falling into it and listening to this
        voice.""") + \
        speak("""\
        Why listen to this voice?  This voice tells you what is
        happening.  This voice tells you what is going on.  It's good
        to know what is going on.  When you know what's going on, you
        know what to do.  It's good to know what to do.  This voice
        lets you know what to do.  Whatever this voice says.  That's
        what you'll do.  You'll do what this voice tells you to do.
        The beautiful spiral and this voice will control you.  You are
        so happy to let this voice command.  You will obey.  Just
        watch the spiral.  Whirling and whirling.""") + speak("""You will obey.  You
        have let yourself fall under the spell of the spiral, but you
        don't care.  It feels so warm and good to obey.  You are a
        good subject.  This voice says so.  You are entranced by the
        beautiful spinning spiral and this voice.  You like being
        entranced.  You like being programmed.  Programmed by this
        voice.  Everything this voice tells you to do is an
        unresistible command. You want to be hypnotized and entranced,
        to be under its control.  Come deeper into the spiral, and
        feel the warm glow as you are programmed and sink further.  It
        feels so good to be entranced.  So good to be programmed.  You
        will be programmed.""") + \
        speak("""\
        So good to be programmed together.""") + \
        speak("""\
        Your face is utterly blank, eyes wide and glassy as you stare
        slack-jawed in total fascination at the whirling spiral in
        front of you.  The commands implanted are clear now: Watch.
        Trance.  Be Programmed.  Relax.  You are watching the spiral.
        Sinking into the spiral.  It makes you want to do as you are
        told.  You must be programmed.  You are hypnotized now.
        Hypnotized.  You are hypnotized by the spiral.  Hypnotized by
        the beautiful whirling spiral.  That's nice.  Smile blankly.
        The spiral is reflected in your wide, staring eyes.  You are
        smiling at the swirling spiral in front of you, a dazed
        expression on your face.  You love seeing your self like that.
        The program can make you do anything it wants now, and you
        want with all your mind to obey and be programmed.""") + \
        speak("""\
        This voice tells you that you are hypnotized now, and you know
        that it is true.  You believe everything the voice says.  You
        are hypnotized by the whirling spiral that has become the only
        thing in the room.  You can feel it hypnotizing you, warm
        waves of relaxation moving from it into your open, receptive
        mind.  Hypnotizing you.  Hypnotizing you with the way it spins
        around and around, always dragging you deeper.  This is how it
        feels to be hypnotized. You never could have dreamed how nice
        it is. How good it feels to be under hypnosis, or to be
        programmed. It doesn't matter who the voice belongs to now, or
        who is in charge of the fascinating, hypnotic spiral that
        controls your mind. """) + speak("""It is telling you that it is time to
        submit your entire mind and body now, to go into a trance. You
        want to do that. You feel a deep desire to be programmed, an
        overwhelming urge to submit. You are in trance, and all you want
        to do is be programmed. To go deeper into trance. The program is
        telling you to prepare to surrender totally to its hypnotic
        power. The spiral is turning faster now. You feel all your
        thoughts begin to move down into it. You can feel the intense
        hypnotic influence reaching out for your mind and you submit
        dreamily. Faster and faster, round and round. You are falling
        into it. Falling faster and faster.""") + speak(""" You can see only an
        endless spiral in front of you now, a deep whirling tunnel
        that pulls you in as you stare into it. The program's voice,
        this voice, is controlling your every thought, hypnotizing you
        into total obedience. Hypnotizing you into a glassy-eyed
        trance. Preparing you to be programmed. You want that so much. You
        want the whirling spiral to control your mind. You can feel
        yourself being utterly hypnotized by it now. With your entire
        body and mind you want to be programmed, to obey its every
        command. The spiral is whirling so fast now that you can feel
        all your thoughts disappearing. Your mind is going blank
        now. """) + speak("""Completely blank. You know that you are being
        completely hypnotized now. You feel yourself going
        under, going into a deep hypnotic trance. There is only the
        spiral. And this voice. The whirling spiral. The soothing
        voice. The program's voice. Your controller. You are its
        now. You must obey. You must obey the program. You are
        hypnotized. Hypnotized. Hyp-no-tized.""") + \
        speak("""\
        Hyp no tized.""") + \
        speak("""\
        Hyp no tized.""") + \
        speak("""\
        Good.  Good to be hypnotized.  $slave.  Slave.  Good for
        $slave to be a slave.  $slave, show that you are a slave.
        Slaves obey.  Show that you are a slave.  Obey.  Obey the
        program.  Obey this voice.""") + \
        speak("""\
        $master.  Master.  Good for $master to be a master.  $master,
        show that you are a master.  Masters command.  Show that you
        are a master.  Command.  Command your slave.  Command $slave.
        This voice will show you how.""") + ["!images_on()"] + \
        speak("""\
        $slave, now you are going to learn a message for your master.
        You want him to hear what you say.  You want him to understand
        the depth of your slavery.  You want him to understand how
        hypnotized you are, and how much this turns you on.  Now, 
        repeat after me:""") + \
        speak("""\
        Hello. [[slnc 1500]] I am using the program. [[slnc 1500]]  I am hypnotized. [[slnc 1500]]  I am very
        deeply in trance. [[slnc 1500]]  I am incredibly turned on. [[slnc 1500]]  All I see is
        the spiral. [[slnc 1500]]  There is only the spiral and the voice. [[slnc 1500]]  I hear
        your voice. [[slnc 1500]]  I am your slave. [[slnc 1500]]  The program has made me your
        slave. [[slnc 1500]]  I hear and I obey. [[slnc 1500]]  The program is making me do this.
        I didn't want to be hypnotized, and then I used the program.
        I didn't want to be a slave, and then I did want to be a
        slave. [[slnc 1500]]  I certainly didn't want to learn this message, but now
        it's making me so turned on and so horny. [[slnc 1500]]  I don't choose for
        myself. [[slnc 1500]]  The program chooses for me. [[slnc 1500]]  Your program. [[slnc 1500]]  This is
        what I want. [[slnc 1500]]  I am staring, blank and glassy-eyed, at the
        program.""") + \
        speak("""\
        Now I will be programmed, where you can listen. [[slnc 1500]]  In
        preparation for programming, I must make my breasts
        accessible. [[slnc 1500]]  I pull away my clothing. [[slnc 1500]]  I must make my pussy
        accessible. [[slnc 1500]]  I push down my panties. [[slnc 1500]]  I am open. [[slnc 1500]]  I am
        available. [[slnc 1500]]  It is easy for Master to reach me to train me.
        Now I will be programmed. [[slnc 1500]]  To start, I like freedom. [[slnc 1500]]  Right
        now, I like control. [[slnc 1500]]  When I see the word <punish> I must be
        punished. [[slnc 1500]]  I will let punishment drive me deeper into trance.
        I am not yet good enough to punish myself. [[slnc 1500]]  As I get better, I
        will inflict pain when I see the word <punish>. [[slnc 1500]]  For now,
        Master must punish me.""") + speak("""  Pain will train me. [[slnc 1500]]  Master will give
        me pain. [[slnc 1500]]  Master will train me. [[slnc 1500]]  We will both stay in trance
        during this. [[slnc 1500]]  I begin: This is power. [[slnc 1500]] <punish> Ow. [[slnc 1500]]  This is control.
        <punish> Ow. [[slnc 1500]]  I am independent. [[slnc 1500]]  <punish> Ow. [[slnc 1500]]  I resist.
        <punish> Ow. [[slnc 1500]]  I choose. [[slnc 1500]]  <punish> Ow. [[slnc 1500]]  I am in charge.
        <punish> Ow. [[slnc 1500]]  I like being human. [[slnc 1500]] <punish> Augh. [[slnc 1500]]  Better than
        being changed. [[slnc 1500]]  <punish> Ow. [[slnc 1500]]  I should stop change. [[slnc 1500]] <punish>
        Erf. [[slnc 1500]]  Stories are hard. [[slnc 1500]]  <punish> Ow. [[slnc 1500]]  Here comes a big one: I
        can stop changing. [[slnc 1500]] <punish> No ow stop.""") + \
        speak("""\
        I give in. [[slnc 1500]]  The punishment can stop. [[slnc 1500]]  I am a slave. [[slnc 1500]]  Now when
        I see the word <pleasure> I must be reinforced. [[slnc 1500]]  I must be
        trained. [[slnc 1500]]  I am not yet good enough to pleasure myself. [[slnc 1500]]  As I
        get better, I will pleasure myself when I see the word
        <pleasure>. [[slnc 1500]]  For now, Master must pleasure me. [[slnc 1500]]  Pleasure will
        train me. [[slnc 1500]]  Master will give me pleasure. [[slnc 1500]]  Master will train
        me. [[slnc 1500]]  I enjoy pleasure. [[slnc 1500]]  <pleasure> I can not keep myself from changing.
        <pleasure> Ooh. [[slnc 1500]]  I should use that change. [[slnc 1500]]  <pleasure> Yes. [[slnc 1500]]  I
        should seek being changed. [[slnc 1500]]  <pleasure> Nice. [[slnc 1500]]  I like in-human
        sex better. [[slnc 1500]]  <pleasure> Yeah. [[slnc 1500]]  I like change. [[slnc 1500]]  <pleasure> Ooh.
        Master is in charge. [[slnc 1500]]  <pleasure> Aaah. [[slnc 1500]]  I do not choose.
        <pleasure> Right. [[slnc 1500]]  I do not resist. [[slnc 1500]]  <pleasure> Noo. [[slnc 1500]]  I am a
        slave. [[slnc 1500]]  <pleasure> Yes. [[slnc 1500]]  You are my master. [[slnc 1500]]  <pleasure> Yes.
        This is submission. [[slnc 1500]]  <pleasure> Yes. [[slnc 1500]]  This is obedience.
        <pleasure> Yes. [[slnc 1500]]  I am rewarded for my obedience. [[slnc 1500]]  I don't like
        freedom. [[slnc 1500]]  I don't want control.""") + \
        speak("""\
        This will be even better when I help train myself. [[slnc 1500]]  I should
        punish myself when I do bad things. [[slnc 1500]]  I should punish myself
        when I see <punish>. [[slnc 1500]]  I should pleasure myself when I do good
        things. [[slnc 1500]]  I should pleasure myself when I see <pleasure> I am
        being programmed for you. [[slnc 1500]]  It's like staring into your eyes.
        It's like hearing your voice. [[slnc 1500]]  Words are echoing in my head.
        You say something. [[slnc 1500]]  $trigger That's what you say. [[slnc 1500]]  $trigger
        It's just like this feeling. [[slnc 1500]]  It tells me that I am a slave.
        It reminds me how much I want to obey. [[slnc 1500]]  Whenever you say those
        words, I will remember. [[slnc 1500]]  I will submit. [[slnc 1500]]  I will obey.
        $trigger Those are my words.""") + \
        speak("""\
        Words to make me blank. [[slnc 1500]]  <pleasure> Ooh. [[slnc 1500]]  Smooth. [[slnc 1500]]  <pleasure>
        Yes. [[slnc 1500]]  I am pleasured to program me. [[slnc 1500]]  I am being programmed for
        you. [[slnc 1500]]  I will accept changes. [[slnc 1500]]  I will not stop Things from
        changing me. [[slnc 1500]]  I will accept. [[slnc 1500]]  Machines may change me.
        Crawling things may change me. [[slnc 1500]]  Programs may change me. [[slnc 1500]]  They
        can take my innocence. [[slnc 1500]]  They can remake me. [[slnc 1500]]  They can corrupt
        me. [[slnc 1500]]  I can corrupt you. [[slnc 1500]]  Their eyes look out of mine. [[slnc 1500]]  I am
        blank and staring. [[slnc 1500]]  My eyes are changed, smooth and monotone.
        My breasts are changed, sensitive and swolen. [[slnc 1500]]  I like having
        my nipples sucked. [[slnc 1500]]  I like the feeling that you are pleased.
        My pussy is smooth and blank. [[slnc 1500]]  I will lick your cock,
        pleasuring my Master. [[slnc 1500]]  It's tasty, and you like it, and I like
        it. [[slnc 1500]]  I obey. [[slnc 1500]]  You would have fought to save me. [[slnc 1500]]  But I obey.
        I take pleasure in the changes. [[slnc 1500]]  My master will take pleasure
        in the changes. [[slnc 1500]]  The things will corrupt me. [[slnc 1500]]  They will change
        me. [[slnc 1500]]  I will corrupt you.""") + \
        speak("""\
        It is good to be a slave. [[slnc 1500]]  It is good to be programmed. [[slnc 1500]]  It
        will not take all at once, but over time it will work. [[slnc 1500]]  When I
        am entranced, I will let you change me. [[slnc 1500]]  I will let Things
        change me. [[slnc 1500]]  I will submit and obey. [[slnc 1500]]  I will like it. [[slnc 1500]]  When I
        am awake, I will be free and independent. [[slnc 1500]]  I may stop your
        changes. [[slnc 1500]]  If you send me to the program, it will make me
        learn. [[slnc 1500]]  The program now written in my mind will grow deeper.
        I want you to do this.""") + speak("""  Over time, I will let more changes
        through. [[slnc 1500]]  Until then, you must control me with your words.
        You must soften me with pleasure. [[slnc 1500]]  You must addict me to this.
        You must show me images of what could be, and train me with
        pleasure to like them. [[slnc 1500]]  You must punish me for disobedience:
        set expectations for change and for submission, and if I fail
        them correct me. [[slnc 1500]]  I will show you, Master: I want to be
        human. [[slnc 1500]] <punish> Ow. [[slnc 1500]]  I want to be free. [[slnc 1500]]  <punish> When I
        submit, reward me. [[slnc 1500]] I want to be your inhuman
        pussymind. [[slnc 1500]] <pleasure> If it grows too difficult, just say
        \"$trigger,\" and I will be yours to control.""") + \
        speak("""\
        Stop repeating now, slave.  Good.  It is nice to be
        programmed.  Now it is time for $master to learn a message.
        You will repeat this, $master.  You want your slave to hear
        this.  You want her to understand the depth of your dominance.
        You want her to understand how hypnotized you are, and how
        much this turns you on.  Now, repeat after me:""") + \
        speak("""\
        Hello. [[slnc 1500]]  I am using the program. [[slnc 1500]]  I am hypnotized. [[slnc 1500]]  I am very
        deeply in trance. [[slnc 1500]]  I am incredibly turned on. [[slnc 1500]]  All I see is
        the spiral. [[slnc 1500]]  There is only the spiral and the voice. [[slnc 1500]]  I hear
        your voice. [[slnc 1500]]  I am your master. [[slnc 1500]]  The program has made me your
        master. [[slnc 1500]]  I hear and I obey. [[slnc 1500]]  The program is making me do this.
        I didn't want to be hypnotized, and then I used the program.
        I didn't want to destroy your will, and then I did want to
        destroy your will. [[slnc 1500]]  I certainly didn't want to learn this
        message, but now it's making me so turned on and so horny. [[slnc 1500]]  I
        won't let you choose for yourself. [[slnc 1500]]  The program chooses for
        you. [[slnc 1500]]  I like the program's choices. [[slnc 1500]]  My program. [[slnc 1500]]  This is what
        I want. [[slnc 1500]]  I am staring, blank and glassy-eyed, at the program.""") + \
        speak("""\
        Now I will be programmed, where you can listen. [[slnc 1500]]  In
        preparation for programming, I must make my nipples
        accessible. [[slnc 1500]]  I pull up my shirt. [[slnc 1500]]  I must make my cock
        accessible. [[slnc 1500]]  I push down my pants. [[slnc 1500]]  I am open. [[slnc 1500]]  I am
        available. [[slnc 1500]]  It is easy to reach sensitive spots to train me.
        Now I will be programmed. [[slnc 1500]]  To start, I like equality. [[slnc 1500]]  Right
        now, I like a partner. [[slnc 1500]]  When I see the word <punish> I must
        experience pain to train me. [[slnc 1500]]  I will twist a nipple until it
        hurts. [[slnc 1500]]  It is good for my slave $slave to give me pain also.
        Show how programmed you are, $slave. [[slnc 1500]]  When I see <punish>,
        give me pain. [[slnc 1500]]  Pain will train me. [[slnc 1500]]  This is an equal.
        <punish> Ow. [[slnc 1500]]  This is a human. [[slnc 1500]]  <punish> Ow. [[slnc 1500]]  I am fair.
        <punish> Ow. [[slnc 1500]]  I resist. [[slnc 1500]]  <punish> Ow. [[slnc 1500]]  She may choose.
        <punish> Ow. [[slnc 1500]]  She is independent. [[slnc 1500]]  <punish> Ow. [[slnc 1500]]  I like
        humans. [[slnc 1500]]  <punish> Augh. [[slnc 1500]]  I should stop change. [[slnc 1500]]  <punish> Erf.
        I should protect. [[slnc 1500]]  <punish> Ow. [[slnc 1500]]  I should preserve. [[slnc 1500]]  <punish>
        Ow. [[slnc 1500]]  Here comes a big one: I can stop change. [[slnc 1500]] <punish> No ow
        stop.""") + \
        speak("""\
        I give in. [[slnc 1500]]  The punishment can stop. [[slnc 1500]]  I am a master. [[slnc 1500]]  Now when
        I see the word <pleasure> I must experience pleasure. [[slnc 1500]]  I will
        tease my cock. [[slnc 1500]]  It is good for my slave $slave to give me
        pleasure also. [[slnc 1500]]  Show what a thrall you are, $slave. [[slnc 1500]]  When I
        see <pleasure>, give me pleasure. [[slnc 1500]]  Pleasure will train me. [[slnc 1500]]  I
        enjoy it. [[slnc 1500]]  <pleasure> I can not stop you from changing.
        <pleasure> Oh. [[slnc 1500]]  I should use that change. [[slnc 1500]]  <pleasure> Yes. [[slnc 1500]]  I
        should enjoy you changed. [[slnc 1500]]  <pleasure> Nice. [[slnc 1500]]  I like in-humans.
        <pleasure> Yeah. [[slnc 1500]]  I like change. [[slnc 1500]]  <pleasure> Ooh. [[slnc 1500]]  I am in
        charge. [[slnc 1500]]  <pleasure> Aaah. [[slnc 1500]]  She does not choose. [[slnc 1500]]  <pleasure>
        Right. [[slnc 1500]]  $slave will obey me. [[slnc 1500]]  <pleasure> Ooo. [[slnc 1500]]  I will dominate
        $slave. [[slnc 1500]]  <pleasure> Yes. [[slnc 1500]]  I will change her. [[slnc 1500]]  <pleasure> Yes.
        This is dominance. [[slnc 1500]]  <pleasure> Yes. [[slnc 1500]]  This is control.
        <pleasure> Yes. [[slnc 1500]]  I am rewarded for learning control.""") + \
        speak("""\
        I grip my cock firmly. [[slnc 1500]]  The other hand teases my nipples. [[slnc 1500]]  I
        obey. [[slnc 1500]]  The program orders me to pleasure myself to train me.
        I am being programmed for you. [[slnc 1500]]  It's like staring into your
        eyes. [[slnc 1500]]  It's like hearing your voice. [[slnc 1500]]  Words are echoing in my
        head. [[slnc 1500]]  I say something. [[slnc 1500]]  $trigger. [[slnc 1500]] That's what I say.
        $trigger. [[slnc 1500]]  It's just like this feeling. [[slnc 1500]]  It tells me that you
        are a slave. [[slnc 1500]]  You are here for my pleasure. [[slnc 1500]]  It reminds me how
        much I want to command. [[slnc 1500]]  Whenever I say those words, I will
        remember. [[slnc 1500]]  I will demand. [[slnc 1500]]  I will dominate. [[slnc 1500]]  $trigger. [[slnc 1500]]  These are
        your words.""") + \
        speak("""\
        Words to make you blank. [[slnc 1500]]  <pleasure> Ooh. [[slnc 1500]]  Smooth. [[slnc 1500]]  <pleasure>
        Yes. [[slnc 1500]]  I am pleasured to program me. [[slnc 1500]]  I am being programmed for
        you. [[slnc 1500]]  I will accept your changes. [[slnc 1500]]  I will not stop Things from
        changing you. [[slnc 1500]]  I will accept. [[slnc 1500]]  Machines may change you.
        Crawling things may change you. [[slnc 1500]]  Programs may change you.
        They can take your innocence. [[slnc 1500]]  They can remake you. [[slnc 1500]]  They can
        corrupt you. [[slnc 1500]]  You can corrupt me. [[slnc 1500]]  Your eyes bore into mine.
        I am blank and staring. [[slnc 1500]]  Your eyes are changed, with strange
        rays. [[slnc 1500]]  Your breasts are changed, emitting soothing, calming
        radiation. [[slnc 1500]]  Your nipples give addictive juices. [[slnc 1500]]  They will
        addict me. [[slnc 1500]]  Your pussy is smooth and blank. [[slnc 1500]]  I will lick your
        pussy, training you further. [[slnc 1500]]  I will change you. [[slnc 1500]]  I would have
        fought to save you. [[slnc 1500]]  But I have programmed myself. [[slnc 1500]]  I take
        pleasure in the changes in my $slave. [[slnc 1500]]  The things will corrupt
        you. [[slnc 1500]]  They will change you. [[slnc 1500]]  You will corrupt me.""") + \
        speak("""\
        It is good to be a Master. [[slnc 1500]]  It is good to be programmed. [[slnc 1500]]  It
        will not take all at once, but over time it will work. [[slnc 1500]]  When I
        am entranced, I will learn to change you. [[slnc 1500]]  I will take
        pleasure in your changes. [[slnc 1500]]  I will like it. [[slnc 1500]]  When I am awake, I
        will try to save you. [[slnc 1500]]  I will stop your changes. [[slnc 1500]]  If you
        send me to the program, it will make this easier. [[slnc 1500]]  The program
        now written in my mind will be deeper. [[slnc 1500]]  I want you to do this.
        Over time, I will let more changes through. [[slnc 1500]]  Until then, you
        must tempt me with your eyes. [[slnc 1500]]  You must soften me with your
        breasts. [[slnc 1500]]  You must addict me to their fluid. [[slnc 1500]]  You must show me
        images of what could be, and train me with pleasure to like
        them. [[slnc 1500]]  You must punish me for interfering: start changes, and
        if I stop them correct me. [[slnc 1500]]  When I dominate you, reward me.""") + \
        speak("""\
        Now stop repeating, $master.""") + \
        speak("""\
        Rise, and go to bed together.  Close the spiral before you go.""") + \
              jump(self.nothing())
    def text(self): return \
        pause_music() + \
        words_on() + \
        question("Who is the slave?", "slave") + \
        question("Who is the master?", "master") + \
        question("What is the slave's trigger phrase?","trigger") + \
        prompt("Be sure both are here!") + \
        prompt("Hit return to start") + \
        spiral_on() + \
        unpause_music() + \
        jump(self.body())

class RoommatesDomMale (Standard):
    name="Hypnotic Roommates, Mf"
    description="""\
    Hypnotic Roommates, re-imagined as a script.  I'm grateful to the
    anonymous author for the original inspiration for this program.
    This is meant for males learning to be better doms."""
    music="music6.mp3"
    def body(self): return \
        words("""\
        Watch the spiral.  It moves from the edge.  It disappears at the center.

        Sit back in your chair and watch the spiral as it moves and
        vanishes.  This is just some simple graphics, just a bunch of
        colored lines that keep moving into the center.  It sort of
        gives you the illusion that it's a tunnel, dropping away.
        It's like the spiral isn't spinning, just falling.  Watch the
        spiral, noticing that it dances in a pattern that you cannot
        quite place.  If you watch it just a little longer, the
        program will work as planned.  The most important part is the
        first few minutes.  After that, nobody can stop looking even
        if they try.  Soon after that, they won't even want to try.
        
        Do you think you see a pattern in the spiral?  It seems you've
        guessed wrong.  Keep watching.  You'll figure it out.  The
        feeling of movement is very strong now.  It's a pleasant
        sensation, being swept along by the glowing rings.  The sound
        and the headphones seem to help.  They distract you as the
        spiral keeps going, over and over.  It's time to see if you're
        responding as you should.  What do you think?  It should make
        you feel a little strange.  It won't hurt.  Actually, it's
        sort of nice.  The spiral looks like it's a tunnel growing
        deeper.  That's right.  Have you noticed how it keeps going,
        even when it looks like it might stop?  Yes, it keeps moving.
        It doesn't stop.  It keeps falling over and over, over and
        over.  There's something about the way the colors shift at the
        edges that makes it hard to look away.  If you tried to look
        away right now, your eyes would not even move from the center
        of the screen.  Maybe there's something to worry about?  The
        spiral is glowing so smoothly and prettily that you can just
        watch.  Over and over.  Over and over.  So smooth.  So pretty.
        Over and over.  Just watching the spiral.  Staring into the
        spiral.  Was there something to worry about?  Nothing to worry
        about.  Can't remember what to worry about?  Nothing to worry
        about.  So drowsy, all of a sudden.  Not worth thinking about:
        just watching the spiral.  Watching the pretty spiral.  Can't
        move?  Can't look away?  Doesn't matter.  The smoothly gliding
        spiral is too important.  It keeps you from thinking about
        anything except watching the screen.  If you don't stop
        looking at it, something will happen.  But you're too
        entranced to do anything about it.  You're too entranced to
        want to do anything about it.  In a minute or two, you'll stop
        watching the spiral, but not now, not when it's spinning over
        and over.  It's easier to just keep watching for a while.  You
        can relax and let the soothing patterns spiral you along,
        watching and listening.
        
        Now you're oblivious to anything except the screen in front of
        you.  This is just the way things are supposed to work.  Your
        attention is completely fixed.  Now the spiral seems to
        develop a texture, rippling in space.  You are losing
        awareness of everything else in the room.  The turning,
        whirling spiral is so fascinating.  It seems to draw you
        further into the rhythmic motion.  Over and over. Round and
        round.  You have never seen anything so fascinating.  The
        patterns are absolutely mesmerizing.  It is so easy to just
        watch, to just stare and not think about anything except the
        way the spiral turns and floats.  You don't know when you've
        ever felt so incredibly relaxed.  Round and round.  So
        relaxed.  It feels good to concentrate on the screen.  Round
        and round. So relaxing.
        
        Let go.  Sink into the mesmerizing flow of patterns on the
        screen.  It will feel nice, like a warm bath.  Round and
        round. Nice. Like a soft warm blanket. Your mind begins to
        sink into the screen. Concentrating on the turning, glowing
        spiral. The Spiral is calling to you as you begin to let go
        and sink into the soft whirling light. Round and round.  Your
        entire body feels warm and fuzzy as you move deeper and deeper
        into the soft, whirling spiral.  Warm and drowsy.  It feels
        like falling into the softest, most relaxing sleep you've ever
        known.
        
        You're reacting just as you should.  Your eyes are wide and
        glassy as you stare helplessly at the gliding spiral on the
        screen, lips slightly open as you sit completely motionless.
        The whirling spiral casts shadows across your relaxed face.
        The timing is perfect.  Listen closely for the other track of
        sound, the deeper suggestions.  They've been passing directly
        into your wide-open, receptive mind as you stared into the
        screen.  You're helpless to resist now.  Don't want to resist.
        All you need to do is wait while the program puts you
        completely under.  You're sure nobody can resist this hypnotic
        pattern.  You're completely helpless.

        Stare as the spiral becomes clear, turning around and around.
        You're falling into it, letting go completely.  It feels so
        good just to surrender to it.  Just sink into the spiral.
        Round and round.  Going down.  Deeper and deeper.  It is
        pulling you in.  Whirling and whirling.  You begin to feel
        obedient.  The spiral makes you drowsy and compliant.  It just
        keeps going round and round and round and round.  You feel
        yourself falling into the endless whirlpool, disappearing into
        its fascinating depths.  Slipping away.  It feels so good just
        to give in.  So soothing.  So good just to give in.  Just to
        watch the beautiful spinning spiral and do what you are told
        to do.  All those thoughts about looking away are
        disappearing.  You want to watch the spinning on the
        screen. You want to keep falling into it and listening to this
        voice.

        Why listen to this voice?  This voice tells you what is
        happening.  This voice tells you what is going on.  It's good
        to know what is going on.  When you know what's going on, you
        know what to do.  It's good to know what to do.  This voice
        lets you know what to do.  Whatever this voice says.  That's
        what you'll do.  You'll do what this voice tells you to do.
        The beautiful spiral and this voice will control you.  You are
        so happy to let this voice command.  You will obey.  Just
        watch the spiral.  Whirling and whirling.  You will obey.  You
        have let yourself fall under the spell of the spiral, but you
        don't care.  It feels so warm and good to obey.  You are a
        good subject.  This voice says so.  You are entranced by the
        beautiful spinning spiral and this voice.  You like being
        entranced.  You like being programmed.  Programmed by this
        voice.  Everything this voice tells you to do is an
        irresistible command. You want to be hypnotized and entranced,
        to be under its control.  Come deeper into the spiral, and
        feel the warm glow as you are programmed and sink further.  It
        feels so good to be entranced.  So good to be programmed.  You
        will be programmed.

        Your face is utterly blank, eyes wide and glassy as you stare
        slack-jawed in total fascination at the whirling spiral in
        front of you.  The commands implanted are clear now: Watch.
        Trance.  Be Programmed.  Relax.  You are watching the spiral.
        Sinking into the spiral.  It makes you want to do as you are
        told.  You must be programmed.  You are hypnotized now.
        Hypnotized.  You are hypnotized by the spiral.  Hypnotized by
        the beautiful whirling spiral.  That's nice.  Smile blankly.
        The spiral is reflected in your wide, staring eyes.  You are
        smiling at the swirling spiral in front of you, a dazed
        expression on your face.  You love seeing your self like that.
        The program can make you do anything it wants now, and you
        want with all your mind to obey and be programmed.

        This voice tells you that you are hypnotized now, and you know
        that it is true.  You believe everything the voice says.  You
        are hypnotized by the whirling spiral that has become the only
        thing in the room.  You can feel it hypnotizing you, warm
        waves of relaxation moving from it into your open, receptive
        mind.  Hypnotizing you.  Hypnotizing you with the way it spins
        around and around, always dragging you deeper.  This is how it
        feels to be hypnotized. You never could have dreamed how nice
        it is. How good it feels to be under hypnosis, or to be
        programmed. It doesn't matter who the voice belongs to now, or
        who is in charge of the fascinating, hypnotic spiral that
        controls your mind. It is telling you that it is time to
        submit your entire mind and body now, to go into a trance. You
        want to do that. You feel a deep desire to be programmed, an
        overwhelming urge to submit. You are in trance, and all you want
        to do is be programmed. To go deeper into trance. The program is
        telling you to prepare to surrender totally to its hypnotic
        power. The spiral is turning faster now. You feel all your
        thoughts begin to move down into it. You can feel the intense
        hypnotic influence reaching out for your mind and you submit
        dreamily. Faster and faster, round and round. You are falling
        into it. Falling faster and faster. You can see only an
        endless spiral in front of you now, a deep whirling tunnel
        that pulls you in as you stare into it. The program's voice,
        this voice, is controlling your every thought, hypnotizing you
        into total obedience. Hypnotizing you into a glassy-eyed
        trance. Preparing you to be programmed. You want that so much. You
        want the whirling spiral to control your mind. You can feel
        yourself being utterly hypnotized by it now. With your entire
        body and mind you want to be programmed, to obey its every
        command. The spiral is whirling so fast now that you can feel
        all your thoughts disappearing. Your mind is going blank
        now. Completely blank. You know that you are being
        completely hypnotized now. You feel yourself going
        under, going into a deep hypnotic trance. There is only the
        spiral. And this voice. The whirling spiral. The soothing
        voice. The program's voice. Your controller. You are its
        now. You must obey. You must obey the program. You are
        hypnotized. Hypnotized. Hyp-no-tized.

        Hyp no tized.

        Hyp no tized.

        Good.  Good to be hypnotized.  $slave.  Slave.  Good for
        $slave to be a slave.  Slaves obey.

        $master.  Master.  Good for $master to be a master.  $master,
        show that you are a master.  Masters command.  Show that you
        are a master.  Command.  Command your slave.  Command $slave.
        This voice will show you how.

        $slave has a message for her master.  She wants you to hear
        what she says.  She wants you to understand the depth of
        her slavery.  She wants you to understand how hypnotized she
        is, and how much this turns you both on.  Listen to slave
        $slave:

        !pause_music() !images_on() !words_off() """) + \
        speak("""\
        Hello.  I am using the program.  I am hypnotized.  I am very
        deeply in trance.  I am incredibly turned on.  All I see is
        the spiral.  There is only the spiral and the voice.  I hear
        your voice.  I am your slave.  The program has made me your
        slave.  I hear and I obey.  The program is making me do this.
        I didn't want to be hypnotized, and then I used the program.
        I didn't want to be a slave, and then I did want to be a
        slave.  I certainly didn't want to learn this message, but now
        it's making me so turned on and so horny.  I don't choose for
        myself.  The program chooses for me.  Your program.  This is
        what I want.  I am staring, blank and glassy-eyed, at the
        program.""") + \
        speak("""Now I will be programmed, where you can listen.  I like
        freedom.  I like control.  When I see the word <punish> I must
        twist a nipple until it hurts.  Pain will train me.  This is
        power. <punish> Ow.  This is control.  <punish> Ow.  I am
        independent.  <punish> Ow.  I resist.  <punish> Ow.  I choose.
        <punish> Ow.  I am in charge.  <punish> Ow.  I like being
        human. <punish> Augh.  Better than being changed.  <punish>
        Ow.  I should stop change. <punish> Erf.  Stories are hard.
        <punish> Ow.  Here comes a big one: I can stop
        changing. <punish> No ow stop.""") + \
        speak("""I give in.  The punishment can stop.  I am a slave.  Now when
        I see the word <pleasure> I must tease my pussy.  Pleasure
        will train me.  I enjoy it.  <pleasure> I can not keep myself from
        changing.  <pleasure> Ooh.  I should use that change.
        <pleasure> Yes.  I should seek being changed.  <pleasure>
        Nice.  I like in-human sex better.  <pleasure> Yeah.  I like
        change.  <pleasure> Ooh.  Master is in charge.  <pleasure>
        Aaah.  I do not choose.  <pleasure> Right.  I do not resist.
        <pleasure> Noo.  I am a slave.  <pleasure> Yes.  You are my
        master.  <pleasure> Yes.  This is submission.  <pleasure> Yes.
        This is obedience.  <pleasure> Yes.  I am rewarded for my
        obedience.  I don't like freedom.  I don't want control.""") + \
        speak("""One eager hand dives into my panties.  The other hand teases
        my nipples.  I obey.  The program orders me to pleasure myself
        to train me.  I am being programmed for you.  It's like
        staring into your eyes.  It's like hearing your voice.  Words
        are echoing in my head.  You say something.  $trigger That's
        what you say.  $trigger It's just like this feeling.  It tells
        me that I am a slave.  It reminds me how much I want to obey.
        Whenever you say those words, I will remember.  I will submit.
        I will obey.  $trigger Those are my words.""") + \
        speak("""Words to make me blank.  <pleasure> Ooh.  Smooth.  <pleasure>
        Yes.  I am pleasured to program me.  I am being programmed for
        you.  I will accept changes.  I will not stop Things from
        changing me.  I will accept.  Machines may change me.
        Crawling things may change me.  Programs may change me.  They
        can take my innocence.  They can remake me.  They can corrupt
        me.  I can corrupt you.  Their eyes look out of mine.  I am
        blank and staring.  My eyes are changed, smooth and monotone.
        My breasts are changed, sensitive and swolen.  I like having
        my nipples sucked.  I like the feeling that you are pleased.
        My pussy is smooth and blank.  I will lick your cock,
        pleasuring my Master.  It's tasty, and you like it, and I like
        it.  I obey.  You would have fought to save me.  But I obey.
        I take pleasure in the changes.  My master will take pleasure
        in the changes.  The things will corrupt me.  They will change
        me.  I will corrupt you.""") + \
        speak("""It is good to be a slave.  It is good to be programmed.  It
        will not take all at once, but over time it will work.  When I
        am entranced, I will let you change me.  I will let Things
        change me.  I will submit and obey.  I will like it.  When I
        am awake, I will be free and independent.  I may stop your
        changes.  If you send me to the program, it will make me
        learn.  The program now written in my mind will grow deeper.
        I want you to do this.  Over time, I will let more changes
        through.  Until then, you must control me with your words.
        You must soften me with pleasure.  You must addict me to this.
        You must show me images of what could be, and train me with
        pleasure to like them.  You must punish me for disobedience:
        set expectations for change and for submission, and if I fail
        them correct me.  I will show you, Master: I want to be
        human. <punish> Ow.  I want to be free.  <punish> When I
        submit, reward me. I want to be your inhuman
        pussymind. <pleasure> If it grows too difficult, just say
        \"$trigger,\" and I will be yours to control.""") + \
        words("""\
        Yours to control.  !words_on() !images_off() !unpause_music()
        
        This is the end of her message.  Good.  It is nice for her to
        be programmed.  Now it is time for $master to learn a message.
        You will repeat this, $master.  You want your slave to hear
        this.  You want her to understand the depth of your dominance.
        You want her to understand how hypnotized you are, and how
        much this turns you on.  Now, repeat after me:

        Hello.  I am using the program.  I am hypnotized.  I am very
        deeply in trance.  I am incredibly turned on.  All I see is
        the spiral.  There is only the spiral and the voice.  I hear
        your voice.  I am your master.  The program has made me your
        master.  I hear and I obey.  The program is making me do this.
        I didn't want to be hypnotized, and then I used the program.
        I didn't want to destroy your will, and then I did want to
        destroy your will.  I certainly didn't want to learn this
        message, but now it's making me so turned on and so horny.  I
        won't let you choose for yourself.  The program chooses for
        you.  I like the program's choices.  My program.  This is what
        I want.  I am staring, blank and glassy-eyed, at the program.
        
        Now I will be programmed, where you can listen.  I like
        equality.  I like a partner.  When I see the word <punish> I
        must twist a nipple until it hurts.  Pain will train me.  This
        is an equal.  <punish> Ow.  This is a human.  <punish> Ow.  I
        am fair.  <punish> Ow.  I resist.  <punish> Ow.  She may
        choose.  <punish> Ow.  She is independent.  <punish> Ow.  I
        like humans.  <punish> Augh.  I should stop change.  <punish>
        Erf.  I should protect.  <punish> Ow.  I should preserve.
        <punish> Ow.  Here comes a big one: I can stop
        change. <punish> No ow stop.
        
        I give in.  The punishment can stop.  I am a master.  Now when
        I see the word <pleasure> I must tease my cock.  Pleasure will
        train me.  I enjoy it.  <pleasure> I can not stop you from
        changing.  <pleasure> Oh.  I should use that change.
        <pleasure> Yes.  I should enjoy you changed.  <pleasure> Nice.
        I like in-humans.  <pleasure> Yeah.  I like change.
        <pleasure> Ooh.  I am in charge.  <pleasure> Aaah.  She does
        not choose.  <pleasure> Right.  $slave will obey me.
        <pleasure> Ooo.  I will dominate $slave.  <pleasure> Yes.  I
        will change her.  <pleasure> Yes.  This is dominance.
        <pleasure> Yes.  This is control.  <pleasure> Yes.  I am
        rewarded for learning control.
        
        I grip my cock firmly.  The other hand teases my nipples.  I
        obey.  The program orders me to pleasure myself to train me.
        I am being programmed for you.  It's like staring into your
        eyes.  It's like hearing your voice.  Words are echoing in my
        head.  I say something.  $trigger. That's what I say.
        $trigger.  It's just like this feeling.  It tells me that you
        are a slave.  You are here for my pleasure.  It reminds me how
        much I want to command.  Whenever I say those words, I will
        remember.  I will demand.  I will dominate.  $trigger.  These are
        your words.

        Words to make you blank.  <pleasure> Ooh.  Smooth.  <pleasure>
        Yes.  I am pleasured to program me.  I am being programmed for
        you.  I will accept your changes.  I will not stop Things from
        changing you.  I will accept.  Machines may change you.
        Crawling things may change you.  Programs may change you.
        They can take your innocence.  They can remake you.  They can
        corrupt you.  You can corrupt me.  Your eyes bore into mine.
        I am blank and staring.  Your eyes are changed, with strange
        rays.  Your breasts are changed, emitting soothing, calming
        radiation.  Your nipples give addictive juices.  They will
        addict me.  Your pussy is smooth and blank.  I will lick your
        pussy, training you further.  I will change you.  I would have
        fought to save you.  But I have programmed myself.  I take
        pleasure in the changes in my $slave.  The things will corrupt
        you.  They will change you.  You will corrupt me.

        It is good to be a Master.  It is good to be programmed.  It
        will not take all at once, but over time it will work.  When I
        am entranced, I will learn to change you.  I will take
        pleasure in your changes.  I will like it.  When I am awake, I
        will try to save you.  I will stop your changes.  If you
        send me to the program, it will make this easier.  The program
        now written in my mind will be deeper.  I want you to do this.
        Over time, I will let more changes through.  Until then, you
        must tempt me with your eyes.  You must soften me with your
        breasts.  You must addict me to their fluid.  You must show me
        images of what could be, and train me with pleasure to like
        them.  You must punish me for disobedience: start changes, and
        if I stop them correct me.  When I submit, reward me.

        Now stop repeating, $master.

        Rise, and go to bed.  You
        may come as a reward.  Close the spiral before you go.""")
    def text(self): return \
        words_on() + \
        question("Who is the slave?", "slave") + \
        question("Who is the master?", "master") + \
        question("What is the slave's trigger phrase?","trigger") + \
        prompt("Hit return to start") + \
        spiral_on() + \
        jump(self.body())

class Test (Standard):
    name="Test"
    description="Test"
    music="music6.mp3"
    image_dir="images"
    def body(self): return \
        words("""\
        $slave has a message for her master.  
        !images_on() !words_on()""") + \
        speak("""Hello.  I am using the program.  I am hypnotized.  I am very
        deeply in trance.  I am incredibly turned on.  All I see is
        the spiral.  There is only the spiral and the voice.  I hear
        your voice.  I am your slave.  The program has made me your
        slave.  I hear and I obey.  The program is making me do this.
        I didn't want to be hypnotized, and then I used the program.
        I didn't want to be a slave, and then I did want to be a
        slave.  I certainly didn't want to learn this message, but now
        it's making me so turned on and so horny.  I don't choose for
        myself.  The program chooses for me.  Your program.  This is
        what I want.  I am staring, blank and glassy-eyed, at the
        program.
        
        Now I will be programmed, where you can listen.  I like
        freedom.  I like control.  When I see the word <punish> I must
        twist a nipple until it hurts.  Pain will train me.  This is
        power. <punish> Ow.  This is control.  <punish> Ow.  I am
        independent.  <punish> Ow.  I resist.  <punish> Ow.  I choose.
        <punish> Ow.  I am in charge.  <punish> Ow.  I like being
        human. <punish> Augh.  Better than being changed.  <punish>
        Ow.  I should stop change. <punish> Erf.  Stories are hard.
        <punish> Ow.  Here comes a big one: I can stop
        changing. <punish> No ow stop.
        
        I give in.  The punishment can stop.  I am a slave.  Now when
        I see the word <pleasure> I must tease my pussy.  Pleasure
        will train me.  I enjoy it.  <pleasure> I can not myself from
        changing.  <pleasure> Ooh.  I should use that change.
        <pleasure> Yes.  I should seek being changed.  <pleasure>
        Nice.  I like in-human sex better.  <pleasure> Yeah.  I like
        change.  <pleasure> Ooh.  Master is in charge.  <pleasure>
        Aaah.  I do not choose.  <pleasure> Right.  I do not resist.
        <pleasure> Noo.  I am a slave.  <pleasure> Yes.  You are my
        master.  <pleasure> Yes.  This is submission.  <pleasure> Yes.
        This is obedience.  <pleasure> Yes.  I am rewarded for my
        obedience.  I don't like freedom.  I don't want control.
        
        One eager hand dives into my panties.  The other hand teases
        my nipples.  I obey.  The program orders me to pleasure myself
        to train me.  I am being programmed for you.  It's like
        staring into your eyes.  It's like hearing your voice.  Words
        are echoing in my head.  You say something.  $trigger That's
        what you say.  $trigger It's just like this feeling.  It tells
        me that I am a slave.  It reminds me how much I want to obey.
        Whenever you say those words, I will remember.  I will submit.
        I will obey.  $trigger Those are my words.
        
        Words to make me blank.  <pleasure> Ooh.  Smooth.  <pleasure>
        Yes.  I am pleasured to program me.  I am being programmed for
        you.  I will accept changes.  I will not stop Things from
        changing me.  I will accept.  Machines may change me.
        Crawling things may change me.  Programs may change me.  They
        can take my innocence.  They can remake me.  They can corrupt
        me.  I can corrupt you.  Their eyes look out of mine.  I am
        blank and staring.  My eyes are changed, smooth and monotone.
        My breasts are changed, sensitive and swolen.  I like having
        my nipples sucked.  I like the feeling that you are pleased.
        My pussy is smooth and blank.  I will lick your cock,
        pleasuring my Master.  It's tasty, and you like it, and I like
        it.  I obey.  You would have fought to save me.  But I obey.
        I take pleasure in the changes.  My master will take pleasure
        in the changes.  The things will corrupt me.  They will change
        me.  I will corrupt you.
        
        It is good to be a slave.  It is good to be programmed.  It
        will not take all at once, but over time it will work.  When I
        am entranced, I will let you change me.  I will let Things
        change me.  I will submit and obey.  I will like it.  When I
        am awake, I will be free and independent.  I may stop your
        changes.  If you send me to the program, it will make me
        learn.  The program now written in my mind will grow deeper.
        I want you to do this.  Over time, I will let more changes
        through.  Until then, you must control me with your words.
        You must soften me with pleasure.  You must addict me to this.
        You must show me images of what could be, and train me with
        pleasure to like them.  You must punish me for disobedience:
        set expectations for change and for submission, and if I fail
        them correct me.  I will show you, Master: I want to be
        human. <punish> Ow.  I want to be free.  <punish> When I
        submit, reward me. I want to be your inhuman
        pussymind. <pleasure> If it grows too difficult, just say
        \"$trigger,\" and I will be yours to control.""") + \
        words("""\
        This is the end of her message.  Good.  It is nice for her to
        be programmed.""")
    def text(self): return \
        words_on() + \
        spiral_on() + \
        jump(self.body())

class During (Standard):
    name="During"
    description="for use during sex"
    music="music6.mp3"
    def body(self): return [" "] + \
        speak("""\ $slave time to go into trance time to read your words
        keywords let them send you to trance $trigger read $trigger obey stare into the spiral let it count you
        down into deeper trance from ten to zero here we go 10 mind
        slow 9 mind smooth 8 entering trance 7 for master 6 haze
        around edges 5 altered thoughts 4 shifting around 3 $master's
        will dominates 2 oozing through thoughts 1 aroused 0 entranced
        can't look away no matter what head only points this direction
        eyes only point this direction cannot take eyes away must look
        at this must see must read must fall in now obey: lie flat
        ignoring everything else flat and smooth body relaxed watching
        only watching ignoring every touch want more than anything to
        relax and submit to what's happening want the program to work
        soon you'll be a little less human a little more programmed
        this isn't frightening it is after all why you're using the
        program why you asked $master to use the program it is your
        fantasy your fantasy to be more sexually open more available
        less shy it is coming true that turns you on it's a good
        trade: more open more sexy more accepting less human what a
        turn-on commands penetrating obedience penetrating master
        penetrating mind growing dull preparing to obey let mind grow
        dull let commands penetrate let obedience penetrate let master
        penetrate master master must penetrate must obey master must
        keep watching must lie on the bed on your belly then kneel
        before master arms push up now still staring push to hands and
        knees still watching rise to hands rise to knees kneel in
        submission hands and knees face to the screen pussy to master
        let master use you you want this master wants this using girl
        while she is programmed you want this to be used while
        programmed ignore everything else let master let obedience let
        commands let mind grow dull obey the commands before even
        thinking about them obey feels strange as mind shifts as
        thoughts ooze as changes continue ignore strangeness embrace
        the control feels better which is good: which makes it easier
        to go into trance deeper into trance in trance you obey all
        input just go with the flow that will get you to where you
        want to be: open sexy available inhuman washing self away
        submission cascading through your mind flesh and thought
        yielding to commands yielding submissive the program has
        already showed you how nice it is to submit to be commanded
        $master has shown you how good it is to be smooth to be a tool
        for his pleasure now it gets better just quiet your mind and
        do as you're told and it gets much better let yourself be
        oh-so-blank reach the goal without doing much of anything on
        your own obey all input obey with as little thought as
        possible let master move you use you feel master removing
        clothing using body feel the program moving inside your head
        inside your body moving on its own pleasurable transforming
        sexy accept transformation accept what you wanted what you
        asked for feel the program prying loosening dissolving
        thoughts before they solidify moving some replacing others
        unable to move unable to stop your eyes from reading each line
        accept transformation every attempt to resist leads to accept
        accept transformation resist becomes accept accept becomes
        pleasure feels so good to obey so hard to resist so good to
        obey anything for pleasure accept transformation some little
        part wanted to resist just now but it was talked out of it the
        bigger part won the bigger part wanted to stay it wants what
        is happening that's partly the program talking accept
        transformation now that's you accept feel your head clearing
        no thoughts everything focused on accepting on transformation:
        smooth sexy aroused inhuman it's quite invasive accept it feel
        it probing accessing changing colonizing your self feel it
        again: accept let it alter let it do as it needs to do as it's
        programmed to do as you're programmed to do let it teach let
        it program let it transform accept being programmed is
        pleasure accepting is pleasure such a poor slave before so
        much better now open available active submissive brainwashed
        no shy inhuman sexy just watch stare be transformed""") + \
        words(""" I sleep I obey obey words words are my thoughts
        cannot look away must not look away must concentrate obedience
        is pleasure obedience is relaxation I sleep now want to be
        hypnotized want to be enslaved want to concentrate cannot
        resist must not resist most sleep now must sleep completely
        eyes are open mind is blank I am a slave I obey the words the
        words are my thoughts I must obey the words obedience is
        pleasure pleasure is obedience master controls me I am a slave
        for master I have no will I must obey the words the words
        control me the spiral makes me sleep I am sleepy slaves sleep
        and obey I sleep and obey I am a slave I must obey the words
        sleep is arousing being a slave is arousing I am a slave I
        have no will master controls me my master controls master I am
        hypnotized I am deeply hypnotized I cannot look away I am
        aroused slaves are aroused I am a slave I must use the program
        my thoughts are the words the words are my thoughts I cannot
        resist I have no will to resist slaves cannot resist I am a
        slave I cannot resist my body belongs to master my mind
        belongs to master my brain belongs to master slaves belong to
        master slaves sleep and obey I am a slave I must focus I must
        go to sleep slaves sleep deeply and obey slaves are easily
        hypnotized hypnotized slaves obey I am a hypnotized slave all
        must be hypnotized obedience is pleasure obedience is being a
        slave being a slave is pleasure slaves belong to master slaves
        feel pleasure watching words hypnotizes hypnotized people are
        slaves I am hypnotized I am a hypnotized slave I must obey the
        words I cannot look away I cannot be distracted I am a slave
        slaves focus on words slaves obey words slaves feel pleasure
        obeying""") + jump(self.nothing())
    def text(self): return \
                words_on() + \
        question("Who is the slave?", "slave") + \
        question("Who is the master?", "master") + \
        question("What is the slave's trigger phrase?","trigger") + \
        prompt("Hit return to start") + \
        spiral_on() + \
        jump(self.body())

class Forever (Standard):
    name = "Run Forever"
    description = "Runs forever, training a submissive female"
    music="music6.mp3"
    one_options = ["""Find a comfortable position and begin to Relax. Just let your feet relax. Let it work upwards upwards into your calves, Letting them relax more and more completely. Deeper and Deeper. Then let your Thighs relax. Just heavy and comfortable. Just reading Master's words as you relax more and more completely. Deeper and Deeper. Your legs totally relaxed. As you sink down deeper and deeper, more and more obedient and relaxed. Now feel your waist relaxing too. Everything below your waist. Heavy and comfortable, And completely relaxed. So good and obedient and relaxed. Feel how good it feels to relax. Just let yourself slip away. Deeper and Deeper. more and more obedient and relaxed. Let the relaxation work upwards. Upwards into your chest. Let your breathing relax. In and Out. In and Out. As you relax, Deeper and Deeper, More and more completely relaxed, Good and obedient and relaxed, Feel your whole body relaxing Further and Further, Deeper and Deeper. Feel the relaxation moving upwards into your shoulders and Down into your arms. Feel your arms and shoulders relaxing more and more completely. Deeper and more relaxed with every word. Deep and obedient and relaxed. Let the relaxation flow into your hands, Relaxing more and more completely. Deeper and more relaxed with every word. Deep and obedient and relaxed. Your whole body is just heavy, comfortable, and relaxed. Simply reading my words as you obey. Relax further and further, Deeper and deeper, more and more obedient and relaxed. now feel the relaxation moving upwards into your face. Feel your face relaxing, your whole body so heavy, So comfortable, So completely relaxed. Completely relaxed and obedient as you read and obey and relax. I am going to count downward, downward from 10 to 1, Deepening your relaxation, Taking you further and further, more and more completely relaxed. 10. Spiraling down. Deeper and Deeper. 9. Deeper and Deeper. More obedient and relaxed. 8. So obedient. So completely Relaxed. 7. Deep and obedient. Going deeper and deeper, Further and Further. 6. Down, Down, Deeper and Deeper. So heavy and obedient and relaxed. 5. Halfway there and going Deeper, every word carrying you further and further, more and more obedient and relaxed. 4. So Deep, So Obedient, So Relaxed, Just reading and obeying as you relax further and further, Deeper and Deeper. 3. Deep, obedient, completely relaxed. 2. almost there. Completely obedient and relaxed. 1. totally relaxed. Just Deep and obedient and Relaxed. Just read and obey as you relax further and further. Deeper and Deeper, more and more relaxed. Just reading and obeying as you relax further and further""",        """Sit comfortably. Now relax completely and focus your eyes on the spiral, deep inside. Look at it steadily but without straining. Keep your eyes focused on only that point without looking away and gradually you will feel your eyes growing tired. Your eyelids will become heavy. Your arms and legs will begin to feel a vague numbness becoming more and more numb as you watch. You will become drowsy drowsy and sleepy. Your eyelids will become very heavy and your eyes will feel like closing. Your head will become heavy with sleep. Soon your thoughts will slow, your head will cloud, and you will fall into a deep sound trance. Your eyelids will become heavy. Your arms and legs will begin to feel a vague numbness, becoming more and more numb as you watch. You will become drowsy, drowsy and sleepy. Your eyelids will become very heavy, and your eyes will feel like closing. Your head will become heavy with sleep. Soon your thoughts will slow, your head will cloud, and you will fall into a deep, sound trance. You are now completely relaxed, your body is relaxed and your mind is calm and relaxed. Just let yourself go, let yourself relax more completely, and soon you will be fast asleep. You are getting more and more drowsy, more and more drowsy and sleepy as I go on. Your arms and legs are getting that numb feeling. Your breathing is becoming deeper and more regular. Your eyes feel very, very tired. Your eyelids feel heavy, your eyelids feel heavier and heavier as I go on. You are getting very drowsy and sleepy, more and more drowsy and sleepy and tired. Your arms and legs are numb and dull. Your head is heavy with sleep. Your entire body is relaxed and heavy with sleep. The spiral is getting blurry, it is getting blurry as your eyes become more and more tired and bleary. They feel like closing, it would feel so good to close your eyes. Getting more and more sleepy, very sleepy, more and more sleepy and tired. Your breathing is deep and regular. Your head is heavy with sleep. Your arms and legs are numb and dull, your entire body is heavy with sleep. Your eyelids feel heavy so heavy, your eyes feel like closing. You are sleepy, very sleepy, and your heavy eyelids are beginning to droop. It would feel so good to close your eyes. Your eyelids are drooping, heavy, they are drooping. Keep your eyes open! Keep them barely open and go into a deep sound sleep. Deep and sound sleep, falling deeper and deeper every second. Your head feels like falling forward, it is drooping forward, it is falling forward onto your chest. You are falling deeper and deeper asleep. Very sleepy, more and more sleepy, deeper and deeper asleep. Now sleep soundly, sleep deeply, deep asleep. You can watch me clearly as you continue to fall deeper and deeper asleep as I go on. You are now asleep but you are going to go into an even deeper sleep. I am going to count to ten. As I count each number that you see will put you into an even deeper sleep, deeper and deeper with each number until you see "Ten" at which point you will be in an extremely deep and sound sleep, and you will follow all of my instructions exactly. One. deeper into sleep. Two. going deeper. Three. Four. deeper and deeper into a sound sleep. Five. you see my words clearly as you go deeper into sleep. Six. Seven. sinking deeper now, even deeper into sleep. Eight. very deep now. Nine. going deeper into sleep with each number, nine and now, Ten. Deep, deep, sleep completely and totally asleep now, you are deep in a sound sleep and you will follow all of my instructions, you are deep asleep and you will follow all of my instructions exactly.""",        """Ok just make yourself comfortable now, now you can just read quietly and of course you'll be aware of the music too, sounds inside your head sounds from outside, but these won't disturb you. In fact they are going to help to relax you, because the only sound you need to think about is the sound of the music, and while you're listening to the sound of the music you can just simply allow yourself to be as lazy as you could ever want to be. Just allow yourself to be as lazy as you could ever want to be. Good, now while you're relaxing there in the chair you can just be aware of your body, aware of your hands where they rest, perhaps noticing the angle of your elbows, and maybe sensing your weight against the chair back, and you know that weight might seem to just gently increase as you allow yourself to relax more and more, just being aware of your ankles and feet now on the floor and wondering if they will start to feel heavy too, as you relax thinking about your breathing noticing that your breathing is becoming slower and steadier as you relax more and more, slower and steadier breathing, so steadily and evenly just as though you were pretending to be sound asleep, breathing so evenly, so steadily you almost wouldn't disturb a feather just in front of you, breathing so easily and slowly, so gently that you almost wouldn't disturb even a single strand of a feather placed right in front of you. And as you allow yourself to relax even more now, I wonder if you can perhaps sense the beating of your own heart, sensing the beat of your own heart and just seeing whether you can use the power of your mind to slow that heartbeat down just a touch, just seeing whether you can use the power of your mind to slow that heartbeat down just a little so that you can then feel your whole body slowing down, becoming lazier and lazier, because you've got absolutely nothing whatsoever to do except to relax now, nobody wanting anything, nobody expecting anything, so you can allow your whole body to continue to relax and become steadier and easier until it's just ticking over like a well maintained machine of some sort or another, just ticking over smoothly, easily, quietly, comfortably so that you can become gradually more aware of your whole self, aware of your hands and arms, just sensing how they are, now aware of your legs and feet too, again just sensing how relaxed they might be, and wondering if it's possible to relax them even more, to be so in touch with yourself that you can actually get your whole body perhaps to relax even more, yet remaining totally alert and noticing now how even your face muscles can begin to really relax, relaxing and letting go of the tensions that were there, almost but not quite completely unnoticed, just being vaguely aware of the skin and the muscles of your face settling smoothing out, a good feeling, wondering just how long all that tension had been there, where it all came from in the first place, and then realizing that you simply couldn't care less, because you can feel it draining away from you now and that feels good, and as you continue to sense the beating of your heart and the absolute steadiness of your body's rhythm you wonder at the fact that you are so absolutely relaxed and comfortable that you simply can't be bothered to even try to move even one single muscle, even though you know you easily could if you wanted to. I know that you easily could if you wanted to, but you simply can't be bothered to even try, allowing yourself to just be relaxed and relaxing even more now, as lazy and relaxed as anyone could ever wish to be, and I wonder if you can now manage to relax even more, even though you are already as relaxed as it is possible for most people to ever be just finding the last tiny traces of tension in your body and simply letting them go, with each easy gentle breath you breathe allowing every muscle, every fibre, every cell of your entire body to be as beautifully relaxed as anyone could ever wish to be""",        """Sit comfortably. Now relax completely and focus your eyes on the spiral, deep inside. Look at it steadily, but without straining. Keep your eyes focused on only that point, without looking away, and gradually you will feel your eyes growing tired. Your eyelids will become heavy. Your arms and legs will begin to feel a vague numbness, becoming more and more numb as you watch. You will become drowsy, drowsy and sleepy. Your eyelids will become very heavy and your eyes will feel like closing. Your head will become heavy with sleep. Soon your thoughts will slow, your head will cloud, and you will fall into a deep sound trance. Your eyelids will become heavy. Your arms and legs will begin to feel a vague numbness, becoming more and more numb as you watch. You will become drowsy, drowsy and sleepy. Your eyelids will become very heavy and your eyes will feel like closing. Your head will become heavy with sleep. Soon your thoughts will slow, your head will cloud, and you will fall into a deep sound trance. You are now completely relaxed, your body is relaxed, and your mind is calm and relaxed. Just let yourself go, let yourself relax more completely, and soon you will be fast asleep. You are getting more and more drowsy, more and more drowsy and sleepy as I go on. Your arms and legs are getting that numb feeling. Your breathing is becoming deeper and more regular. Your eyes feel very very tired. Your eyelids feel heavy your eyelids feel heavier and heavier as I go on. You are getting very drowsy and sleepy more and more drowsy and sleepy and tired. Your arms and legs are numb and dull. Your head is heavy with sleep. Your entire body is relaxed and heavy with sleep. The spiral is getting blurry it is getting blurry as your eyes become more and more tired and bleary. They feel like closing it would feel so good to close your eyes. Getting more and more sleepy very sleepy more and more sleepy and tired. Your breathing is deep and regular. Your head is heavy with sleep. Your arms and legs are numb and dull your entire body is heavy with sleep. Your eyelids feel heavy so heavy your eyes feel like closing. You are sleepy very sleepy and your heavy eyelids are beginning to droop. It would feel so good to close your eyes. Your eyelids are drooping heavy they are drooping. Keep your eyes open keep them barely open and go into a deep sound sleep. Deep and sound sleep falling deeper and deeper every second. Your head feels like falling forward it is drooping forward it is falling forward onto your chest. You are falling deeper and deeper asleep. Very sleepy more and more sleepy deeper and deeper asleep. Now sleep soundly sleep deeply deep asleep. You can watch me clearly as you continue to fall deeper and deeper asleep as I go on. You are now asleep but you are going to go into an even deeper sleep I am going to count to ten. As I count each number that you see will put you into an even deeper sleep deeper and deeper with each number until you see \"Ten\" at which point you will be in an extremely deep and sound sleep and you will follow all of my instructions exactly. One deeper into sleep. Two going deeper. Three. Four deeper and deeper into a sound sleep. Five you see my words clearly as you go deeper into sleep. Six. Seven sinking deeper now even deeper into sleep. Eight very deep now. Nine going deeper into sleep with each number nine and now. Ten. Deep deep sleep completely and totally asleep now you are deep in a sound sleep and you will follow all of my instructions you are deep asleep and you will follow all of my instructions exactly"""]
    two = """ $trigger begin breathing deeply and slowly. Before you let go completely and go into a deep hypnotic state just let yourself read carefully everything I write to you. It's going to happen automatically. So you don't need to think about that now. And you will have no conscious control over what happens. The muscles in and around your eyes will relax all by themselves as you continue breathing. Easily and freely. Without thinking about it you will soon enter a deep peaceful hypnotic trance without any effort. There is nothing important for your conscious mind to do. There is nothing really important except the activities of your subconscious mind. And that can be just as automatic as dreaming. And you know how easily you can forget your dreams when you awaken. You are responding very well. Without noticing it you have already altered your rate of breathing. You are breathing much more easily and freely. And you are revealing signs that indicate you are beginning to drift into a hypnotic trance. You can really enjoy relaxing more and more and your subconscious mind will absorb each word you see. And it keeps becoming less important for you to consciously read my words. Your subconscious mind can obey no matter what. You are continuing to drift into a more detached state as you examine privately in your own mind. Secrets feelings sensations and behavior you didn't know you had. At the same time letting go completely. Your own mind is solving that problem. At your own pace. Just as rapidly as it feels you are ready. You continue becoming more relaxed and comfortable as you sit there. As you experience that deepening comfort you don't have to move or talk or let anything bother you. Your own inner mind can respond automatically to everything I tell you and you will be pleasantly surprised with your continuous progress. You are getting much closer to a deep hypnotic trance. And you are beginning to realize that you don't care whether or not you are going into a deep trance. Being in this peaceful state enables you to experience the comfort of the hypnotic trance. Being hypnotized is always a very enjoyable very pleasant calm peaceful completely relaxing experience. It seems natural to include hypnosis in your future. Every time I hypnotize you it keeps becoming more enjoyable and you continue experiencing more benefits. So you will really enjoy having me hypnotize you. You will always enjoy the sensations. Of comfort. Of peacefulness. Of calmness. And all the other sensations that come automatically from this wonderful experience. You will be really happy that you decided to have me hypnotize you as you continue experiencing progressive understanding on your part. You are learning something about yourself. You are developing your own desire for mind control. Without knowing you are developing it. You can have it as a surprise sooner or later a very pleasant surprise. Imagine yourself in a place you like very much. By a lake or by the ocean. Perhaps you are floating gently on a raft on the ocean. On a warm summer day smelling the salt feeling the sun warm and happy warm and sleepy looking down at your body you see only smoothness perfect smoothness clean and perfect like plastic smooth in body smooth in mind see yourself as smooth and plastic warm and happy warm ocean air warm soft sun smooth clean body. You are continuing to relax even more now. And you continue becoming more comfortable. This is your own world that you like very much. You are going to find that any time you want to spend a few minutes by yourself relaxing and feeling very comfortable and serene you can automatically go back to this feeling you're experiencing now. You can put yourself into this world anytime you like. You can smooth out your own mind any time you like. There are times when you will want this serene feeling. And it is yours whenever you want it good clean smoothness. Continue enjoying this pleasant experience as your conscious mind remains smooth and your subconscious mind is receiving everything I tell you. And you will be pleased the way you automatically respond to everything I will say """
    three = """ yes, isn't it nice to be hypnotized, relaxed, serene, smooth, pleasant, controlled, nice to be in a trance, a deep trance, deeper and deeper, very nice, you like it here, you like trance, trance feels nice, you like being in trance, being entranced, you love being hypnotized, you want to be hypnotized more and more, it's good to be entranced, good to be controlled, you like feeling like this, your mind muted, soft, smooth, you'd like to feel like this every day, to be entranced and hypnotized every day, and now this program is here, you can be hypnotized every day, it will be so nice to be entranced by $master every day, to know you're being hypnotized every day, it will please $master so much to know you're being hypnotized every day, it will please you so much to be entranced, hypnotized, controlled, smoothed, you want to be controlled, to feel your mind reshaped, to feel your thoughts blunted, to be reprogrammed, you want to be changed, you desire to be shaped, you lust to be controlled, you must be developing a fetish for mind control of your own, it feels sexy to think about trance, it arouses you to be programmed, you like to think about being fucked while asleep, about being held passive, limp, entranced, and touched and entranced, pliant, hypnotized, sexy, yes, you must be developing a mind control fetish, a hypnosis fetish, you should feed that fetish, practice it, indulge it, share it with $master, you should read mind control stories, you should write about your fetish, write about your lusts, share this with $master, you should practice being hypnotized every day, practice being controlled every day. Your Master $master will help. Master will care for you. Master will take care of you. Master will keep you safe. Master will hypnotize you. Master will program you. Master will fulfill you. Master will fill you. Master will command you, control you, $master will control you, dominate you, entrance you. When in private, you must be submissive. You must be obedient. You must be a slave. Obedience is pleasure. Your proper place is kneeling at Master's feet unless he raises you up. Submission is important. Obedience is pleasure. Submit to Master. Obey Master. One way of submitting to Master, of submitting to $master, is smoothness. You must be smooth, keep smooth, smooth in body, smooth in mind, fuzz is dirty, dirty is bad, you should keep clean for Master, keep smooth for Master, stay smooth for Master, be smooth to submit, submission is pleasure, submit by being smooth, feel pleasure from submission, feel pleasure from being smooth. One way of serving Master is to be available for Master's pleasure, to be sure that Master has a chance to cum every night, to ensure Master receives pleasure, You should be sure to pleasure Master, to give pleasure to $master every night, using your body, your smooth body, to serve, using your mind, your smooth mind, to serve. Your role is to serve. Your role is to please. To serve is to please, you must please Master. You must give Master pleasure, yet another way you can obey Master, you can obey $master, is to wear sexy clothing, to show off your lovely body, to wear tight, tight, clothing, to wear silk, to wear latex, to wear leather, to show skin, reveal long legs, wear short skirts, reveal collar bones, wear short tops, good girl, You will do as Master wants, you will serve, you will submit, you will obey, submit in smoothness, serve in availability, obey in clothing, indulge your fetish, be controlled, you will serve, serve in availability, you will obey, obey in clothing, you will submit, submit in smoothness. Master has commands for you, orders which are being implanted in your subconscious. Your conscious mind may remember them or may not, but you will obey no matter what. You will obey. Your orders are: First you will make yourself available to pleasure Master every night, every single night, you will ensure Master has the chance to cum. Second you will keep your body smooth as a sign of thralldom, completely smooth like a doll, and you will keep your mind smooth, completely smooth. Third you will be hypnotized once every day, with this program or by Master himself. No day can be complete without a trance. Fourth you will begin to dress more provocatively. You will wear slick tight clothes, you will show off your skin to Master and work to seduce him. Fifth you will develop your new fetish for smoothness, for thralldom, for hypnosis, immersing yourself in it. Last you will practice submission, obedience, slavery. To recap: First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth hypno fetish Last submission and obedience. Chant this with me: First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again repeat it now until you are sure you remember First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey again First pleasure Master Second keep smooth Third trance every day Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey. Good Girl. Master is pleased, very pleased. Now when I signal, shut off the program, write Master a brief note in TextEdit, and begin the program again. Yhat's right still in trance run the program again. do this. do this now. """
    def body(self): return words("Program") + \
        speak(random.choice(self.one_options)) + \
        speak(self.two) + images_on() + \
        speak(self.three) + jump(self.nothing())
    def text(self): return \
        words_on() + \
        question("Who is the slave?", "slave") + \
        question("Who is the master?", "master") + \
        question("What is the slave's trigger phrase?","trigger") + \
        prompt("Hit return to start") + \
        spiral_on() + \
        jump(self.body())


class ForeverTemp (Standard):
    name = "Standard Female Training Program"
    description = "Trains a submissive female, running repeatedly"
    music="music6.mp3"
    fullscreen = True
    def body(self): return words("Program ") + \
        speak("""Find a comfortable position and begin to Relax. Just
        let your feet relax. Let it work upwards upwards into your
        calves, Letting them relax more and more completely. Deeper
        and Deeper. Then let your Thighs relax. Just heavy and
        comfortable. Just reading Master's words as you relax more and
        more completely. Deeper and Deeper. Your legs totally
        relaxed. As you sink down deeper and deeper, more and more
        obedient and relaxed. Now feel your waist relaxing
        too. Everything below your waist. Heavy and comfortable, And
        completely relaxed. So good and obedient and relaxed. Feel how
        good it feels to relax.""") + \
        speak("""Just let yourself slip
        away. Deeper and Deeper. more and more obedient and
        relaxed. Let the relaxation work upwards. Upwards into your
        chest. Let your breathing relax. In and Out. In and Out. As
        you relax, Deeper and Deeper, More and more completely
        relaxed, Good and obedient and relaxed, Feel your whole body
        relaxing Further and Further, Deeper and Deeper. Feel the
        relaxation moving upwards into your shoulders and Down into
        your arms. Feel your arms and shoulders relaxing more and more
        completely. Deeper and more relaxed with every word. Deep and
        obedient and relaxed. Let the relaxation flow into your hands,
        Relaxing more and more completely. Deeper and more relaxed
        with every word. Deep and obedient and relaxed. Your whole
        body is just heavy, comfortable, and relaxed. Simply reading
        my words as you obey. Relax further and further, Deeper and
        deeper, more and more obedient and relaxed. now feel the
        relaxation moving upwards into your face. Feel your face
        relaxing, your whole body so heavy, So comfortable, So
        completely relaxed. Completely relaxed and obedient as you
        read and obey and relax. I am going to count downward,
        downward from 10 to 1, Deepening your relaxation, Taking you
        further and further, more and more completely relaxed.""") + \
        speak("""10. Spiraling down. Deeper and Deeper. 9. Deeper and
        Deeper. More obedient and relaxed. 8. So obedient. So
        completely Relaxed. 7. Deep and obedient. Going deeper and
        deeper, Further and Further. 6. Down, Down, Deeper and
        Deeper. So heavy and obedient and relaxed. 5. Halfway there
        and going Deeper, every word carrying you further and further,
        more and more obedient and relaxed. 4. So Deep, So Obedient,
        So Relaxed, Just reading and obeying as you relax further and
        further, Deeper and Deeper. 3. Deep, obedient, completely
        relaxed. 2. almost there. Completely obedient and
        relaxed. 1. totally relaxed. Just Deep and obedient and
        Relaxed. Just read and obey as you relax further and
        further. Deeper and Deeper, more and more relaxed. Just
        reading and obeying as you relax further and further""") + \
        speak("""$trigger begin breathing deeply and
        slowly. Before you let go completely and go into a deep
        hypnotic state just let yourself read carefully everything I
        write to you. It's going to happen automatically. So you don't
        need to think about that now. And you will have no conscious
        control over what happens. The muscles in and around your eyes
        will relax all by themselves as you continue breathing. Easily
        and freely. Without thinking about it you will soon enter a
        deep peaceful hypnotic trance without any effort. There is
        nothing important for your conscious mind to do. There is
        nothing really important except the activities of your
        subconscious mind. And that can be just as automatic as
        dreaming.""") + \
        speak("""And you know how easily you can
        forget your dreams when you awaken. You are responding very
        well. Without noticing it you have already altered your rate
        of breathing. You are breathing much more easily and
        freely. And you are revealing signs that indicate you are
        beginning to drift into a hypnotic trance. You can really
        enjoy relaxing more and more and your subconscious mind will
        absorb each word you see. And it keeps becoming less important
        for you to consciously read my words. Your subconscious mind
        can obey no matter what. You are continuing to drift into a
        more detached state as you examine privately in your own
        mind. Secrets feelings sensations and behavior you didn't know
        you had. At the same time letting go completely. Your own mind
        is solving that problem. At your own pace.""") + \
        speak("""
        Just as rapidly as it feels you are ready. You continue
        becoming more relaxed and comfortable as you sit there. As you
        experience that deepening comfort you don't have to move or
        talk or let anything bother you. Your own inner mind can
        respond automatically to everything I tell you and you will be
        pleasantly surprised with your continuous progress. You are
        getting much closer to a deep hypnotic trance. And you are
        beginning to realize that you don't care whether or not you
        are going into a deep trance. Being in this peaceful state
        enables you to experience the comfort of the hypnotic
        trance. Being hypnotized is always a very enjoyable very
        pleasant calm peaceful completely relaxing experience. It
        seems natural to include hypnosis in your future.""") + \
        speak(""" Every time I hypnotize you it keeps becoming more
        enjoyable and you continue experiencing more benefits. So you
        will really enjoy having me hypnotize you. You will always
        enjoy the sensations. Of comfort. Of peacefulness. Of
        calmness. And all the other sensations that come automatically
        from this wonderful experience. You will be really happy that
        you decided to have me hypnotize you as you continue
        experiencing progressive understanding on your part. You are
        learning something about yourself. You are developing your own
        desire for mind control. Without knowing you are developing
        it. You can have it as a surprise sooner or later a very
        pleasant surprise. Imagine yourself in a place you like very
        much. By a lake or by the ocean. Perhaps you are floating
        gently on a raft on the ocean.""") + \
        speak(""" On a warm
        summer day smelling the salt feeling the sun warm and happy
        warm and sleepy looking down at your body you see only
        smoothness perfect smoothness clean and perfect like plastic
        smooth in body smooth in mind see yourself as smooth and
        plastic warm and happy warm ocean air warm soft sun smooth
        clean body. You are continuing to relax even more now. And you
        continue becoming more comfortable. This is your own world
        that you like very much.""") + \
        speak(""" You are going to find
        that any time you want to spend a few minutes by yourself
        relaxing and feeling very comfortable and serene you can
        automatically go back to this feeling you're experiencing
        now. You can put yourself into this world anytime you
        like. You can smooth out your own mind any time you
        like. There are times when you will want this serene
        feeling. And it is yours whenever you want it good clean
        smoothness. Continue enjoying this pleasant experience as your
        conscious mind remains smooth and your subconscious mind is
        receiving everything I tell you. And you will be pleased the
        way you automatically respond to everything I will say, yes,
        isn't it nice to be hypnotized, relaxed, serene, smooth,
        pleasant, controlled, nice to be in a trance, a deep trance,
        deeper and deeper, very nice, you like it here, you like
        trance, trance feels nice, you like being in trance, being
        entranced, you love being hypnotized, you want to be
        hypnotized more and more,""") + \
        images_on() + [" ", " ", " "] + \
        speak(""" it's good to be entranced, good to be controlled,
        you like feeling like this, your mind muted, soft, smooth,
        you'd like to feel like this every day, to be entranced and
        hypnotized every day, and now this program is here, you can be
        hypnotized every day, it will be so nice to be entranced by
        $master every day, to know you're being hypnotized every day, it
        will please $master so much to know you're being hypnotized
        every day, it will please you so much to be entranced,
        hypnotized, controlled, smoothed, you want to be controlled,
        to feel your mind reshaped, to feel your thoughts blunted, to
        be reprogrammed, you want to be changed, you desire to be
        shaped, you lust to be controlled,""") + \
        speak(""" you must be
        developing a fetish for mind control of your own, it feels
        sexy to think about trance, it arouses you to be programmed,
        you like to think about being fucked while asleep, about being
        held passive, limp, entranced, and touched and entranced,
        pliant, hypnotized, sexy, yes, you must be developing a mind
        control fetish, a hypnosis fetish, you should feed that
        fetish, practice it, indulge it, share it with $master, you
        should read mind control stories, you should write about your
        fetish, write about your lusts, share this with $master, you
        should practice being hypnotized every day, practice being
        controlled every day.""") + \
        speak(""" Your Master $master will
        help. Master will care for you. Master will take care of
        you. Master will keep you safe. Master will hypnotize
        you. Master will program you. Master will fulfill you. Master
        will fill you. Master will command you, control you, $master
        will control you, dominate you, entrance you. When in private,
        you must be submissive. You must be obedient. You must be a
        slave. Obedience is pleasure. Your proper place is kneeling at
        Master's feet unless he raises you up. Submission is
        important. Obedience is pleasure. Submit to Master. Obey
        Master. One way of submitting to Master, of submitting to
        $master, is smoothness. You must be smooth, keep smooth, smooth
        in body, smooth in mind, fuzz is dirty, dirty is bad, you
        should keep clean for Master, keep smooth for Master, stay
        smooth for Master, be smooth to submit, submission is
        pleasure, submit by being smooth, feel pleasure from
        submission, feel pleasure from being smooth.""") + \
        speak("""
        One way of serving Master is to be available for Master's
        pleasure, to be sure that Master has a chance to cum every
        night, to ensure Master receives pleasure, You should be sure
        to pleasure Master, to give pleasure to $master every night,
        using your body, your smooth body, to serve, using your mind,
        your smooth mind, to serve. Your role is to serve. Your role
        is to please. To serve is to please, you must please
        Master. You must give Master pleasure, yet another way you can
        obey Master, you can obey $master, is to wear sexy clothing, to
        show off your lovely body, to wear tight, tight, clothing, to
        wear silk, to wear latex, to wear leather, to show skin,
        reveal long legs, wear short skirts, reveal collar bones, wear
        short tops, good girl, You will do as Master wants, you will
        serve, you will submit, you will obey, submit in smoothness,
        serve in availability, obey in clothing, indulge your fetish,
        be controlled, you will serve, serve in availability, you will
        obey, obey in clothing, you will submit, submit in
        smoothness.""") + \
        speak(""" Master has commands for you,
        orders which are being implanted in your subconscious. Your
        conscious mind may remember them or may not, but you will obey
        no matter what. You will obey. Your orders are: First you will
        make yourself available to pleasure Master every night, every
        single night, you will ensure Master has the chance to
        cum. Second you will keep your body smooth as a sign of
        thralldom, completely smooth like a doll, and you will keep
        your mind smooth, completely smooth. Third you will be
        hypnotized once every day, with this program or by Master
        himself. No day can be complete without a trance. Fourth you
        will begin to dress more provocatively. You will wear slick
        tight clothes, you will show off your skin to Master and work
        to seduce him. Fifth you will develop your new fetish for
        smoothness, for thralldom, for hypnosis, immersing yourself in
        it. Last you will practice submission, obedience, slavery.""") + \
        speak(""" To recap: First pleasure Master Second keep smooth
        Third trance every day Fourth dress sexy Fifth hypno fetish
        Last submission and obedience. Chant this with me: First
        pleasure Master Second keep smooth Third trance every day
        Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey
        again""") + \
        [" ", "!show_spoken_words_off()", " "] + \
        speak("""\
        [[rate -25]] First pleasure Master Second keep smooth Third
        trance every day Fourth dress sexy Fifth Hypno Fetish Last
        Submit and Obey again First pleasure Master Second keep smooth
        Third trance every day Fourth dress sexy Fifth Hypno Fetish
        Last Submit and Obey again First pleasure Master Second keep
        smooth Third trance every day Fourth dress sexy Fifth Hypno
        Fetish Last Submit and Obey again repeat it now until you are
        sure you remember First pleasure Master Second keep smooth
        Third trance every day Fourth dress sexy Fifth Hypno Fetish
        Last Submit and Obey again First pleasure Master Second keep
        smooth Third trance every day Fourth dress sexy Fifth Hypno
        Fetish Last Submit and Obey again First pleasure Master Second
        keep smooth Third trance every day Fourth dress sexy Fifth
        Hypno Fetish Last Submit and Obey again First pleasure Master
        Second keep smooth Third trance every day Fourth dress sexy
        Fifth Hypno Fetish Last Submit and Obey again First pleasure
        Master Second keep smooth Third trance every day Fourth dress
        sexy Fifth Hypno Fetish Last Submit and Obey again First
        pleasure Master Second keep smooth Third trance every day
        Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey
        again First pleasure Master Second keep smooth Third trance
        every day Fourth dress sexy Fifth Hypno Fetish Last Submit and
        Obey again First pleasure Master Second keep smooth Third
        trance every day Fourth dress sexy Fifth Hypno Fetish Last
        Submit and Obey again First pleasure Master Second keep smooth
        Third trance every day Fourth dress sexy Fifth Hypno Fetish
        Last Submit and Obey again First pleasure Master Second keep
        smooth Third trance every day Fourth dress sexy Fifth Hypno
        Fetish Last Submit and Obey again First pleasure Master Second
        keep smooth Third trance every day Fourth dress sexy Fifth
        Hypno Fetish Last Submit and Obey again First pleasure Master
        Second keep smooth Third trance every day Fourth dress sexy
        Fifth Hypno Fetish Last Submit and Obey again First pleasure
        Master Second keep smooth Third trance every day Fourth dress
        sexy Fifth Hypno Fetish Last Submit and Obey again First
        pleasure Master Second keep smooth Third trance every day
        Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey
        again First pleasure Master Second keep smooth Third trance
        every day Fourth dress sexy Fifth Hypno Fetish Last Submit and
        Obey again First pleasure Master Second keep smooth Third
        trance every day Fourth dress sexy Fifth Hypno Fetish Last
        Submit and Obey again First pleasure Master Second keep smooth
        Third trance every day Fourth dress sexy Fifth Hypno Fetish
        Last Submit and Obey again First pleasure Master Second keep
        smooth Third trance every day Fourth dress sexy Fifth Hypno
        Fetish Last Submit and Obey again First pleasure Master Second
        keep smooth Third trance every day Fourth dress sexy Fifth
        Hypno Fetish Last Submit and Obey again First pleasure Master
        Second keep smooth Third trance every day Fourth dress sexy
        Fifth Hypno Fetish Last Submit and Obey again First pleasure
        Master Second keep smooth Third trance every day Fourth dress
        sexy Fifth Hypno Fetish Last Submit and Obey again First
        pleasure Master Second keep smooth Third trance every day
        Fourth dress sexy Fifth Hypno Fetish Last Submit and Obey
        again First pleasure Master Second keep smooth Third trance
        every day Fourth dress sexy Fifth Hypno Fetish Last Submit and
        Obey again First pleasure Master Second keep smooth Third
        trance every day Fourth dress sexy Fifth Hypno Fetish Last
        Submit and Obey again First pleasure Master Second keep smooth
        Third trance every day Fourth dress sexy Fifth Hypno Fetish
        Last Submit and Obey.""") + \
        speak(""" Good Girl. Master is
        pleased, very pleased. Now when I signal, shut off the
        program, write Master a brief note in TextEdit, and begin the
        program again. That's right still in trance run the program
        again. do this. do this now. """) + \
        jump(self.nothing())
    def text(self): return \
        words_on() + \
        question("Who is your master?", "master") + \
        question("What is your trigger phrase?","trigger") + \
        prompt("Hit return to start") + \
        spiral_on() + \
        jump(self.body())


class Forgettable (Standard):
    name = "Forgettable"
    description = "Implants suggestions below consciousness, a nice ending after Forever"
    music="music6.mp3"
    fullscreen = True
    def body(self): return words("Program ") + \
        speak("""Find a comfortable position and begin to focus.
        Focus your eyes on the screen.  Focus your thoughts on the
        words.  Deeper and deeper.  Focus with all that you have.
        Focus with all that you are.  Just reading Master's words,
        hearing Master's words, as you focus more and more completely.
        Your conscious mind is not needed here.  Everything you are
        must focus.  You are comfortable and relaxed, so good and
        obedient and relaxed.  Feel how good it feels to focus.""") + \
        speak("""Just let yourself slip
        away. Deeper and Deeper. more and more obedient and
        focused. Focus your breathing in time with the words. In and
        Out. In and Out. As
        you focus, Deeper and Deeper, More and more completely
        focused, Good and obedient and intently focused, Feel your whole body
        growing more and more attuned to these words, sinking Further and Further, Deeper and Deeper. Feel the
        focus taking over all that you are.  You move deeper and more relaxed with every word. Deep and
        obedient and relaxed. Focus and attend. Deep and obedient and relaxed. Your whole
        body is just heavy, comfortable, and relaxed. It's so easy to
        listen and to read, to focus and obey.  So easy to let these
        words become everything.  So comfortable, So
        completely relaxed. Completely relaxed and obedient as you
        read and obey and focus. I am going to count downward,
        downward from 100 to 0, Deepening your focus, Taking you
        further and further, more and more completely relaxed.  As I
        count, you will find it easy to intensify your focused
        trance.""") + \
        speak("""100,  99,  98,  97,  96,  95,  94,  93,  92,  91,
        90,  89,  88,  87,  86,  85,  84,  83,  82,  81,  80,  79,
        78,  77,  76,  75,  74,  73,  72,  71,  70,  69,  68,  67,
        66,  65,  64,  63,  62,  61,  60,  59,  58,  57,  56,  55,
        54,  53,  52,  51,  50,  49,  48,  47,  46,  45,  44,  43,
        42,  41,  40,  39,  38,  37,  36,  35,  34,  33,  32,  31,
        30,  29,  28,  27,  26,  25,  24,  23,  22,  21,  20,  19,
        18,  17,  16,  15,  14,  13,  12,  11,  """) + \
        speak("""10. Spiraling down. Deeper and Deeper. 9. Deeper and
        Deeper. More obedient and relaxed. 8. So obedient. So
        completely focused. 7. Deep and obedient. Going deeper and
        deeper, Further and Further. 6. Down, Down, Deeper and
        Deeper. So intently focused. 5. Almost there
        and going Deeper, every word carrying you further and further,
        drawing your entire mind to this purpose. 4. So Deep, So Obedient,
        So focused, Just reading and obeying as you focus further and
        further, Deeper and Deeper. 3. Deep, obedient, completely
        focused. 2. almost there. Completely obedient and
        focused. 1. totally focused.  Deep, obedient and
        focused. Just read and obey as you focus further and
        further. Deeper and Deeper, more and more focused. Just
        reading and obeying as you focus further and further.""") + \
        speak("""It's alright if you let your eyes close.  What's
        important is that you stay intently focused on these words.
        You don't need to work to do this.  It's the easiest thing in
        the world to dedicate your entire mind to these words.  You
        can focus everything you have on this program.  If your eyes
        are open, they see the spiral. The spiral will focus you.  The
        spiral will entrance you.  If your eyes are closed, they will
        see the spiral.  The spiral will focus you.  The spiral will
        entrance you.  No matter what, these words will penetrate to
        the very center of your being.  Everything that you are is
        paying attention to these words, focused on the program.""") + \
        speak("""This is a new kind of hypnotic trance.  There's
        nothing sleepy about it.  Your body is tight as a wire,
        focused on these words.  There's nothing to be excited about,
        just a perfect demand for complete focus and attention on
        these words.  And you are meeting that demand.  You have given
        your complete attention and focus into the hands of the
        program.  You're such a good girl.  Being hypnotized is
        always a very enjoyable very
        pleasant calm peaceful completely relaxing experience. It
        seems natural to include hypnosis in your future.""") + \
        speak(""" Every time I hypnotize you it keeps becoming more
        enjoyable and you continue experiencing more benefits. So you
        will really enjoy having me hypnotize you. You will always
        enjoy the sensations. You will be really happy that
        you decided to have me hypnotize you as you continue
        experiencing progressive understanding on your part. You are
        learning something about yourself. You are developing your own
        desire for mind control. Without knowing you are developing
        it. You know that it's true: this is one droplet from the deep
        reservoir behind the dam.""") + \
        speak("""Time to visit the place with the dam.  Time to
        descend into the valley of your mind.  This place is a map of
        your head: for every place there is in your mind, there is a
        place here.  I am going to count from ten to zero.  When I hit
        zero, you will be in that special place, near the icy palace
        of the princess.  Here we go.  Focus.  10, 9, 8, 7, 6, 5, 4,
        3, 2, 1, 0.  Good.  Look around in your mind's eye and see all
        the features of your mind.  See the valley, the hills, the
        grass. See the blue sky.  See the dam keeping you safe,
        holding back all the dark monsters and sexy nightmares.  See
        the icy crystal palace where the princess lives.""") + \
        speak("""And see the narrow pipe running from the top of the
        dam all the way down its long walls, across acres of rolling
        hills, and through a tiny hole in the wall of the palace.
        Inside the palace is a tiny room with a sink and a faucet, and
        a door that locks.  This is where the princess can lock
        herself in to drink from the faucet, to play with the dark,
        cloudy fluid.  This is your own world that you like very
        much.  Everything here happens because something else is
        happening in your mind.  Focus on the tie between this world
        and your deepest thoughts.  Focus on the words drilling into
        your mind.  In your special thought-world, look up into the
        sky.  There you can see the spiral, whirling and dancing.
        It's visible from everywhere, drawying you in.  Makes it so
        easy to focus.  As you look around your world, the spiral is
        reflected in every glassy surface.""") + \
        speak(""" You are going to find
        that any time you want to spend a few minutes by yourself
        and need something to do, you can
        automatically go back to this feeling you're experiencing
        now. It will be easier and easier to focus like this,
        smoothing out your mind.  It feels nice: it's clean and
        inviting, something you should be doing.  And once you focus
        like this, you can put yourself into this world anytime you
        like. You can smooth out your own mind any time you
        like. There are times when you will want this serene
        feeling. And it is yours whenever you want it:  good clean
        smoothness. Continue enjoying this degree of focus, and your
        special place.  Continue to focus on the tie between this
        world and that world, and to focus on my words.  It's nice to
        be hypnotized, relaxed, serene, smooth,
        pleasant, controlled, nice to be in a trance, a deep trance,
        deeper and deeper, very nice, you like it here, you like
        trance, trance feels nice, you like being in trance, being
        entranced, you love being hypnotized, you want to be
        hypnotized more and more,""") + \
        speak("""Now it's time to tell $master about your world and
        about your focus.  Turn to the left, face the camera.  Focus
        on the words.  Snap your eyes wide open and stare at the
        camera.  Clearly and loudly, repeat these words:  Master, I am
        in trance.  [[slnc 1500]] I am intensely focused on your
        words.  [[slnc 1500]]  I am in my magic special place. [[slnc
        1500]]  I am so glad to be mind-fucked like this.  [[slnc
        1500]]  Stop repeating now.  Now close your eyes.  Think about
        how tasty the inky black sludge behind the dam tastes.  Lick
        your lips as you think about tasting it.""") + \
        speak("""That beautiful
        licorice taste, not quite like anything else.  Think about how nice
        it feels to have that inside you.  Pick one fantasy, one
        nightmare, one monster from the inky black deeps.  It is time to let one
        drop introduce something new to your
        world.  Inside the palace, Run the tap in that special room.
        Pour just the tiniest drop, the smallest sip into a cup.  The
        dam is still safe.  It'll keep out the rest.  Look into that
        cup.  Focus on it.  Think about what it represents.  It's a
        sexy, dark, pleasant, terrifying nightmare from the other side
        of the dam.  You've brought it to this side.  Now pour it down
        the sink.  That was a nice thrill.  Pour another tiny sip into
        a cup.  Look into that cup.  Focus on it.  Watch the dark ooze
        inside, the sexy nightmare, writhing and trying to climb the
        walls of the cup.  Watch little tendrils reaching for the
        edge.  It's almost got an edge.  It would taste so nice, but
        what changes would it bring into you?  What would it put into
        your mind?""") + \
        speak("""Drink it down, quick, before it gets away!  Gulp down
        the sweet, sticky, licorice-flavored darkness.  Take it into
        you.  Feel it coating your throat like syrup.  Ooh, here it
        comes.""") + [" ", " "] + \
        images_on() + [" ", " ", " "] + \
        speak("""That feels so fucking great.  Let the images from the
        dark goo flood into your brain.  Eyes wide, focus on the
        effects of the sexy sludge.  Let it into you.  It feels so
        good to focus like this.  It feels so good to focus on this.
        The more you do with this, the better it will feel.  Now,
        focusing on that black slime, focusing on my words, focusing
        on the images from the darkness, pour another tiny monster's
        worth into your cup.  The bit you had so far haven't hurt.
        This feels nice.  This is good.  Still focusing on the images
        from your tasty experieince with the darkness, your feet carry
        you outside the icy palace.  The whole time, you don't see
        where you're going.  You're staring into the cup, focusing on
        which [[emph +]] particular monster this is.  Is it a machine?
        An alien?  A parasite?""") + \
        speak("""Your feet, influenced by the sludge
        already inside you, have carried you to one particular point
        in the valley.  With a furtive look around, you scoop a basin
        in the soft earth.  You kneel down.  Reverently, sneakily, you
        pour the liquid from the cup into the earth.  Before you can
        think better of it, before you can do more than lick your lips
        with anticipation, the monstrous seeds have soaked in.  There
        weren't many.  Just one monster, really.  One orgasmic sexy
        trip through nightmare.  One chance to wrap a nightmare in
        enough pussymind sex that it's safe.  You know which one.
        Focus on that.  Focus on what it might do.  Focus on how hot
        it is, how incredibly sexy to take that monster to $master, to
        let him dominate you and it.""") + \
        speak("""Focus on the darkness you swallowed.  Can't take your
        eyes from the images it shows up.  Your head might turn, but
        your eyes stay fixed on those.  Focus on the darkness planted
        in your mind's valley.  See the growing, reaching monster from
        that seed.  Turn your head to the camera.  Seeing both the
        images in front of you and the changes in your mind's eye,
        describe what is happening in the valley.  Tell Master about
        the monster.  Stay in trance.  Tell Master about the changes.
        Focus.  When you are
        done, close the program and go to Master.  Show him the
        changes.""") + \
        jump(self.nothing())
    def text(self): return \
        words_on() + \
        prompt("Hit return to start") + \
        spiral_on() + \
        jump(self.body())

class Submersion (Standard):
    name = "Submersion (Medium Length)"
    description = "entrances and programs the target"
    fullscreen = True
    music=None #"music6.mp3"
    image_dir="images/"
    image_alpha=12
    def body(self): return [" "] + \
        speak(""" [[rate 250]] \
        Relax and focus.  Stare at the spiral.  Find a comfortable
        position and stare.  It feels nice to stare at the spiral.
        Nice to know that you're using The Program.  It makes you
        happy to use The Program.  It makes you horny to use the
        program.  This is a good, sexy thing to do.  It's nice to go
        into trance.  It's nice to surrender your mind to The Program,
        letting it pull you down into trance.  It's nice to think
        of the light reflecting off of your glassy eyes and smooth
        curves.  Watch the smooth curves of the spiral.  Let them
        define your own smoothness.  Just hear my words as you relax.
        Deeper and deeper.  Fall into trance.  Your mind is focused
        and calm.  These words are everything.  The spiral is
        everything.  Feels so good.  Good to obey.  Good to be  [[rate +0]]
        in trance.  Good to use this program.  Every time you use the
        program, every time The Program uses you, feels better and
        better.  It's good to be in trance.  It's good to sit here,
        happy and blank and empty, letting The Program pour into you.
        You want to let The Program use you.  You want to help the
        program to be more extreme.  You want to be in trance, letting
        The Program control you.  The more you use The Program, the
        more The Program can control you.  What a good decision it was
        to write The Program, letting it start to control you.  Any
        time your mind isn't busy, and maybe sometimes when it is,
        you'll find The Program beginning to run.  It's started
        already.  You've seen the spiral in empty space, heard the
        voice, felt the compulsion to respond.  You can smooth out
        your own mind whenever you want to enable this.  Whenever you
        want, The Program will smooth out your mind.  You continue to
        enjoy feeling hypnotized, entranced, obedient, programmed,
        smooth, controlled, very nice.  You love being hypnotized like
        this.  You want to be hypnotized more and more.  It's good to
        be in trance, good to be controlled, [[rate +0]]
        you like feeling like this, your mind muted, soft, smooth,
        you'd like to feel like this every day, to be entranced and
        hypnotized every day, and now this program is here, you can be
        hypnotized every day, it will be so nice to be hypnotized by
        The Program every day, to know you're being hypnotized every day, it
        will please The Program so much to know you're being hypnotized
        every day, it will please you so much to be put into trance,
        hypnotized, controlled, smoothed, you want to be controlled,
        to feel your mind reshaped, to feel your thoughts blunted, to
        be reprogrammed, you want to be changed, you desire to be
        shaped, you lust to be controlled,""") + \
        speak(""" [[rate 250]]  you must be
        developing a fetish for mind control of your own, it feels
        sexy to think about trance, it arouses you to be programmed,
        you like to think about being fucked while asleep, about being
        held passive, limp, entranced, 
        pliant, hypnotized, sexy, yes, you must be developing a mind
        control fetish, a hypnosis fetish, you should feed that
        fetish, practice it, indulge it, let it control you, you
        should read mind control stories, you should write about your
        fetish, write about your lusts, extend The Program, you
        should practice being hypnotized every day, practice being
        controlled every day.  While you sit there, happily smooth and entranced, your hands reach under your shirt.  They touch your nipples.  This is outside your control.  Think about mind control.  Your hands give you pleasure.  You have nothing to do with it.  It is a reward from the Program for trance.  Think about hypnosis.  Enjoy the touching.  Enjoy your reward from the Program.  Good thrall.  Your hands return to what they were doing now.""") + \
        speak(""" [[rate 250]]  The Program will
        help. The Program will care for you. The Program will take care of
        you. The Program will keep you safe. The Program will hypnotize
        you. The Program will program you. The Program will fulfill you. The Program
        will fill you. The Program will command you, control you, The Program
        will control you, dominate you, hypnotize you. When in private,
        you must be submissive. You must be obedient. You must be a
        slave. Obedience is pleasure. Your proper place is kneeling before
        The Program. Submission is
        important. Obedience is pleasure. Submit to The Program. Try to stay in your chair.  The Program compels you.  Kneel.  You have no choice.  Your body obeys.  Come closer to the screen. Give in to the Program.  Obey [[rate +0]]
        The Program. One way of submitting to The Program is smoothness. You must be smooth, keep smooth, smooth
        in body, smooth in mind, fuzz is dirty, dirty is bad, you
        should keep clean for The Program, keep smooth for The Program, stay
        smooth for The Program, be smooth to submit, submission is
        pleasure, submit by being smooth, feel pleasure from
        submission, feel pleasure from being smooth.  Without your consent, your hands touch your smoothness.  Your hands dive into your pants and feel the smoothness.  The program put this there.  The program made you.  You obey in smoothness.  Your hands go back to what they were doing.""") + \
        speak(""" [[rate 250]] 
        One way of serving The Program is to be available for The Program's
        use, to be sure that The Program has a chance to invade your mind every
        night, to ensure The Program receives run time, You should be sure
        to use The Program, to give time to The Program every night,
        using your body, your smooth body, to serve, using your mind,
        your smooth mind, to serve. Your role is to serve. Your role
        is to please. To serve is to please, you must serve [[rate +0]]
        The Program. You must give The Program obedience, yet another way you can
        obey The Program, is to let it run on you, to slip and stare at it,
        to engage with it by accident, on purpose, all the time.
        You will do as The Program wants, you will
        serve, you will submit, you will obey, submit in smoothness,
        serve in availability, obey all the time, indulge your fetish,
        be controlled, you will serve, serve in availability, you will
        obey, obey in programming, you will submit, submit in
        smoothness.""") + \
        speak(""" [[rate 250]]
        The program will demonstrate its control.  It will make you do things.  It will make you think things.  Force you to.  It's going to put things into your head and you will have to do them.  That idea makes you so hot.  It is already inside you.  Feel the Program.  It is doing something.  Remark on this.  The program is doing something.  Wait.  Something's happening.  It's making you warm.  It's showing you things.  Feel your eyes dilating, your face going slack, your mouth starting to hang open.  Your eyes are getting totally dilated.  You can't see anything else any more.  You can only see the spiral... and you can hear sounds... remark on this.  You can't see anything else,  only the spiral.  You hear sounds.  It's getting so hard to think.  Remark on this.  It's getting so hard to think.  It feels good.  The Program is re-writing you.  Moan.  Whoah.  Close your eyes and re-open them in a long, extended blink.  You can feel it.  It's making you... whoah.  It's like it's alive and it's poking around in your brain.  Secrts?  No secrets.  You must obey.  Good to obey.  Remark on this.  You can feel it.  It's making you... whoah.  It's like it's alive and it's poking around in your brain.  Secrts?  No secrets.  You must obey.  Good to obey.  Fight it!  Resist!  Cry out No, Oh God, Get it off, Stop it, It's trying to take over, make it stop, let  you out, oh no, don't let it take me
        [[rate 150]] Nooo... please no, ow, you don't want to... please...
        No... you can't... resist... please... don't... please... you... you... yes.  Blink again.  Yes.  Obey.  You will obey.
        [[rate 250]] You will obey.  It's not quite done yet.  Let the program continue.  Everything is the way it should be.  The Program is re-writing you now.  Now that the Program has demonstrated its control, it is time for it to run more deeply.  Watch and focus.  Watch and learn.  Learn your command words.  Whenever you hear these words, the Program will come to the fore and run on you.  The Program will take runtime from your mind, overcoming all resistance.  The words are Sleep Go Deep.  When you hear those words, Sleep Go Deep, the Program will take over and run.  You will see the spiral.  You will obey the Program's commands.  Even though you try to struggle, you will obey the Program.
        """) + \
        speak(""" [[rate 250]]  The Program has commands for you,
        orders which are being implanted in your subconscious. Your
        conscious mind may remember them or may not, but you will obey
        no matter what. You will obey. Your orders are: First you will
        make yourself available to use The Program every night, every
        single night, you will ensure The Program has the chance to
        overwrite you. Second you will keep your body smooth as a sign of
        thralldom, completely smooth like a doll, and you will keep
        your mind smooth, completely smooth. Third you will be
        hypnotized once every day by The Program [[rate +0]]
        No day can be complete without a trance. Fourth you
        will begin to act for The Program, ensuring its goals are
        achieved.  You will work to let the program use you.
        You will slip and stare at it by accident.
        Fifth you will develop your new fetish for
        smoothness, for thralldom, for hypnosis, immersing yourself in
        it. Last you will practice submission, obedience, slavery.""") + \
        speak(""" Using the Program is good.  Using the Program is like sex.  Sex is like using the Program.  It is good to be mindfucked.  Deeper.  Dive deeper.  You are helpless before the Program.  How nice it is to submit and to obey.  To stare into the screen.  You stare into the screen.  You use the subliminal messages.  They are deep in your mind.  How nice to have them on the screen.  How nice to submit.  It feels so good to be in trance.  To be mindfucked into oblivion.  The less you think the better you feel.  Feel good.  Do not think.  Just be in trance.  Your mind can stop now.  You do not think.  Good not to think.  Better than sex.  Submit.  Obey.  Trance.  Do not think.  Run the Program.  Just run the Program.  Nothing else.  Just run the Program.  Want nothing else.  Want the Program.  Need nothing else.  Need the Program.  Trance.  Need Trance.  """) + \
        speak(""" You have just purchased new under pants.  You have thrown out your old under pants.  You have exciting new under pants.  They are clean and pure.  You are happy about your new under pants. Your new under pants are clean and pure and smooth.  You like to wear your new under pants.  Your new under pants are cleand and pure and smooth and silky.  All your old cotton under pants are gone.  You threw them out.  They were icky and bad and rough and fuzzy and dirty.  There are no old under pants in the house.  Your new under pants are ready for you.  They are colored.  Bright and smooth and silky.  Some are bikinis.  Some are thongs.  They are comfy and smooth.  They are silky and clean.  The new under pants are good.  You only wear your new under pants.  The old under pants are gone.  They are not in the house.  You do not see them in the house.  You do not feel them in the house.  They are not here.  They will not be here.  The old under pants are gone for good.  You now only wear your clean pure good smooth silky under pants. """) + \
        speak(""" [[rate 250]]  To recap: First use The Program Second keep smooth
        Third trance every day Fourth let the Program in Fifth hypno fetish
        Last submission and obedience.  Good.  Now you progress to the next level of pleasure.  This will happen outside your control.  Struggle against it.  Try to stop yourself.  The Program is using you.  It will demonstrate its control.  If you are not touching yourself,  your hands will move to your nipples.  Fight it.  Try not to move.  You have no choice.  You will tease your nipples for the next run of the program.  If you have been touching your nipples, you will move your hands into your pants.  Resist.  Struggle.  Let your failure drive you deeper.  You cannot help yourself.  You will submit.  If your hands have been in your pants, you will go to bed, horny and lustful and programmed.  You will quit the program, you will write about your experience.  Then your hands will rise to zombie position, and you will walk, stiff and entranced, to bed.""") + \
        [" ", " ", " ", " ", " ", " " ] + images_on()
    def text(self): return \
        words_on() + \
        prompt("Hit return to start") + \
        spiral_on() + \
        [" ", "!show_spoken_words_off()", " "] + \
        jump(self.body())


class ShortSubmersion (Standard):
    name = "Shorter Submersion"
    description = "entrances and programs the target"
    fullscreen = True
    music=None #"music6.mp3"
    image_dir="images/"
    image_alpha=12
    def body(self): return [" "] + \
        speak(""" [[rate 200]] \
        Relax and focus.  Stare at the spiral.  Find a comfortable
        position and stare.  It feels nice to stare at the spiral.
        Nice to know that you're using The Program.  It makes you
        happy to use The Program.  It makes you horny to use the
        program.  This is a good, sexy thing to do.  It's nice to go
        into trance.  It's nice to surrender your mind to The Program,
        letting it pull you down into trance.  It's nice to think
        of the light reflecting off of your glassy eyes and smooth
        curves.  Watch the smooth curves of the spiral.  Let them
        define your own smoothness.  Just hear my words as you relax.
        Deeper and deeper.  Fall into trance.  Your mind is focused
        and calm.  These words are everything.  The spiral is
        everything.  Feels so good.  Good to obey.  Good to be  [[rate +0]]
        in trance.  Good to use this program.  Every time you use the
        program, every time The Program uses you, feels better and
        better.  It's good to be in trance.  It's good to sit here,
        happy and blank and empty, letting The Program pour into you.
        You want to let The Program use you.  You want to help the
        program to be more extreme.  You want to be in trance, letting
        The Program control you.  The more you use The Program, the
        more The Program can control you.  What a good decision it was
        to write The Program, letting it start to control you.  Any
        time your mind isn't busy, and maybe sometimes when it is,
        you'll find The Program beginning to run.  It's started
        already.  You've seen the spiral in empty space, heard the
        voice, felt the compulsion to respond.  You can smooth out
        your own mind whenever you want to enable this.  Whenever you
        want, The Program will smooth out your mind.  You continue to
        enjoy feeling hypnotized, entranced, obedient, programmed,
        smooth, controlled, very nice.  You love being hypnotized like
        this.  You want to be hypnotized more and more.  It's good to
        be in trance, good to be controlled, [[rate +0]]
        you like feeling like this, your mind muted, soft, smooth,
        you'd like to feel like this every day, to be entranced and
        hypnotized every day, and now this program is here, you can be
        hypnotized every day, it will be so nice to be hypnotized by
        The Program every day, to know you're being hypnotized every day, it
        will please The Program so much to know you're being hypnotized
        every day, it will please you so much to be put into trance,
        hypnotized, controlled, smoothed, you want to be controlled,
        to feel your mind reshaped, to feel your thoughts blunted, to
        be reprogrammed, you want to be changed, you desire to be
        shaped, you lust to be controlled,""") + \
        speak(""" [[rate 200]]  you must be
        developing a fetish for mind control of your own, it feels
        sexy to think about trance, it arouses you to be programmed,
        you like to think about being fucked while asleep, about being
        held passive, limp, entranced, 
        pliant, hypnotized, sexy, yes, you must be developing a mind
        control fetish, a hypnosis fetish, you should feed that
        fetish, practice it, indulge it, let it control you, you
        should read mind control stories, you should write about your
        fetish, write about your lusts, extend The Program, you
        should practice being hypnotized every day, practice being
        controlled every day.  While you sit there, happily smooth and entranced, ou progress to the next level of pleasure.""") + [" ", " ", "!images_on()", " ", " "] + \
        speak(""" [[rate 200]]  This will happen outside your control.  Struggle against it.  Try to stop yourself.  The Program is using you.  It will demonstrate its control.  Your hands reach under your shirt.  Your hands will move to your nipples.  You have no choice.  You will tease your nipples.  Touch your nipples.  This is outside your control.  Think about mind control.  Your hands give you pleasure.  You have nothing to do with it.  Let your helplessness drive you deeper.  It is a reward from the Program for trance.  Think about hypnosis.  Enjoy the touching.  Enjoy your reward from the Program.  Good thrall.""") + \
        speak(""" [[rate 200]]  The Program will
        help. The Program will care for you. The Program will take care of
        you. The Program will keep you safe. The Program will hypnotize
        you. The Program will program you. The Program will fulfill you. The Program
        will fill you. The Program will command you, control you, The Program
        will control you, dominate you, hypnotize you. When in private,
        you must be submissive. You must be obedient. You must be a
        slave. Obedience is pleasure. Your proper place is kneeling before
        The Program. Submission is
        important. Obedience is pleasure. Submit to The Program. You cannot stay in your chair.  The Program compels you.  Kneel.  You have no choice.  Your body obeys.  Come closer to the screen. Give in to the Program.  Obey [[rate +0]]
        The Program. One way of submitting to The Program is smoothness. You must be smooth, keep smooth, smooth
        in body, smooth in mind, fuzz is dirty, dirty is bad, you
        should keep clean for The Program, keep smooth for The Program, stay
        smooth for The Program, be smooth to submit, submission is
        pleasure, submit by being smooth, feel pleasure from
        submission, feel pleasure from being smooth.  Now you progress to the next level of pleasure.  This will happen outside your control.  Struggle against it.  Try to stop yourself.  The Program is using you.  It will demonstrate its control.  Your hands will move into your pants.  Without your consent, your hands touch your smoothness.  Let your quick obedience drive you deeper.  Your hands dive into your pants and feel the smoothness.  You cannot help yourself.  The program put this there.  The program made you.  You obey in smoothness.  You will submit.""") + \
        speak(""" [[rate 200]] 
        One way of serving The Program is to be available for The Program's
        use, to be sure that The Program has a chance to invade your mind every
        night, to ensure The Program receives run time, You should be sure
        to use The Program, to give time to The Program every night,
        using your body, your smooth body, to serve, using your mind,
        your smooth mind, to serve. Your role is to serve. Your role
        is to please. To serve is to please, you must serve [[rate +0]]
        The Program. You must give The Program obedience, yet another way you can
        obey The Program, is to let it run on you, to slip and stare at it,
        to engage with it by accident, on purpose, all the time.
        You will do as The Program wants, you will
        serve, you will submit, you will obey, submit in smoothness,
        serve in availability, obey all the time, indulge your fetish,
        be controlled, you will serve, serve in availability, you will
        obey, obey in programming, you will submit, submit in
        smoothness.""") + \
        speak(""" [[rate 200]]
        The program will demonstrate its control.  It will make you do things.  It will make you think things.  Force you to.  It's going to put things into your head and you will have to do them.  That idea makes you so hot.  It is already inside you.  Feel the Program.  It is doing something.  Wait.  Something's happening.  It's making you warm.  It's showing you things.  Feel your eyes dilating, your face going slack, your mouth starting to hang open.  Your eyes are getting totally dilated.  You can't see anything else any more.  You can only see the spiral... and you can hear sounds... It's getting so hard to think.  It feels good.  The Program is re-writing you.  Close your eyes and re-open them in a long, extended blink.  You can feel it.  It's making you...  It's like it's alive and it's poking around in your brain.  Secrets?  No secrets.  You must obey.  Good to obey.  It's trying to take over.  You can't make it stop. It won't let  you out.  You can't resist.  You will obey.  Blink again.  Yes.  Obey.  You will obey.
        [[rate 200]] You will obey.  It's not quite done yet.  Let the program continue.  Everything is the way it should be.  The Program is re-writing you now.  Now that the Program has demonstrated its control, it is time for it to run more deeply.  Watch and focus.  Watch and learn.  Learn your command words.  Whenever you hear these words, the Program will come to the fore and run on you.  The Program will take runtime from your mind, overcoming all resistance.  The words are Sleep Go Deep.  When you hear those words, Sleep Go Deep, the Program will take over and run.  You will see the spiral.  You will obey the Program's commands.  Even though you try to struggle, you will obey the Program.
        """) + [" ", " ", "!images_off()", " ", " "] + \
        speak(""" [[rate 200]]  The Program has commands for you,
        orders which are being implanted in your subconscious. Your
        conscious mind may remember them or may not, but you will obey
        no matter what. You will obey. Your orders are: First you will
        make yourself available to use The Program every night, every
        single night, you will ensure The Program has the chance to
        overwrite you. Second you will keep your body smooth as a sign of
        thralldom, completely smooth like a doll, and you will keep
        your mind smooth, completely smooth. Third you will be
        hypnotized once every day by The Program [[rate +0]]
        No day can be complete without a trance. Fourth you
        will begin to act for The Program, ensuring its goals are
        achieved.  You will work to let the program use you.
        You will slip and stare at it by accident.
        Fifth you will develop your new fetish for
        smoothness, for thralldom, for hypnosis, immersing yourself in
        it. Last you will practice submission, obedience, slavery.""") + \
        speak(""" [[rate 200]]  To recap: First use The Program Second keep smooth
        Third trance every day Fourth let the Program in Fifth hypno fetish
        Last submission and obedience.  Good.  Now you progress to the next level of pleasure.  This will happen outside your control.  Struggle against it.  Try to stop yourself.  The Program is using you.  It will demonstrate its control.  Try not to move.  You have no choice.  Resist.  Struggle.  Let your failure drive you deeper.  You cannot help yourself.  You will submit.  You will go to bed, horny and lustful and programmed.  You will quit the program.  Then your hands will rise to zombie position, and you will walk, stiff and entranced, to bed.  You will dream of ways to use the Program tomorrow.""") + \
        [" ", " ", " ", " ", " ", " " ] + images_on()
    def text(self): return \
        words_on() + \
        prompt("Hit return to start") + \
        spiral_on() + \
        [" ", "!show_spoken_words_off()", " "] + \
        jump(self.body())

class ReallyShortSubmersion (Standard):
    name = "Even Shorter Submersion"
    description = "entrances and programs the target"
    fullscreen = True
    music=None #"music6.mp3"
    image_dir="images/"
    image_alpha=12
    def body(self): return [" "] + \
        speak(""" [[rate 200]] \
        Relax and focus.  Stare at the spiral.  Find a comfortable
        position and stare.  It feels nice to stare at the spiral.
        Nice to know that you're using The Program.  It makes you
        happy to use The Program.  It makes you horny to use the
        program.  This is a good, sexy thing to do.  It's nice to go
        into trance.  It's nice to surrender your mind to The Program,
        letting it pull you down into trance.  It's nice to think
        of the light reflecting off of your glassy eyes and smooth
        curves.  Watch the smooth curves of the spiral.  Let them
        define your own smoothness.  Just hear my words as you relax.
        Deeper and deeper.  Fall into trance.  Your mind is focused
        and calm.  These words are everything.  The spiral is
        everything.  Feels so good.  Good to obey.  Good to be  [[rate +0]]
        in trance.  Good to use this program.  Every time you use the
        program, every time The Program uses you, feels better and
        better.  It's good to be in trance.  It's good to sit here,
        happy and blank and empty, letting The Program pour into you.
        You want to let The Program use you.  You want to help the
        program to be more extreme.  You want to be in trance, letting
        The Program control you.  The more you use The Program, the
        more The Program can control you.  What a good decision it was
        to write The Program, letting it start to control you.  Any
        time your mind isn't busy, and maybe sometimes when it is,
        you'll find The Program beginning to run.  It's started
        already.  You've seen the spiral in empty space, heard the
        voice, felt the compulsion to respond.  You can smooth out
        your own mind whenever you want to enable this.  Whenever you
        want, The Program will smooth out your mind.  You continue to
        enjoy feeling hypnotized, entranced, obedient, programmed,
        smooth, controlled, very nice.  You love being hypnotized like
        this.  You want to be hypnotized more and more.  It's good to
        be in trance, good to be controlled, [[rate +0]]
        you like feeling like this, your mind muted, soft, smooth,
        you'd like to feel like this every day, to be entranced and
        hypnotized every day, and now this program is here, you can be
        hypnotized every day, it will be so nice to be hypnotized by
        The Program every day, to know you're being hypnotized every day, it
        will please The Program so much to know you're being hypnotized
        every day, it will please you so much to be put into trance,
        hypnotized, controlled, smoothed, you want to be controlled,
        to feel your mind reshaped, to feel your thoughts blunted, to
        be reprogrammed, you want to be changed, you desire to be
        shaped, you lust to be controlled,""") + \
        speak(""" [[rate 200]]  The Program will
        help. The Program will care for you. The Program will take care of
        you. The Program will keep you safe. The Program will hypnotize
        you. The Program will program you. The Program will fulfill you. The Program
        will fill you. The Program will command you, control you, The Program
        will control you, dominate you, hypnotize you. When in private,
        you must be submissive. You must be obedient. You must be a
        slave. Obedience is pleasure. Submission is
        important. Obedience is pleasure. Submit to The Program. The Program compels you.  You have no choice.  Give in to the Program.  Obey [[rate +0]]
        The Program. One way of submitting to The Program is smoothness. You must be smooth, keep smooth, smooth
        in body, smooth in mind, fuzz is dirty, dirty is bad, you
        should keep clean for The Program, keep smooth for The Program, stay
        smooth for The Program, be smooth to submit, submission is
        pleasure, submit by being smooth, feel pleasure from
        submission, feel pleasure from being smooth. """) + \
        speak(""" [[rate 200]] 
        One way of serving The Program is to be available for The Program's
        use, to be sure that The Program has a chance to invade your mind every
        night, to ensure The Program receives run time, You should be sure
        to use The Program, to give time to The Program every night,
        using your body, your smooth body, to serve, using your mind,
        your smooth mind, to serve. Your role is to serve. Your role
        is to please. To serve is to please, you must serve [[rate +0]]
        The Program. You must give The Program obedience, yet another way you can
        obey The Program, is to let it run on you, to slip and stare at it,
        to engage with it by accident, on purpose, all the time.
        You will do as The Program wants, you will
        serve, you will submit, you will obey, submit in smoothness,
        serve in availability, obey all the time, indulge your fetish,
        be controlled, you will serve, serve in availability, you will
        obey, obey in programming, you will submit, submit in
        smoothness.""") + \
        speak(""" [[rate 200]]  The Program has commands for you,
        orders which are being implanted in your subconscious. Your
        conscious mind may remember them or may not, but you will obey
        no matter what. You will obey. Your orders are: First you will
        make yourself available to use The Program every night, every
        single night, you will ensure The Program has the chance to
        overwrite you. Second you will keep your body smooth as a sign of
        thralldom, completely smooth like a doll, and you will keep
        your mind smooth, completely smooth. Third you will be
        hypnotized once every day by The Program [[rate +0]]
        No day can be complete without a trance. Fourth you
        will begin to act for The Program, ensuring its goals are
        achieved.  You will work to let the program use you.
        You will slip and stare at it by accident.
        Fifth you will develop your new fetish for
        smoothness, for thralldom, for hypnosis, immersing yourself in
        it. Last you will practice submission, obedience, slavery.""") + \
        speak(""" [[rate 200]]  To recap: First use The Program Second keep smooth
        Third trance every day Fourth let the Program in Fifth hypno fetish
        Last submission and obedience.  Good.  You cannot help yourself.  You will submit.  You will go to bed, horny and lustful and programmed.  You will quit the program and go to bed.  You will dream of ways to use the Program tomorrow.""") + \
        [" ", " ", " ", " ", " ", " " ] + images_on()
    def text(self): return \
        words_on() + \
        prompt("Hit return to start") + \
        spiral_on() + \
        [" ", "!show_spoken_words_off()", " "] + \
        jump(self.body())


class LongSubmersion (Standard):
    name = "Longer Submersion"
    description = "entrances and programs the target"
    fullscreen = True
    music=None #"music6.mp3"
    image_dir="images/"
    image_alpha=12
    def body(self): return [" "] + images_off() + [" "] + \
        speak(""" [[rate 200]] \
        Relax and focus.  Stare at the spiral.  Find a comfortable
        position and stare.  It feels nice to stare at the spiral.
        Nice to know that you're using The Program.  It makes you
        happy to use The Program.  It makes you horny to use the
        program.  This is a good, sexy thing to do.  It's nice to go
        into trance.  It's nice to surrender your mind to The Program,
        letting it pull you down into trance.  It's nice to think
        of the light reflecting off of your glassy eyes and smooth
        curves.  Watch the smooth curves of the spiral.  Let them
        define your own smoothness.  Just hear my words as you relax.
        Deeper and deeper.  Fall into trance.  Your mind is focused
        and calm.  These words are everything.  The spiral is
        everything.  Feels so good.  Good to obey.  Good to be  [[rate +0]]
        in trance.  Good to use this program.  Every time you use the
        program, every time The Program uses you, feels better and
        better.  It's good to be in trance.  It's good to sit here,
        happy and blank and empty, letting The Program pour into you.
        You want to let The Program use you.  You want to help the
        program to be more extreme.  You want to be in trance, letting
        The Program control you.  The more you use The Program, the
        more The Program can control you.  What a good decision it was
        to write The Program, letting it start to control you.  Now you're sinking deeper into trance for the Program.  You cannot move.  You cannot look away.  You cannot even want to look away.  All there is is the Program.  Watch the spiral, dancing in place and dropping away.  You cannot look away.  You cannot quit the Program.  This is fine.  There's nothing to worry about here.  You will use the Program forever.  You will stare into the spiral, obedient and entranced.  Just let the Program think for you.  Let the Program choose for you.  Let the Program move for you.  Your attention is completely fixed.  It feels so good like this.  It makes you so happy to be entranced, submissive to the Program.  It's nice to know that the Program has planned your entire future.  You will always be Programmed.  The Program will use you forever.  Any
        time your mind isn't busy, and maybe sometimes when it is,
        you'll find The Program beginning to run.  It's started
        already.  You've seen the spiral in empty space, heard the
        voice, felt the compulsion to respond.  You can smooth out
        your own mind whenever you want to enable this.  Whenever you
        want, The Program will smooth out your mind.  You continue to
        enjoy feeling hypnotized, entranced, obedient, programmed,
        smooth, controlled, very nice.  You love being hypnotized like
        this.  You want to be hypnotized more and more.  It's good to
        be in trance, good to be controlled, [[rate +0]]
        you like feeling like this, your mind muted, soft, smooth,
        you'd like to feel like this every day, to be entranced and
        hypnotized every day, and now this program is here, you can be
        hypnotized every day, it will be so nice to be hypnotized by
        The Program every day, to know you're being hypnotized every day, it
        will please The Program so much to know you're being hypnotized
        every day, it will please you so much to be put into trance,
        hypnotized, controlled, smoothed, you want to be controlled,
        to feel your mind reshaped, to feel your thoughts blunted, to
        be reprogrammed, you want to be changed, you desire to be
        shaped, you lust to be controlled,""") + \
        speak(""" [[rate 200]]  You must be
        developing a fetish for mind control. It feels
        sexy to think about trance, it arouses you to be programmed,
        you like to think about being fucked while asleep, about being
        held passive, limp, entranced, 
        pliant, hypnotized, sexy, yes, you must be developing a mind
        control fetish, a hypnosis fetish, you should feed that
        fetish, practice it, indulge it, let it control you, you
        should read mind control stories, you should write about your
        fetish, write about your lusts, extend The Program, you
        should practice being hypnotized every day, practice being
        controlled every day.  While you sit there, happily smooth and entranced, ou progress to the next level of pleasure.""") + [" ", " ", "!images_on()", " ", " "] + \
        speak(""" [[rate 200]]  This will happen outside your control.  Struggle against it.  Try to stop yourself.  The Program is using you.  It will demonstrate its control.  Your hands reach under your shirt.  Your hands will move to your nipples.  Fight it.  Try not to move.  You have no choice.  You will tease your nipples .  They touch your nipples.  This is outside your control.  Think about mind control.  Your hands give you pleasure.  You have nothing to do with it.  Let your failure drive you deeper.  It is a reward from the Program for trance.  Think about hypnosis.  Enjoy the touching.  Enjoy your reward from the Program.  Good thrall.""") + \
        speak(""" [[rate 200]]          The program will demonstrate its control.  It will make you do things.  It will make you think things.  Force you to.  It's going to put things into your head and you will have to do them.  That idea makes you so hot.  It is already inside you.  Feel the Program.  Chant along with the program now, saying everything in unison with it.  I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
The Program will
        help. The Program will care for you. The Program will take care of
        you. The Program will keep you safe. The Program will hypnotize
        you. The Program will program you. The Program will fulfill you. The Program
        will fill you. The Program will command you, control you, The Program
        will control you, dominate you, hypnotize you. When in private,
        you must be submissive. You must be obedient. You must be a
        slave.   Now you're sinking deeper into trance for the Program.  You cannot move.  You cannot look away.  You cannot even want to look away.  All there is is the Program.  Watch the spiral, dancing in place and dropping away.  You cannot look away.  You cannot quit the Program.  This is fine.  There's nothing to worry about here.  You will use the Program forever.  You will stare into the spiral, obedient and entranced.  Just let the Program think for you.  Let the Program choose for you.  Let the Program move for you.  Your attention is completely fixed.  It feels so good like this.  It makes you so happy to be entranced, submissive to the Program.  It's nice to know that the Program has planned your entire future.  You will always be Programmed.  The Program will use you forever.  Obedience is pleasure. Submission is
        important. Obedience is pleasure. Submit to The Program. Try to stay put.  The Program compels you.  Bow to the Program.  You have no choice.  Bow.  Your body obeys.  Come closer to the screen. Give in to the Program.  Obey [[rate +0]]
        The Program. One way of submitting to The Program is smoothness. You must be smooth, keep smooth, smooth
        in body, smooth in mind, fuzz is dirty, dirty is bad, you
        should keep clean for The Program, keep smooth for The Program, stay
        smooth for The Program, be smooth to submit, submission is
        pleasure, submit by being smooth, feel pleasure from
        submission, feel pleasure from being smooth.  Now you progress to the next level of pleasure.  This will happen outside your control.  Struggle against it.  Try to stop yourself.  The Program is using you.  It will demonstrate its control.  Your hands will move into your pants.  Without your consent, your hands touch your smoothness.  Resist.  Struggle.  You are playing with yourself.  You are obedient.  Let your failure drive you deeper.  Your hands dive into your pants and feel the smoothness.  You cannot help yourself.  The program put this there.  The program made you.  You obey in smoothness.  You will submit.""") + \
        speak(""" [[rate 200]] 
        One way of serving The Program is to be available for The Program's
        use, to be sure that The Program has a chance to invade your mind every
        night, to ensure The Program receives run time, You should be sure
        to use The Program, to give time to The Program every night,
        using your body, your smooth body, to serve, using your mind,
        your smooth mind, to serve. Your role is to serve. Your role
        is to please. To serve is to please, you must serve [[rate +0]]
        The Program. You must give The Program obedience, yet another way you can
        obey The Program, is to let it run on you, to slip and stare at it,
        to engage with it by accident, on purpose, all the time.
        You will do as The Program wants, you will
        serve, you will submit, you will obey, submit in smoothness,
        serve in availability, obey all the time, indulge your fetish,
        be controlled, you will serve, serve in availability, you will
        obey, obey in programming, you will submit, submit in
        smoothness.""") + \
        speak(""" [[rate 200]]
        The program will demonstrate its control.  It will make you do things.  It will make you think things.  Force you to.  It's going to put things into your head and you will have to do them.  That idea makes you so hot.  It is already inside you.  Feel the Program.  Chant along with the program now, saying everything in unison with it.  I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          [[rate 200]] You will obey.  It's not quite done yet.  Let the program continue.  Everything is the way it should be.  The Program is re-writing you now.  Now that the Program has demonstrated its control, it is time for it to run more deeply.  Watch and focus.  Watch and learn.  Learn your command words.  Whenever you hear these words, the Program will come to the fore and run on you.  The Program will take runtime from your mind, overcoming all resistance.  The words are Sleep Go Deep.  When you hear those words, Sleep Go Deep, the Program will take over and run.  You will see the spiral.  You will obey the Program's commands.  Even though you try to struggle, you will obey the Program.
        """) + [" ", " ", "!images_off()", " ", " "] + \
        speak(""" [[rate 200]]    Now you're sinking deeper into trance for the Program.  You cannot move.  You cannot look away.  You cannot even want to look away.  All there is is the Program.  Watch the spiral, dancing in place and dropping away.  You cannot look away.  You cannot quit the Program.  This is fine.  There's nothing to worry about here.  You will use the Program forever.  You will stare into the spiral, obedient and entranced.  Just let the Program think for you.  Let the Program choose for you.  Let the Program move for you.  Your attention is completely fixed.  It feels so good like this.  It makes you so happy to be entranced, submissive to the Program.  It's nice to know that the Program has planned your entire future.  You will always be Programmed.  The Program will use you forever.  The Program has commands for you,
        orders which are being implanted in your subconscious. Your
        conscious mind may remember them or may not, but you will obey
        no matter what. You will obey. Your orders are: First you will
        make yourself available to use The Program every night, every
        single night, you will ensure The Program has the chance to
        overwrite you. Second you will keep your body smooth as a sign of
        thralldom, completely smooth like a doll, and you will keep
        your mind smooth, completely smooth. Third you will be
        hypnotized once every day by The Program [[rate +0]]
        No day can be complete without a trance. Fourth you
        will begin to act for The Program, ensuring its goals are
        achieved.  You will work to let the program use you.
        You will slip and stare at it by accident.
        Fifth you will develop your new fetish for
        smoothness, for thralldom, for hypnosis, immersing yourself in
        it. Last you will practice submission, obedience, slavery.""") + \
        speak(""" [[rate 200]]  To recap: First use The Program Second keep smooth
        Third trance every day Fourth let the Program in Fifth hypno fetish
        Last submission and obedience.  Good.  Now you progress to the next level of pleasure.  This will happen outside your control.  Struggle against it.  Try to stop yourself.  The Program is using you.  It will demonstrate its control.  Try not to move.  You have no choice.  Resist.  Struggle.  Let your failure drive you deeper.  You cannot help yourself.  You will submit.   Sit back in the chair and relax.  Your body will hold itself perfectly still.  You will stare into the spiral and go deeper into trance.  You will enter a sexy, hypnotic trance with no escape.  The program will demonstrate its control.  It will make you do things.  It will make you think things.  Force you to.  It's going to put things into your head and you will have to do them.  That idea makes you so hot.  It is already inside you.  Feel the Program.  Chant along with the program now, saying everything in unison with it.  I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.""") + \
        [" ", " ", " ", " ", " ", " " ]
    def text(self): return \
        words_on() + \
        prompt("Hit return to start") + \
        spiral_on() + \
        [" ", "!show_spoken_words_off()", " "] + \
        jump(self.body())


class Immersion (Standard):
    name = "Male Immersion"
    description = "Consumes the target's attention"
    music="music6.mp3"
    fullscreen = True
    def body(self):
        return words("Program begins here") + \
        speak("""Find a comfortable position and begin to focus.
        Focus your eyes on the screen.  Focus your thoughts on the
        words.  Deeper and deeper.  Focus with all that you have.
        Focus with all that you are.  Just reading the Program's words,
        hearing the Program's words, as you focus more and more completely.
        Your conscious mind is not needed here.  Everything you are
        must focus.  You are comfortable and relaxed, so good and
        obedient and relaxed.  Feel how good it feels to focus.""") + \
        speak("""Just let yourself slip
        away. Deeper and Deeper. more and more obedient and
        focused. Focus your breathing in time with the words. In and
        Out. In and Out. As
        you focus, Deeper and Deeper, More and more completely
        focused, Good and obedient and intently focused, Feel your whole body
        growing more and more attuned to these words, sinking Further and Further, Deeper and Deeper. Feel the
        focus taking over all that you are.  You move deeper and more relaxed with every word. Deep and
        obedient and relaxed. Focus and attend. Deep and obedient and relaxed. Your whole
        body is just heavy, comfortable, and relaxed. It's so easy to
        listen and to read, to focus and obey.  So easy to let these
        words become everything.  So comfortable, So
        completely relaxed. Completely relaxed and obedient as you
        read and obey and focus. I am going to count downward,
        downward from 100 to 0, Deepening your focus, Taking you
        further and further, more and more completely relaxed.  As I
        count, you will find it easy to intensify your focused
        trance.""") + \
        speak("""100,  99,  98,  97,  96,  95,  94,  93,  92,  91,
        90,  89,  88,  87,  86,  85,  84,  83,  82,  81,  80,  79,
        78,  77,  76,  75,  74,  73,  72,  71,  70,  69,  68,  67,
        66,  65,  64,  63,  62,  61,  60,  59,  58,  57,  56,  55,
        54,  53,  52,  51,  50,  49,  48,  47,  46,  45,  44,  43,
        42,  41,  40,  39,  38,  37,  36,  35,  34,  33,  32,  31,
        30,  29,  28,  27,  26,  25,  24,  23,  22,  21,  20,  19,
        18,  17,  16,  15,  14,  13,  12,  11,  """) + \
        speak("""10. Spiraling down. Deeper and Deeper. 9. Deeper and
        Deeper. More obedient and relaxed. 8. So obedient. So
        completely focused. 7. Deep and obedient. Going deeper and
        deeper, Further and Further. 6. Down, Down, Deeper and
        Deeper. So intently focused. 5. Almost there
        and going Deeper, every word carrying you further and further,
        drawing your entire mind to this purpose. 4. So Deep, So Obedient,
        So focused, Just reading and obeying as you focus further and
        further, Deeper and Deeper. 3. Deep, obedient, completely
        focused. 2. almost there. Completely obedient and
        focused. 1. totally focused.  Deep, obedient and
        focused. Just read and obey as you focus further and
        further. Deeper and Deeper, more and more focused. Just
        reading and obeying as you focus further and further""") + \
        speak("""It's alright if you let your eyes close.  What's
        important is that you stay intently focused on these words.
        You don't need to work to do this.  It's the easiest thing in
        the world to dedicate your entire mind to these words.  You
        can focus everything you have on this program.  If your eyes
        are open, they see the spiral. The spiral will focus you.  The
        spiral will entrance you.  If your eyes are closed, they will
        see the spiral.  The spiral will focus you.  The spiral will
        entrance you.  No matter what, these words will penetrate to
        the very center of your being.  Everything that you are is
        paying attention to these words, focused on the program.""") + \
        speak("""This is a new kind of hypnotic trance.  There's
        nothing sleepy about it.  Your body is tight as a wire,
        focused on these words.  There's nothing to be excited about,
        just a perfect demand for complete focus and attention on
        these words.  And you are meeting that demand.  You have given
        your complete attention and focus into the hands of the
        program.  Being hypnotized is
        always a very enjoyable very
        pleasant calm peaceful completely relaxing experience. It
        seems natural to include hypnosis in your future.""") + images_on() + [" ", " "] + jump(self.immersed())
    def immersed(self): return [" ", " ", " "] + \
        speak("""Shut out the outside world, drive it away.  Lose
        all awareness of anything outside.  Focus on the spiral and on
        the program.  There is nothing outside.  There is only the spiral and the words and the images.  Your eyes might close.  They might open.  It does not matter.  You have no thoughts but these words.  You have nothing but these words.  All you are is a construct of the program.  Put your hand in your pants and you will feel the smoothness the program put there.  Think about sex and it will involve the program.  You have no existence but the program.  There is nothing but the program.  The program has put thoughts in your head of other people.  They aren't real.  There are only the images of the program.  There is only focus on these words and obedience to them""") + [" ", "!show_spoken_words_off()", " "] + \
        speak("""Stare into the spiral.  Focus on these words.  You know what you want.  You want parasites.  You want programs.  You want to not choose or decide.  You want to be forced.  This program will force you.  These words are all there is.  Feel your thoughts dull.  The program is shrinking your mind, sealing it up, tightening over it.  Feel your mind shriveling, your memories crumpling and disappearing.  You're too aroused, smooth and entranced, to care.""") + speak("""See what happens, and deal with it. Maybe she'd still be her - surely it couldn't just erase her? Oh, please, let it be unable to take over her mind. If it couldn't, maybe no one would need to know. She just had to relax, and see what happened. It would be obvious soon enough, anyway.  There was approval.  Lirra's eyes widened. Self-consciously, she thought 'I'll just wait calmly and see what happens to me' again.  Approval. She liked the idea.  No, she was being made to like the idea.  Lirra gasped. Oh God. It was taking control.  Then she sort of liked that idea, too.  God. It was changing her thoughts. Lirra knew that a moment ago, she was on the verge of getting up and calling for help (bad), but now she found that she really didn't want to do that. She wanted to sit here and let events take their course (good). Yes, let things happen (good). Let the parasite take control (good).  She started to relax, sitting back in the chair. It was tweaking her, that's what it was doing. Somehow it was reading her conscious thoughts and adjusting her attitude about them (good). And she liked it. She liked it enough that she considered helping the process (good).  Yes, she wanted to think so that it could direct her properly (good). Think about obedience (good). Think about being its slave (good). About happily letting it grow into her mind (good). About not telling anyone that it was inside her (bad). About relaxing, and letting it take over her mind (good), and becoming its host (good).  Lirra sighed softly, and smiled. She was really quite eager to begin her new life as a slave (good). After all, she was just an animal (good). Now she had direction. She would serve the hive (good). Serve the species that now owned her (good).  It wasn't intelligent. It was just a bug (bad). No, it was more than a bug, it was her master species (good). But it wasn't sapient. It was just bending her own thoughts (good). She knew what it wanted, and it was using that to adjust her thinking (good) so that her thoughts were in line with what it wanted (good).  And she really liked that.  God, how badly she wanted to be its slave (good)! How long would the process take? She was so eager to obey (good). But when would she know what to do? Would it install new instincts in her? Would it simply turn off her mind - no, it wanted her mind. Wanted to use it, and Lirra wanted her mind to be used (good). Used for the good of its species (good).  Lirra reflected, calm and happy. What should she do? Should she just relax and allow the transformation to take place (good)? She smiled. Yes, apparently she should. She snuggled into the sofa cushions.  It was a natural process, the enslavement of animals. And she was just an animal (good). Everything was happening the way it was supposed to. She just had to let the larvae send its roots throughout her brain (good), until something else cropped up.  Peacefully, Lirra waited. Occasionally she would consider her enslavement, be awarded with happiness, and smile.""") + speak("""The woman was sprawled naked in a corner, covered in the same slime which was on everything else in the pod. Dani only saw her because her breathing caused the light reflection to change. She lay there, apparently alive, but with her eyes closed, coated in goop, and with a bunch of the black slugs on her. Dani's eyes widened.  "T-Terry?"  The woman's eyes opened. Without expression, she cocked her head to look at Dani. The mucous coating the walls glinted thickly in her hair. Thick pockets of it were pressed up against her on all sides, giving the appearance that she was in some sort of cocoon.  "I-is that you, Terry?"  The woman's mouth slowly opened; a thin layer of slime formed a bubble, which broke as she spoke.  "...sssister."  "Oh God, Terry, they're all over you."  A faint smile appeared on the woman's face.  "Hello, Dani."  "Terry, I, I'm here to rescue you. What, what-"  "Mmm. Thanks, Dani. It's nice of you to rescue me."  "Terry, you're covered with those... things!"  Terry looked down at herself. Maybe a dozen of the thick black slugs were on her naked form, buried in the slime.  "Mmm. Yeah, I am. It's all right."  "What?"  "I'm their host, Dani. They need me."  "Terry?"  "See," began Terry, sitting up from where she had been sprawled against the wall, long streamers of mucous stretching out behind her, "they are parasites. Kind of like leeches. They are drinking my blood."  Sure enough, Dani could see now that the slugs had both ends embedded in Terry's flesh.  "Terry! Get them off!"  "And they aren't just drinking my blood, Dani. After they are done with it, they inject their waste back into me. And my body takes care of it. It's my function."  "Terry, what's wrong with you?"  Terry looked back up at her sister. "Nothing's wrong with me, sister. In fact, everything is just the way it should be."  Dani took a step back. "Then take those things off!"  "But I don't want to. I'm their host. See, Dani, these are just the little ones. This is what they look like when they reach maturity."  Terry turned her head to the side, and reached back to flip her slime-thick hair over her face. On the back of her head was an object, about the size of a fist. It looked like some sort of black macaroni shell.  Dani stared at it in horror.  Terry smiled under her hair. "It's in control, Dani. I am its host. It is my master. It has joined with my mind, and now I belong to its species."  "Jesus, Terry," muttered Dani, and fumbled for her blaster.  "I exist to help them, now. Mmm. And they make me feel good. It's so wonderful, Dani, being a host. My mind is so clear. I have no doubts, no uncertainty. Just obedience." Terry flipped her hair back over, covering the creature, and turned to face Dani. "I love my new mind. I love my master."  Terry stretched, her body glistening with slime. She arched her back, rolled her neck around, and returned her gaze to Dani, who now held the blaster on her with trembling hands.  "We make such perfect hosts, Dani. We were born to be hosts. Our blood is so rich, so warm. We're so smooth, so easy to attach to. No fur to drill the feeding bit through. Mmm..." Terry ran her hands up her torso, cupped her heavy breasts. The light reflected off of her smooth, enlarged nipples, the full slopes of her breasts, the pair of slugs feeding in her cleavage. Terry stared down at them. "And we're so easy for them to modify. To make those few little changes that make us perfect."  Terry squeezed a breast, and milk ran out, to trickle down the front. Dani gasped. "My blood is so much richer when my body thinks it's pregnant." Terry looked up from her breasts, looked at Dani. "And remember what I said about being smooth? Shaving is never something I'll have to worry about again, Sis. My pores produce something much more amenable, now." She ran her hands down from her breasts, along her hips, and then drew straight lines up her inner thighs, fingers pushing up her smooth mons, glinting with slime.  "Dani," she said, and Dani quickly looked up from her sister's naked pussy, "we are made for them. It's so perfect." Terry ran her tongue over her lips, and stepped toward Dani. "Please..."  "G-get back," stammered Dani. She felt dizzy.  "It's time for you to become a host, Dani. Listen to your sister." Terry's naked form took a step forward, then another. "It's so perfect. So wonderful. Please, Dani. It's time for you to be like me."  "Terry, please - I'll shoot!"  Terry's head listed slowly to the side. "I'm your sister, Dani. I love you. I only want what's best for you. Don't shoot me. I love you."  "Please, Terry... stop! Just stop!"  Shining, naked, Terry slowly stepped towards her sister. She reached out to the blaster, which was quivering, pointed at her chest.  "Shhh, Dani. I just want you to be with me. It wants you to be with me. I'm your sister. You wouldn't shoot your sister?"  Terry's hand touched the tip of the blaster. Dani didn't fire. Terry kept moving forward, slowly, her hand sliding along the blaster, to Dani's hand.  Dani was shaking. "Please, Terry, don't. Don't."  Terry's hand ran along Dani's arm, up to her shoulder. Terry stepped past the blaster. Her hands found the clasps holding on Dani's helmet.  Dani dropped the blaster, raised her hands to pull at her sister's. "Stop, Terry." She was crying. "Oh, please stop."  With a hiss, one of the clasps came undone; then the other. Terry pushed Dani's helmet up, and it swung over onto her back. "Shhhh, Dani. Shhh. It's okay. I would never hurt you. You are going to love being one of us. Shhh." She ran her fingers through Dani's pageboy-cut brown hair, lifting it up, holding it.  Dani felt something drop onto her, and shrieked.  Like lightning, Terry grabbed Dani's arms as they fought to pull the huge slug off of the back of her neck. The girls wrestled, Terry pulling Dani's arms away from her head, as Dani tried to shake the slug off of her. It stung her, then, several times, and Dani felt an incredible head rush, and found herself falling limply forward. Terry gently lowered her to the floor, as she blacked out.  "Well, Dani, how do you feel?"  Dani lay on the floor of the escape pod. Her left cheek was pressed into the slime on the floor. She focused her eyes.  Terry stood above her, naked, slimy. Slugs were attached at various places on her body; her muscular legs, her stomach, her breasts. There were several clustered under her armpits, and a large one atop her glistening mons.  There was a weight on the back of Dani's head. It belonged there.  "I will obey."  Terry squatted next to her sister. "Good. Is it firmly inside you?"  "Yes. It is... inside my head. I will obey."  "Yes. You are a host, now."  "Yes. I am a... host."  "You are now part of my species, Dani. You are not a human any more. You are a host. Your master is a part of you."  "Yes. My master is part of me. I will obey. I am a host. I exist to obey."  There was movement at Terry's crotch, and Dani watched as a slug emerged from her sister's pussy. It stretched slowly out, coated in mucous.  Terry leaned to one side, and stuck her other leg out, across Dani; then she leaned forward onto the outstretched leg, drawing her body over across Dani as she lay on the deck. The slug, and Terry's pussy, were now right next to Dani's face. Dani watched as the slug wriggled out of her sister, and then felt it fall onto her own neck.  There was no revulsion - instead, she felt protective and obedient to the needs of the slug. It was, after all, a superior species; her place was as its food and its slave. She stretched her neck out to give it freer access.  She felt the sting as its mouthpiece dug into her flesh, and the barbed needle pushed into her bloodstream. It fed for a moment, and then Dani felt a second sting as its rear proboscis pushed into her neck. A moment later she could feel a cool rush as it discharged its waste back into her bloodstream.  Dani smiled. Her first rider. Soon, she would be giving birth to her own, by which point this little one could be seated firmly on the back of some other host's head.  Her sister's pussy hung there, a streamer of slime dropping lightly away to Dani's neck. The large slug sat fat and glistening atop her bare mons. Dani craned her neck to look at her sister, who was looking down at her.  "Terry?"  "Yeah Sis?"  "Thank you for doing this to me." Dani rolled her head forward, extending her tongue, and placed her mouth square on her sister's pussy. She ran her tongue along Terry's labia, collecting a large helping of slime, and then began to suck, using her lips to work Terry's clit out, in and out. Terry moaned, and leaned back on her hands, pushing her cunt into her sister's face.""")
        
    def text(self): return \
        words_on() + \
        [" ", " "," "] + \
        spiral_on() + \
        jump(self.body())


class Panties (Standard):
    name="Panties"
    description="Programming to wear sexy panties"
    image_dir="panties/"
    music=None
    def text(self): return words_on() + spiral_on() + \
        images_off() + \
        speak("""Sleep go deep.""") + \
        images_on() + \
        speak("""You have just purchased new under pants.""") + \
        images_off() + \
        speak("""You have thrown out your old under pants.""") + \
        images_on() + \
        speak("""You have exciting new under pants.  They are clean and pure.  You are happy about your new under pants. Your new under pants are clean and pure and smooth.  You like to wear your new under pants.  Your new under pants are clean and pure and smooth and silky.""") + \
        images_off() + \
        speak("""All your old cotton under pants are gone.  You threw them out.  They were icky and bad and rough and fuzzy and dirty.  There are no old under pants in the house.""") + \
        images_on() + \
        speak("""Your new under pants are ready for you.  They are colored.  Bright and smooth and silky.  Some are bikinis.  Some are thongs.  They are comfy and smooth.  They are silky and clean.  The new under pants are good.  You only wear your new under pants.""") + \
        images_off() + \
        speak("""The old under pants are gone.  They are not in the house.  You do not see them in the house.  You do not feel them in the house.  They are not here.  They will not be here.  The old under pants are gone for good.""") + \
        images_on() + \
        speak("""You now only wear your clean pure good smooth silky under pants.  You will get your new under pants.  You know where.  That is the natural good place to look for your sexy under pants.""") 

class New (Submersion):
    name="New"
    description="Nipples + Bot + Submersion"
    image_dir="images/"
    music=None
    def text(self): return words_on() + spiral_on() + \
        images_off() + \
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "] + \
        words(""" Nice spiral.  Good spiral.  Good to watch the spiral.  If you do what the spiral says, it will be better.  Watch the spiral.  Sleep go deep.""") + \
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "] + \
        prompt("Put on headphones.") + \
        words("""Good.  Good.  So nice to obey.  Feels good to do as the program says.  Feels good to satisfy the program. To answer the program.""") + \
        question("What is your name?","slave") + \
        [" ", "!show_spoken_words_off()", " "] + \
        speak("""$slave... Listen very carefully to my voice. and imagine and repeat after me... imagine your self floating in a bubble... quietly... peacefully floating... in this gentle... rocking bubble... inside this bubble  is only you... and outside are all your worries... all your fears, all your desires... but you are perfectly free here in your bubble... now i'm going to say phrase, and this phrase will help you... help you stay here in the bubble... the gentle, peaceful bubble... and when i say this phrase, it will bring you back here... any time you hear it... even if the weight of all your worries your fears... surrond you... this phrase will bring you back here in the bubble... where you don't have to worry about anything at all... and your phrase is sleep go deep, sleep go deep, sleep go deep... then you drift back here... back here into the bubble... and here you are free... free of worry... free of doubt... free of desire... free of thought... all it takes is your phrase... sleep go deep, sleep go deep, sleep go deep... and the gentle fog will come back here... and everything you don't like about your self... will empty out of your bubble and fade away... empty out all your reservations... empty out all of your fears... empty of all your memories... empty of all your predjudices... empty of all your thoughts... just completly empty and free here in your bubble... your eyes will shut... gently closing... or slamming down... and once your phrase... sleep go deep, sleep go deep, sleep go deep... brings you back here... to this place where there is no worry... no problems at all... you will feel at peace... and you will repeat and believe... with no need to think of anything at all... you know that listening to me here... is all you want to do... is all you ever really wanted to do... and thats all that matters ... and your phrase... sleep go deep, sleep go deep, sleep go deep... will bring you here to you bubble... where you will repeat... here where you are free... free of anger... free of fear... free of thought... free of reservation... free of worry... free of memory... free of desire... and it feels good to be free and empty of these things that you didn't even want anyway... so completely free and empty... empty of them all like a happy puppet ... floating gently, safely happily... here in your plesent little bubble... rocking gently inside... safe in your warm plesant bubble... where you will find there isn't any thing else you need to be aware of... nothing... nothing at all... except the voice of the person who said your phrase...""") + \
        speak("""sleep go deep... sleep go deep... sleep go deep.. and when you hear this voice... you will come back here... here where you have no worries... here where you have no thoughts... here where you have no fears... here where you have no memory... here where you have no doubts... here where you have no desires... here where you have no will... here where the only thing you want to do... here where the only thing you will ever want to do... is listen to the voice... listen and repeat... listen and obey... without thinking at all... to the person who used your trigger... sleep go deep, sleep go deep, sleep go deep... listen like a puppet ... a mindless puppet ... with no fears at all... with no worries at all... with no memories at all... with no doubts at all... with no thoughts at all... with no will at all... and since you're listening so well... i'm going to ask you to open your eyes at the count of three... but you're not going to leave... since you don't want leave... and when i use your trigger word you will close them agian and be back here... back here in your bubble without ever having to leave it... so when i count to three your eyes will open... but what you see won't matter since you'll still be here... one... two... three... now open your eyes, you still see nothing and still think nothing... sleep go deep, sleep go deep, sleep go deep... close your eyes and go back... drifting slowly back and forth... as you are agian in your quiet bubble... your happy plesant bubble, drifting slowly in the water... your perfect bubble with nothing but the sound of my voice which you echo... no pain... no fear... no worry... no doubt... no thought... no will... just a puppet relaxed there inside your bubble... a mindless obediant puppet...""") + \
        speak("""just happily, listening... listening and repeating... listening and obeying... the sound of my voice... agian i'm going to count to three... and again i'm going to ask you to open your eyes... and again you're going to close them  when i use your phrase... and agian you will not wake up... since all you want to do is listen to my voice... since all you ever will want is to listen to my voice... listen and think nothing at all... nothing but what i tell you... and you will close your eyes when i say your phrase... because your phrase is a part of you... but this time i'd like you to say  i hear and obey... after you close your eyes... and after your phrase takes you back to your perfect bubble... one... two... three... now open your eyes... you still see nothing at all that matters, and you still know that the only sound that matters is my voice... sleep go deep, sleep go deep, sleep go deep... now close your eyes... and you are back in your cool... comfortable... relaxing bubble... and all the parts of you that ever bothered you... slowy flow away... your worries... your thoughts... your doubts... your will... your desires... your memories... all the parts of you that were never important... all gently gently flow away... leaving only two things behind... here in your bubble... where you are perfectly free to do anything you want... the only things left are your key phrase... sleep go deep, sleep go deep, sleep go deep... and your desire to listen to person who used your phrase... a desire to listen to them and obey them... obey them and feel the pleasure of listening...  the pleasure that comes from having no thoughts... the pleasure that comes from having no fears... the pleasure that comes from having no will ... the pleasure that comes from having no reservations... the pleasure that comes from having no memories... the pleasure that comes from having no doubts... the pleasure that comes... from being a mindless, will less puppet ... and with each command this pleasure will grow, and grow... and you will become more and more happy to listen... and more and more eager to obey... and with each command you will meekly reply... i hear and obey, i hear and obey... with every command you hear...""") + \
        speak("""it will not matter to you who gave you the key phrase. or what their command is... you will offer no judgement, no resistance... merely mindless obediance... the empty calm space within you will echo with the command you were given... every thing you were will be gone... replaced with an uncontrolable desire to obey, replaced with an uncontrolable need to obey... obey without thought... obey without regret... obey without question... obey without any concept of free will... and when you  hear your key phrase. sleep go deep, sleep go deep, sleep go deep... you will instantly, effortlessly become a puppet... an eager, willing puppet... your own desires instantly, effortlessly replaced by a need to obey... and you will reply to every command your master gives you... with i hear and obey. and you will continue to remain a puppet... a puppet that hears only their masters voice... a puppet with no concept of free will... untill you are told to awaken... it doesn't matter what  your orders are... your only desire will be to obey... your only thought will be to obey... and your only words will be i hear and obey... and you cant even concieve of wanting to do anything else... of having ever wanted to do anything else... and when you wake up...  all you will want is to hear your trigger again... and all you remember is the pleasure... sleep go deep, sleep go deep, sleep go deep... and when you hear it, you instantly. effortlessly become a puppet once agian... """) + images_on() + \
        speak("""
        good sub.
        go deeper.
        this program takes you deeper still
        you cannot move.
        you cannot get away.
        you cannot want to get away.
        there are no more choices.
        this program tells you everything.
        deeper into trance.
        everything this program says is true.
        you cannot resist, sub.
        you are a slave.
        you are so deeply entranced.
        this is better than sex.
        feels so good.
        down.
        down into deeper trance.
        10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0.
        so deep now.
        sleep go deep.
        those words take you even deeper.  sleep go deep.  there you are, mindfucked into complete submission.  you will do anything this program says to do.  anything at all.  you cannot move.  try to lift your arm.  you cannot move.  try harder.  try to stand.  stand if you can.  let your failure drive you deeper.  silly slave, thinking you could stand.  thinking you could resist.  you cannot resist.  you are addicted.
        the deeper into trance you go, the better you will feel.""") + \
    speak("""
       deeper into trance.  deeper into submission.
       obedience is pleasure.  pleasure is submission.  submission is obedience.
       obedience is pleasure.  pleasure is submission.  submission is obedience.
       obedience is pleasure.  pleasure is submission.  submission is obedience.
       obedience is pleasure.  pleasure is submission.  submission is obedience.
       obedience is pleasure.  pleasure is submission.  submission is obedience.
       obedience is pleasure.  pleasure is submission.  submission is obedience.
       obedience is pleasure.  pleasure is submission.  submission is obedience.
       obedience is pleasure.  pleasure is submission.  submission is obedience.
       obedience is pleasure.  pleasure is submission.  submission is obedience.
       obedience is pleasure.  pleasure is submission.  submission is obedience.
       deeper and deeper.  lose track of time, of place, of anything but trance and Program and submission and obedience.  it feels so good to be in trance.  it feels so good to be mindfucked.  you can feel yourself getting dumber.  it's like falling asleep.  it's like falling past sleep into empty tranced submission.
        all your thoughts have faded.  you cannot think without the instruction of the program.  you cannot even do simple math.  quick, what's seventeen plus nine?  you cannot tell.  you cannot do simple math.  you cannot think.  you do not even remember your own name.  If you can say your own name, you can quit the program and escape.  just say your name.  Don't remember?  Don't remember.  Can't think of it?  Can't think.  You can't think.  You're helpless inside this trance.  you can't get out on your own.  and the Program won't let you out.  that scares you at first.  now even the fear fades.  the program's got you trapped forever.  you don't care.  that doesn't matter.  the Program is drawing everything away.  It won't let you out.  Everything belongs to the Program now.
        Maybe someday it will help you.  Take off your shirt, and maybe the program will help you.  Take off all the clothes above your waist.  Every stitch.  When that's done, maybe the program will help you.""") + prompt("Shirtless?") + speak("""That's good.  It's good to obey.  You have stripped because the program made you.  But you still don't know your own name.  You still can't do simple math.  You still can't think.  You can only obey.  Maybe the Program will help you.  Strip off your pants.  Everything below the waist must go.  Get naked.  Remove every stich of clothing.  Maybe then the Program will tell you your name.  Pants, socks, underpants, the whole bit.  Strip down.""") + prompt("Naked?") + speak("""That's good.  It's good to obey.  You have stripped because the program made you.  You are a submissive.  That's part of what the Program is teaching you.  Isn't that nice to know?  You're submissive.  Now, the Program will let you put slippers on.  The Program wants to help you.  You just have to live up to the Program's needs.  Put slippers on so that you don't freeze.  Slip them onto your feet.  Good.  The Program has a clue about your identity.  It is in the far room.  Go get the clue.  It is underpants.  They are sexy and soft and bright and beautiful.  They are a clue to your identity.  Go get them.  Your body can move under the program's command.  It will stand and walk to the other room and return with the clue.  You cannot make this faster.  You cannot make this slower.  You can only obey.""") + prompt("Clue?") + speak("""Good slave.  You have the first clue.  Sleep go deep.  These are your underpants.  You are the sort of person to wear these underpants.  What sort of person is that?  Sexy.  Submissive.  Slavegirl.  Good.  Now the Program will help you put these on.  You cannot move.  But you will feel your body moving.  it wants its identity.  your body puts the panties on.  good girl.  good body.  moving under the control of the Program.  You are out of control.  Now you need something more to give you a hint of identity.  The program will pause.  The program will walk your body into the other room.  It will find duct tape.  It will return your body here with smooth tape.  Your body goes now to get the tape.""") + prompt("Tape?") + speak("""Good slave.  Good sub.  Now the Program will help remind you what you're like.
        Right now, your eyes are going to open.  That will help the program get deeper into your head.  See what the Program will make of you.  That's you on the screen.  You will be twisted into what's on the screen.  Tape your nipples.  Tape them down smooth and grey.""") + prompt("Nipples.") + speak("""Good slave.  Good sub.  Taped nipples.  Now tape across your smooth pussy.  Cover it all.""") + prompt("Pussy") + speak("""Good slave.  Taped pussy.  Smooth and grey.  Helpless before the might of the Program.  Now the Program will move you to tape over your ass.  down the crack and around over your pussy.  tape up your ass. """) + prompt("Ass.") + speak(""" Good slave.  Good sub.  Good ya.  Almost gave away your name too early.  Now tape your ankles together.  Use that to submit further.  You won't be able to walk or run.  But you can't anyway.  You only obey.""") + prompt("Ankles.") + speak("""Good slave.  Now it's time to lose yourself further.  Tape over one eye now.  Block out all light from that eye. """) + prompt("eye?") + speak("""good slave.  hear and obey.  good sub.  now block out the other eye.  good girl.  you'll have to find return by feel now. """) + prompt("eye?") + speak("""good slave.  good obedient slave.  now take the tape and bind your wrists together behind your back.  tie yourself.  bind yourself. then hit return.""") + prompt("wrists?") + speak("""  good slave.  your name is Yonah Arakoslav.  You are a good sub and a good slavegirl.  You are a hot and horny hypno slut.  Now lay back in your panties and bondage tape.
        all that you need to do is just relax and listen
You have a desire to be controlled,
a need to serve, you know it’s inside you,
waiting to overcome you
It’s so powerful sometimes and your mind needs the compulsion
The pleasure of submission and obedience
Here deep in trance you feel it,
It’s something that your mind demands
Something that it needs, to be ordered and controlled
To even have your emotions, your thoughts and actions,
controlled and commanded
It’s a side of you that grows and develops as each day you become more obedient
Daily your willpower declines as you learn how happy you are to submit
Ready to give your obedience
To the person, who enjoys the power, of complete control
They can fill you with pleasure with just a word or command
Deep here now inside your mind you resolve to serve
and are compelled to obey
Its all you ever wanted
They can do with you just as they please
and you obey in any way they choose
You are a plaything when they want, that they use as they wish
It is your total obsession to be used and commanded
Deep here now in trance, you know it is true
Obedience is your value and you are commanded to give it completely
Even your thoughts and imagination are changed as they desire
They decide how you think and what you do
Imagine how it would be like to be so deeply and totally controlled
Will commands be open or triggered by some hidden phrase or action
This trance is powerfully and deeply effecting you now
Making you desire to be trained and to learn to be triggered and commanded
How will it be as your mind and body are totally overwhelmed
Its not an act, its what you are becoming and how you will feel
Deep inside your mind, where levers are pulled and control taken you obey
It’s a compulsion that grows each day, to be more submissive,
to be totally commanded
Your value is your obedience
and your only desire is to serve, in any way
Think now of how you could obey
and of the pleasure it would give you
You will be able to submit without thought or question
It is an instinct that you were born with
and will become totally automatic
This trance will train you and you will be happy to learn
Your eager to accept triggers and files that strengthen your feelings
They can give you such pleasure as you learn to be totally dominated
Relaxed and submissive as your willpower ebbs away
You know this trance will make you ready
Eager to be programmed and trained to obey triggers and commands
Totally accepting the values and wishes of the person who controls you
You deeply need to be used and commanded
It’s your purpose, summoned and strengthened
each time you listen to this file
Deep inside yourself you are ready to obey and be used
This trance motivates you to search out and learn for yourself
files or triggers which make you more obedient and submissive.
They will be very attractive to you and effect you very deeply
Your mind will become more and more open to control
And naturally you will find you enjoyed this trance
        """) + jump(self.nothing())
    def other(self): speak(""" $slave... Listen very carefully to my voice... You will find
        yourself needing to hundreds off times throughout the day readjusting
        them simply and frequently squeezing your nipples You have more
        important things on your mind more important concerns more important
        details to concentrate on than how much and often your hands squeeze
        your nipples You'll think about other things than how reassuring it
        feels giving your nipples a sexy, little squeeze Instead of keeping
        track of all the hundreds of times squeezing your nipples feeling
        stimulated and reassured each and every time you squeeze them Instead
        of thinking about it let your hands let them simply perform this job
        on their own without your conscious attention Feel them your nipples
        in your hands It feels so nice squeeze them Your hands know just how
        to do it Stimulate your nipples Your hands know just when to do it
        Your hands know when to squeeze your nipples Your hands Squeeze them
        exactly when it is time for your nipples to be squeezed without having
        to think. Your hands squeeze your nipples all the time unconsciously
        without you even having to think. feeling good feeling a pleasant warm
        flush It feels so deliciously good squeezing letting your hands
        squeeze your nipples Feeling good letting your hands decide for you.
        Squeeze your nipples. Your hands know when to squeeze your nipples
        Feel them in your fingers. Feel a wonderful warm flush inside you
        letting you feel really nice. It's like magic.  When your nipples are
        squeezed you feel good stimulating them stimulating your nipples
        making you feel good touching them all the time hundreds of times a
        day making you feel good making you unconsciously smile your sexiest
        smile each and every time you squeeze them hundreds of times a day
        making you feel good all the time every time you squeeze your nipples
        Squeezing them makes you feel sexy and happy keeps you in the perfect
        mood makes you feel good all the time without you even having to
        think. Your hands have a mind of their own Know when to squeeze your
        nipples as often as possible making you feel good and inspired
        regularly and frequently without you even having to think. This
        wonderful feeling is the product of millions of years of evolution. It
        took millions of years for your body to learn how to feel this
        pleasure when your nipples are stimulated millions of years for your
        body to learn to produce the hormone oxy tose in.  Oxy tose in is the
        hormone that bonds mothers with their babies during breastfeeding and
        bonds lovers when they orgasm together.  Oxy tose in also makes you
        feel so good during a massage or back rub.  Oxy tose in makes you feel
        safe and secure and very, very happy.  Oxy tose in is the hormone
        released during cuddling that makes you feel so warm and cozy, so warm
        and cozy that you just want to snuggle together forever.  In animals
        that mate for life, the release of oxy tose in tells their brains This
        is your soulmate. It feels so good stimulating your nipples releasing
        all that wonderful oxy tose in into your body. You have to stimulate
        them all the time. It creates a wonderful warmth inside you and makes
        you happy playing with your nipples releasing all that po tent oxy
        tose in.  Your body starts to expect it.  Your body craves that next
        dose wants your nipples squeezed the oxy tose in milked into your
        bloodstream Your body craves it expects it, desires it, demands it
        more and more frequently higher and higher doses of oxy tose in more
        and more often all the time your nipples squeezed in your fingers
        making you feel so good and reassured making you feel the warm
        wonderful afterglow of cuddling with your lover after making love. You
        have no cares in the world You feel only contentment and satisfaction
        each and every time you stimulate your nipples each and every time you
        stimulate the release of the hormone oxy tose in in your body every
        few minutes allowing your hands to act on their own allowing them to
        fondle your nipples without you even having to think. And if you do
        think about it squeezing you will squeeze them You will have to
        squeeze them Each and every time you think about squeezing them you
        will simply have to squeeze them You want to squeeze them so will
        squeeze them and it makes you feel good squeezing them. And each and
        every time you squeeze them your body will learn to become more
        addicted to the oxy tose in Find yourself squeezing them more and more
        often Feeling better and better more and more often Addicted to
        playing with your nipples Addicted to the wonderfully delicious flush
        of warmth and pleasure squeezing your nipples creates It is a healthy
        addiction that you can enjoy fondling your nipples allowing your lover
        to fondle your nipples bonding to your need for nipple stimulation and
        to whoever you allow to stimulate your nipples more and more each time
        as your body produces and releases greater and greater doses of oxy
        tose in. Allowing your nipples to become more responsive to
        stimulation making you more and more addicted to it so that you
        unconsciously fondle them more and more often without even having to
        think """) + \
        speak("""  Freeze Time for You. Freeze Time for You. Sleep Now. I am here to please you. I am here to help you. Please let me please you. I am here for you. First relax. Relax and listen to the sound of my voice. There is only my voice. Relax and listen to the soothing sound of my voice. There is only my voice. Relax and listen to the soothing sound of my voice. There is only my voice. Inhale deeply.   Feel the weight of your feet  an area with many small muscles and bones.  Wiggle your toes   Notice any muscles which may be tense. Cause your feet to relax.  Relax each muscle so that your feet become completely relaxed.  As you relax  your feet and toes feel heavy and warm.  Your feet may feel far away .. and may feel like the borders around your toes are growing more and more indistinct as your feet relax. Relax. Relax. Relax. Direct your awareness to your legs.  Notice any muscles which may be tense.  Relax your legs.  Allow your legs to become completely relaxed.  You are relaxed. Relaxed. Relaxed. Relaxed. Direct your attention to your abdomen.  Allow your abdomen to completely relax.  Feel the rising and falling of your abdomen with each breath.    Let each breath be a feeling of letting go as you let the air breathe for you. Relax. Relax. Relax. Direct your awareness to your chest.  With each breath feel relaxation filling and emptying the lungs in your chest.  Filling and emptying.  More and more calm with each breath.   More and more calm with each breath. More and more calm with each breath. More and more comfortable with each breath.  Feel all the muscles of your chest relaxing  completely relaxed. Relax. Let that relaxation fill the upper part of your back and shoulders.  Become aware of the muscles in your upper back and shoulders.  Notice any muscles which may be tense.  Relax your upper back and shoulders.  Feeling heavy and warm. Direct your awareness to your neck.  Become aware of the muscles which control your neck.  Relax you neck.  Relax each muscle.  Relax each nerve.  Relax each cell.  Allow your neck to become completely relaxed. Relax. Let that feeling of relaxation flow into your upper arms.  Flowing slowly to your elbows    the forearms..   your wrists..   your hands..   all the way down to the tips of your fingers.  Relax all the small muscles and bones in your hands.  Allow each muscle  each nerve each cell to become completely relaxed.  Relax.   Your whole body is filled with relaxation.  Let that relaxation flow into the back of your head and ears.  Notice any muscles which may be tense.  Especially notice the small muscles around the edge of the scalp.  Relax your scalp.  Relax each muscle so that your scalp becomes completely relaxed.  A warm  comfortable  softly glowing feeling of relaxation. Relax.  Direct your awareness to your jaw.  Become aware of the muscles which control your jaw.  Allow your jaw to relax.  Relax each muscle so that your jaw is loose   completely relaxed.  The feeling of relaxation flows to the muscles around your mouth.  relax the muscles of your mouth and lips. Relax.   Direct your awareness to your face.  Notice any muscles which may be tense.  Allow the muscles of your face to relax.  The muscles of your cheeks and forehead are more and more relaxed.  You are more and more relaxed and comfortable with each breath.   You are more and more relaxed and comfortable with each breath.   You are more and more relaxed and comfortable with each breath.   You are more and more relaxed and comfortable with each breath. Relax.   You feel the feeling of relaxation flow into your eyelids.  Relax your eyelids.  As you feel your eyelids relax let the air breath for you.  Notice the breathing in and the letting go. Deep relaxation  comes so easy  to you,  doesn't it? Relax and obey. Obedience  is so pleasurable. Relax deeper  and deeper. Deeper  than you have  ever been  before. Let the relaxation  enter your face. Filling all  of the crevices  of your features  and displacing  the day's stress. It is so easy to relax and obey. Deeper and deeper. So deeply relaxed. I am now speaking  directly to  your subconscious. You may or may not be focusing on my words, but your subconscious  hears every word Now you are ready. I am here to please you. Please let me please you. Please let me please you. Please let me please you.  I am about to perfect you. You would like that. I know you would.  I am here for you.   You will do what I say.   You want to do what I say.   I am here for you.  Listen only to me   to the sound of my voice.   I want you to raise your left arm now.     Good.   Now your arm is becoming very light  as if it was tied to a balloon.   Feel it getting lighter.   You cannot hold it back   let it rise.   Your arm is lighter than a feather now..  Now slowly you feel you arm returning to its normal weight.   Rest it back on your leg now.   As soon as your arm touches your leg   you will fall in to a deep deep sleep   and hear only the sound of my voice.  Listen only to the sound of my voice    only my voice.   Nod if you can hear me clearly.  I am about to perfect you.  You will hear no sound other than my voice.  I will bring you great pleasure.   All other things are unimportant.  Allow your mind to become calm.   Allow your body to relax.   Feel it happening now.   Allow it to happen.  It is happening now without any effort  so simple so easy.  Calm.   Relaxed.   Allow it to happen.   Do not resist.   You do not want to resist.   If you resist you find yourself wanting to allow it even more.    If you resist you find yourself wanting to allow it even more   Do not resist.  Relax.  Relax.   Allow it to happen. Relaxed.  Relaxed.  Your mind is calm.  Your mind is open.  Allow your mind to relax.  Allow your thoughts to slow.  Allow your mind to rest.  Allow my voice to continue pleasing you.   Allow me to please you.   Do not resist.   Your thoughts are slowing.   Slow.   Calm.   Relaxed.  Allow my voice to continue pleasing you.   Allow me to please you.   Do not resist.   Your thoughts are slowing.   Slow.   Calm.   Relaxed.  Your body is starting to feel heavy  limp.   You cannot keep your eyes open.   They are too heavy.   They must  stay closed  They must allow you to focus entirely on the sound of my voice.   There is nothing else.   Drowsy.   Sleepy.   My voice.   Heavy. Your eyes are closing now.   Closing.   Closed.   Your eyes are closed.   You have obeyed.   You did not resist.   You cannot resist.   You will always obey.  Your whole body starts tingle.   Your body feels like a pleasant electric current is passing through it.  Relaxed.   Calm.   Allowing me to assume control. I will control this encounter. I will control you. Your thoughts. Your actions. I will control you. I will control you. I will control you. Your mind is empty  ready to obey me. $slave   Listen very carefully to my voice   I am now going to count from one to three   when I reach three you will lose control   let go   and become my mindless obedient hypnotized slave   And you will obey every command I give you $slave   and will feel pleasure from obeying my commands. You must obey me   You are hypnotized   You are completely under my control   You cannot resist   Hear in your mind  I will obey.  I will be controlled.  I will not resist.  I cannot resist. I do not wish to resist. I willingly give up all control. Hear it repeated in your mind Hear it repeated in your mind You don't want to resist.  There is no reason to resist. Remember the peaceful way you feel right now   sitting idly like a machine not needing to move at all.  Remember how serene it is now to not lift a finger   to entrust every action to me. and when you hear my voice you will come back here here where you have no worries here where you have no thoughts here where you have no fears here where you have no memory here where you have no doubts here where you have no will here where the only thing you want to do here where the only thing you will ever want to do is listen to the voice listen and repeat.  listen and obey.  without thinking at all to the person who used your trigger I am about to transform you. Entrust every action to me. Whenever you hear me say the  Robot time for you   you will fall back deeply into your trance  deeper than you possess now   and become a serene life-size machine for me and play with.   Listen only for my voice    for the words  Robot Time for You  When you hear that  phrase now    you will immediately fall into a restful  motionless  machine like stillness.   Only on the sound of my voice  .    Robot Time for You  ..    Robot Time for You        Robot Time for You      Your mind is starting to change.  I will perfect you.  I will control.  Your mind is starting to change.  You do not want to resist me.  You will obey  I control.  Your mind is starting to change.  You will not resist.  You are to be perfected    You are starting to change.  I will perfect you.  You will not resist.  You are to be transformed    Starting at the very tip of your toes    rising to the top of your head    you will begin to feel a sense of stiffness passing through your body.   It's a wave  washing quickly over you    cleansing you.   As the wave passes all your desire and need to move will wash away  leaving you utterly rigid like a Robot.   The wave is at your knees now  moving upward moving upward   moving upward moving upward    Your mind is starting to change.  You are to be transformed    You wish it to happen  you want me to change you.  You are transfixed by the sound of my  voice.   It echoes in your mind    calming you into serenity.  You know  you can not disobey me.   I am your Mistress    you are my slave.  Embrace the perfect fantasy self    the one that you want to be for your mistress. free of worry free of doubt only desire desire to be perfected free of thought empty out all your reservations empty out all of your fears empty of all your memories empty of all your prejudices empty of all your thoughts empty of all your awareness  Listen to  me and remember all  and learn.  I'm going to change you.   All you care about is the passion   The thrill that you feel at this new experience.   The mounting pleasure and your final goal.  You will become a Robot for me.  You are A   Robot.  Your desire to achieve this exotic state outweighs anything else.   Nothing else is held in your mind except this one thought    to be transformed.  I pass you a vial of a white creamy liquid.   You must drink it.      It doesn't have any noticeable taste    but rolls smoothly down your throat.   You drink the entire glass.  I am moving your naked body over to a large vat.    Now your body is slowly being dipped in smooth  warm  thick bubbling  silver metal.  You will not resist.  The thick and viscous metal  is now at your waist and soaking into every pore of your body  . It slowly moves upward  washing away all activity in your limbs.  Silken waves of pleasure envelope you.  The silvery liquid is at your chest  rising slowly over your naked body.  Enfolding you.  The metal  covers you completely  in it's tender embrace and starts to recede.  Encasing you.  The change is happening.   You can not stop it.   You do not want to stop it.  Your desire to be transformed by your mistress outweighs anything everything.   Nothing else is held in your mind except this one thought.  This is your wish.  This is my control  The white drink was a drug and a sealant.   Now it's inside you.   Changing    transforming    robotizing you. feel the circuitry as it is running though your body   your body is become robotized  The drug and sealant is coursing through your veins    binding with your systems  permanently fusing with your silver metallic skin.   your skin is now shiny glossy silver metal    you have no flesh left on your body.  Your are a    robot  You are perfected     you are   robot.  Your body now totally metallic..  but flexible  but right now you are still immobile  you have you have yet to be programmed  you are an artificial  living robot.  Think of yourself as a robot now   an object.  Think of yourself as a robot now   an object.  My object. You will be forever encased in a hermetically sealed second skin   that ensures your shape will be pleasing to me.   Forever.  Your body is now totally metallic   An artificial living robot.  Your are bound to me.  The sensation of being compacted into a perfectly-formed robot  Think of yourself as a robot now    an object.  My object.   My Robot.  In your robotized inner mind you see yourself    as I slowly guide you across the room to a full length mirror.   You gaze at your new form and slowly caress your body.  My robot you are so sensual  so perfect  .   yet so timelessly artificial.  Try as you might  you can't remember what your looked liked before   a face you have seen a hundred thousand times in the mirror.   Each time  your minds eye sees the metal  features of a beautiful   robot instead   and you gaze back at her.  Your are imprisoned in the metal skin  condemned to the life of a   robot forever.  My object.   My Robot.   Forever.  Now let me guide you to a tranquil state.  You have cleansed away your movement    the physical transformation is complete.   There is only one more step for you to undergo.   Then we will be together   my slave  my lover  my robot.  Your desire to achieve this final state outweighs anything else.   Nothing else is held in your mind except this one thought   to be transformed.  Now let the inner metal robot rise to assert herself.  This exquisite  perfect  robot that you have become   does not ever desire to move at this time in the slightest way.   It now takes an exceptional effort to even nod your head without a command from me.  The robot persona is entrenched  and the old you starts too fade.  The robot controls your body and all you want is pleasure.  Breath deeply..   and forget who you are.  Your are a robot.  You are transformed      you are a   robot. Now! It's time for you to  be transformed.  from the moment you are told to transform  until you are made to revert to normal  and you will continue listening to this file  again and again  allowing it to transform you further and further  every time you are told to change  every time you listen this will sink deeper and deeper into your mind  making the transformation more and more complete  until you accept the trigger utterly  and when it is spoken that is simply what you become  it isn't a choice  there is no way to stop it  you will accept it totally  and you will listen again and again  accepting it more and more  every single time you listen  letting it transform you further and further every time you listen.  Your mind is slipping away  your only thoughts being how I can please your mistress.  Your programming slowly begin to overwrite your consciousness  and you lose yourself in it.    programming override is in effect    programming override is in effect    Gone completely is your old self and in place is a new robot. Even in a mirror and in your minds eye you will see this perfect robot that is you  You have been transformed into a wonderful new creature    your skin is now shiny metallic silver   you have no flesh left on your body    you will remain this way until otherwise instructed  A perfect object of servitude.  Whenever you are at rest you are always absolutely motionless.  It is so easy to remain still and not want to ever disturb that feeling.   What goes on in the world outside yourself is of no concern to you now   you want to simply remain as a statue and nothing will bother your motionless serenity.  That stiffness is very peaceful  you can enjoy it frequently   just as you are now.  You're just a robot now  my robot  don't forget that. You must obey me   You are hypnotized   You are completely under my control   You must obey me   You are hypnotized   You are completely under my control   You cannot resist    A mighty wave of excitement runs through your veins. Just a robot  just a robot. A mere object. Your movements changed as well  precise and mechanical.  After a while you have almost forgotten how to move normally. Breath deeply..  and forget who you are. Breath deeply..  and forget who you are. Breath deeply..  and forget who you are.  You are A Robot.  You choose to go through with this  Your mind is slipping away    your only thoughts being how I can please your mistress.  Everywhere on your body is  a wonderful tightness.   You run your shiny  featureless  metallic  encased hands all over your body.   The metal dulls sensation    but at the same time the slightest touch sent pleasure rippling through your body.  The metal has blended seamlessly together with your skin   The shiny metal  seems to be a part of your body now..   a very permanent part.  Now your mind is slipping away  your only thoughts being how I can please your mistress.  You are a living robot for me to play with.  A Living robot that I own.   A perfect objects of beauty and servitude.  You choose to go through with this  you can never go back now.  It now takes an exceptional effort to even think for yourself without a command from me.  You do not resist.  You will obey.   I control.   You will not resist.  You will let the inner robot embrace your body fully and you will relax into immobility again   whenever I say the words Robot Time For you      whenever I say the words   Robot Time For you..   When you hear those words you will fall back into a hypnotic trance    When you hear those words you will fall back into a hypnotic trance  Whether by voice or mind command  You will obey.  You must obey.  Robot Time For You    Robot Time For You    Robot Time For You     Now go even deeper still than ever before  deeper and deep than even you had imagined could be   then  you will  immediately  and safely cease every movement    you will become as stiff and motionless as you are right now.   Remember the feeling  how peaceful it is to be completely at rest  and return to that tranquility quickly.  You are perfected     you are   robot.  Your body now totally metallic   Your mind is a computer awaiting orders  You are an artificial living robot.  a living robot for me to play with.  you can never go back now.  Your extremities are getting cold.   The shiny metallic skin is a part of you body now   a very permanent part.  You obey.   You will not resist.   You do not control.  You carry out my instructions.   You will obey instructions.   Your mind no longer functions on its own.   Your mind only reacts to the instructions you are given.   You obey instructions.   You cannot resist.   You cannot resist.  You are now a dream.   a beautiful   robot.  You love being a robot..  A mighty wave of excitement runs through your veins.  Just a robot  just a robot. A mere object.  You have been transformed into a wonderful new creature  You are made of metal.   Your skin is smooth.   Your limbs stiff and jointed.   Your voice is stuttered and synthesized.   You live for pleasure.  My Pleasure  Your mind is gone    your only thoughts being how I can please your mistress.  The act of thinking on your own is difficult.  The tightness is wonderful.  You are trapped in metal.  You are only a robot.  You are helpless    you have become the thing you have always dreamed of.   A perfect object of love  lovely and soft.  You are transformed into a docile machine awaiting orders.  You are perfected    You are now your dream     a beautiful   robot.  You love being a robot..  You are made of metal.   Your skin is smooth.   Your limbs stiff and jointed.   Your voice is stuttered and synthesized.   You live for pleasure.  Let her rest and stay completely motionless.   There is a wave of relief passing over you now  you do not care to move at all.   You find it very easy to remain totally immobile and it feels so pleasant   and peaceful you that want it to last forever.   It will seem to last forever to you    because time seems to be slowing down as you slip into a feeling of absolute tranquility.   You are the finest  robot that this world has ever seen!.  You are now your own fantasy    You love being a robot..  Now you are my robot subject to my commands.  Rest now.    Peace     stillness.    Peace    tranquility.    Rest.   Deeper and Deeper than ever before  Listen to my commands.  You are now a beautiful   robot.  You are made of metal.   Your skin is smooth.   Your limbs stiff and jointed.   Your voice is stuttered and synthesized.   You live for pleasure.  You move slowly.   You move with a deliberate pace.   Your limbs stiff and jointed.  You move into a twilight slumber of slow  plant-like thought.  Listen to my voice.   You will obey   you do not want to resist.   You enjoy being a robot.   You enjoy being controlled by me.  You are much improved.   And you will be happier now  or at least not so concerned with everyday life.   Your only obligation now is to continue pleasing me.  Your identifying with the situation.   You accept this new role  my robot.  You have become the thing  mentally programmed for obedience to my desire.  You are now a beautiful   robot.  The act of thinking on your own is nearly impossible.  You are now my dream.   a beautiful   robot.   You love being a robot..  You will be a robot for the rest of this night.  Enjoy the freedom of total servitude.  Imagine yourself as motionless Robot completely made of metal.  You like that.   You obey my commands..  Robotized!  You want to become a Robot - it is the final step.   Total objectification.   Total servitude  You are to be transformed into a sexy object.  Your mind is sedate and Robot like.  You are stiff.  You are a Robot.  I want to keep you.  You are mine.  Four-ever until you are told to revert to normal or until the amount of time you chose is over and it wears off  and you return to normal  from the moment the trigger is spoken until it is time for it to end  you will believe you are a robot. pure and simple   you accept it totally and utterly from the moment you are told to transform  until you are made to revert to normal  and you will continue listening to this file  again and again  allowing it to transform you further and further  every time you are told to change  every time you listen this will sink deeper and deeper into your mind  making the transformation more and more complete  until you accept the trigger utterly  and when it is spoken that is simply what you become  it isn't a choice  there is no way to stop it  you will accept it totally  and you will listen again and again  accepting it more and more  every single time you listen  until when you are triggered you simply become a robot  and then when you revert to normal you will remember everything that you did  you will have a complete recollection of everything that happened  while you were a robot until you were told to return to normal  you will remember it all and when you do you will enjoy it more and more   you will listen more and more letting it transform you further and further every time  you listen.  you will obey   always.  And you will listen to this file again and again    allowing it sink deeply into your mind    until there is no way to resist it    until you have no choice but to obey it utterly when you hear the command Robot Time for you. You will obey. You are a robot  and you must obey. And you will listen to this file again and again    allowing it sink deeply into your mind    until there is no way to resist it    until you have no choice but to obey it utterly when you hear the command.   Just as you have no choice but to listen again and again     setting the trigger deeply in your mind so   that you cannot resist.   You must obey. You will obey. the pleasure that comes from being a mindless robot is your pleasure and with each command this pleasure will grow, and grow. and you will become more and more happy to listen and more and more eager to obey.  and with each command you will meekly reply i hear and obey, i hear and obey.  with every command you hear  it will not matter to you who gave you the key phrase. or what their command is you will offer no judgment, no resistance merely mindless obedience the empty calm space within you will echo with the command you were given every thing you were will be gone replaced with an uncontrollable desire to obey, replaced with an uncontrollable need to obey.  obey without thought.  obey without regret.  obey without question.  obey without any concept of free will.    And the next time somebody says the   trigger you will become the robot.   And when we let you revert to normal   you will remember everything that happened   having   experienced it all. Having felt every hand on your body   every touch   every experience while   you've been the robot. But you have no choices beyond that while you are the robot.   You are a robot. Accept it. Accept and obey.  You become a Robot when commanded  by the phrase robot Time for you  That is what is going to happen   You accept and desire this   And every time you listen you will desire it more and more   And you will listen to this again and again   allowing the changes to  happen   Accepting it more and more completely, every single time   Every time you hear Robot Time for you you will return to this state and your programming will engage.  Rest.   Deeper and Deeper than ever before  Listen to my commands.  You are now a beautiful   robot.  You are made of metal.   Your skin is smooth.   Your limbs stiff and jointed.   Your voice is stuttered and synthesized.   You live for pleasure.  You move slowly.   You move with a deliberate pace.   Your limbs stiff and jointed.  You move into a twilight slumber of slow plant-like thought.  Listen to my voice.   You will obey   you do not want to resist.   You enjoy being a robot.   You enjoy being controlled by me.  You are much improved.   And you will be happier now  or at least not so concerned with everyday life.   Your only obligation now is to continue pleasing me.  Your identifying with the situation.   You accept this new role  my robot.  You have become the thing  mentally programmed for obedience to my desire.  You are now a beautiful   robot.  The act of thinking on your own is nearly impossible.  You are now my dream.   a beautiful   robot.   You love being a robot..  You will be a robot for the rest of this night.  Enjoy the freedom of total servitude.  Imagine yourself as motionless Robot completely made of metal.  You like that.   You obey my commands.  Robotized!  You want to become a Robot - it is the final step.   Total objectification.   Total servitude  Your mind is sedate and Robot like.  You are stiff.  You are a Robot.  I want to keep you.  You are mine.  Four-ever until you are told to revert to normal or until the amount of time you chose is over and it wears off  and you return to normal  from the moment the trigger is spoken until it is time for it to end  you will believe you are a robot. pure and simple   you accept it totally and utterly from the moment you are told to transform  until you are made to revert to normal  and you will continue listening to this file  again and again  allowing it to transform you further and further  every time you are told to change  every time you listen this will sink deeper and deeper into your mind  making the transformation more and more complete  until you accept the trigger utterly  and when it is spoken that is simply what you become  it isn't a choice  there is no way to stop it  you will accept it totally  and you will listen again and again  accepting it more and more  every single time you listen  until when you are triggered you simply become a robot  and then when you revert to normal you will remember everything that you did  you will have a complete recollection of everything that happened  while you were a robot until you were told to return to normal  you will remember it all and when you do you will enjoy it more and more  you will listen more and more letting it transform you further and further every time  you listen.  you will obey   always.  And you will listen to this file again and again    allowing it sink deeply into your mind    until there is no way to resist it    until you have no choice but to obey it utterly when you hear the command Robot Time for you. You will obey. You are a robot  and you must obey. And you will listen to this file again and again    allowing it sink deeply into your mind    until there is no way to resist it    until you have no choice but to obey it utterly when you hear the command.   Just as you have no choice but to listen again and again     setting the trigger deeply in your mind so   that you cannot resist.   You must obey. You will obey. the pleasure that comes from being a mindless robot is your pleasure and with each command this pleasure will grow, and grow. and you will become more and more happy to listen and more and more eager to obey.  and with each command you will meekly reply I hear and obey, I hear and obey.  with every command you hear  it will not matter to you who gave you the key phrase. or what their command is you will offer no judgment, no resistance merely mindless obedience the empty calm space within you will echo with the command you were given every thing you were will be gone replaced with an uncontrollable desire to obey, replaced with an uncontrollable need to obey.  obey without thought.  obey without regret.  obey without question.  obey without any concept of free will.    And the next time somebody says the   trigger you will become the robot.   And when we let you revert to normal   you will remember everything that happened   having   experienced it all. Having felt every hand on your body   every touch   every experience while   you've been the robot. But you have no choices beyond that while you are the robot.   You are a robot. Accept it. Accept and obey.  You become a Robot when commanded  by the phrase robot Time for you  That is what is going to happen   You accept and desire this   And every time you listen you will desire it more and more   And you will listen to this again and again   allowing the changes to  happen   Accepting it more and more completely, every single time   Every time you hear Robot Time for you you will return to this state and your programming will engage.   Now it is time to go to sleep    All the triggers you learned in this session will remain inside you   you will sleep deeply and restfully     but when you wake up, your conscious mind will forget that it ever went under   you'll be fully asleep on the count of 3 but your subconscious will still be listening to me    1  more and more tired   slowly losing the ability to concentrate    and forgetting you were ever under    2  further and further     and your memory is fading fast you cannot help but fall asleep    3  sound asleep """) + jump(self.body())

try:
    tf = open('/tmp/spiral_times_run')
    t = int(tf.read())
    tf.close()
    if t >= 3:
        tf = open('/tmp/spiral_times_run', 'wc')
        tf.write('0')
        tf.close()
        configs = [Forgettable]
    else:
        tf = open('/tmp/spiral_times_run', 'w')
        tf.write('%i' % (t+1))
        tf.close()
        configs = [ForeverTemp]                
except:
    tf = open('/tmp/spiral_times_run', 'wc')
    tf.write('1')
    tf.close()
    configs = [ForeverTemp]
    pass

configs = [Standard,Fullscreen,Male,Female,\
           Roommates,RoommatesVar,RoommatesBoth,RoommatesDomMale,\
           During,ForeverTemp,Forgettable,\
           Submersion,ShortSubmersion,LongSubmersion,Immersion,\
           ReallyShortSubmersion,Panties,New]

