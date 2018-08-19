#!/usr/bin/env python
# Speech-driven spiral
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

# To do:
#  * modular system, making it easier to add new components like:
#  * click-if-awake
#  * randomly placed words
#  * record user, video (probably Mac iSight only) and audio
#  * mail variable contents to a master
#  * mail audio and video to a master

import pygame, math, os, sys, random, textwrap, string, re
from datetime import datetime
from pygame.locals import *
from configSpeaker import configs
from AppKit import *
try:
    from PySight import *
    camera = True
except:
    camera = False

def pick_config(cs):
    if len(cs) == 0:
        print "No configurations.  Define 'configs' at the end of config.py."
        sys.exit(1)
    elif len(cs) == 1:
        return cs[0]
    if len(sys.argv) == 2:
        for c in cs:
            if c.name == sys.argv[1]:
                return c
    print "Select a configuration:"
    for i in xrange(0,len(cs)):
        print "  %i) %s" % (i, cs[i].name)
        try:
            for line in textwrap.wrap(textwrap.dedent(cs[i].description)):
                print "     %s" % line
        except:
            pass
    while 1:
        try:
            input = raw_input('> ')
            return cs[int(input)]
        except KeyboardInterrupt:
            print
            sys.exit(0)
        except:
            print "I didn't understand that.  Please try again."

# From http://www.pygame.org/pcr/hollow_outline/index.php
def textHollow(font, message, fontcolor):
    notcolor = [c^0xFF for c in fontcolor]
    base = font.render(message, 0, fontcolor, notcolor)
    size = base.get_width() + 2, base.get_height() + 2
    img = pygame.Surface(size, 16)
    img.fill(notcolor)
    base.set_colorkey(0)
    img.blit(base, (0, 0))
    img.blit(base, (2, 0))
    img.blit(base, (0, 2))
    img.blit(base, (2, 2))
    base.set_colorkey(0)
    base.set_palette_at(1, notcolor)
    img.blit(base, (1, 1))
    img.set_colorkey(notcolor)
    return img

def textOutline(font, message, fontcolor, outlinecolor):
    base = font.render(message, 0, fontcolor)
    outline = textHollow(font, message, outlinecolor)
    img = pygame.Surface(outline.get_size(), 16)
    img.blit(base, (1, 1))
    img.blit(outline, (0, 0))
    img.set_colorkey(0)
    return img

class Spiral (NSObject) :
    def init_screen(self):
        flags = HWSURFACE | DOUBLEBUF | ASYNCBLIT
        if self.config.fullscreen:
            flags |= FULLSCREEN
            pygame.mouse.set_visible(False)                   
            if self.config.size in pygame.display.list_modes():
                self.x_size, self.y_size = self.config.size
            else:
                self.x_size, self.y_size = pygame.display.list_modes()[0]
        else:
            flags |= RESIZABLE
            self.x_size, self.y_size = self.config.size
        self.screen = pygame.display.set_mode((self.x_size, self.y_size),flags)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.unicode == 'f':
                    self.config.fullscreen = not self.config.fullscreen
                    self.init_screen()
                    self.rescale()
                elif event.unicode in ['<',',']:
                    self.config.time_scale = max(self.config.time_scale-1,1)
                elif event.unicode in ['>','.']:
                    self.config.time_scale = self.config.time_scale+1
                elif event.unicode == 'i':
                    self.draw_image = not self.draw_image
                elif event.unicode == 'n':
                    if self.speaking():
                        self.speaking_text = None
                        self.v.stopSpeaking()
                    self.advance_text()
                elif event.unicode == 'q':
                    self.stop_recording()
                    sys.exit(0)
                    self.running=False
            elif event.type == VIDEORESIZE:
                self.config.size = event.size
                self.init_screen()
                self.rescale()

    def init_camera(self): pass
        #self.camera = CSGCamera.alloc().init()
        #self.camera.setDelegate_(self)
        #self.camera_index = 0

    def start_recording(self):
        #self.camera.startWithSize_((320,240))
        pass #os.system('osascript start_recording')

    def stop_recording(self):
        pass #self.camera.stop()

    def camera_didReceiveFrame_(self, camera, frame):
        self.camera_index += 1
        if self.camera_index % 30 == 0:
            filename="video/img%s.tif" % (datetime.now())
            frame.TIFFRepresentation().writeToFile_atomically_(filename, 0)

    def init_speech(self):
        voice = self.config.voice
        self.v = NSSpeechSynthesizer.alloc().initWithVoice_(voice)
        self.v.setDelegate_(self)
        self.spoken_word = " "
        self.speaking_text = None
        
    def speak(self,text):
        re.sub("\n? +"," ",text)
        # print "Speaking text beginning with %s" % text[0:20]
        if ' !' in text: print "Warning: script command embedded in spoken text"
        self.speaking_text = self.varsub(text)
        self.should_advance = False
        self.v.startSpeakingString_(self.speaking_text)
            
    def speaking(self):
        return self.speaking_text != None # (self.v.isSpeaking() != 0)
    
    def init_text(self):
        self.scale_font()
        self.words_index = 0
        self.text = self.config.text()
        self.variables={}
        self.persistent_text=""
        self.persistent_word = self.font.render("",True,self.config.text_color)

    def display_box(self,message):
        x,y = self.font.size(message)
        x/=2
        y/=2
        margin=1
        pygame.draw.rect(self.screen, (0,0,0),
                         ((self.x_size / 2) - x,
                          (self.y_size / 2) - y,
                          2*x,2*y), 0)
        pygame.draw.rect(self.screen, self.config.color,
                         ((self.x_size / 2) - (x+margin),
                          (self.y_size / 2) - (y+margin),
                          2*(x+margin),2*(y+margin)), 1)
        if len(message) != 0:
            self.screen.blit(self.font.render(message, True,
                                              self.config.text_color),
                             (self.x_size / 2 - x, self.y_size / 2 - y))
        pygame.display.flip()

    def advance_text(self):
	self.words_index = (self.words_index + 1) % len(self.text)

    def varsub(self,word):
        if '$' in word:
            try:
                for var in self.variables:
                    word=word.replace(var,self.variables[var])
            except KeyError:
                print "Bad variable '%s'" % word
        return word

    def act_on(self,command):
        try:
            exec "self.%s" % command[1:]
            self.advance_text()
        except:
             print "Unrecognized command: %s" % command

    def images_on(self): self.draw_image=True
    def images_off(self): self.draw_image=False
    def hold_image_start(self):
                self.advance_text()
                image_name=""
                while ((self.text[self.words_index+1].startswith("!") != True) and (self.words_index+2 < len(self.text))):
                        word = self.text[self.words_index]
                        image_name=image_name+" "+self.varsub(word)
                        self.advance_text()
    
                word = self.text[self.words_index]
                image_name=image_name+self.varsub(word)
		if (self.image_lookup[image_name] >=0):
			self.hold_image_index=self.image_lookup[image_name]
		#print self.hold_image_index,

    def hold_image_end(self): 
		word=""
                self.draw_image=True
    def hold_image_blank(self): 
		self.hold_image_index=-1
                self.draw_image=False
    def hold_text_start(self):
                self.advance_text()
                self.persistent_text=""
                while ((self.text[self.words_index+1].startswith("!") != True) and (self.words_index+2 < len(self.text))):
                        word = self.text[self.words_index]
                        self.persistent_text=self.persistent_text+" "+self.varsub(word)
                        self.advance_text()
    
                word = self.text[self.words_index]
                self.persistent_text=self.persistent_text+" "+self.varsub(word)
                if self.config.broken_fonts:
                    self.persistent_word = self.font.render(self.persistent_text,True,self.config.text_color)
                else:
                    self.persistent_word = textOutline(self.font,
                                    self.persistent_text,
                                    self.config.text_color,
                                    self.config.color)
                    self.persistent_word.set_alpha(self.config.text_alpha)

    def hold_text_end(self): word=""
    def hold_text_blank(self): self.persistent_text=""
    def toggle_images(self): self.draw_image=not self.draw_image
    def words_on(self): self.draw_words=True
    def words_off(self): self.draw_words=False
    def spiral_on(self): self.draw_spiral=True
    def spiral_off(self): self.draw_spiral=False
    def quit(self): self.running=False
    def pause_music(self): pygame.mixer.music.pause()
    def unpause_music(self): pygame.mixer.music.unpause()
    def stop_music(self): pygame.mixer.music.stop()
    def shell(self,text): os.system(text)
    def start_music(self,filename):
        self.config.music=filename
        self.init_music()
    def new_text(self,new):
        while type(new)==str:
            new=eval(new)
        self.text = new
        self.words_index=0
    def insert_text(self,t):
        index = self.words_index+1
        self.text[index:index] = t
    def show_spoken_words_off(self):
        self.show_spoken_words = False
    def show_spoken_words_on(self):
        self.show_spoken_words = True
    def prompt(self,text):
        self.display_box(self.varsub(text))
        while True:
            event = pygame.event.wait()
            if event.type==KEYDOWN and event.key==K_RETURN: break
    def yn_question(self,question,yes=None,no=None):
        self.display_box(self.varsub(question) + "(y/n)")
        while True:
            event = pygame.event.wait()
            if event.type==KEYDOWN:
                if event.key==K_y:
                    if yes: self.new_text(yes)
                    break
                elif event.key==K_n:
                    if no: self.new_text(no)
                    break
    def open_question(self,question,var):
        answer=""
        while True:
            self.display_box(self.varsub(question) + ": " + answer)
            event = pygame.event.wait()
            if event.type==KEYDOWN:
                if event.key==K_BACKSPACE:
                    answer = answer[0:-1]
                elif event.key==K_RETURN:
                    break
                else:
                    answer += event.unicode
        self.variables['$'+var]=answer
    def cond_jump(self,test,yes=None,no=None):
        if eval(test) and yes:
            self.new_text(yes)
        elif no:
            self.new_text(no)
    def conditional(self,test,yes=[],no=[]):
        if eval(test):
            self.insert_text(yes)
        else:
            self.insert_text(no)
    def init_spiral(self):
        self.clear_screen()
        self.draw_text("Loading spiral")
        if (self.config.spiral_image != ""):
                tmpspiral=pygame.image.load(self.config.spiral_image).convert()
                scale=1.0
                spiral = pygame.transform.rotozoom(tmpspiral,0,scale)
        elif True:
        	spiral_size = int(1.2* max(self.x_size, self.y_size))
        	spiral = pygame.Surface((spiral_size, spiral_size))
        	dots = []
		offset_x = []
		offset_y = []
        	for t in range(1, spiral_size*self.config.scale):
            		t *= 0.5 / self.config.scale
            		x =  t * t * math.cos(t)
            		y =  t * t * math.sin(t)
            		dots.append((int(x+spiral_size/2.0), int(y+spiral_size/2.0)))
            		self.process_events()
        	pygame.draw.lines(spiral, self.config.color, False, dots, 4)
        	a = pygame.transform.rotate(spiral,90)
        	b = pygame.transform.rotate(spiral,180)
        	c = pygame.transform.rotate(spiral,270)
        	spiral.blit(a,(0,0),None,BLEND_ADD)
        	spiral.blit(b,(0,0),None,BLEND_ADD)
        	spiral.blit(c,(0,0),None,BLEND_ADD)
		spiral.set_colorkey(None)
       	spiral.set_alpha(self.config.alpha)
        self.spirals=[]
        for t in xrange(0,self.config.spiral_range/self.config.spiral_step):
            self.spirals.append(pygame.transform.rotate(spiral,-t*self.config.spiral_step))
        self.clear_screen()
        self.spirals_index=0

    def load_image(self,i):
        self.process_events()
        path = os.path.join(self.config.image_dir,i)
        i = pygame.image.load(path).convert()
        i.set_alpha(self.config.image_alpha)
        return i

    def scale_font(self):
        fontsize = self.x_size/10
        self.font = pygame.font.SysFont(None,fontsize) # use default font

    def scale_images(self):
        x = self.x_size * 4.0 / 5.0
        y = self.y_size * 4.0 / 5.0
        for i in range(0,len(self.images)):
            pic_x,pic_y = self.images[i].get_size()
            x_factor = x / pic_x 
            y_factor = y / pic_y
            scale = min(x_factor, y_factor)
            #scale = min(scale,1.0)
            self.images[i] = pygame.transform.rotozoom(self.images[i],0,scale)

    def scale_unshuffled_images(self):
        x = self.x_size * 4.0 / 5.0
        y = self.y_size * 4.0 / 5.0
        for i in range(0,len(self.unshuffled_images)):
            pic_x,pic_y = self.unshuffled_images[i].get_size()
            x_factor = x / pic_x 
            y_factor = y / pic_y
            scale = min(x_factor, y_factor)
            #scale = min(scale,1.0)
            self.unshuffled_images[i] = pygame.transform.rotozoom(self.unshuffled_images[i],0,scale)

    def rescale(self):
        self.scale_font()
        if self.images_initialized:
            self.scale_images()
    
    def init_images(self):
        self.clear_screen()
        self.draw_text("Loading images")
        image_file_names = os.listdir(self.config.image_dir)
	list_number=0
	self.hold_image_index=-1
	self.image_lookup={'':-1}
        self.images=[]
	self.unshuffled_images=[]
	for i in image_file_names:
		if i.endswith(".jpg"):
			self.image_lookup[i]=list_number
			list_number=list_number+1
			self.images.append(self.load_image(i))
			self.unshuffled_images.append(self.load_image(i))
        #self.images = [self.load_image(i) for i in image_file_names
        #               if i.endswith(".jpg")]
        self.scale_images()
        self.scale_unshuffled_images()
        if self.config.shuffle_images:
            random.shuffle(self.images)
        else:
            self.images.sort(key=lambda img: int(img.get_size()[0] / 10))
            self.images.sort(key=lambda img: int(img.get_size()[1] / 10))
            rev = self.images[:] # copy
            rev.reverse()
            self.images.extend(rev)
        self.clear_screen()
        self.image_index=0
        self.images_initialized = True

    def init_music(self):
        if self.config.music:
            pygame.mixer.music.load(self.config.music)
            pygame.mixer.music.play(-1)
    
    def draw_surface(self,surface,delay=False):
        cx, cy = surface.get_rect().center
        x_off = (self.x_size/2) - cx
        y_off = (self.y_size/2) - cy
        self.screen.blit(surface, (x_off, y_off))
        if not delay: pygame.display.flip()

    def draw_text(self,word,delay=False):
        if word=="":return
        if self.config.broken_fonts:
            temp_word = self.font.render(word,True,self.config.text_color)
        else:
            temp_word = textOutline(self.font,
                                    word,
                                    self.config.text_color,
                                    self.config.color)
        temp_word.set_alpha(self.config.text_alpha)
        self.draw_surface(temp_word,delay)

    def clear_screen(self,delay=False):
        self.screen.fill((0,0,0))
        if not delay: pygame.display.flip()

    def speechSynthesizer_willSpeakWord_ofString_(self, synth, word, text):
        if text==None:
            text = self.speaking_text
        start, end = word.location, (word.location + word.length)
        while text[start] not in string.whitespace and start >= 0: start -=1
        while text[end] not in string.whitespace and end<len(text)-1: end += 1
        self.spoken_word = text[start:end]

    def speechSynthesizer_didFinishSpeaking_(self, synth, success):
        self.should_advance = True
        self.spoken_word = " "
        
    def run_spiral(self):
        self.running = True
        self.should_advance = True
        self.draw_image = False
        self.draw_spiral = False
        self.draw_words = False
        self.show_spoken_words = True
        ticks = dict(self.config.frequencies)
        c = pygame.time.Clock()
        self.start_recording()
        while self.running:
            c.tick(self.config.frame_rate)
            for key in ticks:
                ticks[key] -= self.config.time_scale
                if ticks[key]<0:
                    ticks[key] = self.config.frequencies[key]
                    if key=='images':
                        self.image_index = (self.image_index + 1) % \
                                           len(self.images)
                        if self.config.shuffle_images and 0==self.image_index:
                            random.shuffle(self.images)
                    elif key=='spiral':
			inc = 1 # random.randint(1,3)
                        self.spirals_index = (self.spirals_index + inc) % \
                                             len(self.spirals)
                    elif key=='words' and \
                         self.should_advance:
                        self.advance_text()
            self.clear_screen(True)
            if self.draw_image:
		if (self.hold_image_index >= 0):
			self.draw_surface(self.unshuffled_images[self.hold_image_index],True)
		elif True:
                	self.draw_surface(self.images[self.image_index],True)
            if self.draw_spiral:
                try:
                    self.draw_surface(self.spirals[self.spirals_index],True)
                except IndexError:
                    print "Index %i out of range 0..%i" % (self.spirals_index,
                                                           len(self.spirals))
            word = self.text[self.words_index]
            if word.startswith("!"):
                self.act_on(word)
            elif word.startswith("[[") and word.endswith("]]"):
                pass
            elif self.show_spoken_words and self.speaking():
                self.draw_text(self.spoken_word,True)
            elif self.draw_words: #and ticks['words'] != self.config.frequencies['words']:
                self.draw_text(self.varsub(word),True)
	    if (self.persistent_text != ""):
                        self.draw_surface(self.persistent_word,True)
            pygame.display.flip()
            self.process_events()
            
    def init_(self,config):
        pygame.init()
        self.config = config()
        self.init_screen()
        self.init_text()
        self.init_spiral()
        self.init_images()
        self.init_music()
        self.init_speech()
        self.init_camera()
        return self

startup = """Hypnotic Spiral, Copyright (C) 2006 Yonah Arakoslav
This program comes with ABSOLUTELY NO WARRANTY.  This is free software,
and you are welcome to redistribute it under certain conditions.
Read the top of the spiral.py source file for details"""

usage = """Keys:
 q: quit
 f: toggle fullscreen
 i: toggle images
 ,: slow down (or <)
 .: speed up (or >)"""
        
if __name__=='__main__':
    print startup
    c = pick_config(configs)
    print usage
    s = Spiral.alloc().init_(c)
    s.run_spiral()
