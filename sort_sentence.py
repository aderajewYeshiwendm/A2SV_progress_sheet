class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()

    
        word_indices = []

     
        for word in words:
           
            index = int(word[-1])
            
            word_without_index = word[:-1]
        
            word_indices.append((index, word_without_index))

        
        word_indices.sort()

        
        

        return ' '.join(word for _, word in word_indices)
