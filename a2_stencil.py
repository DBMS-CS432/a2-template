import sqlite3

class DbStreamer:

	@staticmethod
	def jsonify_data(data):
		json_data = []
		
		for result in data:
			json_data.append(dict(zip(row_headers, result)))
		
		# print(json_data, end="\n\n")
		return json_data


	def __init__(self, host, user, password, database):
		# TODO: Create the connection by replacing None with appropriate code.
		self.conn = None 
		
		# Do not modify code in this definition below this line.
		_cursor = self.conn.cursor()
		# When using SQLite, include the following line to ensure foreign key commands are recognized
		_cursor.execute('PRAGMA foreign_keys = ON')
		
		return self.conn

	def get_connection(self):
		return self.conn

	def close_connection(self):
		self.conn.commit()
		self.conn.close()
		return
	
	def get_tables(self):
		sql = "SHOW TABLES;"
		
		_cursor = self.conn.cursor()
		_cursor.execute(sql)
		data = _cursor.fetchall()

		return data

	# TODO: Add your logic for each of the questions in the corresponding methods provided below.
	def q1(self):
		_cursor = self.conn.cursor()

		# TODO: Add logic here
		# ------------------------------------------------------------------------------------



		# ------------------------------------------------------------------------------------
		# Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

		data = _cursor.fetchall()
		return data

    def q2(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        data = _cursor.fetchall()
        return data

    def q3(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        data = _cursor.fetchall()
        return data

    def q4(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        data = _cursor.fetchall()
        return data

    def q5(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        data = _cursor.fetchall()
        return data

    def q6(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        data = _cursor.fetchall()
        return data

    def q7(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        data = _cursor.fetchall()
        return data

    def q8(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        data = _cursor.fetchall()
        return data

    def q9(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        data = _cursor.fetchall()
        return data

    def q10(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        data = _cursor.fetchall()
        return data

    def q11(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        data = _cursor.fetchall()
        return data

    def q12(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        data = _cursor.fetchall()
        return data

    def q13(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        data = _cursor.fetchall()
        return data

    def q14(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        data = _cursor.fetchall()
        return data

    def q15(self):
        _cursor = self.conn.cursor()

        # TODO: Add logic here
        # ------------------------------------------------------------------------------------



        # ------------------------------------------------------------------------------------
        # Do not edit below this line, otherwise the autograder won't be able to evaluate your code.

        data = _cursor.fetchall()
        return data


if __name__ == "__main__":

    ## TODO: Initialize the DbStreamer object
    db_streamer = DbStreamer()
