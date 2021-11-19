import re

bad_words =['đụ','đĩ','cặc','buồi','lồn','đéo','chịch','địt mẹ','địt má','địt bố','địt cụ','địt đĩ','địt lồn','di me', 'du me', 'du ma', 'dit cu','chet me may','dit ma','dit cu', 'dit bo', 'dit lon', 'cc', ' cl ', 'clmm', 'im me','im mẹ', 'im bố', 'dit me','ditme','dime','ditbo','dime', 'dit chet cu', 'dit chet cha', 'địt', 'loz', 'sex', 'dume', 'duma','đm','Đcm','dkm', 'đcm']
bad_words2 = ['chich','lon','cac', 'dm','duma', 'dcm']

def replaceBadWords(UserMessage, BadWordsList):
    finalMessage = UserMessage
    for item in BadWordsList:
      for word in re.sub('[^a-zA-Z 0-9 \n\. á à ả ã ạ â ấ ầ ậ ẫ ă ẳ ắ ẵ ằ ặ đ ọ ò õ ỏ ó ẹ é è ẽ ẻ ỉ í ị ì ĩ ê ệ ế ề ễ ể ọ ô ố ồ ổ ộ ỗ ợ ơ ở ớ ờ ỡ ụ ù ủ ũ ú ự ư ứ ừ ữ ử ỵ ý ỷ ý ỳ ỹ đ]','', str(finalMessage)).split():
        if word == item or (item in word and ( (word[0] == 'c' and word[-1]=='c') or (word[0]== 'l' and word[-1] == 'n'))):
          finalMessage = finalMessage.replace(item,"\*"*len(item))
    return finalMessage

def checkBadWords(message):
  content = re.sub('[^a-zA-Z 0-9 \n\. các á à ả ã ạ â ấ ầ ậ ẫ ă ẳ ắ ẵ ằ ặ đ ọ ò õ ỏ ó ẹ é è ẽ ẻ ỉ í ị ì ĩ ê ệ ế ề ễ ể ọ ô ố ồ ổ ộ ỗ ợ ơ ở ớ ờ ỡ ụ ù ủ ũ ú ự ư ứ ừ ữ ử ỵ ý ỷ ý ỳ ỹ đ]', '', str(message.lower()))
  for item in bad_words2:
    for word in content.split():
      if word == item or (item in word and ( (word[0] == 'c' and word[-1]=='c') or  (word[0]== 'l' and word[-1] == 'n'))):
        #Fix and re-send the message
        replace_message = replaceBadWords(message.lower(), bad_words2)
        return replace_message
        return
        
  for item in bad_words:
    for word in content.split():
      if word == item:
        print(word+"/"+item)
        return True
        return
  return False