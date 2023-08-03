class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    p_min = prices[0]
    p_max = prices[0]
    p_return = 0
    
    for price in prices:
        if price < p_min:
            p_min = price
            p_max = price
        elif price > p_max:
            p_max = price
            if p_return < p_max - p_min:
                p_return = p_max - p_min
            
    return p_return