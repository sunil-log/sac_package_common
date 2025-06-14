
# -*- coding: utf-8 -*-
"""
Created on  May 07 2025

@author: sac
"""

from numbers import Number
import numpy as np

def cast_np_scalar(value):
	"""
	numpy scalar‧array → Python native 타입 변환 + JSON 직렬화 호환.
	"""
	# ① numpy scalar(np.int64, np.float64, …)를 가장 먼저 처리
	if isinstance(value, np.generic):
		return value.item()

	# ② Python 기본형 그대로 유지
	if value is None or isinstance(value, (str, bool)):
		return value
	if isinstance(value, Number):		  # np.generic은 이미 걸렀으므로 안전
		return value

	# ③ numpy array → list
	if isinstance(value, np.ndarray):
		return value.tolist()

	# ④ set/tuple → list
	if isinstance(value, (set, tuple)):
		return list(value)

	# ⑤ 마지막 수단
	raise TypeError(f"{type(value).__name__} is not JSON serializable")
