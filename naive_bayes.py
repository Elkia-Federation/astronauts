from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from essays.en1 import essay_en1
from essays.en2 import essay_en2

f = open("timecube.txt", "r")
timecube = f.read()
train = [
('On behalf of the American people, THANK YOU to our incredible law enforcement officers. As President of the United States - I will fight for you, and I will never, ever let you down. Now, more than ever, we must support the men and women in blue! #LawEnforcementAppreciationDay','trump'),
('African American unemployment is the lowest ever recorded in our country. The Hispanic unemployment rate dropped a full point in the last year and is close to the lowest in recorded history. Dems did nothing for you but get your vote!  #NeverForget  @foxandfriends','trump'),
('Dow goes from 18,589 on November 9, 2016, to 25,075 today, for a new all-time Record. Jumped 1000 points in last 5 weeks, Record fastest 1000 point move in history. This is all about the Make America Great Again agenda! Jobs, Jobs, Jobs. Six trillion dollars in value created!','trump'),
('Thank you to the great Republican Senators who showed up to our mtg on immigration reform. We must BUILD THE WALL, stop illegal immigration, end chain migration & cancel the visa lottery. The current system is unsafe & unfair to the great people of our country - time for change!','trump'),
('Stock Market had another good day but, now that the Tax Cut Bill has passed, we have tremendous upward potential. Dow just short of 25,000, a number that few thought would be possible this soon into my administration. Also, unemployment went down to 4.1%. Only getting better!','trump'),
('North Korean Leader Kim Jong Un just stated that the “Nuclear Button is on his desk at all times.” Will someone from his depleted and food starved regime please inform him that I too have a Nuclear Button, but it is a much bigger & more powerful one than his, and my Button works!','trump'),
('All across America people chose to get involved, get engaged and stand up. Each of us can make a difference, and all of us ought to try. So go keep changing the world in 2018.','obama'),
('As we count down to the new year, we get to reflect and prepare for what’s ahead. For all the bad news that seemed to dominate our collective consciousness, there are countless stories from this year that remind us what is best about America.', 'obama'),
('Michelle and I are thinking of the victims of today attack in NYC and everyone who keeps us safe. New Yorkers are as tough as they come.', 'obama'),
('May God also grant all of us the wisdom to ask what concrete steps we can take to reduce the violence and weaponry in our midst.','obama'),
('Michelle and I are thinking of the victims and their families in Barcelona. Americans will always stand with our Spanish friends. Un abrazo.', 'obama'),
('Humbled to be recognized by a family with a legacy of service. Who is your #ProfileInCourage? Tell me about them: https://www.obama.org/your-voice/ ','obama'),
('Thank you to all the first responders and people helping each other out. That is what we do as Americans. Here is one way you can help now.','obama'),
]
classifier = NaiveBayesClassifier(train)
print(classifier.classify(essay_en1))
print(classifier.classify(essay_en2))
