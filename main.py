from mrr import API

API_KEY = "YOUR API KEY"
API_SECRET = "YOUR API SECRET"
mrr_obj = API(API_KEY, API_SECRET)

print(mrr_obj.extras.get_servers_info())
print(mrr_obj.rigs.create_rig(name='Test Rig', server='us-central01.miningrigrentals.com', algo='sha256',
                              hash={"hash": 10, 'type': 'mh'}))
print(mrr_obj.rigs.get_my_rigs())

print(mrr_obj.account.delete_pool([0]))
