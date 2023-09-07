---
author: Timothy Johnson
title: Emacs as a server 
date: 2022-09-24

---

<a id="orgdc40ca8"></a>

## Emacs as a Daemon

This guide will get emacs running as a server on Linux systems. This means that each time you load a file emacs is ready and doesn't need to load. On some systems emacs start up times can be several seconds so having emacs there and ready to go can save you some real time and improve your workflows.

I always forget how to do this so this guide is for me more than anyone else!

First, create the following file:

`~/.config/systemd/user/emacs.service`.

Within this file paste the following:

    [Unit]
    Description=Emacs text editor
    Documentation=info:emacs man:emacs(1) https://gnu.org/software/emacs/
    
    [Service]
    Type=forking
    ExecStart=/usr/bin/emacs --daemon
    ExecStop=/usr/bin/emacsclient --eval "(kill-emacs)"
    Environment=SSH_AUTH_SOCK=%t/keyring/ssh
    Restart=on-failure
    
    [Install]
    WantedBy=default.target

Enable this by running:

    systemctl enable --user emacs
    systemctl start --user emacs

This starts the server on boot.

Open `~/.bashrc` and add the following:

    alias emacs="emacsclient --create-frame" 


This means each time you type "emacs" in the terminal, it will open a new instance of the client in a new frame.

Finally run

    xdg-mime default emacsclient.desktop text/plain

This will open all text files within the emacs client.

Give the system a reboot and you are good to go. 

All done! This has emacs running how *I* like it. Feel free to change to suit your workflow. 


<a id="orgc17607c"></a>

## Refrences

<https://www.emacswiki.org/emacs/EmacsAsDaemon>

<https://askubuntu.com/questions/17536/how-do-i-create-a-permanent-bash-alias>

<https://emacs.stackexchange.com/questions/31704/run-emacs-gui-from-emacsclient>

<https://taingram.org/blog/emacs-client.html#fn.1>

<https://askubuntu.com/questions/809546/opening-text-files-with-emacsclient-by-default>

