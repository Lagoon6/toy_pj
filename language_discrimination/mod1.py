#!/usr/bin/env python
# coding: utf-8

from sklearn import svm,metrics
import glob, os.path, re, json


def check_freq(fname):
    basename = os.path.basename(fname)
    lang = basename.split('-')[0]
    
    with open(fname,"r",encoding="utf-8") as f:
        text = f.read()
        text= text.lower()
        
    code_a = ord("a")
    code_z = ord("z")
    cnt = [0 for n in range(0,26)]
    for char in text:
        code_current = ord(char)
        if code_a <= code_current <= code_z:
            cnt[code_current-code_a] +=1
    total = sum(cnt)
    freq = list(map(lambda n: n/total , cnt))
    return (freq,lang)


#지정된 경로내의 모든 파일을 읽어들여 오기
# 각 파일 처리하기
def load_files(path):
    freqs = []
    labels = []
    file_list = glob.glob(path)
    
    for fname in file_list:
        r = check_freq(fname)
        freqs.append(r[0])
        labels.append(r[1])
        
    return {"freqs":freqs, "labels":labels}



data = load_files('./lang/train/*.txt')
test = load_files('./lang/test/*.txt')


with open("./lang/freq.json", "w", encoding="utf-8") as fp:
    json.dump([data, test], fp)



# 학습하기 --- (※4)
clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])

# 예측하기 --- (※5)
predict = clf.predict(test["freqs"])




# 결과 테스트하기 --- (※6)
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 =", ac_score)
print("리포트 =")
print(cl_report)






