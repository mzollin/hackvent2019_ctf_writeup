# Day 04: HV19.04 password policy circumvention
To be honest I found this one a bit too straightforward, although it's a cute idea.  

> Santa released a new password policy (more than 40 characters, upper, lower, digit, special).  
> The elves can't remember such long passwords, so they found a way to continue to use their old (bad) password:  
> merry christmas geeks  

We got a zip archive containing a .ahk file. This is the filename extension for [AutoHotkey](https://www.autohotkey.com/) scripts, which define keyboard buttons or keystroke sequences that when pressed trigger other virtual keystrokes in response. So we execute this script (ideally in a safe environment where it couldn't cause any harm if it were malicious) and in a text editor slowly type the old password and let AutoHotkey scramble it up as it replaces your keystrokes with parts of the flag until it's complete.  

![](autohotkey.gif) 

[Next day](../05)
