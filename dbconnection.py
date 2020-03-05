import pymysql

db = pymysql.connect("127.0.0.1","root","password","integrasbd" )


def insert_users_list(users_list):
	cursor = db.cursor()

	for user in users_list:
		sqlInsert = "INSERT INTO users(`user_id`,`email`,`username`,`emoney_user_id`,`emoney_owner_id`,`emoney_owner_name`,`names`,`display_names`) \
		   VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
		   (0, user['Email'], user['UserName'], user['UserID'], user['OwnerUserId'], user['OwnerName'], user['FirstNameLastName'], user['DisplayName'])

		sqlUpdate = "UPDATE users SET `email` = '%s',`username` = '%s',`emoney_owner_id` = '%s',`emoney_owner_name` = '%s',`names` = '%s',`display_names` = '%s' WHERE `emoney_user_id` = '%s';" % \
		   (user['Email'], user['UserName'], user['OwnerUserId'], user['OwnerName'], user['FirstNameLastName'], user['DisplayName'], user['UserID'])
		# print(user['Email'], user['UserName'], user['UserID'], user['OwnerUserId'], user['OwnerName'], user['FirstNameLastName'], user['DisplayName'])
		try:
			cursor.execute("SELECT user_id FROM users WHERE emoney_user_id=%s", user['UserID'])
		
			result = cursor.fetchone()
			if result == None:
		   		cursor.execute(sqlInsert)
		   		db.commit()
		   		print('USER INSERTED')
			else: 
				cursor.execute(sqlUpdate)
				db.commit()
				print('USER ALREADY IN DB, UPDATED')
		except:
		   	db.rollback()

	db.close()