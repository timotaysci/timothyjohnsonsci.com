---
author: Timothy Johnson
title: Start-up Scripts, Screens and Jekyll
date: 2021-12-26
---

<a id="org436e8c4"></a>

## Why bother?

Static websites are great - tools like [Jekyll](https://jekyllrb.com/showcase/) make building, deploying and editing sites a cinch! So easy in fact it is easy to have sites for multiple projects all running off one server. This is great but can cause issues as manually serving each site on server reboots takes time.

Below is an example script that will create a screen, move to the website directory and launch it. 


<a id="orgbe347b7"></a>

## Example

    #!/bin/bash
    #Kill any running screens
    killall screen
    #Start a screen for SiteOne. Build a serve jekyll
    screen -S Site1 -d -m
    screen -S Site1 -X stuff $'cd ~/website/SiteOne/^M' &&
    screen -S Site1 -X stuff $'bundle exec jekyll build^M'&&
    screen -S Site1 -X stuff $'bundle exec jekyll serve^M'&
    #Start a screen for SiteTwo. Build a serve jekyll
    screen -S Site2 -d -m
    screen -S Site2 -X stuff $'cd ~/website/SiteTwo/^M' &&
    screen -S Site2 -X stuff $'bundle exec jekyll build^M'&&
    screen -S Site2 -X stuff $'bundle exec jekyll serve^M'&
    #Give time for sites to launch. Should be done with wait. This is a bodge, bodges are fun and never break. 
    sleep 30
    printf "Done! \n"


<a id="org8d85495"></a>

## Wrap-up and next steps

This is scaleable - just add new screens and update the directories to reflect! If you want a challenge get this running on server start-up! I have done this with `crontab -e` - a good guide [here](https://www.baeldung.com/linux/run-script-on-startup).

