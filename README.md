# TotalWarWarhammer
Extracting information from the stats in Total War: Warhammer

If you're familiar with generic Python download the unitsDict.p file and open it with pickle.load( open( "unitsDict.p", "rb" ) ). Inside is a dictionary where each key is for a stat like name, damage, ground_speed, and so on. It isn't the easiest to work with but it should work with any Python distribution.

If you know the pandas module then download and unpickle the unitsDF.p file instead, that has a dataframe with the same information.

To see how the unitsDict and unitsDF files were created take a look at the MergeStats file. Hopefully the comments there are useful. 

All of the other files contain analysis of the dataset.
