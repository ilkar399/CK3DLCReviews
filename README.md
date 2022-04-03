---
editor_options: 
  markdown: 
    wrap: 72
---

# About

This project is an analysis of the Steam reviews for the [Crusader Kings
III: Royal Court
DLC](https://store.steampowered.com/app/1158310/Crusader_Kings_III/).
When I was exploring Steam reviews for [Crusader Kings
III](https://store.steampowered.com/app/1158310/Crusader_Kings_III/)
computer game, I've noticed there is a significant difference between
players reviews the Royal Court DLC and the base game.

The purpose is to explore the players' critics and compare the base game
and DLC reviews, making the possible recommendations for improving
player's perceptions.

The project is done using Python for data collection, R for cleaning
data and analysis. Presentation is done in Microsoft PowerPoint and
there is a dashboard created using Tableau Public.

**Last Update:** 03.04.2022

# Project structure

## Folder structure:
```
CK3DLCReviews
    ├── data
    │   ├── *.csv
    │   └── *.json
    ├── data-collection
    │   ├── gamedata_collection.R
    │   ├── review_collection.py
    │   └── review_json_to_dataset.R
    ├── snippets
    │   └── *.R
    ├── Data_Analysis_Log.Rmd
    ├── Data_Cleanup_Log.Rmd
    └── Presentation.pptx
```
### data folder

Contains both downloaded, cleaned-up and prepared for Tableau usage data.
Initially downloaded data is in json format, processed data is in csv tables. 

### data-collection folder

review_collection.py - downloading data from Steam using Steam API and 
steamreviews Python package.

gamedata_collection.R - collecting the overall game data. Not strictly
necessary for analysis, just the game information.

review_json_to_dataset.R - converting json to the R-compatible CSV dataset.
No cleaning/data converting is done here.

### snippets folder

Some R code snippets used in data analysis/chart making.

### Data_Cleanup_Log.Rmd
Data cleanup log in R Markdown notebook.

### Data_Analysis_Log.Rmd
Data analysis log (with the chart creation) in R Markdown notebook.

### Presentation.pptx
Microsoft Office PowerPoint presentation.


# Data Sources

### Steam reviews

Collected using [steamreviews](https://pypi.org/project/steamreviews/)
PyPi package that is using [Steamworks getreviews
API](https://partner.steamgames.com/doc/store/getreviews). Review Data
is collected for two applications, refer to
data-collection/review_collection.py:

-   *AppID 1158310* - Crusader Kings III, collected *15.03.2022*

-   *AppID 1303182* - Crusader Kings III: Royal Court, collected
    *15.03.2022*

After the collection, json data is unwrapped into the R dataset and
saved into a csv table using R tidyverse, tidyjson and jsonlite packages
(refer to data-collection/review_json_to_dataset.R)

### Overall Game data

Collected from Steam API and saved into the data/steam_app_data.csv.
Collected and rearranged using jsonlite and tidyjson packages. Refer to
data-collection/gamedata_collection.R

# Data Analysis and conclusions

-   Data cleanup and initial organizing is done in
    "Data_Cleanup_Log.Rmd" notebook.

-   Data Analysis and creating visualizations using ggplot is done in
    "Data_Analysis_Log.Rmd" notebook.

-   Completed Microsoft PowerPoint presentation is in the
    "Presentation.pptx".

-   [Tableau
    dashboard](https://public.tableau.com/app/profile/%20mike.kazantsev/viz/CrusaderKingsIIIRoyalCourt-SteamReviews/Dashboard)
    is done using Tableau Public. The tables for it are created in
    "Data_Analysis_Log.Rmd" notebook.
