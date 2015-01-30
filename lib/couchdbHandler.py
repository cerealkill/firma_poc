# -*- coding: utf-8 -*-
import sys
import couchdb
from uuid import uuid4


class Couch():
    """Couchdb Utils Class.

    >>> Usage:
    
        couch = Couch(url_=URL, session_=None)
        couch.print_dbs()
        db = couch.fetch_db(DATABASE) # Iterate through 'db' to get all documents from that database.
        i1_doc = couch.add_doc(db, dict(i1))
        i1_doc['desc'] = 'alface-crespa'
        couch.update_doc(db, i1_doc)
        couch.del_doc(db, i1_doc)
        
    
    >>> Databases:
    
        client = couch.get_client() # Iterate through 'client' to get all database names from server.
        db = couch.create_db(DATABASE)
        couch.del_db(DATABASE)
    """
    

    def __init__(self, url_, session_):
        self.url_ = url_
        self.session_ = session_
        self.__set_client()

    def print_dbs(self):
        print '\n[+] Databases on CouchDB server are: '
        for dbs in self.client:
            print '[-]     ' + str(dbs)

    def get_client(self):
        return self.client

    def __set_client(self):
        self.client = couchdb.client.Server(
            url=self.url_, full_commit=True, session=self.session_)

    def fetch_db(self, db):
        if(db in self.client):
            return self.client[db]
        else:
            self.create_db(db)

    def create_db(self, db):
        try:
            print '\n[+] Creating database "' + db + '".'
            database = self.client.create(db)
            print '[*]     Done.'
            return database

        except(couchdb.PreconditionFailed):
            print '[!] Database already exists.'
            return

        except:
            print "[!] Error: ", sys.exc_info()[0]
            return

    def del_db(self, db):
        try:
            print '\n[+] Deleting database "' + db + '".'
            self.client.delete(db)
            print '[*]     Done.'

        except(couchdb.ResourceNotFound):
            print '[!] Database doesnt exist.'

        except:
            print "[!] Error: ", sys.exc_info()[0]

    def add_doc(self, db, dict_):
        doc_id = uuid4().hex
        db[doc_id]= dict_
        print '\n[*] Done saving document id: ' + doc_id
        return db[doc_id] 

    def update_doc(self, db, doc):
        try:
            print '\n[+] Updating document id: ' + doc.id
            doc_meta = db.save(doc)
            print '[*]     Done rev: ' + doc_meta[1]
            return doc_meta

        except(couchdb.ResourceConflict):
            print '[!] Incorrect document revision'
        except:
            print "[!] Error: ", sys.exc_info()[0]

    def del_doc(self, db, doc):
        try:
            print '\n[+] Deleting document id: ' + doc.id
            db.delete(doc)
            print '[*]     Done.'

        except(couchdb.ResourceConflict):
            print '[!] Incorrect document revision'
        except:
            print "[!] Error: ", sys.exc_info()[0]
