from dao.DAOInterface import DAOInterface


class AssociationDAO(DAOInterface):

    def __init__(self):
        super()

    def selectAll(self):
        #   return a list of all parts
        return "We are all parts"

    def select(self, a):
        #   uses sql to select a specific part based on part ID
        return "I am a select part"

    def insert(self, a):
        #   uses sql to insert the part into the database
        return "New part inserted into DB"

    def update(self, a):
        #   updates a part using sql
        return "Selected part updated into DB"

    def delete(self, a):
        #   deletes a specific part based on part ID
        return "Selected part was deleted from DB"