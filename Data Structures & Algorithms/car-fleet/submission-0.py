class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key = lambda x: x[0], reverse = True)
        stack = []
        for car_pos, car_speed in cars:
            time_to_finish = (target - car_pos) / car_speed
            if not stack or stack[-1] < time_to_finish:
                stack.append(time_to_finish)
        
        return len(stack)
    