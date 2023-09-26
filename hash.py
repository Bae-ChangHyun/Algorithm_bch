# 백준: https://www.acmicpc.net/problem/10930
# 알고리즘: 해쉬

# 예제 입력
# ---------------------------
# Baekjoon
# ---------------------------
# 예제 출력
# ---------------------------
# 9944e1862efbb2a4e2486392dc6701896416b251eccdecb8332deb7f4cf2a857

import hashlib

input_data = input()
encoded_data = input_data.encode()
result = hashlib.sha256(encoded_data).hexdigest()
print(result)
