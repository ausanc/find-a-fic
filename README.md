# Find-a-Fic
*The Search for a Housemate's FanFiction.net username*

## Algorithm
```
for page in range (370, 500):
  seen_authors = []
  for author on page:
    if author not in seen_authors:
      seen_authors.append(author)
      if author has 2 stories:
        yield author
```

## Valid Authors JSON
The list of authors with 2 stories, one of which is about Ginny and was published around 2012
