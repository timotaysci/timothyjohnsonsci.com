---
author: Timothy Johnson
title: Learning by doing - emacs and fastref
date: 2021-08-04
---




<a id="org5cd02aa"></a>

![img](/img/code.jpg)



## Background

It has become clear over the last year of constant emacs use for almost all my work - that this workflow is key to my long term sustainable productivity. Emacs allows for complex tasks to be completed effortlessly with planning, content production and publishing handled without any issues. Importantly customizability is key and baked in.

It has also became clear that learning the language of emacs - elisp - is going to be a super useful tool that will allow me the flexibility to continue using this tool indefinably with the agility that I need. I want to be able to bend it to any task I might come across.

To this end I intend to create a few minor modes that solve problems I have and, in so doing, hopefully learn how this Goliath ticks.


<a id="org8c1ad65"></a>

## fastref

The idea behind fastref is the production and insertion of references that appear quickly during talks. This personal project aimed to solve this rather nasty problem of people showing references within live presentations but not giving you enough time to write it down. Sure I could have created an `org-capture` template for this but I wanted to learn how to write my own modes, so here we are. The below is an explanation of that code. This is for my own reference but also for anyone else dipping their toes into elisp - we can all learn form each other!

Please note. This is, almost certainly, not the best way to implement this. I am open to constructive feedback here so do reach out if you have comments.


<a id="org10bc552"></a>

### Getting the "pieces"

My aim is to capture references. However this is not as trivial as this task appears to be. References consist of several "parts" that can be joined together in several ways. These create a style and that style differs in each field and for each user.  For that reason I wanted to abstract this problem so the below code gets from the user information of the author, journal, year, volume and page(s). These "pieces" can then be stitched together in a style the user needs. 

    
    
    (defun fast-ref-first-author()
      "Gets first author for fast-ref"
      (setq fast-ref-first (read-string "First Author: ")))
    
    (defun fast-ref-journal()
      "Gets journal for fast-ref"
      (setq fast-ref-jour (read-string "Journal: ")))
    
    (defun fast-ref-year()
      "Gets year for fast-ref"
      (setq fast-ref-yr (read-string "Year: ")))
    
    (defun fast-ref-volume()
      "Gets volume for fast-ref"
      (setq fast-ref-vol (read-string "Volume: ")))
    
    (defun fast-ref-pages()
      "Gets page(s) for fast-ref"
      (setq fast-ref-pg (read-string "Page(s): ")))

The `read-string` function initiates a text input in the minibuffer and stores it as `fast-ref-x`. 


<a id="org5c8e913"></a>

### What's the style?

We now have the pieces but we have to construct them as a final reference. So how do we approach this problem? I define a variable `fast-ref-style-final` which concatenates the various pieces from the above section with punctuation, /et al./s and spaces. I have defined `plain`, `rsc` and `acs` using this approach. For now a user would need to define their style here and use that for their final style. This is not how the final solution will look - more on that later.  

    (defun fast-ref-style-final()
      (cond
       ((string= fast-ref-cite-style "rsc") (concat fast-ref-first ", /et al./, /" fast-ref-jour "/, " fast-ref-yr ", *" fast-ref-vol "*, " fast-ref-pg "."))
       ((string= fast-ref-cite-style "acs") (concat fast-ref-first ", /et al./, /" fast-ref-jour "/, *" fast-ref-yr "*, /" fast-ref-vol "/, " fast-ref-pg "."))
       ((string= fast-ref-cite-style "plain") (concat fast-ref-first ", et al., " fast-ref-jour ", " fast-ref-yr ", " fast-ref-vol ", " fast-ref-pg "."))
       )
      ) 


<a id="orgc6ec228"></a>

### Defining behaviour

We also declare two variables here that dictate the behaviour of the mode. `fast-ref-site-style` sets the style of the reference - as discussed above. Here the default is `asc`. You can either set this with `M-x - customize-variable` or by setting it in your `init.el` file. `fast-ref-auto-insert` defines whether you want to have the citation auto inserted or held the kill ring. This gives the user some choice however I want to make this a per citation option (or at least an option to have it as per citation).   

    
    (defvar fast-ref-cite-style "acs" "Set the desired ref style for fast-ref")
    
    (defvar fast-ref-auto-insert t "Toggle auto put into point. nil will add to kill ring")


<a id="orgb4f0de3"></a>

### Bringing it all together

Finally we define `fast-ref`. This is an interactive (ie can be activated with `M-x`) and call the various "piece" functions. Finally it checks if you wanted auto insert then either pastes into buffer or saves to kill ring. 

    
    
    (defun fast-ref()
      "Start fast-ref - requests various inputs - copies to clip board"
      (interactive)
      (fast-ref-first-author)
      (fast-ref-journal)
      (fast-ref-year)
      (fast-ref-volume)
      (fast-ref-pages)
      ;;(insert (fast-ref-style-final)))
      (if fast-ref-auto-insert
          (insert (fast-ref-style-final))
        (kill-new (fast-ref-style-final))))
    
    (provide 'fast-ref)


<a id="org70b8e7b"></a>

## Final thoughts and next steps

In around 45 lines of code I have created (i think) a super neat and useful package for my work. It isn't the cleanest and I'm sure there are better ways to approach this problem but the learning was invaluable. It is not however done. The below is a todo list which I will cross out as they have been completed.

-   Let the user define the style they want in their init.el.
-   Convert the "pieces" into an ordered list that can be called in the style section. I think this will be a more elegant solution but needs work!
-   Get onto MELPA
-   Allow user to choose if they want to choose the insertion method at a per citation level.

You can find the repo [here](https://github.com/timotaysci/fast-ref) and the raw .org mode file [here](https://github.com/timotaysci/fast-ref/blob/main/blogpost.org). 

