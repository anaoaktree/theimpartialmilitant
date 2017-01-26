import requests, re



class Issue:
    def __init__(self, question, answer=None, url=None):
        self.__question = question
        self.__answer = answer
        self.__url = url

    def question(self):
        return self.__question

    def answer(self):
		return self.__answer

    def url(self):
        return self.__url

	def __repr__(self):
		return "Question: %s \nReply:%s" % (self.__question, self.__answer)



def get_data():
    r = requests.get("http://lda.data.parliament.uk/commonsansweredquestions.json?_view=Commons+Written+Answers&_pageSize=10&_sort=-dateOfAnswer&_page=0")
    body = r.json()
    replies = body["result"]["items"]

    def question_url(q_id):
    	return "http://lda.data.parliament.uk/resources/%s.json" % q_id

    results = []
    for reply in replies:
    	q_id = re.findall(r'\d+',reply["_about"])[0]
    	q = requests.get(question_url(q_id))
    	question = q.json()["result"]
        q = question["primaryTopic"]["questionText"]
        ans = reply["answerText"]["_value"]

        results.append(Issue(q, ans, question["_about"]))
        # url
    return results
