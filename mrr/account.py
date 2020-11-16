class Account:
    mrr_obj = None

    def __init__(self, mrr_obj):
        self.mrr_obj = mrr_obj

    def get_account_details(self):
        """
        Get account details.
        """
        return self.mrr_obj.get('/account')

    def get_account_balance(self):
        """
        Retrieve account balances.
        """
        return self.mrr_obj.get('/account/balance')

    def get_account_transactions(self, **kwargs):
        """
        Get all account transactions.
        :param kwargs:
        """
        return self.mrr_obj.get('/account/transactions', params=kwargs)

    def get_pool_profiles(self, algo=None):
        """
        Get all pool profiles.Can be filtered based on algorithm.
        :param algo:
        """
        if algo:
            return self.mrr_obj.get('/account/profile', params={'algo': algo})
        else:
            return self.mrr_obj.get('/account/profile')

    def get_pool_profile_by_id(self, id):
        """
        Get pool profile by id.
        :param id:
        """
        return self.mrr_obj.get('/account/profile/' + str(id))

    def create_pool_profile(self, name, algo):
        """
        Create a pool profile
        :param name:
        :param algo:
        """
        return self.mrr_obj.put('/account/profile', data={'name': name, 'algo': algo})

    def create_pool(self, algo, name, host, port, username, pwd, notes=None):
        """
        Create a pool
        :param algo:
        :param name:
        :param host:
        :param port:
        :param username:
        :param pwd:
        :param notes:
        """
        if notes:
            return self.mrr_obj.put('/account/pool',
                                    data={'type': algo, 'name': name, 'host': host, 'port': port, 'user': username,
                                          'pass': pwd, 'notes': notes})
        else:
            return self.mrr_obj.put('/account/pool',
                                    data={'type': algo, 'name': name, 'host': host, 'port': port, 'user': username,
                                          'pass': pwd})

    def add_pool_to_pool_profile(self, profile_id, pool_id, pool_priority):
        """
        Add a pool to pool profile
        :param profile_id:
        :param pool_id:
        :param pool_priority:
        """
        return self.mrr_obj.put('/account/profile/' + str(profile_id),
                                data={'poolid': pool_id, 'priority': pool_priority})

    def delete_pool(self, ids):
        """
        Delete a set of pools.
        :param ids:
        """
        ids = [str(id) for id in ids]
        return self.mrr_obj.delete('/account/pool/' + ';'.join(ids))

    def get_all_pools(self):
        """
        Get all saved pools.
        """
        return self.mrr_obj.get('/account/pool')

    def update_pool(self, ids, **kwargs):
        """
        Update saved pools
        :param ids:
        :param kwargs:
        """
        ids = [str(id) for id in ids]
        return self.mrr_obj.put('/account/pool/' + ';'.join(ids), data=kwargs)
