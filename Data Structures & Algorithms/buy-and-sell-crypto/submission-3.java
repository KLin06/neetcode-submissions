class Solution {
    public int maxProfit(int[] prices) {
        int lowestValue = 1000000;
        int maxDifference = 0;

        for(int i = 0; i < prices.length; i++){
            if(prices[i] - lowestValue > maxDifference)
                maxDifference = prices[i] - lowestValue;
            if(prices[i] < lowestValue)
                lowestValue = prices[i];
        }

        return maxDifference;

    }
}
