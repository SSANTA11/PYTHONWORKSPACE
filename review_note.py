# 모듈(=라이브러리) 사용하기
    # import 모듈
    # from 패키지 import 모듈
            
        # from random import radiant, choice
        # radiant(1, 45)
            # from을 사용하게 되면 선택적인 기능을 수행할 수 있기 때문에 메모리 효율적이다

        # from random import * 
            # '*'은 모든 것을 의미함, 유용하지만 프로그램이 무거워짐

# install은 파이썬에 기본 설치되지 않은 모듈을 의미하고 이러한 모듈을 설치하는 것을 pip라고 지칭한다
# 기본함수 (0부터 1사이)
    # import random
# 특정범위의 무작위 
    # print(random.randint(1,45))
# 여러 개의 값 중에서 무작위로 하나 선택
    # random.choice('absdfsfrfsdfsdfasd')
                                    # from ppp.abc import func
                                        # ppp안에 abc라는 파일 안에서 func라는 기능을 사용한다
                                        # func는 다양하다(?)
# import numpy as np
# np.array()
# import pandas as pd
# import matplotlib.pyplot as plt