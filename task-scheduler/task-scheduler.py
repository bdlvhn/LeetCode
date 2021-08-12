class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:        
        
        counts = list(collections.Counter(tasks).values())
        max_count = max(counts)
        num_of_chars_with_max_count = counts.count(max_count)
        
        num_of_chunks_with_idles = max_count-1
        
        length_of_a_chunk_with_idle = n+1
        length_of_the_final_chunk = num_of_chars_with_max_count  # 2  

        length_of_all_chunks = (num_of_chunks_with_idles*length_of_a_chunk_with_idle) + length_of_the_final_chunk

        return max(len(tasks), length_of_all_chunks)