
from manimlib.imports import *
import random
import math


def fade_none(self):
    self.fade_all(1)


def fade_all(self, amount=0.5):
    for other_part in self.submobjects:
        other_part.set_fill(opacity=amount)


setattr(BulletedList, 'fade_none', fade_none)
setattr(BulletedList, 'fade_all', fade_all)


class TitleScene(Scene):
    def construct(self):
        title = TextMobject("The Mess Detector", height=0.5)
        subtitle = TextMobject("Animation by Earthcomputer", height=0.25)
        subtitle.next_to(title, DOWN)
        circle = Circle(color=YELLOW)
        circle.surround(title)
        tnt = Rectangle(width=0.1, height=0.1, color=RED, fill_color=RED, fill_opacity=1.0)

        # No talking during this section

        self.play(Write(title, run_time=2.0))
        self.wait(1.5)
        self.play(ShowCreation(circle))
        self.play(Write(subtitle))
        for i in range(7):
            tnt.move_to(circle)
            self.add(tnt)
            angle = random.random() * 2 * math.pi
            self.play(ApplyMethod(tnt.shift, (np.cos(angle) * RIGHT + np.sin(angle) * UP) * (circle.get_width() / 2)))
            self.remove(tnt)
            self.wait(0.1)


class WhyScene(Scene):
    def construct(self):
        rngs = ['World RNG', 'Player RNG', 'Entity RNG', 'Math.random()']
        rng_list = BulletedList(*rngs)
        self.add(rng_list)
        # There are many different random number generators which the game uses, including
        self.wait(5)
        self.play(ApplyMethod(rng_list.fade_all_but, 0, 0.2))
        # World RNG for natural "world" processes
        self.wait(2)
        self.play(ApplyMethod(rng_list.fade_all_but, 1, 0.2))
        # Player RNG for stuff related to players
        self.wait(2)
        self.play(ApplyMethod(rng_list.fade_all_but, 2, 0.2))
        # Entity RNG for deciding what entities and mobs are going to do next
        self.wait(2)
        self.play(ApplyMethod(rng_list.fade_none))
        # But
        self.wait(2)
        self.play(ApplyMethod(rng_list.fade_all_but, 3, 0.2))
        self.wait(5)


class UsedForScene(Scene):
    def construct(self):
        calls = ['Particles from Eating', 'Velocity of Item Entity', 'Velocity of XP Orb', 'TNT Angle',
                 'Pack Size of a Mob Spawn']
        other_calls = ['Creation of Most Entities', 'Knockback from Attacks', 'Particles from Breaking an Item',
                       'Liquid Mixing e.g. Cobble Gen', 'Trying to Place Water in the Nether',
                       'Taking Item out of Furnace']

        call_list = BulletedList(*calls)
        call_list.align_on_border(LEFT)
        other_call_list = BulletedList(*other_calls, height=1)
        other_call_list.next_to(call_list, RIGHT)
        group = Group(call_list, other_call_list)
        self.play(ShowCreation(group))
        self.remove(group)
        self.add(call_list, other_call_list)
        self.wait()
        self.play(ApplyMethod(other_call_list.fade_all, 0.2))
        self.wait()
        self.play(AnimationGroup(ApplyMethod(call_list.fade_all, 0.2),
                                 ApplyMethod(other_call_list.fade_none)))
        self.wait()
        self.play(ApplyMethod(call_list.fade_none))
        self.wait()
        self.play(ApplyMethod(other_call_list.fade_all, 0.2))
        self.wait(4)


class LcgScene(Scene):
    def construct(self):
        steps = [
            'Start with a number from 0-99',
            'Multiply by 21',
            'Add 9',
            'Take the last 2 digits',
            'Repeat with this number'
        ]
        step_list = BulletedList(*steps)

        self.play(ShowCreation(step_list))
        # This is how our random number generator is going to work
        self.wait(3)
        seed = 47
        for i in range(5):
            self.play(step_list.fade_all_but, 0, 0.2)
            # We start with a number from 0-99, called the seed. Let's use 47 as an example.
            if i == 0:
                self.wait(3)
            seed_obj_0 = TexMobject('%02d' % seed)
            seed_obj_0.next_to(step_list, RIGHT)
            seed_obj_0.set_y(step_list.get_y(UP), UP)
            seed_obj_0.shift(RIGHT * 0.5)
            if i == 0:
                self.play(Write(seed_obj_0))
                self.wait()
            else:
                # noinspection PyUnboundLocalVariable
                self.play(Transform(seed_obj_3, seed_obj_0, remover=True))
                self.add(seed_obj_0)
            self.play(step_list.fade_all_but, 1, 0.2)
            # The next step is to multiply it by 21
            if i == 0:
                self.wait(4)
            seed *= 21
            seed_obj_1 = TexMobject('%02d' % seed)
            seed_obj_1.next_to(seed_obj_0, DOWN)
            seed_obj_1.shift(DOWN * 0.3)
            seed_obj_1.set_x(seed_obj_0.get_x(LEFT), LEFT)
            self.play(Transform(seed_obj_0, seed_obj_1, remover=True))
            self.add(seed_obj_1)
            if i == 0:
                self.wait()
            self.play(step_list.fade_all_but, 2, 0.2)
            # Then you add 9
            if i == 0:
                self.wait(4)
            seed += 9
            seed_obj_2 = TexMobject('%02d' % seed)
            seed_obj_2.next_to(seed_obj_1, DOWN)
            seed_obj_2.shift(DOWN * 0.3)
            seed_obj_2.set_x(seed_obj_1.get_x(LEFT), LEFT)
            self.play(Transform(seed_obj_1, seed_obj_2, remover=True))
            self.add(seed_obj_2)
            if i == 0:
                self.wait()
            self.play(step_list.fade_all_but, 3, 0.2)
            # Then just take the last 2 digits of what you have
            if i == 0:
                self.wait(4)
            seed %= 100
            seed_obj_3 = TexMobject('%02d' % seed)
            seed_obj_3.next_to(seed_obj_2, DOWN)
            seed_obj_3.shift(DOWN * 0.3)
            seed_obj_3.set_x(seed_obj_2.get_x(LEFT), LEFT)
            self.play(Transform(seed_obj_2, seed_obj_3, remover=True))
            self.add(seed_obj_3)
            if i == 0:
                self.wait()
                self.play(step_list.fade_all_but, 4, 0.2)
                # This is your next random number. Then just repeat this over and over to get a sequence of pseudorandom
                # numbers
                self.wait(4)

