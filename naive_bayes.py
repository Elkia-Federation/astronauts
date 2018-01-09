from textblob import (TextBlob, NaiveBayesClassifier)
from essays.en1 import essay_en1
from essays.en2 import essay_en2

f = open("timecube.txt", "r")
timecube = f.read()
train = [(str(timecube), 'timecube')
('On behalf of the American people, THANK YOU to our incredible law enforcement officers. As President of the United States - I will fight for you, and I will never, ever let you down. Now, more than ever, we must support the men and women in blue! #LawEnforcementAppreciationDay','trump')
('African American unemployment is the lowest ever recorded in our country. The Hispanic unemployment rate dropped a full point in the last year and is close to the lowest in recorded history. Dems did nothing for you but get your vote!  #NeverForget  @foxandfriends','trump')
]
classifier = NaiveBayesClassifier(train)
cl.classify(essay_en1)
