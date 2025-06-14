
# -*- coding: utf-8 -*-
"""
Created on  May 06 2025

@author: sac
"""

def filter_dict_by_keyword(d: dict, keyword: str) -> dict:
	"""dictionary에서 keyword를 포함한 key만 추려 반환한다."""
	return {k: v for k, v in d.items() if keyword in k}
