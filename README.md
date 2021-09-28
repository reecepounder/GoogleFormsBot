# Google Forms Bot
### Selenium bot to automatically complete Google Forms - great for rigging surveys, or just for messing with friends.

#### Requirements:
  - selenium
  - time [default]
  - random [default]
  - Chrome Web Driver (currently set to /Python/Python3X/Scripts/chromedriver[-87].exe, which is default. This can be changed, Google it)
#### Features:
  - Pick a random entry from a list, or if given, data from a dictionary.
  - Log which items were chosen to a log file
  - Print out when one submission is successful
  - Wait random duration between two submissions (currently set to minutes) to reduce chance of detection
#### Notes:
  - This will require modification to work with your form. It currently works for a form with 30 consecutive short answer submission boxes, as these will be incramentally numbered and we can loop through the same XPATH with one number changed. You would probably want to loop through an array of XPATHs to work with your particular scenario
  - It may work in headless mode without the 0.2 second delay, but my testing shows it needs to remain due to animations (thanks, Google).
  - It would probably be a lot easier to send a bunch of POST requests instead of using Selenium and all that, but this was more fun and I wanted to learn how to use Selenium. Plus, this allows for easier customization by newcomers.
  
Use this project as an example for your own.
  
