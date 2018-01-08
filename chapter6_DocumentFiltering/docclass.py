import re
from sqlite3 import dbapi2 as sqlite
import math


def getwords(doc):
    splitter = re.compile('\\W*')
    words = [s.lower() for s in splitter.split(doc) if len(s)>2 and len(s)<20]
    return dict([w,1] for w in words)

class classifier:
    def __init__(self,getfeatures,filename=None):
        # 统计特征组合的数量
        self.fc = {}
#         统计每个分类中文档数量
        self.cc={}
        self.getfeatures = getfeatures

    def setdb(self, dbfile):
        self.con = sqlite.connect(dbfile)
        self.con.execute("create table if not exists fc(feature,category,count)")
        self.con.execute("create table if not exists cc(category,count)")
    #增加特征组合的数量
    def incf(self,f,cat):
        # self.fc.setdefault(f,{})
        # self.fc[f].setdefault(cat,0)
        # self.fc[f][cat] += 1
        count = self.fcount(f,cat)
        if count == 0:
            self.con.execute("insert into fc VALUES('%s','%s',1)" %(f,cat))
        else:
            self.con.execute("update fc set count=%d where feature='%s' AND  category='%s'" %(count+1,f,cat))

    def incc(self,cat):
        # self.cc.setdefault(cat,0)
        # self.cc[cat]+=1
        count = self.catcount(cat)
        if count == 0:
            self.con.execute("insert into cc VALUES ('%s',1)"%(cat))
        else:
            self.con.execute("update cc set count=%d where category='%s'" % (count+1,cat))

    def fcount(self,f,cat):
        # if f in self.fc and cat in self.fc[f]:
        #     return float(self.fc[f][cat])
        # return 0.0
        res =self.con.execute("select count from fc where feature='%s' and category='%s'" %(f,cat)).fetchone()
        if res == None:
            return 0
        else:
            return float(res[0])

    def catcount(self,cat):
        # if cat in self.cc:
        #     return self.cc[cat]
        # return 0
        res=self.con.execute("select count from cc WHERE category='%s'" % (cat)).fetchone()
        if res==None:
            return 0
        else:
            return res[0]
    # 所有内容项数量
    def totalcount(self):
        res = self.con.execute("select sum(count) from cc").fetchone()
        if res==None:
            return 0
        return res[0]

    def categories(self):
        cur=self.con.execute("select category from cc")
        return [d[0] for d in cur]

    def train(self,item,cat):
        feature = self.getfeatures(item)
        for f in feature:
            self.incf(f,cat)
        self.incc(cat)
        self.con.commit()

    def fprob(self,f,cat):
        if self.catcount(cat)==0:
            return 0
        return self.fcount(f,cat)/self.catcount(cat)

    def weightedprob(self,f,cat,prf,weight=1.0,ap=0.5):
        basicprob = prf(f,cat)
        totals = sum([self.fcount(f,c) for c in self.categories()])
        bp = ((weight*ap) + (totals*basicprob))/(weight+totals)
        return bp

class naivebayes(classifier):
    def __init__(self,getfeatures):
        classifier.__init__(self,getfeatures)
        self.thresholds={}
    def setthreshold(self,cat,t):
        self.thresholds[cat] = t
    def getthreshold(self,cat):
        if cat not in self.thresholds:
            return 1.0
        return self.thresholds[cat]

    def docprob(self,item,cat):
        features = self.getfeatures(item)
        p=1
        for f in features:
            p*=self.weightedprob(f,cat,self.fprob)
        return p
    def prob(self,item,cat):
        catprob = self.catcount(cat)/self.totalcount()
        docprob = self.docprob(item,cat)
        return catprob*docprob

    def classify(self,item,default=None):
        probs={}
        max = 0.0
        for cat in self.categories():
            probs[cat] = self.prob(item,cat)
            if probs[cat]>max:
                max = probs[cat]
                best = cat

        for cat in probs:
            if cat==best:
                continue
            if probs[cat]*self.getthreshold(best)>probs[best]:
                return default
        return best

class fisherclassifier(classifier):
    def __init__(self,getfeatures):
        classifier.__init__(self,getfeatures)
        self.minimums={}

    def cprob(self,f,cat):
        clf = self.fprob(f,cat)
        if clf ==0:
            return 0
        freqsum = sum([self.fprob(f,c) for c in self.categories()])
        p=clf/freqsum
        return p
    def fisherprob(self,item,cat):
        p=1
        features = self.getfeatures(item)
        for f in features:
            p*=(self.weightedprob(f,cat,self.cprob))
        fscore=-2*math.log(p)
        return self.invchi2(fscore,len(features)*2)

    def invchi2(self,chi,df):
        m=chi/2.0
        sum=term=math.exp(-m)
        for i in range(1,df//2):
            term *= m/i
            sum+=term
        return min(sum,1.0)

    def setminimum(self,cat,min):
        self.minimums[cat]=min
    def getminimum(self,cat):
        if cat not in self.minimums:
            return 0
        return self.minimums[cat]

    def classify(self, item, default=None):
        # Loop through looking for the best result
        best = default
        max = 0.0
        for c in self.categories():
            p = self.fisherprob(item, c)
            # Make sure it exceeds its minimum
            if p > self.getminimum(c) and p > max:
                best = c
                max = p
        return best



def sampletrain(cl):
    cl.train('Nobody owns the water.', 'good')
    cl.train('the quick rabbit jumps fences', 'good')
    cl.train('buy pharmaceuticals now', 'bad')
    cl.train('make quick money at the online casino', 'bad')
    cl.train('the quick brown fox jumps', 'good')
