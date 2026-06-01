# ==================================================
# WEB SCRAPING WITH BEAUTIFULSOUP — LOCAL HTML FILE
# ==================================================

# Web scraping means extracting data from web pages or HTML documents.
# In this beginner example, we are not scraping a live website yet.
# We are reading a local HTML file called simple.html.
#
# This is good for learning because:
# - no internet is needed
# - the HTML structure is simple
# - we can practice finding tags, classes, text, and links


# ==================================================
# IMPORT BEAUTIFULSOUP
# ==================================================

# BeautifulSoup is used to parse HTML.
# It turns raw HTML into a searchable Python object.

from bs4 import BeautifulSoup


# ==================================================
# OPEN LOCAL HTML FILE
# ==================================================

# open() reads the simple.html file from the same folder as this Python file.
# encoding='utf-8' is recommended so text characters are read correctly.

with open('simple.html', 'r', encoding='utf-8') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


# ==================================================
# PRINTING SOUP VS PRETTIFY
# ==================================================

# print(soup)
# - prints the parsed HTML normally
# - more compact
# - closer to the original structure
# - useful when you want raw output

print(soup)


# print(soup.prettify())
# - prints formatted HTML
# - adds indentation and line breaks
# - easier for humans to read
# - useful while learning or debugging scraping

print(soup.prettify())


# ==================================================
# ACCESSING BASIC HTML TAGS
# ==================================================

# soup.title gets the full <title> tag.
# Example output:
# <title>Test - A Sample Website</title>

print(soup.title)


# soup.title.text gets only the text inside the title tag.
# Example output:
# Test - A Sample Website

print(soup.title.text)


# soup.p gets the first <p> tag in the document.
# It only returns the first paragraph it finds.

print(soup.p)


# soup.p.text gets only the text inside the first <p> tag.

print(soup.p.text)


# ==================================================
# FINDING ONE ELEMENT
# ==================================================

# soup.find() returns the first matching element.
# Here we find the first div with class="article".

article = soup.find('div', class_='article')

# class_ is used because class is a reserved keyword in Python.
# In HTML we write class="article".
# In BeautifulSoup we write class_='article'.


# The article HTML looks like this:
#
# <div class="article">
#     <h2>
#         <a href="article_1.html">Article 1 Headline</a>
#     </h2>
#     <p>This is a summary of article 1</p>
# </div>


# article.h2 gets the <h2> tag inside the article.
# article.h2.a gets the <a> tag inside the <h2>.
# article.h2.a.text gets the headline text.

heading = article.h2.a.text

print(heading)


# article.p gets the <p> tag inside the article.
# article.p.text gets the summary text.

summary = article.p.text

print(summary)


# article.h2.a['href'] gets the href attribute from the <a> tag.
# Example:
# <a href="article_1.html">Article 1 Headline</a>
#
# Result:
# article_1.html

link = article.h2.a['href']

print(link)



# ==================================================
# FINDING ALL ELEMENTS
# ==================================================

# soup.find_all() returns a list-like collection of all matching elements.
# Here we find all div elements with class="article".

articles = soup.find_all('div', class_='article')


# We loop through each article and extract:
# - heading
# - summary
# - link

for article in articles:
    heading = article.h2.a.text
    summary = article.p.text
    link = article.h2.a['href']

    print(heading)
    print(summary)
    print(link)
    print()


# ==================================================
# SAFER REAL-WORLD VERSION
# ==================================================

# The simple version above works because our HTML is clean.
# But real websites are not always clean.
#
# Sometimes:
# - an article may not have h2
# - an article may not have a link
# - an article may not have a paragraph
#
# If we directly write article.h2.a.text and h2 is missing,
# Python will give an error.
#
# So in real scraping, it is better to check if tags exist first.

print("SAFE VERSION")
print("-" * 40)

for article in soup.find_all('div', class_='article'):
    heading_tag = article.find('h2')
    summary_tag = article.find('p')

    if heading_tag is None or summary_tag is None:
        continue

    link_tag = heading_tag.find('a')

    if link_tag is None:
        continue

    heading = link_tag.text
    summary = summary_tag.text
    link = link_tag['href']

    print(heading)
    print(summary)
    print(link)
    print()


# ==================================================
# IMPORTANT BEAUTIFULSOUP METHODS SUMMARY
# ==================================================

# soup.title
# Gets the first <title> tag.

# soup.title.text
# Gets only the text inside the <title> tag.

# soup.p
# Gets the first <p> tag.

# soup.find('tag')
# Finds the first matching tag.

# soup.find('div', class_='article')
# Finds the first <div class="article">.

# soup.find_all('div', class_='article')
# Finds all <div class="article"> elements.

# tag.text
# Gets the text inside a tag.

# tag['href']
# Gets the href attribute from an <a> tag.

# soup.prettify()
# Formats HTML nicely for reading.


# ==================================================
# FINAL IDEA
# ==================================================

# BeautifulSoup lets us move from this:
#
# raw HTML document
#
# to this:
#
# specific data we need:
# - title
# - headings
# - summaries
# - links
#
# This is the foundation of web scraping.