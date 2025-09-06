from typing import List, Optional

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        top1: Optional[int] = None  # 1등
        top2: Optional[int] = None  # 2등
        top3: Optional[int] = None  # 3등

        for x in nums:
            # 이미 기록된 값(중복)은 건너뜀
            if x == top1 or x == top2 or x == top3:
                continue

            if top1 is None or x > top1:
                # x가 새 1등 → (1등->2등, 2등->3등)으로 밀기
                top1, top2, top3 = x, top1, top2
            elif top2 is None or x > top2:
                # x가 새 2등 → (2등->3등)으로 밀기
                top2, top3 = x, top2
            elif top3 is None or x > top3:
                # x가 새 3등
                top3 = x

        # 3등이 있으면 3등, 없으면 1등(최대) 반환
        return top3 if top3 is not None else top1
