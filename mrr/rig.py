class Rig:
    mrr_obj = None

    def __init__(self, mrr_obj):
        self.mrr_obj = mrr_obj

    def get_rigs(self, algo, **kwargs):
        """
        Equivalent to main Rig list pages.Search for rigs on a specified algo.
        :param algo:
        :param kwargs:
        """
        params = kwargs
        params['type'] = algo
        return self.mrr_obj.get('/rig', params=params)

    def get_my_rigs(self, **kwargs):
        """
        Get a list of the user's rigs.
        :param kwargs:
        """
        return self.mrr_obj.get('/rig/mine', params=kwargs)

    def create_rig(self, name, algo, server, **kwargs):
        """
        To create a rig
        :param name:
        :param algo:
        :param server:
        :param kwargs:
        """
        params = kwargs
        params['name'] = name
        params['server'] = server
        params['type'] = algo
        return self.mrr_obj.put('/rig', data=params)

    def delete_rig(self, ids):
        """
        To delete a rig
        :param ids:
        """
        ids = [str(id_val) for id_val in ids]
        return self.mrr_obj.delete('/rig/' + ';'.join(ids))

    def get_rigs_by_id(self, ids):
        """
        Get details of rigs by specifying a list of rig ids.
        :param ids:
        """
        ids = [str(id_val) for id_val in ids]
        return self.mrr_obj.get('/rig/' + ';'.join(ids))

    def extend_rental(self, ids, **kwargs):
        """
        Extend rental for one or more rigs.
        :param ids:
        :param kwargs:
        """
        ids = [str(id_val) for id_val in ids]
        return self.mrr_obj.put('/rig/' + ';'.join(ids) + '/extend', data=kwargs)

    def active_threads(self, ids):
        """
        Get active threads for a list of rigs.
        :param ids:
        """
        ids = [str(id_val) for id_val in ids]
        return self.mrr_obj.get('/rig/' + ';'.join(ids) + '/threads')

    def graph_data(self, ids, **kwargs):
        """
        Get graph data for a list of rigs.
        :param ids:
        :param kwargs:
        """
        ids = [str(id_val) for id_val in ids]
        return self.mrr_obj.get('/rig/' + ';'.join(ids) + '/graph', params=kwargs)

    def get_rig_port(self, ids):
        """
        Get specific ports(other than 3333) for a list of rigs.
        :param ids:
        """
        ids = [str(id_val) for id_val in ids]
        return self.mrr_obj.get('/rig/' + ';'.join(ids) + '/port')

    def delete_pool(self, ids, pool_priority):
        """
        Delete a pool from a list of rigs
        :param ids:
        :param pool_priority:
        :return:
        """
        ids = [str(id_val) for id_val in ids]
        return self.mrr_obj.delete('/rig/' + ';'.join(ids) + '/pool/' + str(pool_priority))

    def add_pool(self, ids, host, port, username, password, priority):
        """
        Add or replace a pool in one or more rigs.
        :param ids:
        :param host:
        :param port:
        :param username:
        :param password:
        :param priority:
        """
        ids = [str(id_val) for id_val in ids]
        data = {'host': host, 'port': port, 'user': username, 'pass': password, 'priority': priority}
        return self.mrr_obj.put('/rig/' + ';'.join(ids) + '/pool', data=data)

    def get_pools(self, ids):
        """
        List pools assigned to one or more rigs.
        :param ids:
        """
        ids = [str(id_val) for id_val in ids]
        return self.mrr_obj.get('/rig/' + ';'.join(ids) + '/pool')

    def add_profile_to_rigs(self, ids, profile):
        """
        Apply a pool profile to one or more rigs.
        :param ids:
        :param profile:
        """
        ids = [str(id_val) for id_val in ids]
        return self.mrr_obj.put('/rig/' + ';'.join(ids) + '/' + profile)

    def update_rigs(self, rigs):
        """
        Update a batch of rigs using a 'rigs' array.
        :param rigs:
        """
        return self.mrr_obj.put('/rig/batch', data=rigs)
