If you see screenshot of my terminals, you will see that there is a /home/sayukta/Desktop/IITM-Courses/Cloud/Assgn-3 directory, which has the directories 'project1' and 'Datasets'. The latter has all the:
1) ALS.txt and FP_Part1.csv, FP_Part2.csv input files
2) The file which is to input in sbt terminal for FPGrowth for FP_Part1: FP_Part-1_new.csv
3) The data cleaning files generated for FP_Part-2: 'FP_Part-2_new.csv' and 'FP_Part-2_real_new.csv'.
4) The file which is to input in sbt terminal for FPGrowth for FP_Part2: formatted.csv
5) Output files present in the folder: 'Output files'.

The former is the folder where I run my sbt.

Now, replace, /home/sayukta/Desktop/IITM-Courses/Cloud/Assgn-3 with the 'foler_path_in_which_you_put_CS17B104/CS17B104'.

To run ALS, you have to take the file MovieLensALS.scala inside the folder CS17B104, and put it as the solo file inside CS17B104/project1/src/main/scala. Copy any other file therein to some other place. Similar steps to run FPGrowthExample.scala.

"run /home/sayukta/Desktop/IITM-Courses/Cloud/Assgn-3/Datasets/ALS.txt –numIterations 20 –-rank 5 –-lambda 0.1" is my ultimate command to run ALS.

"run /home/sayukta/Desktop/IITM-Courses/Cloud/Assgn-3/Datasets/FP_Part-1_new.csv --numPartition 2 --minSupport 0.1" is my ultimate command to run FP_Part2.

"run /home/sayukta/Desktop/IITM-Courses/Cloud/Assgn-3/Datasets/formatted.csv --numPartition 3 --minSupport 0.06" is my ultimate command to run FP_Part2.

Set up instructions are mentioned in "Report.pdf".
