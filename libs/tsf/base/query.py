#######
# Base: Query
#######

import os
import sys

class Search:
    """ Search Class - Finds all modules in modules folder """

    def search_specific(word) -> list:
        """ returns a list that has matched the specified word """
        
        final_result = []
        all_modules = Search.all_modules()
        for i in all_modules:
            if word in i:
                final_result.append(i)
        return sorted(final_result)


    def all_modules() -> list:
        """ returns a list of all module available in modules folder """
        
        result = []
        final_result = []
        low = []

        path = os.path.join(sys.path[0] + "/modules")
        for root, dirs, _ in os.walk(path):
            for x in dirs:
              f = os.listdir(root+'/'+x)
              for i in f:
                  result.append(root+'/'+x+'/'+i)

        a = len(result[0].split('/'))
        for y in result:
            count = len(y.split('/'))
            low.append(count if count < a else a )

        # Removing __init__.py if there is.
        clear_init = [x for x in result if '__init__.py' not in x]
        for x in clear_init:
            if len(x.split('/')) != low[-1]:
                r = x.split('/')
                if '.py' in r[-1]:
                    g = x.replace(path + '/','')
                    module_path = g.replace('.py','')
                    final_result.append(module_path)
                else:
                    pass
            if len(x.split('/')) == low[-1]:
                r = x.split('/')
                if '.py' in r[-1]:
                    g = x.replace(path + '/','')
                    module_path = g.replace('.py','')
                    final_result.append(module_path)
                else:
                    pass

        return sorted(final_result)