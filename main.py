import collections
import collections.abc
collections.Iterable = collections.abc.Iterable
# 猴子补丁，用于解决一个报错

import sys
import numpy.core.multiarray
sys.modules['numpy._core.multiarray'] = numpy.core.multiarray
# 猴子补丁，用于解决一个报错

import torch
from utils import execute_function, get_args

if __name__ == '__main__':
    args = get_args()
    if torch.cuda.is_available():
        args.device = f'cuda:{args.gpu}'
        print(f'Using GPU: {args.device}')
    else:
        args.device = 'cpu'
        print('Using CPU')

    # if not args.save_path:
    #     args.save_path = f'synthetic/{args.dataname}/{args.method}.csv'
    main_fn = execute_function(args.method, args.mode)

    main_fn(args)