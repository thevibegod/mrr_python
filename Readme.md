# MiningRigRentals API V2 Python3 Wrapper

Python3 Wrapper class for MiningRigRentals.
For detailed documentation visit https://www.miningrigrentals.com/apidocv2

#### Usage

```python
from mrr import API
API_KEY = "YOUR API KEY"
API_SECRET = "YOUR API SECRET"
mrr_obj = API(API_KEY, API_SECRET)
my_rigs = mrr_obj.rigs.get_my_rigs() #Get list of your rigs
```