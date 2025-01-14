# password-cracker

This repository is based on an [MCoding YouTube video](https://www.youtube.com/watch?v=XThL0LP3RjY) which looks at a very simple password cracker based on response times.

It is worth noting that the majority of password applications have developed considerably since this was a viable method of breaking a digital password, and as such this approach would be unlikely to get any results in the modern day.

I decided to code my own, albeit it incredibly similar version, for fun and to learn more about very simple cyber-security measures.

## Usage

Enter a chosen password into the PASSWORD variable in secret.py. The allowed characters are: 0-9, a-z, and the following characters: .,-_()*@£$?! . These can be changed in utils.py.

Run main.py to see how the password cracker (cracker.py) is able to determine the string by using the response times from the password application (password.py).


