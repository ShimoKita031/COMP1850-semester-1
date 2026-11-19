# Week 1.6, Session 1: Task 5

# Write a program here that uses the QuakeFeed and QuakeDataset
# classes to download earthquake data from a USGS data feed,
# analyze it and display the results

# See README.md for full details of what is required and what
# program output should look like
from feed import QuakeFeed
from dataset import QuakeDataset

sig_lvl = str(input("PLease enter significance level: "))
period = str(input("Please enter time period: "))

QuakeFeed(sig_lvl, period)
QuakeDataset(QuakeFeed(sig_lvl, period))
quakes = QuakeDataset.read_feed()
print(f"{len(quakes)} quakes, from ")