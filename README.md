# Google Forms Bot
### A bot I built for a Google Form survey. Feel free to adapt this to your project or just use it as an example.

#### Requirements:
  - selenium
  - time [default]
  - random [default]
  - Chrome Web Driver (currently set to /Python/Python3X/Scripts/chromedriver[-87].exe, which is default. This can be changed, Google it)
#### Features:
  - Pick a random entry from a list, or if given, data from a dictionary.
  - Log which items were chosen to a log file
  - Print out when one submission is successful
  - Wait random duration between two values (currently set to minutes)
#### Notes:
  - This will require modification to work with your form. It currently works for a form with 30 consecutive short answer submission boxes, as these will be incramentally numbered and we can loop through the same XPATH with one number changed. You would probably want to loop through an array of XPATHs to work with your particular scenario
  - It may work in headless mode without the 0.2 second delay, but my testing shows it needs to remain for whatever reason Google has decided.
  - It would probably be easier to send a bunch of POST requests instead of using Selenium and all that, but this was more fun and I wanted to learn how to use Selenium.
  
Use this project as an example for your own.
  
