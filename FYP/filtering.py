from nltk import sent_tokenize,word_tokenize,PorterStemmer
from nltk.corpus import wordnet,stopwords
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer
from collections import Counter
import math
from event.models import Event, Activity
from account.models import User,Profile

class filtering(object):
    def __init__(self,id,similarity):
        self.id = id
        self.similarity = similarity


def eventProfile(id):

    rec = []
    events = Event.objects.get(pk=id)
    activity = Activity.objects.filter(event=id)

    eventDetail = events.title +" "+ events.location
    for x in activity:
        eventDetail = eventDetail +" "+ x.title +" "+ x.category +" "+ x.description

    eventVec = text_to_vector(eventDetail)
    #print(eventVec)


    user = User.objects.all()
    profile = " "
    for x in user:
        user_profile = Profile.objects.get(user=x.id)
        profile = user_profile.home_state +" "+user_profile.skill+" "+user_profile.cause
        profile = text_to_vector(profile)
        #print(profile)
        similarity = get_cosine(eventVec,profile)
        rec.append(filtering(x.id,similarity))

    return rec



ps=PorterStemmer()
lemmatizer=WordNetLemmatizer()
stop_words = stopwords.words('english')
special=['.',',','\'','"','-','/','*','+','=','!','@','$','%','^','&','``','\'\'','We','The','This','it','for']


def normalise(word):
    word = word.lower()
    word = ps.stem(word)
    return word

def get_cosine(vec1, vec2):
    intersection = set(vec1) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return numerator / denominator


def text_to_vector(text):
    words = word_tokenize(text)
    vec=[]
    for word in words:
        if(word not in stop_words):
            if(word not in special):
                w=normalise(word)
                vec.append(w)
    return Counter(vec)
