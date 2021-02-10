#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is a port of https://github.com/Seeed-Studio/Grove_LCD_RGB_Backlight
# (c) 2017 Alex Bucknall <alex.bucknall@gmail.com>


import i2c_lcd_backlight
import i2c_lcd_screen

class Display(object):
    backlight = None
    screen = None
    from machine import I2C, Pin
    i2c = I2C(scl=Pin(2), sda=Pin(0), freq=400000)

    def __init__(self, i2c, lcd_addr=0x3e, rgb_addr=0x62):
        self.backlight = i2c_lcd_backlight.Backlight(i2c, rgb_addr)
        self.screen = i2c_lcd_screen.Screen(i2c, lcd_addr)

    def write(self, text):
        self.screen.write(text)

    def cursor(self, state):
        self.screen.cursor(state)

    def blink(self, state):
        self.screen.blink(state)

    def blinkLed(self):
        self.backlight.blinkLed()

    def autoscroll(self, state):
        self.screen.autoscroll(state)

    def display(self, state):
        self.screen.display(state)

    def clear(self):
        self.screen.clear()

    def home(self):
        self.screen.home()

    def color(self, r, g, b):
        self.backlight.set_color(r, g, b)

    def move(self, col, row):
        self.screen.setCursor(col, row)


if __name__ == "__main__":
    from time import sleep_ms, ticks_ms
    from machine import I2C, Pin
    from i2c_lcd import I2cLcd

    i2c = I2C(scl=Pin(2), sda=Pin(0), freq=400000)

    lcd = i2c_lcd.I2cLcd(i2c, 0x27, 2, 16)
    lcd.putstr("Hello ernitron\nIt's working!")
    lcd.clear()
    lcd.putstr("Using dhylands\npython_lcd")

    lcd = I2cLcd(i2c, 0x27, 4, 20)
    lcd.putstr("WeMos D1 Mini with  PCF8574 I2C backpackWorks with HD44780s:08x2 16x1 16x2 20x4")
    lcd.clear()
    lcd.putstr("line 1\nline 2\nline 3\nline 4")

