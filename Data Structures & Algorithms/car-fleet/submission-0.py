class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))          # ascending by position
        stack = [(target - p) / s for p, s in cars]  # time-to-target, no ceil
        #print(cars)
        #print(stack)

        fleet = 0
        while stack:
            t = stack.pop()
            fleet += 1
            while stack and t >= stack[-1]:
                stack.pop()
        return fleet
        