**NFL QB Stats Analysis**

**Project Summary**

A comparative analysis of Drake Maye’s passing performance using a small dataset of other quarterbacks as well as the current top 5 quarterbacks in the league. All statistics and comparisons are through the first 13 weeks of the 2025 season. The goal is to evaluate Drake Maye on key metrics and understand how he stacks up against both his peers and the league’s leading passers.

The analysis utilizes meaningful measures of quarterback performance including Completion Percentage, Yards per Attempt (YPA), and Touchdowns. These metrics provide insight into passing accuracy, efficiency, and scoring ability.

We examine both a smaller group of randomly selected quarterbacks plus Josh Allen and an aggregate consensus of the top 5 leaderboard for the quarterback position based on week 13 qb starter data. 

**Key Questions Answered**

**_How accurate is Drake Maye compared to other quarterbacks and the top 5 quarterbacks?_**
Completion percentage is used to measure passing accuracy and reliability. This metric allows for a straightforward comparison of Drake Maye against both peer quarterbacks and the top performers in the league.

**_How efficient is Drake Maye as a passer in terms of yards gained per attempt?_**
Yards per Attempt (YPA) is calculated for each quarterback, providing insight into how productive each throw is. Comparing YPA across quarterbacks highlights whether Drake Maye gains more or fewer yards per passing attempt relative to others.

**_How does Drake Maye perform in terms of scoring, compared to other quarterbacks and the top 5?_**
Touchdowns are analyzed both in total and relative to passing attempts or completions. This measure indicates Drake Maye’s ability to generate points and helps contextualize his effectiveness in scoring situations.

**Folder Structure**
nfl-qb-stats-analysis/
│
├── data/
|   ├── placeholder.txt
│   ├── qb_stats.csv
│   └── qb_stats_top5.csv
├── md_stats_notebook.ipynb
├── analysis.py
├── README.md
├── progress-report.txt
├── final-report.txt
├── requirements.txt
└── rough-draft-report.txt

**Included Files**

**/data/qb_stats.csv:** Contains passing attempts, completions, yards, completion percentage, and touchdowns for Drake Maye and a small group of other quarterbacks (through Week 13 of 2025).

**/data/qb_stats_top5.csv:** Contains the same metrics for Drake Maye and the top 5 quarterbacks in the league through Week 13 of the 2025 season.

**analysis.py:** A Python script that loads the datasets, calculates metrics, and outputs a comparison table ranking Drake Maye against both sets of quarterbacks.

**md_stats_notebook.ipynb:** A collab notebook containing a modular view of code execution that makes up the analysis.py file. this entire presentation can be run via this notebook.

The file **md_stats_notebook.ipynb** should be run in the order of the cells contained within the notebook. Start with cell 1 and work your way down. Alternatively, performing a "Run All" cell execution will also produce the same desired results. The necessary packages and csv files are loaded at the top of the notebook for your convenience. 
