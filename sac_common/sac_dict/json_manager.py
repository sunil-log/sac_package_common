
# -*- coding: utf-8 -*-
"""
Created on  Mar 15 2025

@author: sac
"""

from .cast_scalar import cast_np_scalar


import json
import argparse
from types import SimpleNamespace
from typing import Any, Mapping




def save_json(args: Any, filename: str) -> None:
	"""
	argparse.Namespace, types.SimpleNamespace, dict → JSON 파일 저장.
	numpy scalar/array 도 지원하도록 default 인코더를 지정한다.
	"""
	if isinstance(args, (argparse.Namespace, SimpleNamespace)):
		data = vars(args)
	elif isinstance(args, Mapping):
		data = args
	else:
		raise ValueError(
			"지원되지 않는 args 타입이다. "
			"'argparse.Namespace', 'types.SimpleNamespace' 또는 'dict'만 가능하다."
		)

	with open(filename, "w", encoding="utf-8") as f:
		json.dump(
			data,
			f,
			indent=4,
			ensure_ascii=False,
			default=cast_np_scalar,     # serializable 문제 해결
		)


def load_json(filename):
	"""JSON 파일을 읽어서 dict 형태로 불러온다."""
	try:
		with open(filename, "r", encoding="utf-8") as f:
			args_dict = json.load(f)
	except FileNotFoundError:
		raise FileNotFoundError(f"파일 {filename} 을(를) 찾을 수 없다.")
	except json.JSONDecodeError:
		raise ValueError(f"파일 {filename} 의 JSON 파싱에 실패했다.")

	return args_dict
