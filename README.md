# mergefolders
This utility will merge two folder files into new one that will contains files from both excluded identical

Describing situation:

I have two folders. 
One of them was created first and got lots of files from other hdd.
Second one was created weeks later from same source, but at that moment folder structure was changed and files moved to different subfolders.
Also I sure this folder contains lots of identical files as it was used to backup all files from all sources for years.

So, here we go with:

Folder initialdump has subfolders:
* video
* photo
* audio
* some named folders like Crimea2007 etc.
* some files like DCIM20012.png etc.
 
Folder lastdump has subfolders:
* video
* photo
* audio
* tools
* trash
 
# Steps To Fix
Fix idea. I don't care of new folder structure. I can manually restructure all files. What I am carrying of it is to hold all the files in one place.

1. I will start from creating list of hashes of all the in every folder. 
2. Then will run caomparison program to check difference between folders. 
3. After I have a list of hashes I have to analyze these lists and do the merge.
