from selenium import webdriver
from time import time, sleep
import random
a = time()

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("service_log_path=NUL")
option.add_argument("--headless")  # faster, optional
option.add_argument("disable-gpu") # faster, optional
browser = webdriver.Chrome(options=option)

data = [
    ['','','',''], 
    ['','','',''], 
    ['','','',''], 
   # ...
]

random_entries = [
    '',
    '',
    '',
    # ...
]

f = open("submissions.log", "a")
v = 450 # How many submissions

for i in range(0,v): 
    x = time() # begin time
    browser.get("<FORM URL>") #  Live URL
    #browser.get('<TEST URL>') # Testing form, has same field types in same order
    sleep(0.2) # Too fast in headless mode, have to give the elements a chance to appear.
    f.write('[')

    for j in range(0,30):
        if data[j][0] == '': # if data table for this question is blank
            k = random.choice(random_entries)
            browser.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[%d]/div/div/div[2]/div/div[1]/div/div[1]/input' % (j+1)).send_keys(k)
            f.write('   "%s", \n' % (k))
        else:
            # 0.1 percent chance it will be a random entry rather than the original data object to add a little bit of variance.
            k = random.choice(data[j])
            if random.random() < 0.1:               # optional
                k = random.choice(random_entries)   # optional
            browser.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[%d]/div/div/div[2]/div/div[1]/div/div[1]/input' % (j+1)).send_keys(k)
            f.write('   "%s", \n' % (k))

    f.write('], \n')
    browser.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div').click()
    print("\rCompleted %d, took %s seconds; total time elapsed is %s minutes." % (i+1, round(time()-x, 2), str((time()-a)/60)))

    delay = random.randrange(1,6)
    print("[" + str(int(time())) + "] Waiting %s minutes to continue" % str(delay))
    sleep(delay*60)

print("Took %s minutes to complete %d submissions" % (str(time()-x), v))
