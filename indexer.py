class LookOP(object):
    def __init__(self):
        self.terms={}

    def tokenize(self, text):
        import re
        clean_string = re.sub('[^a-z0-9 ]', ' ', text.lower())
        tokens = clean_string.split()
        return tokens


    def index(self,fn):
        import csv
        self.terms={}
        self.documents={}
        curdoc=0
        
        with open(fn, 'rb') as csvfile:
             spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
             for row in spamreader:

                for token in self.tokenize(row[4]):
                    if token not in self.terms:
                        self.terms[token]={}
                        self.terms[token]['tf']=1
                        self.terms[token]['pos']=0
                        self.terms[token]['neut']=0
                        self.terms[token]['neg']=0
                        self.terms[token]['tweets']=[]
                        tweet = {}
                        tweet['date']=row[2]
                        tweet['text']=row[5]
                        tweet['user']=row[4]
    
                        self.terms[token]['tweets'].append(tweet)

                        if row[0]=="4":
                            self.terms[token]['pos']=1
                        if row[0]=="2":
                            self.terms[token]['neut']=1
                        if row[0]=="0":
                            self.terms[token]['neg']=1
                    else:                        
                        self.terms[token]['tf']+=1
                        if row[0]=="4":
                            self.terms[token]['pos']+=1
                        if row[0]=="2":
                            self.terms[token]['neut']+=1
                        if row[0]=="0":
                            self.terms[token]['neg']+=1

                        tweet = {}
                        tweet['date']=row[2]
                        tweet['text']=row[5]
                        tweet['user']=row[4]
    
                        self.terms[token]['tweets'].append(tweet)

                for token in self.tokenize(row[5]):
                    if token not in self.terms:
                        self.terms[token]={}                            
                        self.terms[token]['tf']=1
                        self.terms[token]['pos']=0
                        self.terms[token]['neut']=0
                        self.terms[token]['neg']=0
                        self.terms[token]['tweets']=[]
                        tweet = {}
                        tweet['date']=row[2]
                        tweet['text']=row[5]
                        tweet['user']=row[4]

                        self.terms[token]['tweets'].append(tweet)

                        if row[0] == "4":
                            self.terms[token]['pos']=1
                        if row[0] is "2":
                            self.terms[token]['neut']=1
                        if row[0] is "0":
                            self.terms[token]['neg']=1
                    else:
                        self.terms[token]['tf']+=1
                        if row[0] is "4":
                            self.terms[token]['pos']+=1
                        if row[0] is "2":
                            self.terms[token]['neut']+=1
                        if row[0] is "0":
                            self.terms[token]['neg']+=1

                        tweet = {}
                        tweet['date']=row[2]
                        tweet['text']=row[5]
                        tweet['user']=row[4]

                        self.terms[token]['tweets'].append(tweet)

        print self.terms['scotthamilton']
#        print self.terms['kindle']


def main(args):
    lookop=LookOP()
#    lookop.index("testdata.manual.2009.06.14.csv")
    lookop.index("training.1600000.processed.noemoticon.csv")

if __name__ == "__main__":
    import sys
    main(sys.argv)

