# about file size limits on github and/or your local laptop. 

This is not an uncommon problem especially if you're doing a data analysis. I'm going to start a thread (to keep the the main channel clear) and provide some alternatives.

## 1 - don't physically store your datasources, period. 
If they are publically available, then download from the source site at run time. Yes, it will take longer to run your project bc of the download time.
Downside -- URLs change; online public data sources get deleted. To mitigate, you should always keep somewhere safe a redundant & compressed backup of your datasources.
Here is an example where I do the above -- github.com/stevewatkins17/PythonForDataAnalysis/blob/mainline/IpythonNotebooks/SQL_demo_20180925.ipynb (edited) 

## 2 -- store your files on non-github cloud storage
See this for guidance -- www.softwaretestinghelp.com/cloud-storage-providers/.  This can also double as your BU since that is a standard feature of cloud storage.
Many such providers provide some free storage to start.

## 3 -- compress the file & only store the compressed copy in your repo. 
An example of this is here -- github.com/stevewatkins17/PythonForDataAnalysis/blob/mainline/IpythonNotebooks/demo_AmexTransactions_FileHandlingExplicit.ipynb
Downsides to using compression -- they sometimes fail to decompress, especially if you decompress/re-compress repeatably or use different OSes.

You might notice that the demo script above actually fails to decompress the pkzip file bc the file is corrupted. I regularly use macos & windows (and sometimes linux centos) and am certain that I moved between OSes while working with the (corrupted) pkzip file in my repo. I leave it there as a corrupted file mainly for instructional purposes. (edited) 
