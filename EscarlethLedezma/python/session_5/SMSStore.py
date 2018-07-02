class SMS_Store:

    def __init__(self):
        self.sms_store = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        '''Add a new SMS'''
        has_been_viewed = False
        self.sms_store.append((has_been_viewed, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        '''Return tne length of the sms store'''
        return len(self.sms_store)

    def get_unread_indexes(self):
        '''Return a lis with the indexes of the sms without view'''
        unread_indexes = []
        for i in range(len(self.sms_store)):
            converted_list = list(self.sms_store[i])
            if converted_list[0] is False:
                unread_indexes.append(i)
        return unread_indexes

    def get_message(self, index):
        '''Given a index of the sms return the attributes'''
        if 0 <= index < len(self.sms_store):
            lists = list(self.sms_store[index])
            lists[0] = True
            self.sms_store[index] = lists
            return lists[1], lists[2], lists[3]

    def delete(self, i):
        '''Delete a specific sms'''
        if 0 <= i < len(self.sms_store):
            del self.sms_store[i]

    def clear(self):
        '''Clean all the sms store'''
        self.sms_store.clear()


store = SMS_Store()
store.add_new_arrival(111111, 10, 'hello')
store.add_new_arrival(222222, 10, 'hola')
print(store.get_message(0))
print(store.get_unread_indexes())
