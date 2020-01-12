from nltk import sent_tokenize,word_tokenize,PorterStemmer
from nltk.corpus import wordnet,stopwords
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer
from collections import Counter
import math
from django.contrib.auth.models import User
from event.models import Event, Activity
from account.models import Profile,Skill,Cause,NGO,Address,Education,Contact,Experiance

class filtering(object):
    def __init__(self,id,similarity):
        self.id = id
        self.similarity = similarity


def eventProfile(id):

    rec = []
    events = Event.objects.get(pk=id)
    activity = Activity.objects.filter(event=events.id)

    eventDetail = events.title +" "+ events.location
    for x in activity:
        eventDetail = eventDetail +" "+ x.title +" "+ x.category +" "+ x.description

    eventVec = text_to_vector(eventDetail)




    user = User.objects.all()
    for users in user:
        string = ""
        profile = Profile.objects.all().filter(user = users.id)
        skill = Skill.objects.all().filter(profile = users.profile.id)
        cause = Cause.objects.all().filter(profile = users.profile.id)
        ngo = NGO.objects.all().filter(profile = users.profile.id)
        address = Address.objects.all().filter(profile = users.profile.id)
        education = Education.objects.all().filter(profile = users.profile.id)
        experiance = Experiance.objects.all().filter(profile = users.profile.id)
        for x in profile:
            string = string +' '+ x.occupation
        for x in skill:
            string = string +' '+  x.skill
        for x in cause:
            string = string +' '+  x.cause
        for x in ngo:
            string = string +' '+  x.name
        for x in address:
            string = string +' '+  x.address+' '+  x.zip_code+' '+  x.state+' '+  x.office_address+' '+  x.office_zip_code+' '+  x.office_state
        for x in education:
            string = string +' '+  x.level+' '+  x.description
        for x in experiance:
            string = string +' '+  x.detail

        string = text_to_vector(string)
        similarity = get_cosine(eventVec,string)
        if similarity > 0.0:
            rec.append(filtering(users.id,similarity))

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
