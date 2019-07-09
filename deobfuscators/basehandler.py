class BaseHandler:
    def add_to_collection(self, key, value, collection, increment_value=True):
        """
        Save a key value pair to the collection of declarations
        :param key: 
        :param value: 
        :param collection: 
        :param increment_value: 
        :return: 
        """
        if key not in collection.keys():
            if increment_value:
                count = len(collection.items()) + 1
                collection[key] = value + str(count)
            else:
                collection[key] = value
