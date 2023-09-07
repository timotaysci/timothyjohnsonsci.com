---
author: Timothy Johnson
title: Finding Tidal API Token on Linux
date: 2021-01-16
---


![img](/img/HiFi.jpg)


<a id="org967c8db"></a>

# Tidal on Linux

Tidal is a great way to access a vast, high quality, music collection. Bit rates are significantly higher than other streaming services. It is because of this that many want to use it as the corner stone of the audiophile set ups.

The problem? There is limited Linux support. No official GUI application exists for Tidal on Linux and the only way to access music is by the web app.

Unofficial solutions do exist. The below is a guide to set up Tidal using a music player called Strawberry. I will outline at the end of this post my issues and areas I intend to work on to improve this but if you are like me and had issues with the documentation on the web, I hope the below helps you.


<a id="org77ea389"></a>

# Install Strawberry

Strawberry is a fork of the popular music player Clementine. It's useful as it does report bit rates during operation. Great for testing and confirming you are getting the best quality possible from your player: 

    sudo add-apt-repository ppa:jonaski/strawberry
    sudo apt update
    sudo apt install strawberry


<a id="org7f91ce5"></a>

# Finding your Tidal API

This part proved difficult for me. I have no access to a Windows machine and so tool like [this](https://github.com/lucaslg26/TidalAPI) do not work. To solve this you can use files found on an android phone.

1.  Turn on developer mode on your phone if not done so already - this differs from android version but it is a well documented process.
2.  Ensure that your phone will allow for file transfer when connected to a PC.
3.  Navigate to the tidal app files on your phone.
    
        
        .../Android/data/com.aspiro.tidal/cache/okhttp

4.  Here you will see a bunch of files. To find out your API token run the following command:

    	grep -r "X-Tidal-Token"

1.  Copy the returned value - this is your Tidal API token.


<a id="orgbb85c7d"></a>

# Getting Strawberry to Talk to Tidal

1.  Open Strawberry and navigate to tools -> settings.

2.  Navigate to Tidal in the "Streaming" section, left side ribbon.

3.  Ensure "OAuth" is ticked.

4.  Enter your API token collected in the previous section and paste into Client ID.

5.  Click "Login". A browser will open, follow the prompts to log into Tidal.

6.  A green tick should now appear below the "Login" button.

7.  Ensure "Enable" is also ticked - this allows Tidal to appear in the left side ribbon on the main music player.


<a id="org4c0ffff"></a>

# Wrapping up

That's it. You should now access to Tidal in Strawberry. I've tested the bit rates of songs streamed and FLAC songs in my collection and they are very close - so a success. This seems like a reasonable way to use tidal on your Linux machine without using the web app.


<a id="orgbd72cb8"></a>

# Extra - musings and next steps

Most of my critical listening is done at my PC. This works well but I would much rather have several listening "stations" so that I can be unbound from the desk. I have been exploring options for this and clearly I can spend much money and buy commercial solutions. Not really in the spirit. One option I'm keen to explore is the use of a raspberry Pi or similar with an external amp/DAC. Several good Pi hats [exist](https://www.hifiberry.com/) for [this](https://shop.pimoroni.com/collections/pirate-audio) solution or an inexpensive amp/DAC would also be an option.

Additionally I don't really like using GUI apps where possible - further work on my part is needed to see if I can control my Tidal music via a terminal app or from within emacs. If you have any experience in either of the areas, do reach out. 

