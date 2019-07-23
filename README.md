# etrian_qr_code
A program that can dump the data from a QR code saved in the videogame Etrian Odyssey V or Nexus
## What it does now
Essentially nothing - you can provide it with a QR code saved on EOV/Nexus and it will allow you to dump the data on there.
You can run it by calling `python3 qr_decode.py <name of image> <output file name>`, and it will dump the binary data to a file.

## Getting the QR codes from the game.
This program needs the 'screenshot' image of the QR code (obtained by going to the Inn -> Data Settings -> Manage Guild Cards -> <Your Guild Card> -> Press A to edit -> QR Code Output). This will save the image to your SD card and you can grab it from there.
## Solved problems
 * EOV/Nexus QR codes are not properly formed - a few lines are one pixel wide or tall instead of the expected two pixels, rendering them unreadable by the python libraries. I just do some preprocessing (in fix_lines.py) to crop out the QR code and fix those lines.

## Unsolved problems
Originally, I wanted to be able to modify the data and create new QR codes with the modified data. I ran into a number of issues in this process:
 * The QR encoding library can't encode it to the needed QR code version 17 - it uses a version with a larger number of modules. I suspect that the EO games use some atypical chunking methods to shrink the size down quite a bit.
 * The data from the QR isn't easy to understand - it doesn't appear to be encrypted or anything fancy like that, but the only thing I could find by looking at the data was the level of the characters. Things that I thought would be straightforward (like the name) were not easily visible.
