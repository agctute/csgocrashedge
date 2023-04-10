# csgocrashedge
This is an old project made in 2020 that I decided to upload here. The goal was to scrape the prior "crashes" on the gambling website WTFskins.com and determine 
if there existed a house edge or a pattern among the distribution of crashes. I noticed a pattern before but never really
analyzed it or looked at why the pattern existed. So now, on November 4th, 2022, I finished a casual report on
how the numbers of CSGOCrash results are derived in ```csgocrash_report.ipynb```. 

Note: The file ```visualizations.ipynb``` contains a lot of me playing around with statistical tests as well as refreshing my knowledge. 
There are some cool results there not included in the final report such as Anderson-Darling Tests instead of Cramer-von Mises Tests. 
Those provide much higher test statistics since Anderson-Darling puts more emphasis on the tails of the distribution, and 
the Pareto Distribution has a *very long* tail. Also some MLE, where the data doesn't fit since it performed with the house
edge included, but a section with latex which I'm pretty proud of. 

## Location
```csgocrash_report.ipynb``` for the main report, and ```visualizations.ipynb``` for some other side visuals I made that weren't included. 
