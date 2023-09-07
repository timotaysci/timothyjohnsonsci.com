---
author: Timothy Johnson
title:  Fixing Sound for Steam Linux
date: 2020-07-20
---



I have had some issues with crackling sound and Steam on my latest build - notably during Fallout 4.

To fix this I came across this post and this [video](https://www.youtube.com/watch?v=UQ-Ml78kiEE) - unfortunately the links in the video are dead. 

I believe it is caused by high rate sample rate audio being play though low rate kit. 

For my future reference and for anyone also stumbling across this - I please see a link to my [git](https://github.com/timotayj/PulseAudioFix) up which has the pulse audio .conf fig file that - at least for now- works for me.

To use - backup your /etc/pulse/daemon.conf file with the below code to save a copy in your home dir:

    sudo cp /etc/pulse/daemon.conf daemon.conf_working

then either clone file from git or change manually with

    sudo gedit /etc/pulse/daemon.conf 

*\*Other text editors are available!*

