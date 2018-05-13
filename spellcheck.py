import sys
import os
import json
import difflib 



def load_json_file(path):
    data = open(path, 'r').read()
    try:
        return list(json.loads(data).keys())
    except Exception as e:
	print str(e)
	print "Exiting spellcheck"
	sys.exit()

def spellcheck(sorted_ip_str, eng_dict_keys):
	misspelledwords=0
	for word in sorted_ip_str:
		if word not in eng_dict_keys:
			print word
			misspelledwords+=1
	if misspelledwords==0:
		print "found 0 misspelled words"
	

def main():
	input_line=sys.argv[1]
	eng_dict=sys.argv[2]
	dict_words_list=load_json_file(eng_dict)	
	
	ip_words=input_line.strip().split(' ')
 	uniq_ip_words=set(ip_words)
	sorted_uniq_ip_words=sorted(list(uniq_ip_words))
	spellcheck(sorted_uniq_ip_words, dict_words_list)	

if __name__=="__main__":
	main()
