class Solution:
    @staticmethod
    def addBinary(a: str, b: str) -> str:
        """두 이진수 문자열을 더하여 이진수 문자열로 반환합니다."""

        # 두 문자열의 길이를 맞추기 위해 0을 채웁니다.
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        result = ""
        carry = 0

        # 맨 오른쪽 자리부터 차례대로 더합니다.
        for i in range(max_len - 1, -1, -1):
            sum_bit = carry + int(a[i]) + int(b[i])
            carry = sum_bit // 2
            result = str(sum_bit % 2) + result

        # 최종적으로 carry가 남아있으면 결과 앞에 1을 추가합니다.
        if carry:
            result = '1' + result

        return result
