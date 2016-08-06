# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tetsuya Yamamoto
#
# Created:     27/07/2016
# Copyright:   (c) Tetsuya Yamamoto 2016
# Licence:     MIT
#-------------------------------------------------------------------------------

import pywinauto

app = pywinauto.application.Application()




### クリックテスト
##comapp = app.connect_(path = "explorer")
##comapp[1].ClickInput(coords=(450, 200))

##for i in comapp.windows_():
##    if "Progman" == i.FriendlyClassName():
##        i.ClickInput(coords=(450, 200))

