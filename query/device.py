class QueryDevices:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def getDeviceHistoryBySAPID(self, sap_id):
        '''This method returns a List of the Device's history when a SAP_ID is passed as parameter.'''
        db_cursor = self.db_connection.cursor()
        q = 'SELECT * FROM PC9_DEVICE_RATE WHERE SAP_ID = :SAP_ID'
        results = []
        try:
            fetched_data = db_cursor.execute(q, [sap_id])
            results = [row for row in fetched_data]
        except Exception as err:
            print(err)
        finally:
            db_cursor.close()

            return results