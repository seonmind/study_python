url="http://naver.com"

domain=url.replace("http://","")
domain=domain[:domain.index(".")]
password1=domain[:3]
password2=len(domain)
password3=domain.count('e')
password=password1+str(password2)+str(password3)+"!"
print("생성된 비밀번호 :%s"%password)
