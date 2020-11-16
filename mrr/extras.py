class Extras:
    mrr_obj = None

    def __init__(self, mrr_obj):
        self.mrr_obj = mrr_obj

    def get_self_account_details(self):
        """
        Test connectivity and return information about you
        """
        return self.mrr_obj.get('/whoami')

    def get_servers_info(self):
        """
        Get a list of MRR rig servers.
        """
        return self.mrr_obj.get('/info/servers')

    def get_algo_info(self, algo=None, **kwargs):
        """
        Get all algos and statistics for them (suggested price, unit information, current rented hash/etc)
        :param algo:
        :param kwargs:
        """
        if algo:
            return self.mrr_obj.get('/info/algos' + '/' + algo, **kwargs)
        return self.mrr_obj.get('/info/algos')

    def get_rentals_on_my_rigs(self, **kwargs):
        """
        Lists rentals on your rigs.
        :param kwargs:
        """
        kwargs['type'] = 'owner'
        return self.mrr_obj.get('/rental', params=kwargs)
