from . import user_input
from typing import List, Dict
from math import ceil

class Pagination:
    def __init__(self, pagination_input = user_input, db_con = None):
        self.page = max(1, pagination_input['page'])
        self.page_size = max(1, pagination_input['page_size'])
        self.db_con = db_con

    def get_paginated_results(self):
        all_results = self._get_all_results()
        
        total_results = len(all_results)
        total_pages = ceil(total_results / self.page_size)
        
        self.page = min(self.page, total_pages)
        
        start_index = (self.page - 1) * self.page_size
        end_index = start_index + self.page_size
        
        paginated_results = all_results[start_index:end_index]
        
        return {
            "total_results": total_results,
            "page": self.page,
            "page_size": self.page_size,
            "total_pages": total_pages,
            "results": paginated_results,
            "has_next": self.page < total_pages,
            "has_prev": self.page > 1
        }

    def _get_all_results(self):
        return []