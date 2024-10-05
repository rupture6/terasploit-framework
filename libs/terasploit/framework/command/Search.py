#######
# Command: Search
#######


from init.teralib.ui import Table
from init.teralib.core import Get
from init.teralib.util import contents
from init.teralib.base import (
    Search,
    value_required
)

# Command class

class _search_:    

    @staticmethod
    @value_required
    def function() -> None:

        path = Get.parameter()
        result = Search.search_specific(path)

        tabled_result = Table.module(result,'Search',path)
        if tabled_result == True:
            print (contents.interact_message)