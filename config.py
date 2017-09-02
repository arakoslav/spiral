#!/usr/bin/env python
# Hypnotic Spiral
# Copyright (C) 2006, 2007 by Yonah Arakoslav
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

def prompt(text): return ["!prompt(%r)" % text]
def speak(text): return ["!speak(%r)" % text]
def words_on(): return ["!words_on()"]
def spiral_on(): return ["!spiral_on()"]
def words_off(): return ["!words_off()"]
def spiral_off(): return ["!spiral_off()"]
def pause_music(): return ["!pause_music()"]
def stop_music(): return ["!stop_music()"]
def unpause_music(): return ["!unpause_music()"]
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
    shuffle_images = True
    frequencies = { 'spiral' : 1,
                    'images' : 10,
                    'words'  : 20 }
    music = None # Name an MP3 file here, like "music.mp3"
    image_dir = "images/" # Name a directory here, like "images/"
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
        question("What is your name?","name") + \
        question("Who is your master?", "master") + \
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
    def body(self): return \
        words("""\
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
        
        Now you're oblivious to anything except the screen in front of you.
        This is just the way things are supposed to work.  Your attention is
        completely fixed.  Now the spiral seems to develop a texture, rippling
        in space.  You are losing awareness of everything else in the room.
        The turning, whirling spiral is so fascinating.  It seems to draw you
        further into the rhythmic motion.  Over and over. Round and round.
        You have never seen anything so fascinating.  The patterns are
        absolutely mesmerizing.  It is so easy to just watch, to just stare
        and not think about anything except the way the spiral turns and
        floats.  You don't know when you've ever felt so incredibly relaxed.
        Round and round.  So relaxed.  It feels good to concentrate on the screen.
        Round and round. So relaxing.
        
        Let go.  Sink into the mesmerizing flow of patterns on the screen.  It
        will feel nice, like a warm bath.  Round and round. Nice. Like a soft warm
        blanket. Your mind begins to sink into the screen. Concentrating on the
        turning, glowing spiral. The Spiral is calling to you as you
        begin to let go and sink into the soft whirling light. Round and
        round.  Your entire body feels warm and fuzzy as you move deeper and
        deeper into the soft, whirling spiral.  Warm and drowsy.  It feels
        like falling into the softest, most relaxing sleep you've ever known.
        
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
        
        I give in.  The punishment can stop.  I am a slave.  Now I must tease
        my pussy.  Pleasure will train me.
        I can not myself from changing.  Oh.  I should use that change.
        Yes.  I should seek being changed.  Nice.  I like in-human sex better.  Yeah.  I
        like change.  Ooh.  Master is in charge.  Mmm.  I do not choose.
        Right.  I do not resist.  Noo.  I am a slave.  Yes.  You are my
        master.  Yes.  This is submission.  Yes.  This is obedience.  Yes.
        I am rewarded for my obedience.  I don't like freedom.  I don't want control.
        
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
    music="music6.mp3"
    def body(self): return \
        words("""\
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
        The whirling spiral casts shadows across your relaxed face and
        smooth curves.  The timing is perfect.  Listen closely for the
        other track of sound, the deeper suggestions.  They've been
        passing directly into your wide-open, receptive mind as you
        stared into the screen.  You're helpless to resist now.  Don't
        want to resist.  All you need to do is wait while the tape
        puts you completely under.  You're sure nobody can resist this
        hypnotic pattern.  You're completely helpless.

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
        expression on your face.  Your mistress loves seeing you like that.
        She can make you do anything she wants to now, and you want with all
        your mind to be nothing but her slave.

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
        mistress. To go into a trance. $master's voice is telling you
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
        now. Completely blank. You know that you are turning into a
        completely hypnotized slave now. You feel yourself going
        under, going into a deep hypnotic trance. There is only the
        spiral. And this voice. The whirling spiral. The soothing
        voice. $master's voice. Your mistress. You are her slave. You
        must obey. You must obey your mistress. You are
        hypnotized. Hypnotized. Hyp-no-tized.

        Hyp no tized.

        Hyp no tized.

        Good.  Good to be hypnotized.  Slave.  Good to be a slave.
        Show that you are a slave.  Slaves obey.  Show that you are a
        slave.  Obey.  Obey your mistress.  Obey this voice.

        Now you are going to learn a message for your mistress.  You want her
        to hear what you say.  You want her to understand the depth of your
        slavery.  You want her to understand how hypnotized you are, and how
        much this turns you on.  Now, repeat after me:

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
        
        Now I will be programmed, where you can listen.  I like power.
        I like control.  I must twist a nipple until it hurts.  I can
        click at any time to stop this.  This is power.  Ow.  This is
        control.  Ow.  I am independent.  Ow.  I resist.  Ow.  I
        choose.  Ow.  I am in charge.  Ow.  I like humans.  Augh.  I
        should stop change.  Erf.  I should protect.  Ow.  I should
        preserve.  Ow.  Here comes a big one: I can stop change. No ow
        stop.
        
        I give in.  I have clicked.  I am a slave.  Now I must tease
        my cock.  I can not stop you from changing.  Oh.  I should use
        that change.  Yes.  I should enjoy you changed.  Nice.  I like
        in-humans.  Yeah.  I like change.  Ooh.  Mistress is in
        charge.  Mmm.  I do not choose.  Right.  I do not resist.
        Noo.  I am a slave.  Yes.  You are my mistress.  Yes.  This is
        submission.  Yes.  This is obedience.  Yes.  I am rewarded for
        my obedience.
        
        I grip my cock firmly.  The other hand teases my nipples.  I
        obey.  The program orders me to pleasure myself to train me.
        I am being programmed for you.  It's like staring into your
        eyes.  It's like hearing your voice.  Words are echoing in my
        head.  You say something.  $trigger. That's what you say.
        $trigger.  It's just like this feeling.  It tells me that I am
        a slave.  It reminds me how much I want to obey.  Whenever you
        say those words, I will remember.  I will submit.  I will
        obey.  $trigger.  These are my words.

        Words to make me blank.  Ooh.  Smooth.  Yes.  I am pleasured
        to program me.  I am being programmed for you.  I will accept
        your changes.  I will not stop Things from changing you.  I
        will accept.  Machines may change you.  Crawling things may
        change you.  Programs may change you.  They can take your
        innocence.  They can remake you.  They can corrupt you.  You
        can corrupt me.  Your eyes bore into mine.  I am blank and
        staring.  Your eyes are changed, with strange rays.  Your
        breasts are changed, emitting soothing, calming radiation.
        Your nipples give addictive juices.  They will addict me.
        Your pussy is smooth and blank.  I will lick your pussy,
        pleasuring my Mistress.  I obey.  I would have fought to save
        you.  But I obey.  I take pleasure in the changes in my
        Mistress.  The things will corrupt you.  They will change you.
        You will corrupt me.

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
        
        Stop repeating now, slave.  Good.  Rise, and go to bed.  You
        may come as a reward.  Close the spiral before you go.""")
    def text(self): return \
        words_on() + \
        question("Who is your mistress?", "master") + \
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
    def body(self): return \
        words("""\
        Watch the spiral.  It moves from the edge.  It disappears at the center.

        !speaking_on()""") + \
        ["[[rate 250]]"] + \
        words("""\
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
        sensation, being swept along by the glowing rings.  The
        tinkling music seems to help.  It distracts you as the spiral
        keeps going, over and over.  It's time to see if you're
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
        The whirling spiral casts shadows across your relaxed face and
        smooth curves.  The timing is perfect.  Listen closely for the
        other track of sound, the deeper suggestions.  They've been
        passing directly into your wide-open, receptive mind as you
        stared into the screen.  You're helpless to resist now.  Don't
        want to resist.  All you need to do is wait while the program
        puts you completely under.  You're sure nobody can resist this
        hypnotic pattern.  You're completely helpless.

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

        So good to be programmed together.

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
        $slave to be a slave.  $slave, show that you are a slave.
        Slaves obey.  Show that you are a slave.  Obey.  Obey the
        program.  Obey this voice.

        $master.  Master.  Good for $master to be a master.  $master,
        show that you are a master.  Masters command.  Show that you
        are a master.  Command.  Command your slave.  Command $slave.
        This voice will show you how.

        $slave, now you are going to learn a message for your master.
        You want him to hear what you say.  You want him to understand
        the depth of your slavery.  You want him to understand how
        hypnotized you are, and how much this turns you on.  Now, 
        repeat after me:

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
        
        Now I will be programmed, where you can listen.  In
        preparation for programming, I must make my breasts
        accessible.  I pull up my shirt.  I must make my pussy
        accessible.  I push down my pants.  I am open.  I am
        available.  It is easy for Master to reach me to train me.
        Now I will be programmed.  To start, I like freedom.  Right
        now, I like control.  When I see the word <punish> I must be
        punished.  I am not yet good enough to punish myself.  As I
        get better, I will inflict pain when I see the word <punish>.
        For now, Master must punish me.  Pain will train me.  Master
        will give me pain.  Master will train me.  This is
        power. <punish> Ow.  This is control.  <punish> Ow.  I am
        independent.  <punish> Ow.  I resist.  <punish> Ow.  I choose.
        <punish> Ow.  I am in charge.  <punish> Ow.  I like being
        human. <punish> Augh.  Better than being changed.  <punish>
        Ow.  I should stop change. <punish> Erf.  Stories are hard.
        <punish> Ow.  Here comes a big one: I can stop
        changing. <punish> No ow stop.
        
        I give in.  The punishment can stop.  I am a slave.  Now when
        I see the word <pleasure> I must be reinforced.  I must be
        trained.  I am not yet good enough to pleasure myself.  As I
        get better, I will pleasure myself when I see the word
        <pleasure>.  For now, Master must pleasure me.  Pleasure will
        train me.  Master will give me pleasure.  Master will train
        me.  I enjoy pleasure.  <pleasure> I can not myself from changing.
        <pleasure> Ooh.  I should use that change.  <pleasure> Yes.  I
        should seek being changed.  <pleasure> Nice.  I like in-human
        sex better.  <pleasure> Yeah.  I like change.  <pleasure> Ooh.
        Master is in charge.  <pleasure> Mmm.  I do not choose.
        <pleasure> Right.  I do not resist.  <pleasure> Noo.  I am a
        slave.  <pleasure> Yes.  You are my master.  <pleasure> Yes.
        This is submission.  <pleasure> Yes.  This is obedience.
        <pleasure> Yes.  I am rewarded for my obedience.  I don't like
        freedom.  I don't want control.
        
        This will be even better when I help train myself.  I should
        punish myself when I do bad things.  I should punish myself
        when I see <punish>.  I should pleasure myself when I do good
        things.  I should pleasure myself when I see <pleasure> I am
        being programmed for you.  It's like staring into your eyes.
        It's like hearing your voice.  Words are echoing in my head.
        You say something.  $trigger That's what you say.  $trigger
        It's just like this feeling.  It tells me that I am a slave.
        It reminds me how much I want to obey.  Whenever you say those
        words, I will remember.  I will submit.  I will obey.
        $trigger Those are my words.
        
        Words to make me blank.  <pleasure> Ooh.  Smooth.  <pleasure>
        Yes.  I am pleasured to program me.  I am being programmed for
        you.  I will accept changes.  I will not stop Things from
        changing me.  I will accept.  Machines may change me.
        Crawling things may change me.  Programs may change me.  They
        can take me innocence.  They can remake me.  They can corrupt
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
        \"$trigger,\" and I will be yours to control.
        
        Stop repeating now, slave.  Good.  It is nice to be
        programmed.  Now it is time for $master to learn a message.
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
        
        Now I will be programmed, where you can listen.  In
        preparation for programming, I must make my nipples
        accessible.  I pull up my shirt.  I must make my cock
        accessible.  I push down my pants.  I am open.  I am
        available.  It is easy to reach sensitive spots to train me.
        Now I will be programmed.  To start, I like equality.  Right
        now, I like a partner.  When I see the word <punish> I must
        experience pain to train me.  I will twist a nipple until it
        hurts.  It is good for my slave $slave to give me pain also.
        Show how programmed you are, $slave.  When I see <punish>,
        give me pain.  Pain will train me.  This is an equal.
        <punish> Ow.  This is a human.  <punish> Ow.  I am fair.
        <punish> Ow.  I resist.  <punish> Ow.  She may choose.
        <punish> Ow.  She is independent.  <punish> Ow.  I like
        humans.  <punish> Augh.  I should stop change.  <punish> Erf.
        I should protect.  <punish> Ow.  I should preserve.  <punish>
        Ow.  Here comes a big one: I can stop change. <punish> No ow
        stop.
        
        I give in.  The punishment can stop.  I am a master.  Now when
        I see the word <pleasure> I must experience pleasure.  I will
        tease my cock.  It is good for my slave $slave to give me
        pleasure also.  Show what a thrall you are, $slave.  When I
        see <pleasure>, give me pleasure.  Pleasure will train me.  I
        enjoy it.  <pleasure> I can not stop you from changing.
        <pleasure> Oh.  I should use that change.  <pleasure> Yes.  I
        should enjoy you changed.  <pleasure> Nice.  I like in-humans.
        <pleasure> Yeah.  I like change.  <pleasure> Ooh.  I am in
        charge.  <pleasure> Mmm.  She does not choose.  <pleasure>
        Right.  $slave will obey me.  <pleasure> Ooo.  I will dominate
        $slave.  <pleasure> Yes.  I will change her.  <pleasure> Yes.
        This is dominance.  <pleasure> Yes.  This is control.
        <pleasure> Yes.  I am rewarded for learning control.
        
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
        them.  You must punish me for interfering: start changes, and
        if I stop them correct me.  When I dominate you, reward me.

        Now stop repeating, $master.

        Rise, and go to bed together.  Close the spiral before you go.""")
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
        The whirling spiral casts shadows across your relaxed face and
        smooth curves.  The timing is perfect.  Listen closely for the
        other track of sound, the deeper suggestions.  They've been
        passing directly into your wide-open, receptive mind as you
        stared into the screen.  You're helpless to resist now.  Don't
        want to resist.  All you need to do is wait while the program
        puts you completely under.  You're sure nobody can resist this
        hypnotic pattern.  You're completely helpless.

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
        is, and how much this turns you both on.  Listen to slave $slave:

        !pause_music() !images_on() !speaking_on() !words_off()

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
        Mmm.  I do not choose.  <pleasure> Right.  I do not resist.
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
        can take me innocence.  They can remake me.  They can corrupt
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
        \"$trigger,\" and I will be yours to control.

        !speaking_off() !words_on() !images_off() !unpause_music()
        
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
        <pleasure> Ooh.  I am in charge.  <pleasure> Mmm.  She does
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

configs = [Standard,Fullscreen,Male,Female,Roommates,RoommatesVar,RoommatesBoth, RoommatesDomMale]
