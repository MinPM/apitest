#my_settings.py
SECRET = {
        'secret' : '' # 숨기기!
}

ALGORITHM = 'HS256'

DATABASES = {
	'default' : {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'dabase2', #aws mysql에 올렸던 데이터베이스의 이름
		'USER': 'admin', 
		'PASSWORD': 'chlalswl9*',	#비밀번호!
		'HOST': 'database-2.cuhle7dfp5lv.us-east-2.rds.amazonaws.com', #RDS의 엔드포인트 주소를 입력
		'PORT': '3306',
	}
}