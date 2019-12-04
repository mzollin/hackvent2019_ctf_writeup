# Day 03: HV19.03 Hodor, Hodor, Hodor
This one seemed like a really weird code until I saw that the categories were "fun" and "programming", and not "cryptography". So I just searched the web for "Hodor esoteric programming language" or something similar and quickly found [hodor-lang](http://www.hodor-lang.org/).  

![](confused.jpg)  

Ok, so I guess we're doing this. You can easily install it with npm:  

    npm install -g hodor-lang
    
And then run the code with:  

    hodor challenge.hd
    
Which produces the following output:  

    Awesome, you decoded Hodors language! 
    As sis a real h4xx0r he loves base64 as well.
    SFYxOXtoMDFkLXRoMy1kMDByLTQyMDQtbGQ0WX0=

So we got the flag encoded as base64, which we can decode like this:

    echo SFYxOXtoMDFkLXRoMy1kMDByLTQyMDQtbGQ0WX0= | base64 --decode
    
And we get the solution: HV19{h01d-th3-d00r-4204-ld4Y}  

[Next day](../04)
