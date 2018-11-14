# Find-a-Fic
*The Search for a Housemate's FanFiction.net username*

## Background

A housemate of mine mentioned that they had written a couple of Harry Potter stories on [FanFiction.net](https://www.fanfiction.net/), but didn't want to say what their username was, or the titles of the stories. They did however reveal some details during conversation, apparently unaware of the effectiveness of web-scraping. Below is the key information that narrowed the search down from 797k Harry Potter stories to just 18 authors.

- They author only has 2 stories published.
- Both stories were about the Harry Potter series.
- Both stories were published in 2012.
- One story featured Ginny Weasley as the main character.
- One story featured Hermione Granger as the main character.

I had a little more information, such as the approximate number of reviews that one story had, but for my housemate's sake I will not detail how those 18 authors were narrowed down to 1.

## 44.9k stories
First we have to decide whether to trawl through stories with Hermione or stories with Ginny. Going to fanfiction.net, we can browse the stories. Selecting stories written in English, then a character, we find that there are 141k stories featuring Hermione, and only 44.9k with Ginny. We'll focus on Ginny.

## 6.5k stories
Sorting by date published and clicking through pages of results, we find a bracket of pages to search. Stories published in 2012 are entirely contained between pages 370 and 500 of the search results. With 50 results per page and 130 pages to search, we're now down to 6.5k stories.

## 244 authors
For each of the 6.5k stories written in 2012 which include Ginny, we can go to the user page for the author of each story and check to see if the author has exactly 2 stories published. Creating a [list of each valid author](valid_authors.json), we find we have 244 candidates.

## 18 authors
Now that we have a list of authors who wrote a Ginny story in 2012 and have only 2 stories published, we just need to find the subset whose other story includes Hermione. Returning to each of these authors pages, we check the description of each story to see if they contain "Ginny W." or "Hermione G.", and if Story A has Ginny and Story B has Hermione (or vice-versa), we consider the author to viably be our target. Storing each viable author in [another list](viable_authors.json), we find we now have just 18 authors left.
