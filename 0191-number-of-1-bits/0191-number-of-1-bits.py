class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0  # 1의 개수를 저장할 변수 초기화
        while n > 0:
            if n % 2 == 1:  # 2로 나눈 나머지가 1이면 (즉, 마지막 비트가 1이면)
                count += 1  # 1의 개수 증가
            n //= 2  # n을 2로 나눈 몫으로 업데이트 (오른쪽 시프트 연산과 동일)
        return count
        