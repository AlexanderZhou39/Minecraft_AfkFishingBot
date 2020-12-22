# AfkFishingBot
A simple Afk fishing bot for minecraft.

Since 1.16, Afk fishing isn't the same as it once was. I didn't like that, so I tried a workaround. 

Should work for Windows and MacOS. 

## Python Libraries
Might need some special steps for each depending on your OS
- pyautogui
- keyboard

## Settings
Currently the key for throwing out the rod is set to "i". Set your minecraft controls accordingly.

Feel free to customize anything yourself in the <i>bot.py</i> file.

## Instructions
Clone the repo. Run <i>bot.py</i> using python. You might need to use sudo and change some permissions.

Once the bot is ready, it'll print "ready" into the console. Switch to minecraft and get your fishing spot setup. 

Once you are set, press ";" key or semicolon and the bot should throw out the line automatically. Once you are done, press and hold "b" key, and it should reel the line back in (or throw it out if it was reeled in). The number of reel-ins due to not detecting the bobber is printed into the console. 

## How it works
The bot works by monitoring the narrow column of pixels at the center of the screen for the red color of the fishing bobber. It'll check around every 0.5 sec (time may be longer depending on your computer specs). Make sure the bobber is beneath the crosshair (a decent distance lower is fine. Just not too above or below the crosshair) and around the same x/horizontal coordinate. If it cannot detect the red bobber, it'll reel in the line before throwing out the fishing rod again. The line will also be reeled in if the bobber is seen above water for 25+ seconds (referencing minecraft's fishing mechanics). 

### The area around the crosshair the bot checks for the bobber—fish accordingly. 
<img src="https://i.imgur.com/H5Cg8LY.png">

## What it doesn't do and warnings
The bot does not check for hunger, health, or durability. Keep that in mind. The bot should work reasonably well at night: the red color on the bobber is checked by a ratio of the rgb values. Though, this also means that any red thing near the crosshair will also count as a "bobber." 

<hr>

I hope you find this well!


