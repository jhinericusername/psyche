import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

test_str = b"Hosted by Sabrina Tavernise\nFeaturing Nate Cohn\nProduced by Rob Szypko,\xc2\xa0Mooj Zadie and Diana Nguyen\nEdited by Rachel Quester\nOriginal music by Diane Wong,\xc2\xa0Marion Lozano and Dan Powell\nEngineered by Alyssa Moxley\nListen and follow The DailyApple Podcasts | Spotify | Amazon Music\nMillions of voters in states across the country cast their ballots in the presidential primary on Super Tuesday, leaving little doubt that the November election will be a rematch between President Biden and former President Donald J. Trump.\n The Daily is made by Rachel Quester, Lynsea Garrison, Clare Toeniskoetter, Paige Cowett, Michael Simon Johnson, Brad Fisher, Chris Wood, Jessica Cheung, Stella Tan, Alexandra Leigh Young, Lisa Chow, Eric Krupke, Marc Georges, Luke Vander Ploeg, M.J. Davis Lin, Dan Powell, Sydney Harper, Mike Benoist, Liz O. Baylen, Asthaa Chaturvedi, Rachelle Bonja, Diana Nguyen, Marion Lozano, Corey Schreppel, Rob Szypko, Elisheba Ittoop, Mooj Zadie, Patricia Willens, Rowan Niemisto, Jody Becker, Rikki Novetsky, John Ketchum, Nina Feldman, Will Reid, Carlos Prieto, Ben Calhoun, Susan Lee, Lexie Diao, Mary Wilson, Alex Stern, Dan Farrell, Sophia Lanman, Shannon Lin, Diane Wong, Devon Taylor, Alyssa Moxley, Summer Thomad, Olivia Natt, Daniel Ramirez and Brendan Klinkenberg.\n But in a race that is increasingly inevitable, a New York Times/Siena College poll found a critical group of voters who are making the outcome of that race anything but certain.\n The Unhappy Voters Who Could Swing the Election\nIn 2020 as in 2016, a potentially decisive slice of the electorate dislikes both main candidates. On today\xe2\x80\x99s episode\nNate Cohn, the chief political analyst for The New York Times.\n"

test_str = str(test_str)[2:-1]
print(test_str + "\n\n")

# test2 = str(b"hello\xc2asdf\xa0xxdxd")
# print(test2)
# print(re.findall("\\\\...", test2))
# test2 = re.sub("\\\\...", "_", test2)
# print(test2)

# remove \n from content
test_str = re.sub("\\\\n", " ", test_str)

# remove html tags from content
test_str = re.sub("\\\\...", " ", test_str)

# remove non-alphanumeric characters from content
test_str = re.sub("[|,./]", "", test_str)

# turn content into lowercase
test_str = test_str.lower()

# get nltk stopwords
stop_words = set(stopwords.words("english"))

# tokenize content
word_tokens = word_tokenize(test_str)

# filter out stopwords from content
filtered = [w for w in word_tokens if not w.lower() in stop_words]

# generate filtered sentence from filtered list
filtered_sentence = ""
for w in filtered:
    filtered_sentence = filtered_sentence + " " + w

print(filtered_sentence)