# Regular Expressions in Python
#
# A regular expression, often called regex, is a pattern used to search,
# match, validate, or extract text.
#
# Python gives us regex through the built-in re module.

import re


####################################################################
# re.search(pattern, string, flags=0)
####################################################################
# re.search() looks through a string and returns a match object if the
# pattern appears anywhere inside the string.
#
# Syntax:
# re.search(pattern, string, flags=0)
#
# pattern:
# The regex rule you are looking for.
#
# string:
# The text you want to search inside.
#
# flags:
# Optional settings that change how the search works.
# Example: re.IGNORECASE makes the search case-insensitive.
#
# If re.search() finds a match, it returns a match object.
# If it does not find a match, it returns None.

text = "Hello, my name is John Doe."
pattern = r"John"

match = re.search(pattern, text)

if match:
    print("Pattern found!")
    print("Matched text:", match.group())
else:
    print("Pattern not found.")


####################################################################
# Common Regex Symbols
####################################################################
# .      matches any one character except a newline
# \d     matches any digit, same as [0-9]
# \w     matches a letter, digit, or underscore
# \s     matches whitespace such as a space, tab, or newline
# +      matches one or more of the previous pattern
# *      matches zero or more of the previous pattern
# ?      matches zero or one of the previous pattern
# []     matches one character from a group, for example [abc]
# [^]    means not these characters, for example [^@]
# ^      matches the start of the string
# $      matches the end of the string
# |      means or
# ()     groups part of a pattern


####################################################################
# Detailed Regex Symbols: . * + ? {m} {m,n}
####################################################################
# These symbols control what can match and how many times it can repeat.

# . means any one character except a newline.
# Pattern: c.t
# This can match cat, cot, cut, c9t, c-t, and so on.
dot_examples = ["cat", "cot", "cut", "c9t", "ct", "coat"]

for word in dot_examples:
    if re.fullmatch(r"c.t", word):
        print(f". matched: {word}")
    else:
        print(f". did not match: {word}")


# * means 0 or more repetitions of the previous pattern.
# Pattern: ab*c
# The b is optional and can repeat many times.
# This matches ac, abc, abbc, abbbc, and so on.
star_examples = ["ac", "abc", "abbc", "abbbc", "abdc"]

for word in star_examples:
    if re.fullmatch(r"ab*c", word):
        print(f"* matched: {word}")
    else:
        print(f"* did not match: {word}")


# + means 1 or more repetitions of the previous pattern.
# Pattern: ab+c
# At least one b is required.
# This matches abc, abbc, abbbc, but not ac.
plus_examples = ["ac", "abc", "abbc", "abbbc"]

for word in plus_examples:
    if re.fullmatch(r"ab+c", word):
        print(f"+ matched: {word}")
    else:
        print(f"+ did not match: {word}")


# ? means 0 or 1 repetition of the previous pattern.
# Pattern: colou?r
# The u is optional.
# This matches color and colour, but not colouur.
question_examples = ["color", "colour", "colouur"]

for word in question_examples:
    if re.fullmatch(r"colou?r", word):
        print(f"? matched: {word}")
    else:
        print(f"? did not match: {word}")


# {m} means exactly m repetitions.
# Pattern: \d{4}
# This matches exactly 4 digits.
exact_examples = ["123", "1234", "12345", "abcd"]

for value in exact_examples:
    if re.fullmatch(r"\d{4}", value):
        print(f"{{m}} matched exactly 4 digits: {value}")
    else:
        print(f"{{m}} did not match exactly 4 digits: {value}")


# {m,n} means from m to n repetitions.
# Pattern: \d{2,4}
# This matches 2, 3, or 4 digits.
range_examples = ["1", "12", "123", "1234", "12345"]

for value in range_examples:
    if re.fullmatch(r"\d{2,4}", value):
        print(f"{{m,n}} matched 2 to 4 digits: {value}")
    else:
        print(f"{{m,n}} did not match 2 to 4 digits: {value}")


####################################################################
# re.findall()
####################################################################
# re.findall() returns all matching pieces as a list.

sentence = "The rain in Spain stays mainly in the plain."
matches = re.findall(r"in", sentence)
print(f"Found {len(matches)} occurrences of 'in'.")


####################################################################
# re.search() vs re.fullmatch()
####################################################################
# re.search() checks whether a pattern appears anywhere in the string.
# re.fullmatch() checks whether the whole string matches the pattern.
#
# For validation, re.fullmatch() is usually better because random extra
# text before or after the valid part should not be accepted.

random_text = "my email is student@example.com thanks"

search_match = re.search(r"\w+@\w+\.\w+", random_text)
full_match = re.fullmatch(r"\w+@\w+\.\w+", random_text)

print("re.search found:", search_match.group() if search_match else None)
print("re.fullmatch found:", full_match.group() if full_match else None)


####################################################################
# re.match(pattern, string, flags=0)
####################################################################
# re.match() checks whether the pattern matches at the beginning of the
# string.
#
# Syntax:
# re.match(pattern, string, flags=0)
#
# pattern:
# The regex rule you want to match.
#
# string:
# The text you want to check.
#
# flags:
# Optional settings, such as re.IGNORECASE.
#
# Return value:
# If the pattern matches at the beginning, re.match() returns a match object.
# If the pattern does not match at the beginning, it returns None.
#
# A match object contains information about the match.
# Common methods:
# match.group()  gives the matched text
# match.start()  gives the start index of the match
# match.end()    gives the end index of the match
# match.span()   gives both start and end as a tuple
#
# Important difference:
# re.search()     looks anywhere in the string.
# re.match()      looks only at the beginning of the string.
# re.fullmatch()  requires the whole string to match.
#
# re.match() is similar to using re.search() with ^ at the start of the
# pattern, because both require the match to start at index 0.
#
# These are similar:
# re.match(r"\d+", text)
# re.search(r"^\d+", text)
#
# But re.fullmatch() is stricter than both. It requires the whole input
# to match from start to end.

match_text = "student@example.com is my email"
email_pattern = r"\w+@\w+\.\w+"

match_result = re.match(email_pattern, match_text)
search_result = re.search(email_pattern, match_text)
fullmatch_result = re.fullmatch(email_pattern, match_text)

print("re.match found:", match_result.group() if match_result else None)
print("re.search found:", search_result.group() if search_result else None)
print("re.fullmatch found:", fullmatch_result.group() if fullmatch_result else None)

# In the example above:
# re.match() finds student@example.com because the email starts at the
# beginning of the string.
#
# re.search() also finds student@example.com because it can search anywhere.
#
# re.fullmatch() returns None because the whole string is not only the
# email. It has extra text: " is my email".
#
# Because match_result is a match object, we can inspect it:

if match_result:
    print("re.match start index:", match_result.start())
    print("re.match end index:", match_result.end())
    print("re.match span:", match_result.span())

match_text_with_prefix = "My email is student@example.com"

match_result = re.match(email_pattern, match_text_with_prefix)
search_result = re.search(email_pattern, match_text_with_prefix)

print("re.match with prefix found:", match_result.group() if match_result else None)
print("re.search with prefix found:", search_result.group() if search_result else None)

# In this second example:
# re.match() returns None because the email is not at the beginning.
# re.search() finds student@example.com because it scans through the string.
#
# Example with flags:
# re.IGNORECASE lets uppercase and lowercase match the same pattern.

case_text = "Python is fun"
case_pattern = r"python"

case_sensitive_match = re.match(case_pattern, case_text)
case_insensitive_match = re.match(case_pattern, case_text, flags=re.IGNORECASE)

print(
    "re.match without IGNORECASE:",
    case_sensitive_match.group() if case_sensitive_match else None,
)
print(
    "re.match with IGNORECASE:",
    case_insensitive_match.group() if case_insensitive_match else None,
)

# Validation warning:
# re.match() can be too loose for validation because it accepts a valid
# pattern at the beginning even when extra invalid text comes after it.
#
# Example:
# "student@example.com extra text"
#
# re.match(email_pattern, text) accepts the email part at the beginning.
# re.fullmatch(email_pattern, text) rejects the input because the whole
# string is not only an email.
#
# For validation, re.fullmatch() is usually the clearest choice because it
# means the entire input must match the pattern.


####################################################################
# Piece-by-Piece .edu Email Validation
####################################################################
# Exact pattern:
# r"^\w+@(\w+\.)?\w+\.edu$"
#
# This pattern validates a simple school email ending in .edu.
# It is useful for learning because it contains many important regex ideas:
# anchors, word characters, groups, optional parts, escaped dots, and endings.
#
# Full meaning:
# Start at the beginning of the input, match one or more word characters,
# then an @ sign, then maybe one subdomain like cs., then a domain name,
# then .edu, and finally stop at the end of the input.
#
# Piece by piece:
#
# r"..."
# This creates a raw string.
# Regex uses many backslashes, such as \w and \.
# A raw string tells Python to treat backslashes more literally, which makes
# regex patterns easier to read and write.
#
# ^
# This is an anchor for the start of the string.
# It forces the match to begin at index 0, the first character of the
# input.
#
# This matters because re.search() scans through the whole string looking
# for a match anywhere. It does not automatically require the whole input
# to be an email.
#
# Without ^, this input can pass with re.search():
# "hello student@school.edu"
#
# The pattern can skip "hello " and match only:
# "student@school.edu"
#
# With ^, the pattern is not allowed to skip "hello ". It must start
# matching at the first character, so the input is rejected.
#
# \w
# This means one word character.
# In beginner terms, \w matches:
# - letters: a-z, A-Z
# - digits: 0-9
# - underscore: _
#
# \w does not match:
# - dot: .
# - hyphen: -
# - space
#
# +
# This means one or more repetitions of the thing before it.
# So \w+ means one or more word characters.
#
# In this pattern, the first \w+ is the username:
# student@school.edu
# ^^^^^^^
#
# Accepted username examples:
# student
# student123
# student_name
#
# Rejected username examples:
# john.doe    because dot is not included in \w
# john-doe    because hyphen is not included in \w
# empty name  because + requires at least one character
#
# @
# This matches the literal @ character.
# Email addresses need exactly one separator between username and domain.
#
# (...)
# Parentheses create a group.
# A group lets us treat multiple regex pieces as one unit.
#
# Inside the group:
# \w+\.
#
# \w+ means one or more word characters.
# \. means a real dot.
#
# Important:
# .  means any one character except a newline.
# \. means an actual dot character.
#
# So \w+\. can match:
# cs.
# math.
# mail.
#
# ?
# This means zero or one repetition of the thing before it.
# Because it comes after the group, the whole group is optional:
# (\w+\.)?
#
# This means the email may have one subdomain, or it may have no subdomain.
#
# Accepted:
# student@school.edu       no optional subdomain
# student@cs.school.edu    optional subdomain is cs.
#
# Rejected by this beginner pattern:
# student@cs.math.school.edu
#
# Why rejected?
# Because (\w+\.)? allows only zero or one subdomain.
# cs.math. has two subdomain parts.
#
# The second \w+
# This is the main domain name before .edu.
#
# In student@cs.school.edu:
# student = username
# cs.     = optional subdomain
# school  = main domain
# .edu    = required ending
#
# \.edu
# This matches a real dot followed by edu.
# It forces the email to use the .edu ending.
#
# Accepted:
# student@school.edu
#
# Rejected:
# student@school.com
# student@school.org
# student@school
#
# $
# This is an anchor for the end of the string.
# It means the match must finish at the last character.
#
# Without $, this could pass with re.search():
# "student@school.edu hello"
#
# With $, random text after the email is rejected.
#
# re.IGNORECASE
# This flag makes uppercase and lowercase count the same.
#
# With re.IGNORECASE, these are both accepted:
# student@school.edu
# STUDENT@SCHOOL.EDU

school_email_pattern = r"^\w+@(\w+\.)?\w+\.edu$"

school_email_tests = [
    "student@school.edu",
    "student@cs.school.edu",
    "STUDENT@SCHOOL.EDU",
    "student@gmail.com",
    "hello student@school.edu",
    "student@school.edu hello",
    "john.doe@school.edu",
    "student@cs.math.school.edu",
]

for email in school_email_tests:
    if re.search(school_email_pattern, email, flags=re.IGNORECASE):
        print(f"Valid .edu email: {email}")
    else:
        print(f"Invalid .edu email: {email}")

# Limits of this beginner pattern:
# john.doe@school.edu is rejected because \w does not include dots.
# student@cs.math.school.edu is rejected because the pattern allows only
# one optional subdomain.
#
# More practical .edu email pattern:
# r"^[A-Za-z0-9._%+-]+@([A-Za-z0-9-]+\.)+edu$"
#
# This allows dots in the username and multiple domain parts.

better_school_email_pattern = r"^[A-Za-z0-9._%+-]+@([A-Za-z0-9-]+\.)+edu$"

for email in school_email_tests:
    if re.fullmatch(better_school_email_pattern, email, flags=re.IGNORECASE):
        print(f"Better .edu pattern accepted: {email}")
    else:
        print(f"Better .edu pattern rejected: {email}")


####################################################################
# Email Validation From Random Input
####################################################################
# Important:
# Email validation can become very complicated in real-world systems.
# For beginner programs, we usually validate a practical/simple email:
#
# username@domain.extension
#
# Examples accepted:
# student@example.com
# john.doe22@gmail.com
# user_name@school.edu
#
# Examples rejected:
# studentexample.com        missing @
# student@                  missing domain
# @example.com              missing username
# student@example           missing extension
# student@example..com      double dot
# hello student@example.com extra random text
#
# Good validation steps:
# 1. Strip whitespace from the beginning and end.
# 2. Use re.fullmatch(), not re.search(), when validating the whole input.
# 3. Use a pattern that describes the full allowed email format.
# 4. Add extra simple checks for things regex alone may not express clearly.


def is_valid_email(email):
    email = email.strip()

    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    if not re.fullmatch(email_pattern, email, flags=re.IGNORECASE):
        return False

    if ".." in email:
        return False

    return True


test_emails = [
    "student@example.com",
    " john.doe22@gmail.com ",
    "studentexample.com",
    "student@",
    "@example.com",
    "student@example",
    "student@example..com",
    "hello student@example.com",
]

for email in test_emails:
    if is_valid_email(email):
        print(f"Valid email: {email.strip()}")
    else:
        print(f"Invalid email: {email.strip()}")


####################################################################
# Validating User Input
####################################################################
# Uncomment these lines if you want to ask the user for random input:
#
# user_email = input("Email: ")
#
# if is_valid_email(user_email):
#     print("Valid email")
# else:
#     print("Invalid email")


####################################################################
# Summary
####################################################################
# Use re.search() when you want to find a pattern anywhere in text.
# Use re.findall() when you want all matching pieces.
# Use re.fullmatch() when you want to validate the whole input.
# Use flags like re.IGNORECASE to change matching behavior.
# For validation, always think about random extra input, not only the
# correct example.


####################################################################
####################################################################
# Detailed Longer Email Regex
####################################################################
####################################################################
# A more detailed email validation pattern can look like this:
#
# r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
#
# This pattern validates a more realistic email format:
#
# local-part@domain
#
# Example:
# student.name+test@sub.school.edu
#
# The pattern has two main parts:
# 1. The local part before @
# 2. The domain part after @
#
#
# Part 1: Start and Local Part
####################################################################
# ^
# Start of the string. The email must begin at the first character.
#
# [a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+
# This matches the local part before @.
#
# [] creates a character set. It means "match one character from this
# allowed group."
#
# Inside the character set:
# a-z       lowercase letters
# A-Z       uppercase letters
# 0-9       digits
# .         dot
# !#$%&'*+  allowed email symbols
# /=?^_`    more allowed email symbols
# {|}~-     more allowed email symbols
#
# + means one or more of those allowed characters.
#
# So this part accepts local names like:
# student
# john.doe
# user_name
# student+test
# first.last+school
#
# @
# A literal @ symbol. This separates the local part from the domain.
#
#
# Part 2: First Domain Label
####################################################################
# [a-zA-Z0-9]
# The first domain label must start with a letter or digit.
#
# This is important because domain parts should not start with a hyphen.
#
# Accepted:
# school.edu
# sub.school.edu
#
# Rejected:
# -school.edu
#
# (?: ... )
# This is a non-capturing group.
#
# A normal group uses:
# (...)
#
# A non-capturing group uses:
# (?:...)
#
# Both group pieces of regex together. The difference is that a
# non-capturing group does not store the matched text for later. Use it
# when you need grouping only for structure.
#
# [a-zA-Z0-9-]{0,61}
# This matches 0 to 61 letters, digits, or hyphens.
#
# {0,61} means from 0 up to 61 repetitions.
#
# [a-zA-Z0-9]
# The domain label must end with a letter or digit.
#
# This prevents the label from ending with a hyphen.
#
# The whole optional group:
# (?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?
#
# ? means the group is optional.
#
# Why optional?
# Because a domain label can be short.
#
# Example:
# a.com
#
# The domain label "a" has only one character, so it matches the first
# [a-zA-Z0-9] and does not need the optional rest.
#
# Together, this domain-label logic means:
# - starts with a letter or digit
# - may contain letters, digits, or hyphens in the middle
# - ends with a letter or digit
# - allows labels from 1 to 63 characters
#
#
# Part 3: More Domain Labels
####################################################################
# (?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*
#
# This part allows more domain labels after dots.
#
# \.
# A real dot.
#
# [a-zA-Z0-9]
# The next domain label starts with a letter or digit.
#
# (?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?
# Optional rest of that domain label.
#
# *
# Zero or more repetitions.
#
# This allows:
# example.com
# school.edu
# sub.school.edu
# mail.cs.school.edu
#
# $
# End of the string. Nothing is allowed after the email.
#
#
# Testing the Longer Pattern
####################################################################

long_email_pattern = (
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@"
    r"[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
    r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
)

long_email_tests = [
    "student@example.com",
    "john.doe+test@sub.school.edu",
    "user_name@school.edu",
    "student@a.com",
    "student@school",
    "student@-school.edu",
    "student@school-.edu",
    "student@@school.edu",
    "hello student@school.edu",
    "student@school.edu hello",
]

for email in long_email_tests:
    if re.fullmatch(long_email_pattern, email):
        print(f"Long pattern accepted: {email}")
    else:
        print(f"Long pattern rejected: {email}")


####################################################################
# Final Note About Email Validation
####################################################################
# Regex can check whether an email looks correctly shaped.
# Regex cannot prove that the email account really exists.
#
# In real applications, the best validation is:
# 1. Check the basic format with a reasonable pattern.
# 2. Send a verification email.
# 3. Let the user confirm by clicking a link or entering a code.


####################################################################
# Name Formatting From Different User Inputs
####################################################################
# Sometimes users type names in different formats.
#
# Examples:
# David Malan
# Malan, David
#   Malan,   David
# David   Malan
# David Malan, Jr
# Malan,David
# Malan, David Jr
# Malan, David, Jr
#
# We can use regex to recognize and clean these formats.


def clean_name_spacing(name):
    # Remove spaces at the beginning and end.
    name = name.strip()

    # Change many spaces into one space.
    name = re.sub(r"\s+", " ", name)

    # Clean spaces around commas.
    # "Malan,David" becomes "Malan, David"
    # "Malan ,   David" becomes "Malan, David"
    name = re.sub(r"\s*,\s*", ", ", name)

    return name


def title_case_name(name):
    # .title() gives a simple readable format:
    # "david malan" becomes "David Malan"
    # "o'brien" becomes "O'Brien"
    # "smith-jones" becomes "Smith-Jones"
    return name.title()


def format_name(name):
    name = clean_name_spacing(name)

    # name_part allows letters plus apostrophes and hyphens.
    #
    # [A-Za-z]+              one or more letters
    # (?:['-][A-Za-z]+)*     optional apostrophe/hyphen pieces
    #
    # Example:
    # Malan
    # O'Brien
    # Smith-Jones
    name_part = r"[A-Za-z]+(?:['-][A-Za-z]+)*"

    # suffix_part allows common suffixes.
    #
    # Jr
    # Jr.
    # Sr
    # Sr.
    # II
    # III
    # IV
    suffix_part = r"(?:Jr\.?|Sr\.?|II|III|IV)"

    # Pattern 1: Last, First
    # Examples:
    # Malan, David
    # Malan,David
    # O'Brien, Conan
    reverse_name_match = re.fullmatch(
        rf"(?P<last>{name_part}), (?P<first>{name_part})",
        name,
        flags=re.IGNORECASE,
    )

    if reverse_name_match:
        first = reverse_name_match.group("first")
        last = reverse_name_match.group("last")
        return title_case_name(f"{first} {last}")

    # Pattern 2: Last, First, Suffix
    # Examples:
    # Malan, David, Jr
    # Malan, David, Jr.
    reverse_name_suffix_match = re.fullmatch(
        rf"(?P<last>{name_part}), (?P<first>{name_part}), (?P<suffix>{suffix_part})",
        name,
        flags=re.IGNORECASE,
    )

    if reverse_name_suffix_match:
        first = reverse_name_suffix_match.group("first")
        last = reverse_name_suffix_match.group("last")
        suffix = reverse_name_suffix_match.group("suffix")
        return title_case_name(f"{first} {last}, {suffix}")

    # Pattern 3: First Last, Suffix
    # Examples:
    # David Malan, Jr
    # David Malan, Jr.
    normal_name_suffix_match = re.fullmatch(
        rf"(?P<first>{name_part}) (?P<last>{name_part}), (?P<suffix>{suffix_part})",
        name,
        flags=re.IGNORECASE,
    )

    if normal_name_suffix_match:
        first = normal_name_suffix_match.group("first")
        last = normal_name_suffix_match.group("last")
        suffix = normal_name_suffix_match.group("suffix")
        return title_case_name(f"{first} {last}, {suffix}")

    # Pattern 4: Last, First Suffix
    # Example:
    # Malan, David Jr
    reverse_name_suffix_no_second_comma_match = re.fullmatch(
        rf"(?P<last>{name_part}), (?P<first>{name_part}) (?P<suffix>{suffix_part})",
        name,
        flags=re.IGNORECASE,
    )

    if reverse_name_suffix_no_second_comma_match:
        first = reverse_name_suffix_no_second_comma_match.group("first")
        last = reverse_name_suffix_no_second_comma_match.group("last")
        suffix = reverse_name_suffix_no_second_comma_match.group("suffix")
        return title_case_name(f"{first} {last}, {suffix}")

    # If the name is already in normal order, clean extra spaces.
    return title_case_name(name)


name_tests = [
    "David Malan",
    "Malan, David",
    "Malan,David",
    "  Malan,   David  ",
    "David   Malan",
    "David Malan, Jr",
    "David Malan, Jr.",
    "Malan, David Jr",
    "Malan, David, Jr",
    "Malan, David, Jr.",
    "o'brien, conan",
    "smith-jones, anna",
    "Ada Lovelace",
]

for name in name_tests:
    print(f"Formatted name: {format_name(name)}")


####################################################################
# Real-Time Name Input
####################################################################
# Uncomment these lines if you want to ask the user for a name:
#
# user_name = input("What's your name? ")
# formatted_name = format_name(user_name)
# print(f"Hello, {formatted_name}")


####################################################################
####################################################################
# The Walrus Operator :=
####################################################################
####################################################################
# The symbol := is called the walrus operator.
#
# Official name:
# Assignment expression
#
# Purpose:
# It lets you assign a value to a variable while also using that value
# inside an expression.
#
# This is especially useful with regex because re.search(), re.match(),
# and re.fullmatch() return either:
# - a match object
# - None
#
# Without :=, we usually write:
#
# match = re.search(r"^(.+), (.+)$", "Malan, David")
#
# if match:
#     last = match.group(1)
#     first = match.group(2)
#     print(f"{first} {last}")
#
# With :=, we can assign match and check it in the same if statement:

walrus_name = "Malan, David"

if match := re.search(r"^(.+), (.+)$", walrus_name):
    last = match.group(1)
    first = match.group(2)
    print(f"Walrus formatted name: {first} {last}")

# This line:
# if match := re.search(...):
#
# means:
# 1. Run re.search(...)
# 2. Store the result in match
# 3. Check whether match is truthy
#
# If re.search() finds something, match is a match object, so the if block
# runs.
#
# If re.search() finds nothing, match is None, so the if block does not run.
#
# Use case:
# Use := when you need the result immediately after checking it.
#
# Good use:
# if match := re.search(pattern, text):
#     print(match.group())
#
# Less useful:
# if number := 10:
#     print(number)
#
# The walrus operator is helpful when it removes repetition and keeps the
# code readable. Do not use it everywhere just to make code shorter.


####################################################################
# Extracting a Username From a Full URL or Plain Username
####################################################################
# Users may type the same account in different ways:
#
# davidjmalan
# @davidjmalan
# My username is davidjmalan
# twitter.com/davidjmalan
# https://twitter.com/davidjmalan
# My username is https://twitter.com/davidjmalan
# https://www.twitter.com/davidjmalan/
# https://x.com/davidjmalan?lang=en
#
# Our goal:
# Always return only the username:
#
# davidjmalan


def extract_social_username(user_input):
    user_input = user_input.strip()

    # We use several patterns in a careful order.
    #
    # Why not one loose pattern?
    # If the URL part is optional and we use re.search(), the regex may
    # accidentally match ordinary words like "My" or "not".
    #
    # Better approach:
    # 1. Look for a Twitter/X URL anywhere in the input.
    # 2. Look for @username anywhere in the input.
    # 3. Look for phrases like "username is davidjmalan".
    # 4. Accept a plain username only if the whole input is just that username.

    username_part = r"[A-Za-z0-9_]{1,15}"

    # Pattern 1: Twitter/X URL anywhere in the input.
    #
    # Examples:
    # https://twitter.com/davidjmalan
    # My username is https://twitter.com/davidjmalan
    # https://x.com/davidjmalan?lang=en
    #
    # This captures only the first path part after twitter.com/ or x.com/.
    url_pattern = (
        rf"(?:https?://)?"
        rf"(?:www\.)?"
        rf"(?:twitter|x)\.com/"
        rf"(?P<username>{username_part})"
        rf"(?:[/?#]\S*)?"
    )

    if match := re.search(url_pattern, user_input, flags=re.IGNORECASE):
        return match.group("username")

    # Pattern 2: @username anywhere in the input.
    #
    # Example:
    # My username is @davidjmalan
    at_username_pattern = rf"@(?P<username>{username_part})\b"

    if match := re.search(at_username_pattern, user_input):
        return match.group("username")

    # Pattern 3: phrases that clearly introduce a username.
    #
    # Examples:
    # username is davidjmalan
    # user name: davidjmalan
    # handle davidjmalan
    phrase_pattern = (
        rf"\b(?:username|user name|handle)\b"
        rf"\s*(?:is|:)?\s*"
        rf"(?P<username>{username_part})\b"
    )

    if match := re.search(phrase_pattern, user_input, flags=re.IGNORECASE):
        return match.group("username")

    # Pattern 4: plain username only.
    #
    # This uses re.fullmatch() so random sentences like "not a username"
    # do not accidentally return the first word.
    plain_username_pattern = rf"@?(?P<username>{username_part})"

    if match := re.fullmatch(plain_username_pattern, user_input):
        return match.group("username")

    return None


username_tests = [
    "davidjmalan",
    "@davidjmalan",
    "My username is davidjmalan",
    "twitter.com/davidjmalan",
    "https://twitter.com/davidjmalan",
    "My username is https://twitter.com/davidjmalan",
    "https://www.twitter.com/davidjmalan/",
    "https://x.com/davidjmalan?lang=en",
    "https://twitter.com/davidjmalan/status/123",
    "https://instagram.com/davidjmalan",
    "not a username",
]

for value in username_tests:
    username = extract_social_username(value)

    if username:
        print(f"Username extracted: {username}")
    else:
        print(f"Invalid username or URL: {value}")


####################################################################
# Why replace() Is Not Enough
####################################################################
# This approach works only for one exact prefix:
#
# url = "https://twitter.com/davidjmalan"
# username = url.replace("https://twitter.com/", "")
#
# Result:
# davidjmalan
#
# But if the input is:
# "My username is https://twitter.com/davidjmalan"
#
# replace() gives:
# "My username is davidjmalan"
#
# That is not only the username.
#
# Regex is better here because it can search the whole sentence and
# extract only the part we care about.

replace_example = "My username is https://twitter.com/davidjmalan"
replace_username = replace_example.replace("https://twitter.com/", "")
regex_username = extract_social_username(replace_example)

print("replace() result:", replace_username)
print("regex result:", regex_username)


####################################################################
# Real-Time Username Input
####################################################################
# Uncomment these lines if you want to ask the user:
#
# url_or_username = input("URL or username: ")
# username = extract_social_username(url_or_username)
#
# if username:
#     print(f"Username: {username}")
# else:
#     print("Invalid username or URL")


####################################################################
# re.sub(pattern, repl, string, count=0, flags=0)
####################################################################
# re.sub() means regex substitution.
# It finds text that matches a pattern and replaces it with something else.
#
# Syntax:
# re.sub(pattern, repl, string, count=0, flags=0)
#
# pattern:
# The regex pattern to find.
#
# repl:
# The replacement text.
#
# string:
# The original text to change.
#
# count:
# How many replacements to make.
# The default is 0, which means replace all matches.
#
# flags:
# Optional settings such as re.IGNORECASE.

messy_sentence = "Python     is      fun"
clean_sentence = re.sub(r"\s+", " ", messy_sentence)

print("Clean sentence:", clean_sentence)

# In this example:
# \s+ means one or more whitespace characters.
# re.sub(r"\s+", " ", messy_sentence) replaces all long spaces with one space.


####################################################################
# re.sub() with count
####################################################################
# count controls how many replacements happen.

text_with_many_spaces = "one   two   three   four"

replace_all_spaces = re.sub(r"\s+", " ", text_with_many_spaces)
replace_one_space = re.sub(r"\s+", " ", text_with_many_spaces, count=1)

print("Replace all spaces:", replace_all_spaces)
print("Replace one space:", replace_one_space)


####################################################################
# re.sub() with flags
####################################################################
# flags can change how matching works.

case_text = "python PYTHON Python"
case_cleaned = re.sub(r"python", "JavaScript", case_text, flags=re.IGNORECASE)

print("Case-insensitive replace:", case_cleaned)


####################################################################
# re.sub() with Groups
####################################################################
# re.sub() can use captured groups in the replacement.
#
# In the replacement string:
# \1 means group 1
# \2 means group 2
# \3 means group 3

phone = "123-456-7890"

formatted_phone = re.sub(
    r"(\d{3})-(\d{3})-(\d{4})",
    r"(\1) \2-\3",
    phone,
)

print("Formatted phone:", formatted_phone)

# Pattern:
# (\d{3}) captures the first 3 digits
# -       matches the hyphen
# (\d{3}) captures the next 3 digits
# -       matches the hyphen
# (\d{4}) captures the last 4 digits
#
# Replacement:
# r"(\1) \2-\3"
#
# \1 is the first group
# \2 is the second group
# \3 is the third group


####################################################################
# re.sub() with Named Groups
####################################################################
# Named groups make replacements easier to read.
#
# (?P<area>\d{3}) names the first group area.
# \g<area> uses that group in the replacement.

phone = "123-456-7890"

formatted_phone_named = re.sub(
    r"(?P<area>\d{3})-(?P<middle>\d{3})-(?P<last>\d{4})",
    r"(\g<area>) \g<middle>-\g<last>",
    phone,
)

print("Formatted phone with names:", formatted_phone_named)


####################################################################
# re.sub() for URL Cleanup
####################################################################
# Sometimes we want to remove the beginning of a URL.
# This is similar to replace(), but more flexible.

twitter_url = "https://www.twitter.com/davidjmalan"

username_from_sub = re.sub(
    r"^https?://(?:www\.)?(?:twitter|x)\.com/",
    "",
    twitter_url,
    flags=re.IGNORECASE,
)

print("Username from re.sub:", username_from_sub)

# This removes:
# http://twitter.com/
# https://twitter.com/
# https://www.twitter.com/
# https://x.com/
#
# But for serious extraction, re.search() with a captured username is often
# better because it can pull the username from inside a longer sentence.


####################################################################
# Exact Twitter re.sub() Example
####################################################################
# Example:
#
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
#
# This removes a Twitter URL prefix and leaves the username.
#
# Piece by piece:
#
# ^
# Start of the string. The prefix must be at the beginning.
#
# (https?://)?
# Optional http:// or https://
#
# http
# Literal text.
#
# s?
# The s is optional.
# So this matches both:
# http://
# https://
#
# ://
# Literal ://
#
# The outer ? after the group means the whole protocol part is optional.
# So this also allows:
# twitter.com/davidjmalan
#
# (www\.)?
# Optional www.
#
# www
# Literal text.
#
# \.
# A real dot. We escape it because . alone means any character in regex.
#
# twitter\.com/
# Literal twitter.com/
#
# Replacement:
# ""
#
# This means replace the matched prefix with nothing.

twitter_sub_tests = [
    "https://twitter.com/davidjmalan",
    "http://twitter.com/davidjmalan",
    "https://www.twitter.com/davidjmalan",
    "twitter.com/davidjmalan",
    "My username is https://twitter.com/davidjmalan",
]

for url in twitter_sub_tests:
    username = re.sub(
        r"^(https?://)?(www\.)?twitter\.com/",
        "",
        url,
        flags=re.IGNORECASE,
    )
    print(f"Twitter re.sub result: {username}")

# Notice:
# This works well when the input starts with the Twitter URL.
#
# But this input:
# "My username is https://twitter.com/davidjmalan"
#
# does not start with the URL, so ^ prevents the replacement.
# That is why the sentence remains unchanged.
#
# If the input might be a whole sentence, use re.search() to extract the
# username instead of using re.sub() to remove a prefix.


####################################################################
# Fixing the Unrelated Domain Problem
####################################################################
# Problem:
# If we only use re.sub(), unrelated domains are not rejected.
#
# Example:
# https://www.google.com/
#
# This line:
# re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
#
# does not find a Twitter prefix, so it returns the original input:
# https://www.google.com/
#
# Then the program may accidentally print:
# Username: https://www.google.com/
#
# That is wrong because google.com is not a Twitter/X profile.
#
# Fix:
# Validate and extract at the same time.
# Use re.fullmatch() when the input must be only a valid Twitter/X profile.


def extract_twitter_username_from_url(url):
    url = url.strip()

    twitter_url_pattern = (
        r"^(?:https?://)?"
        r"(?:www\.)?"
        r"(?:twitter|x)\.com/"
        r"(?P<username>[A-Za-z0-9_]{1,15})"
        r"/?"
        r"(?:\?.*)?"
        r"$"
    )

    if match := re.fullmatch(twitter_url_pattern, url, flags=re.IGNORECASE):
        return match.group("username")

    return None


domain_validation_tests = [
    "https://twitter.com/davidjmalan",
    "https://www.twitter.com/davidjmalan/",
    "https://x.com/davidjmalan",
    "twitter.com/davidjmalan",
    "https://www.google.com/",
    "https://instagram.com/davidjmalan",
    "not a url",
]

for url in domain_validation_tests:
    username = extract_twitter_username_from_url(url)

    if username:
        print(f"Validated Twitter/X username: {username}")
    else:
        print(f"Rejected non-Twitter/X input: {url}")

# Real-time version:
#
# url = input("URL: ").strip()
# username = extract_twitter_username_from_url(url)
#
# if username:
#     print(f"Username: {username}")
# else:
#     print("Invalid Twitter/X URL")


####################################################################
# re.sub() Summary
####################################################################
# Use re.sub() when you want to find a pattern and replace it.
#
# Good use cases:
# - Clean extra spaces
# - Normalize punctuation
# - Format phone numbers
# - Remove URL prefixes
# - Replace words case-insensitively
#
# Use re.search() or re.fullmatch() when you want to extract or validate.


####################################################################
# Non-Capturing Groups Fix Group Numbering
####################################################################
# Problem pattern:
#
# r"^https?://(www\.)?twitter\.com/(.+)$"
#
# This pattern works, but it creates two capturing groups:
#
# Group 1:
# (www\.)?
#
# Group 2:
# (.+)
#
# So the username is group(2), not group(1).

group_number_url = "https://www.twitter.com/davidjmalan"

if match := re.search(
    r"^https?://(www\.)?twitter\.com/(.+)$",
    group_number_url,
    flags=re.IGNORECASE,
):
    print("With capturing www group:")
    print("group 1:", match.group(1))
    print("group 2:", match.group(2))

# But we do not really need to save www.
# We only need to group it so ? can make the whole www. part optional.
#
# Solution:
# Use a non-capturing group:
#
# (?:www\.)?
#
# Meaning:
# (?:...)  group for structure only, do not save it
# www      literal www
# \.       real dot
# ?        the whole group is optional
#
# Fixed pattern:
#
# r"^https?://(?:www\.)?twitter\.com/(.+)$"
#
# Now there is only one capturing group:
#
# Group 1:
# (.+)

if match := re.search(
    r"^https?://(?:www\.)?twitter\.com/(.+)$",
    group_number_url,
    flags=re.IGNORECASE,
):
    print("With non-capturing www group:")
    print("group 1:", match.group(1))

# Better username-specific version:
# Instead of (.+), use a pattern for a real Twitter/X username.
#
# [A-Za-z0-9_]{1,15}
#
# This means:
# - letters are allowed
# - digits are allowed
# - underscore is allowed
# - length must be 1 to 15 characters
#
# Full piece:
# ([A-Za-z0-9_]{1,15})/?
#
# ([A-Za-z0-9_]{1,15})
# This is a capturing group.
# It captures the username so we can use match.group(1).
#
# [A-Za-z0-9_]
# This is a character set. It allows one character from this group:
# A-Z uppercase letters
# a-z lowercase letters
# 0-9 digits
# _ underscore
#
# Why do we add something after []?
# A character set by itself matches only one character.
#
# [A-Za-z0-9_]
# This matches one valid username character.
#
# Examples it can match:
# d
# 7
# _
#
# But a username usually has many characters, such as:
# davidjmalan
#
# So we add a repetition rule after the character set.
#
# [A-Za-z0-9_]+
# The + means one or more valid username characters.
#
# [A-Za-z0-9_]{1,15}
# This means from 1 to 15 valid username characters.
#
# [A-Za-z0-9_]{5,15}
# This means from 5 to 15 valid username characters.
#
# {1,15}
# This repeats the allowed character set from 1 to 15 times.
# Twitter/X usernames are 1 to 15 characters long.
#
# /?
# This allows an optional slash after the username.
#
# So both of these can match:
# https://twitter.com/davidjmalan
# https://twitter.com/davidjmalan/
#
# The slash is accepted, but it is not captured because it is outside the
# parentheses. Only the username is captured.
#
# Thinking about the platform rule:
# X Help currently says usernames can contain only letters, numbers, and
# underscores. It also says usernames cannot be longer than 15 characters
# or shorter than 4 characters.
#
# That means:
# - For extracting usernames from existing profile URLs, {1,15} is useful
#   because it accepts any profile-shaped username up to 15 characters.
# - For validating a new username according to current X registration
#   rules, {5,15} is stricter because "more than 4" means at least 5.
#
# Extraction pattern:
# ([A-Za-z0-9_]{1,15})/?
#
# Registration-style validation pattern:
# ([A-Za-z0-9_]{5,15})/?

strict_username_url_tests = [
    "https://twitter.com/davidjmalan",
    "https://www.twitter.com/davidjmalan/",
    "https://www.google.com/",
    "https://twitter.com/davidjmalan/status/123",
]

for url in strict_username_url_tests:
    if match := re.search(
        r"^https?://(?:www\.)?twitter\.com/([A-Za-z0-9_]{1,15})/?$",
        url,
        flags=re.IGNORECASE,
    ):
        print("Strict non-capturing solution username:", match.group(1))
    else:
        print("Strict non-capturing solution rejected:", url)

# Summary:
# Use (...) when you want to capture and use the matched text later.
# Use (?:...) when you only need grouping for regex logic.
# Non-capturing groups keep group numbers cleaner.


####################################################################
# re.split(pattern, string, maxsplit=0, flags=0)
####################################################################
# re.split() splits a string wherever the regex pattern matches.
#
# Syntax:
# re.split(pattern, string, maxsplit=0, flags=0)
#
# pattern:
# The regex separator.
#
# string:
# The text you want to split.
#
# maxsplit:
# Maximum number of splits.
# Default is 0, which means split everywhere the pattern matches.
#
# flags:
# Optional settings such as re.IGNORECASE.

messy_names = "David,  Emma;John   Sara"

split_names = re.split(r"[,;\s]+", messy_names)

print("Split names:", split_names)

# Pattern:
# [,;\s]+
#
# [] means one character from this set.
# , means comma.
# ; means semicolon.
# \s means whitespace.
# + means one or more.
#
# So this splits on commas, semicolons, spaces, or many spaces.

limited_split = re.split(r"[,;\s]+", messy_names, maxsplit=2)
print("Limited split:", limited_split)

# maxsplit=2 means only make the first two splits.

case_split_text = "appleXbananaxtomatoxgrape"
case_split = re.split(r"x", case_split_text, flags=re.IGNORECASE)
print("Case-insensitive split:", case_split)


####################################################################
# re.findall(pattern, string, flags=0)
####################################################################
# re.findall() returns all non-overlapping matches as a list.
#
# Syntax:
# re.findall(pattern, string, flags=0)
#
# pattern:
# The regex pattern to find.
#
# string:
# The text to search.
#
# flags:
# Optional settings such as re.IGNORECASE.

email_text = "Emails: a@example.com, b@test.org, and c@school.edu"
all_emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email_text)

print("All emails:", all_emails)

# If the pattern has no capturing groups, findall() returns full matches.
#
# Example result:
# ["a@example.com", "b@test.org", "c@school.edu"]

email_parts = re.findall(
    r"([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\.[A-Za-z]{2,})",
    email_text,
)

print("Email parts:", email_parts)

# If the pattern has capturing groups, findall() returns the captured groups.
#
# Example result:
# [("a", "example.com"), ("b", "test.org"), ("c", "school.edu")]
#
# This is useful when you want pieces instead of the whole match.

usernames_text = "Follow @davidjmalan, @python_dev, and @CS50."
all_usernames = re.findall(r"@([A-Za-z0-9_]{1,15})\b", usernames_text)

print("All usernames:", all_usernames)

# The @ is matched, but it is outside the parentheses.
# Only the username is captured and returned.

words_text = "Python python PYTHON"
all_python_words = re.findall(r"python", words_text, flags=re.IGNORECASE)

print("Case-insensitive findall:", all_python_words)


####################################################################
# re.split() and re.findall() Summary
####################################################################
# Use re.split() when separators are flexible or messy.
#
# Example:
# Split on comma, semicolon, or any amount of whitespace.
#
# Use re.findall() when you want every match in the text.
#
# Example:
# Extract every email or every @username from a sentence.

##################################################################
