class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_counter = Counter(tasks)
        frequencies = list(tasks_counter.values())

        max_freq = max(frequencies)
        max_freq_count = frequencies.count(max_freq)
        
        minimum_slots = (max_freq - 1) * (n + 1) + max_freq_count
        
        return max(len(tasks), minimum_slots)

        