
# -*- coding: utf-8 -*-
"""
Created on  May 02 2025

@author: sac
"""

def add_affix_to_keys(d: dict,
					  *,
					  prefix: str = "",
					  postfix: str = "",
					  recursive: bool = False) -> dict:
	"""
	모든 key 앞뒤에 prefix/postfix를 붙여 새로운 dict를 반환한다.

	Parameters
	----------
	d : dict
		원본 dictionary.
	prefix : str, optional
		key 앞에 붙일 문자열. 기본값 "".
	postfix : str, optional
		key 뒤에 붙일 문자열. 기본값 "".
	recursive : bool, optional
		True이면 value가 dict인 항목에도 재귀적으로 동일 작업을 수행한다.

	Returns
	-------
	dict
		변환된 dictionary.
	"""
	def _transform(target: dict) -> dict:
		out = {}
		for k, v in target.items():
			new_key = f"{prefix}{k}{postfix}"
			if recursive and isinstance(v, dict):
				out[new_key] = _transform(v)
			else:
				out[new_key] = v
		return out

	return _transform(d)
