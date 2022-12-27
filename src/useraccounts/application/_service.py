class Service:
    def initiate_db_transaction(self, function, *args):
        data = None

        with self.unit_of_work as unit_of_work:
            data = function(unit_of_work, *args)

        return data
