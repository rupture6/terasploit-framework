#######
# Command: Search
#######

from init.tsf.ui.wildcard import Table
from init.tsf.util.wildcard import contents
from init.tsf.core.wildcard import Get

from init.tsf.base.wildcard import (
    Search,
    value_required
)

class _search_:    

    @value_required
    def function() -> None:
        path = Get.parameter()
        result = Search.search_specific(path)

        tabled_result = Table.module(result,'Search',path)
        if tabled_result == True:
            print (contents.interact_message)