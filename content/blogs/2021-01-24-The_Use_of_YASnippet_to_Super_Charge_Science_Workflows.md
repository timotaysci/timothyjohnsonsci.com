---
author: Timothy Johnson
title: The Use of YASnippet to Super Charge Science Workflows
date: 2021-01-24
featured_image: "/img/rocket.jpg"
---

<a id="org48edde4"></a>


![img](/img/rocket.jpg)

# The Use of YASnippet to Super Charge Science Workflows

[Emacs](https://www.gnu.org/software/emacs/) (specifically the [Spacemacs](https://www.spacemacs.org/) distro) has become my go to tool for almost all my scientific work. Writing and producing documents, organising my day and all data analysis and plotting is now done within emacs. The move away from GUI based applications to a more keyboard orientated workflows has allowed me to create at the speed I think.

One of the key tools for that is YASnippet. Using this allows you to quickly insert blocks of text. Ideal for automating typing. I will demonstrate some usecases below. The point here is not to use what I say verbatim but to understand and apply this to your own workflows.


<a id="org9906369"></a>

# Basic Usage

[YASnippet](https://github.com/joaotavora/yasnippet) can be installed from malpa. `M-x install-package` will get it for you. Then either require the package in your `init.el` or add yas-snippet to the configuration layers in your `.spacemacs` - if you are using spacemacs.

To add a new snippet simply use `M-x yas-new-snippet`. A new buffer will open, just give it a title and paste your snippet below the header. Save the buffer and run `M-x yas-reload-all` to ensure all your snippets are available. Use either `M-x yas-insert-snippet` or `SPC i s` to open the YASnippet selection buffer, then just chose which one you want. It will be automatically imported into you working buffer.  


![img](/img/snippet.png)
{:.image-caption}
*YASnippet insert buffer - this template when called would insert the words `test snippet` into your working buffer*



<a id="orgc60b04c"></a>

# Meeting Notes

A key part of my work is the production and dissemination of meeting notes. Only one thing will  makes you look as professional as well produced meeting notes circulated in a timely fashion and that is finding and referring back to notes made previously.   I have a nice setup now where I use a single .org file to keep all meeting notes.

This .org acts like a central paper notebook but it is completely searchable. Additionally all TODOs can be linked straight into org-agenda. I have found this approach super useful however it was cumbersome to generate the meeting note template each time.

By creating a YASnippet template I can quickly create all the heading I need for my next meeting.

For me the key info is:

1.  Meeting tile
2.  Date (easily filled out with `C-c . RET`)
3.  Attendees
4.  Notes
5.  Actions

The actions are kept as just org mode TODOs or in a table ready to export. This is useful if I need to share the document with other.

<table border="2" cellspacing="0" cellpadding="0" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th  class="org-left">What?</th>
<th  class="org-left">Who?</th>
<th class="org-left">When?</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-right">Example Task</td>
<td class="org-right">TJ</td>
<td class="org-right">ASAP</td>
</tr>


<tr>
<td class="org-left">&#x2026;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>
</table>

If I do need to share these notes with others I copy to a separate file that generates a PDF via LaTeX. This is done using a LaTeX template. More info on this can be found below. 


<a id="org4011d54"></a>

# Python

Org mode is a great coding environment. Code block interspersed with text is a great may to keep track of your data, plotting and calculations.

However it is not ideal to generate the code block. This requires several key presses (`C-c C-, s`) and typing the correct header arguments (`python :results output :session one etc.`)

On top of that you almost all my code needs pandas, matplotlib and the correct colour library imported. Keeping several python code block in YASnippet allows me to quickly produce code without the need to continually type the same stuff. An example is below:

    
	
    
    import pandas as pd
     import matplotlib.pyplot as plt
    
     PersonalColors = { 1:'blue',2:'red',3:'green'}
    
     df = pd.read_csv('test.csv', names = ['x','y'])
    
     plt.plot(df['x'],df['y'], color = PersColors[1])
    
     plt.show()
     #plt.savefig("test.png", dpi = 1200)

Having the above snippet saved allows for very fast plotting. The "PersColors" variable allows you to quickly import a personal (or corporate) colour scheme into you work. `plt.show()` is of most use while coding but `plt.savefig()` is needed once a plot is finalised so I like to have both easily accessible and just comment out which ever I do not need.  


<a id="org23f30bc"></a>

# LaTeX

As stated above, one of the key benefits to this type of work flow is the ability to quickly produce PDFs that can be shared with those working outside emacs and org mode. To generate PDFs from org mode is trivial but there are plenty of configuration needed to generate the right PDF.

This includes things like the inclusion of templates for your institutions, fonts and typefaces that remain consistent over documents.

To do this you can include various header arguments in a YASnippet and load them in at the top of your file. Some samples below:

`#+TITLE: Example Title`

`#+AUTHOR: TJ`

`#+OPTIONS: TOC:nil`

`#+LATEX_CLASS: report`

`#+LATEX_CLASS_OPTIONS: [a4paper]`

`#+LATEX_HEADER: \usepackage{times}`


<a id="org3cda637"></a>

# Final Thoughts

I hope this shows that YASnippet is a useful package and how you can include it in your workflows. Give it a go - see what you can automate in your day. Remember - work smarter not harder. 

